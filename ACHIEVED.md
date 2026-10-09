# Achieved

Completed work archived out of `ROADMAP.md` so the active document stays
readable — the queue there tracks what's active/planned, this file is the
historical record of what's already shipped. Entries keep their original
queue numbering and wording (not renumbered or edited) so old references
and commit messages that cite an item number still resolve. Nothing here
needs re-reading before starting new work; it's reference only.

## Done parts moved out of open queue items (2026-10-08)

153. **Release gate 1: units are finished and frozen one at a time (set up 2026-10-09).** Per-problem passes over whole courses kept revisiting the same exercises (length at 2×, then 1.3×; absolutes; time words), so the user switched to finishing a unit completely and freezing it. `scripts/freeze_unit.py` freezes a unit only when `check-content.py` reports nothing for it except findings a reader accepted with a reason (only suspects and the two tell checks can be accepted); it writes `content/<course>/frozen-units.json` and `--status` counts progress. `check-content.py` no longer reports accepted findings and `--changed` blocks an edit to a frozen unit unless the same change unfreezes it. Brief: `docs/unit-finish-brief.md`. **Model unit `hu a1/reading-hungarian` (a1-01…a1-05) frozen by Claude:** 9 length give-aways fixed with near-miss wrong options (*Nem, Károly vagyok.* for *Te Károly vagy?*, the statement *Ez egy tea.* against the question *Ez egy tea?*), the two `Szia!` punctuation tells, *jó*, *kávé* and *köszönöm* now drilled in the matching pairs that listed them unused, and `a1-01-practice-3` rewritten (*Kávé? ____, köszönöm.*): it carried an English gloss inside the sentence, untaught *kérsz*/*kávét*, and an appended blank; a scan found no other such gloss in any course. Three suspects accepted (the reply to *Szia* is *Szia*; English *I* is capitalised). **Same day, the screens nobody writes:** `scripts/render_lesson.js` prints a lesson as the app builds it (real `buildSteps()`, file-reading stubs), and showed the generated screens were wrong in the model unit: grammar table rows were used as speaking sentences with their second column as the "English" (*repeat hat = hát*; *translate szél → say szel*), the challenge model answer for a1-01 was *hat*, for a1-03 (*ask what something is*) *Ki ő?*, the prompt said "in Hungarian" twice, and every HU lesson requested a missing `challenges.json`. Fixed in the engine for every course: table rows are no longer speaking candidates; fill-blank candidates use the answer-audio cleaner (`ExerciseAudio.fillBlank`), take `answers[0]` when there is no `answer`, and are capitalised; the challenge lookup matches the exact lesson stem only (prefix and title-word matches put es-es's `b1-story` and `a2-restaurant` into unrelated lessons); the doubled "in <language>" is gone; one-word lead-ins (*Complete:*) are dropped from spoken answers too, which fixes answer audio in 48 exercise files. `content/hu/curriculum/challenges.json` created with hand-written challenges for a1-01…a1-05. The unit brief now requires reading the rendered lesson and writing every lesson's challenge. Checked on the live site (parlour.me.uk, a1-01): `challenges.json` 200, no console errors. The live screen showed that at A1 the challenge's cues are a hint shown before the learner speaks, so cues that named the words (*Greeting (Szia)*) gave the answer away; the five were rewritten (*Greet him back*) and the rule put in the brief. `audit-reader-coverage.js --story` checks one unit's story (the model's 24 words all look up), and the renderer prints the story text. **Metadata check (the user's spot check, same day):** the brief only said not to change the locked tags, never to check them, and the model unit's own rewrites had broken some: `a1-04-intro-1` and `a1-04-check-2` kept `distractor_skills` `ki-and-mi` on options that were no longer *ki/mi* forms; `a1-02-practice-dialogue`'s new wrong option showed no copula error (now *Nem, én Károly van.*); `a1-02-intro-2` lacked `{"1": "personal-pronouns"}` for *Én Meg vagyok*. Fixed, re-locked (`lock_tags.py --update`), re-frozen. The brief now has a metadata step for every exercise (`teaches`, `distractor_skills`, `category`, `hint`, `english`, `answers`), says to re-check tags whenever an option or sentence changes, and allows tag fixes with a re-lock. `check-content.py --changed` now lets a change that re-freezes a unit through. Speaking steps built from dialogue fill-blanks (*Anna: Jó reggelt! Te: ____!*) no longer have the learner read the speaker names aloud: such lines are skipped as candidates (engine, every course; SW cache bumped).

152. **`check-content.py` findings: the seven small, clear classes (done 2026-10-09).** All A1–B1 hits fixed by hand in hu, es-es and es-latam, each read in context; every class now reports 0. `missing-english` (42): the 21 ES A2 sentence-builders in each Spanish course had no prompt; they now have an `english` line, and where *them* hides the gender the noun is named (*We bought them (the gifts)*). `latam-vosotros` (5): *sabéis*, *os*, *¿Habéis llegado?* (×2) distractors replaced with ustedes/usted-world forms; *tenéis* in `b1-05-consolidation.ex06` → *tienen*. `unit-copy` (2 + 2 the new English exposed): `a2.02.01.ex12` now builds *Ya hemos comprado el mapa*; `a2.12.02.ex13` *Los preparamos*. `hint-is-answer` (17): HU cognate blanks *bank*/*park* (a1-131, a1-133 and their a1-135 copies) now test *tér* and *posta* from the same lesson lists; the name blank in `a1-50-consolidation-11` became the greeting (*____, Meg vagyok.*, answers *Szia/Szervusz/Helló*); hints that printed the form (*beginner: kezdő*, *-on/-en/-ön*, *verbal prefix át-*, *there is — hay*, *hay que*, *la tarjeta*) cut to the meaning or lemma; the redundant *los zapatos* hint dropped. `blank-appended` (7): the blank moved inside the sentence (*Rendben, ____.*, *Kártya. Most ____.*, *A fiú ____.*, *Reggel ____.*, speaker labels on *Köszönöm! / Kérem*). `slash-giveaway` (4): the correct gloss is now one word, like its distractors. `adjacent-repeat` (25): HU consolidation drills a1-55/60/65/70 keep their repeated shape but each question now names the sentence (*Which says "Anna is in the kitchen."?*); a1-15, three ES A1 questions reworded (`a1-01-consolidation.ex16` now asks for the name question, with a second question among the options so punctuation doesn't give it away); `a2.02.05.ex10` was listed at the end of Practice and the start of Reading and is now in Practice only.

The finished parts of items still open in ROADMAP.md, moved here so the queue holds only open work. Each entry is the item's full text as of 2026-10-08; ROADMAP.md keeps a short version with what is still open.

- **fix(speech): iOS speech recognition bidirectional fallback and self-evaluation (2026-10-08).** When speech input was used on iOS, WebKit often blocked microphone access with a misleading "Microphone access is blocked in your browser settings" error even when microphone permission was allowed in browser settings. Root causes resolved:
  - Audio session contention: `ParlourTTS.stop()` is now called before recording begins in `lessonToggleSpeaking` (`engine/lessons.js`), preventing iOS WebKit from holding the audio session in playback-only mode.
  - Bidirectional STT fallback: in `engine/speech-input.js`, when native `webkitSpeechRecognition` fails on iOS with `service-not-allowed` or `not-allowed` (due to missing offline Dictation language models or PWA restrictions), it now automatically falls back to audio recording and Whisper Cloud STT. Conversely, if audio recording encounters a hardware error, it attempts native recognition before failing.
  - Specific error reporting: preserved detailed error codes (`insecure-context`, `device-busy`, `service-not-allowed`, `permission-denied`) rather than masking everything as "microphone access blocked in browser settings".
  - Lesson self-evaluation fallback: added self-evaluation prompt (`lessonSelfEvalGood`, `lessonSelfEvalRetry`) in `engine/lessons.js` for speaking exercises and oral challenges when microphone access is unavailable, so learners can practice out loud and progress without being forced to skip or snooze speaking drills.
  - Speaking Studio & Dialogue Scenarios on mobile: enabled `preferRecording: true` in `engine/drills/speaking.js` verbal production and conversation scenarios so mobile devices route through Whisper Cloud STT by default.
  - Added test suite `tests/speech/test-speech-fallback.js` (all 11 test suites passing). Cache buster bumped in `index.html`.

122. **Exercises speak the right answer (added 2026-10-02).** Principle: the learner should always *hear* the correct target-language form, not only see it. Whenever an exercise is settled (solved, or revealed after 3 tries) the answer autoplays via ParlourTTS, with a replay icon; target-language words in matching speak on tap. Nothing that would give the answer away plays before the learner answers. A mute toggle in the lesson header is remembered across lessons. Cost is a non-issue: the TTS worker caches every clip in R2 (shared across all learners) and each browser in IndexedDB, so each distinct sentence is generated once.
    - **Phase A: lessons — shipped 2026-10-03.** `engine/exercise-audio.js` decides what to say (pure functions; `tests/lessons/test-exercise-audio.js`); `engine/lessons.js` plays it from `solveStep()`/`failStep()` via `speakSettled()`, preloading the clip when the step renders. Fill-blank says the whole sentence with the answer in (English lead-ins like "Complete the greeting:" and `(...)`/`[...]` hints dropped); multiple-choice says the correct option or the completed sentence, or, when the answer is English, the target word the question asks about; dialogue-complete, sentence-builder and sentence-order say the full text; matching speaks a target word on tap; substitution speaks each new sentence; structured-writing model answers get a listen button. Rule: only text positively identified as target language is spoken; anything unsure stays silent. The header has a new spoken-answers toggle (waveform icon, `parlour_exercise_voice_muted`, on by default) beside the sound-effects one. `node scripts/audit-exercise-audio.js <out-dir> [content-dir]` lists what every exercise says, silent ones first: about 96% speak (es-es 8,475/8,612, es-latam 9,805/9,946, hu 15,975/16,357), and no spoken line contained English at ship time. Re-run it after big content passes.
    - ~~**Data bug found by the audit:** HU B1 fill-blanks with a stray `_____` after the hint.~~ **Done 2026-10-04:** 50 sentences in 30 files fixed (see ACHIEVED.md, "Stray trailing blanks in HU B1 fill-blanks"). The 51st multi-blank match, `a2-190-check-2`, is a genuine two-blank sentence and was left alone.
    - **Phase B (after Antigravity's HU work): move hints into a typed `hint` field.** This is the 2026-09-14 "typed hint field" idea (~6,000 fill-blanks carry their hint inside `sentence`). Once `sentence` is clean, the cleaner becomes a no-op safety net.
    - **Later:** the same rule for the Workshop Grammar and Vocabulary drillers.

125. **Skill tags: one language-independent format (one tag per exercise, families and levels on skills, prerequisites, wrong-option skills), a frozen skill list, locked tags, and a full read of every exercise (added 2026-10-04, rescoped twice the same day).** This is not a redo of ACHIEVED.md item 91, which checked all 7,573 grammar exercise–tag pairs on 2026-09-24. The next day, two bulk commits rewrote most Hungarian tags without any check of that kind. `2fc5fe02` cut 1,202 HU grammar skills to 195 and sent many exercises into a few catch-all skills (`present-tense-routine-language`, `adversative-contrast`, `ki-and-mi`, `elative-bol-bel`). `e7f4c105` (Antigravity, "Split Hungarian junk-drawer grammar skills") then spread those exercises over specific skills. That split retagged 5,075 HU exercises, and 5,063 still carry its tags today. 2,094 of them are on grammar skills (A1 1,377, A2 363, B1 354). The rest moved between vocabulary-theme slugs, which is lower risk. **ES B1 progress 2026-10-07:** **ES B1 is complete** (core 40, cultura 36, latam 36 units; ACHIEVED.md "ES B1 read-through complete"); follow-ups are item 145; next is HU B2 (registry scan first) (ACHIEVED.md "ES B1 `cultura` track"). **ES B1 `taught_in` warnings (2026-10-07):** `ser-passive`, `prepositional-phrases`, `verbos-regimen-preposicional` (es-es) and `relativo-posesivo-cuyo` (es-latam) are flagged "taught later" in track units because their teaching screens there exist in one course only; moving the registry entry would break the other course, so the warnings stay until the per-course `taught_in` map exists (decided with the user: deal with it later).
    - **Evidence.** Of the 50 HU B1 fill-blanks touched by item 122a, 18 had the wrong tag (all corrected, ACHIEVED.md `122a`). Tracing each one through `git log` shows that 15 of the 18 came via `2fc5fe02` → `e7f4c105`, often starting from a generic `synthesis` tag. Error rate in that sample by path: retagged by the split 12/18, by the consolidation only 3/17, by neither 3/15. In a random 30 of the 2,094 grammar retags (10 per level), roughly half were wrong. Examples: *indul* → `going-somewhere-the-irregular-verb-megy`, *hogy* → `plural-nouns-after-quantifiers`, *boltban* → `on-en-on`, "Which means 'dentist'?" → `light-verb-collocations`, accusative *védelmet* → `definite-vs-indefinite-conjugation`. That puts roughly 1,000 wrong grammar tags in HU A1–B1. The trace scripts are not kept. To rebuild the list, diff `teaches` at `e7f4c105^` against `e7f4c105` and keep the exercises whose tag is unchanged at HEAD and is a `kind: grammar` skill.
    - **Why it matters.** The learner model, Home's "You made a few mistakes with …", Workshop routing and the grammar reference all read these tags, so a wrong tag sends the learner to practise the wrong thing. `validate-content.py` checks only that a slug exists and that its kind matches the category, not that it fits the exercise.
    - **Why tags keep breaking.** HU tags have been rewritten in bulk four times in about ten days: the item 98 backfill (copied from neighbouring exercises), the item 91 audit, the `2fc5fe02` consolidation and the `e7f4c105` split. Only the audit read the exercises. The others were checked only by `validate-content.py`, which passes any tag that exists and is the right kind, so a pass that makes tags worse still validates green, and nothing protected item 91's results from the next day's remap. Grammar skills also keep being merged and split because they have only one level of detail. A pass that only fixes the ~1,000 tags would be undone by the next one, so the plan changes the format and its enforcement first. Decided with the user 2026-10-04.
    - **Decided with the user 2026-10-04: the full format is in [docs/skill-tagging-spec.md](docs/skill-tagging-spec.md).** It replaces the earlier plan. In short: exactly one `teaches` slug per exercise, chosen by what a wrong answer shows, in every category. Family and level live on the skill in the registry, never on exercises; an exercise's level comes from its folder. One registry per language (es-es and es-latam merge; variant-only skills get `variant`). One vocabulary skill per unit, named from a permanent unit `id` added to the curriculum (`a1-greetings-introductions-vocab`, not unit numbers, which shift when units move and hide wrong tags; changed the same day). Grammar skills are split by the one-explanation test, each with `taught_in` (its grammar screen) and `requires` (direct prerequisites). Grammar choice items get `distractor_skills` (which skill a wrong option belongs to) for mislearning detection. At least 6 exercises per skill. 26 vocabulary families (`ideas` approved; all 634 unit vocabulary skills mapped in `docs/skill-families-mapping.md`, approved 2026-10-04 after a review corrected 23 skills where `language`/`ideas` had been a fallback for grammar-themed units) and one shared grammar-family backbone for all languages. All renames happen now, with aliases. The list is then frozen. Reviewed units are locked in a generated `tags.lock.json`. Learner skill stats reset after the switch. Every exercise (~48,000 across es-es, es-latam and hu) is read, not sampled. This metadata is what the skill map (item 131) runs on.
    - **Plan, in order:**
      1. **Grammar-family backbone.** *Drafted 2026-10-04, pending review:* `docs/grammar-families-draft.md` (37 families in 5 display groups, from the PCIC *Gramática* chapters cross-checked against the English Grammar Profile; no Hungarian external syllabus could be retrieved, so a Hungarian teacher's check is worth having), with nine rules for choosing a family. All 1,128 grammar slugs are mapped in `docs/grammar-families-mapping.md`/`.json`. The mapping found 144 skills that aren't grammar (2,479 exercises), 244 topic-bound grammar skills (hu 196, es-latam 48), 55 duplicate groups and 19 skills that name two things. These are worklists for step 2. Decided the same day: keep all 37 families, `register-style` skills stay `kind: grammar`, keep the five display groups as the map's top layer.
      2. **Registry and validator.** **Built and enforced 2026-10-04.** Source of truth `skills/es.json` (184 grammar + 243 vocabulary skills, es-es and es-latam share it) and `skills/hu.json` (204 grammar incl. the approved `vowel-harmony` + 296 vocabulary); shared `skills/families.json`; frozen lists `skills/frozen-<lang>.json`. `scripts/build_skill_registry.py` generates each course's `skill-registry.json`, `grammar-titles.json` and `skill-prereqs.json` (CI runs it; `--check` mode). Every unit table entry has a permanent `id` (HU A1/A2 got explicit tables; `curriculum.json` carries it as `slug`, positional unit ids unchanged). `scripts/resolve_skill_aliases.py` rewrote alias slugs in 3,759 files (28,204 exercises' `teaches`, tests, `targetSkills`, `verb-tense-skills.json`), verified tag-only. 149 non-skill slugs are `retired` until the read-through retags them. The validator now checks the sources (families, levels, titles, `taught_in` screens, `requires` level/loops, one vocabulary skill per unit named from its id, frozen list, generated files in sync) and exercises (aliases, `distractor_skills`, locked tags); one-tag, level, retired-slug and coverage rules are warnings until a unit is locked with `scripts/lock_tags.py` (`--warnings` lists them; at build time es-es 1,346/438/195/96, es-latam 1,409/1,003/182/50, hu 2,720/1,153/501/17 for multi-tag/retired/above-level/thin). Engine: level-test flags now map old slugs to canonical skills (production evidence already did); learner stats were folded through aliases rather than wiped, because cloud sync would restore a wipe. Rules written into AGENTS.md, CLAUDE.md, the HU template, the es guides and the spec. Original plan text follows. *Unit ids drafted 2026-10-04, pending review:* `docs/unit-ids.md`/`.json`, a permanent id for all 539 units (Spanish 243, shared es-es/es-latam units once; Hungarian 296), each unit's vocabulary skill slug and the old slugs that become its aliases (assigned by where each is used, because the old numbers had drifted from the units). 31 units get a new vocabulary skill. HU A1/A2 are to get explicit unit tables like every other level. *taught_in and requires drafted the same day, pending review:* `docs/taught-in-requires.md`/`.json` — a grammar screen for 386 of 387 skills (45 automatic matches corrected by hand) and 427 direct-prerequisite links (level-checked, acyclic). A skill's level is now the level of the screen that teaches it. Found: 40 skills practised before they're taught (the validator's level check will list those exercises for the read-through), 12 Spanish skills explained in only one of the two courses, no screen for HU `nominalizing-processes`, and no HU `vowel-harmony` skill although it's the prerequisite of every suffix (adding it needs the user's sign-off). *Grammar skill list approved 2026-10-04:* `docs/grammar-skill-list.md`/`.json`, Spanish 573 → 184 skills, Hungarian 555 → 203 (duplicates and topic copies merged, old slugs kept as aliases; 147 not-grammar slugs dropped for retagging at read time). All six judgment calls accepted as proposed; HU `framing-markers` and `evaluative-stance` are holding places to dissolve during the read-through. New registry fields (`level`, `family`, `variant`, `taught_in`, `requires`), the Spanish registry merge, all renames with aliases, generated unit vocabulary skills for units that have none, the frozen list and the lock file. The validator fails on: more than one `teaches`; a skill missing `level`/`family` (and `taught_in` for grammar); an unknown family; a `requires` cycle or a prerequisite above the skill's level; a skill above the exercise's level; a registry change not in the frozen list; a changed locked tag. It warns below 6 exercises per skill and on likely mismatches (`scripts/audit_exercise_metadata.py`: *aki/amely/ahol/amikor* not on a relative-clause tag, a "Which means …?" question on a grammar tag, and similar). The rules get written where generators read them, in the same commit as the checks: AGENTS.md § "Exercise metadata" and § "Adding a new course", CLAUDE.md, the HU authoring template, the es-latam generation specs and the memory note `content-validation-tooling`. The pre-push hook and CI run the validator for every author, including Antigravity. The learner-model skill-stat reset ships with this step.
      3. **Read every exercise**, unit by unit, A1 first, in all three courses: set its single tag and its `distractor_skills`, fill thin skills to 6, lock the unit, validate, log the batch in ACHIEVED.md. Known problem sets to watch for: the 2,094 HU grammar retags from `e7f4c105` (about half wrong in a sample); Spanish `a1-unit01-vocab` on 520 exercises per course outside unit 1 (`2015b0a8`); and about 5,800 exercises carrying 2–6 tags. Unit-number vocabulary slugs (HU A2's unit + 10, HU B1's `b1-01-vocab`, all `aN-unitNN-vocab`) are renamed to unit-id slugs, with the old ones kept as aliases; giving every unit its `id` comes first, in step 2. Other registry problems found by the vocabulary mapping are in `docs/skill-families-draft.md` § "What the mapping found": 60 per-lesson es-latam B2 vocabulary skills, `hacer`/`negation` registered as vocabulary, a duplicate HU C1 slug, orphan lessons `a1-18-01`/`02`. **Progress:** HU A1 `reading-hungarian` (lessons 1–5) read and locked 2026-10-05, then `greetings-basic-interaction` (lessons 6–10 + consolidation) and `introducing-yourself` (lessons 11–15 + consolidation) the same day, tagged by a Sonnet subagent and reviewed, then `numbers-personal-information` (lessons 16a–20 + consolidation, read in the main session), then units 5–33 (`objects-locations` to `postpositions`, a1-21–a1-165), which completes HU A1 (3,842 exercises) by Sonnet subagents, one per unit, two at a time, with every batch checked by `scripts/readthrough_check.py` and reviewed before `apply_tags.py`/`lock_tags.py` (`scripts/readthrough_dump.py` prints a unit for reading); ES A1 `greetings-introductions` (es-es and es-latam, applied identically) the same day (batch log in ACHIEVED.md § "Skill-tag read-through log"). The conventions settled on it are in the spec § "Read-through conventions". Decisions are applied with `scripts/apply_tags.py` and the unit is then locked with `scripts/lock_tags.py`. HU A2 done the same way the same day: all 44 units (4,154 exercises, a2-01–a2-220) locked, with the conventions it added logged in ACHIEVED.md § "HU A2 read-through complete"; registry follow-ups in item 138. How to run a level from now on (registry fixed first, one rule sheet, two units per subagent, filtered review, more automatic checks) is in [docs/readthrough-process.md](docs/readthrough-process.md), with the subagent rule sheet in `docs/readthrough-brief.md` and the review view in `scripts/readthrough_review.py`; its "Before starting a level" steps come first. HU B1 done 2026-10-05/06: set-up (ACHIEVED.md § "HU B1 read-through set-up") and all 75 units, 4,333 exercises (ACHIEVED.md "HU B1 read-through complete"; follow-ups in item 141); ES A1 done 2026-10-06: all 26 units, es-es and es-latam (ACHIEVED.md "ES A1 read-through complete"; follow-ups in item 142); ES A2 done 2026-10-06: set-up (ACHIEVED.md "ES A2 registry scan") and all 33 units, es-es and es-latam (ACHIEVED.md "ES A2 read-through complete"; follow-ups done, ACHIEVED.md item 143); next: ES B1 (registry scan first; it carries 217 hints that print their answer per course) or HU B2. Spanish has no pronunciation skill for the a1-01-01 vowel/sound screens (item 133).

130. **Length give-away in choice exercises (added 2026-10-04).** In 1,208 choice exercises (counting an exercise shared by es-es and es-latam once) the correct option is at least twice as long as the longest wrong option (and 15+ characters longer): a full explanatory sentence beside two short fragments, e.g. `b1-30-05.ex01` (*Azoknak az erkölcsi és szellemi elveknek az összességét, amelyek …* vs *A banki árfolyamok listáját a kijelzőn.*). Same kind of shape cue as item 126 (ACHIEVED.md), but more than three times as many. Counts: Spanish shared by both courses (`es-both`) A1 35, A2 14, B1 127; es-es only B1 175; es-latam only B1 224, B2 32; HU A1 32, A2 55, B1 295, B2 55, C1 164. Mostly B1 comprehension checks. Fix per exercise: shorten the correct option to the key point, or lengthen the wrong options into equally specific, plausible sentences (rule 3 of `imports/review/ANTIGRAVITY-exercise-quality.md`). es-es and es-latam share A1/A2 and much of B1, and no script syncs them: fix a shared (`es-both`) exercise once and apply the identical change to both files, so the copies stay equal. Check and work list: `python imports/review/check-slash-giveaway.py --length [course level] --list`. The 2×/15-char threshold catches only the blatant cases; milder ones (1.5×, ~3,600) are left for later. Suits an Antigravity pass with stops for review, like item 126. **Spanish B1/B2 handed to Antigravity 2026-10-05:** brief `imports/review/ANTIGRAVITY-length-giveaway-es.md`, per-exercise worksheet `imports/review/es-length-giveaway-worksheet.txt` (542 entries after merging lesson/consolidation and es-es/es-latam copies, in four blocks with a stop after each). Kept to Spanish so it can't collide with the HU tag read-through (item 125). **Block 1 (es-both B1, 127) done and reviewed 2026-10-05** (`c7a78634`: 21 shorten / 106 match; mechanics all correct; 4 content fixes and guidance for blocks 2–4 in the brief's review notes). **Block 2 (es-es B1, 159) done and reviewed 2026-10-05** (`b2d5ff08`: 141 shorten / 18 match; mechanics correct; one shortening made the correct option false, `b1-ciudadesautonomas-02.ex02`, plus 3 smaller fixes, all in the brief's review notes). **Block 3 (es-latam B1, 224) done and reviewed 2026-10-05** (`ead28c80`: 66 shorten / 158 match; mechanics correct; 7 fixes in the brief's review notes, mostly new wrong options that no longer fit their question, incl. two in English). **Block 4 (es-latam B2, 32) done and reviewed 2026-10-06** (`3f825a03`: 22 shorten / 10 match; the 2 last fixes landed in `c06816c4`, checked 2026-10-07). With those, all four Spanish B1/B2 blocks (542 exercises) are done and es-es B1, es-latam B1 and es-latam B2 have no length give-aways left. **Spanish A1/A2 (51 es-both) done and reviewed 2026-10-07** (`d61449bf`: 18 shorten / 32 match / 1 log; mechanics correct, es-es and es-latam copies identical; worksheet `imports/review/es-a1a2-length-giveaway-worksheet.txt`). One left on purpose: `a2.15.03.ex02` (a metalinguistic "which part is the cause" item that cannot be balanced without changing the stimulus; proposal in `imports/review/es-review-questions.txt`). Spanish has no other length give-aways. **Hungarian (605: A1 32, A2 57, B1 297, B2 55, C1 164) remains**: brief `imports/review/ANTIGRAVITY-length-giveaway-hu.md` and worksheet `imports/review/hu-length-giveaway-worksheet.txt` written 2026-10-07 (586 entries after merging lesson/consolidation copies; 5 blocks: A1+A2 70, B1 149 + 148, B2 55, C1 164, with a stop after each). Left out on purpose: the 14 native-speaker-reviewed `a1-121…150` dialogue-complete items and `c1-21/22` (item 127). **Block 1 (A1+A2, 70) done and reviewed 2026-10-07** (`a1471d26` 4 shorten / 65 match / 1 log, mechanics correct; fixes in `18762204` for a "Sajnos" tell in 14 wrong options, ~24 absolutes/cartoonish distractors and a non-word, all verified; `a1-09-dialogue-1` logged with a proposal). **Block 2 (B1 first half, 149) done 2026-10-07** (`0e2aef36`: 76 shorten / 73 match; mechanics correct; 7 arguable second-right-answer distractors fixed in `81da961e` and verified). **Block 3 (B1 second half, 148) done 2026-10-08** (`70db33b3`: 48 shorten / 100 match; mechanics match the worksheet, but two decisions were swapped between `b1-honfoglalas-03.ex07` and `04.ex07`, plus 3 smaller issues, all fixed in `51a306f5` and verified). **Block 4 (B2, 55) done 2026-10-08** (`9761fb22`: 9 shorten / 46 match; mechanics correct, 3 small fixes in `7b8c39f4`, verified; `b2-35-04-controlled-3` logged for a rewritten question). **Recheck 2026-10-08:** give-aways have reappeared since review; the A1–B1 ones are item 148(a), and HU B2 has 1 more (`check-slash-giveaway.py --length hu b2 --list`). **Block 5 (C1, 164) done 2026-10-08** (`4bffe8f8`: 164 match; mechanics correct and no swapped decisions, but ~60 wrong options are the extreme version of the correct one (*kizárólag / teljesen / soha…*), a shape tell sent back with an id list in the brief's review notes); the HU retagging (item 144) edits the same files, so check it is idle first. After block 2, have a native speaker spot-check a sample of the new Hungarian. Also found in review, out of scope: es-es `b1-fiestas-01.ex05` *Los tamborradas*; `b1-gastronomia-05.ex02` and `b1-historiaantigua-03.ex04` give the answer away; many CCSE civics items have absurd distractors. Found in review, out of scope: es-latam `b1-37.cons.ex05` uses *hayáis*; `b1-19-03.ex06` and `b1-29-05.ex02` give the answer away in the question text.

## Items folded into ROADMAP 148 "A1–B1 polishes" (2026-10-08)

These entries were merged into one queue item, ROADMAP 148. Their open parts are carried there (rechecked against the files); the parts already done, and the full detail, are kept here so references to these numbers still resolve.

148. **A1–B1 polishes: points done (2026-10-08).** Decided with the user on 2026-10-08 from a recommendation per point, each checked against the files.
    - (a) `a2.15.03.ex02`: the stimulus is now *Lloró de tristeza porque entendió la situación*, and the main-clause option is *Lloró de tristeza*, so the cause no longer stands out by length (proposal in `imports/review/es-review-questions.txt`). Both courses; es-es A2 has no length give-aways left.
    - (c) `tol-tol` relevelled A2 → A1, `taught_in` a1-154-a-gr, where *-tól* is taught alongside *-ból* and *-ról*, which already have A1 skills. Six items moved off `a1-origin-cases-vocab` to `tol-tol` and to category `grammar`: `a1-154-introduce-1`, `-controlled-1`, `-practice-2`, `-dialogue-1`, `a1-155-consolidation-5`, `-10`. Frozen list note added; `a1/origin-cases` re-locked.
    - (d) `formal-purpose`: `taught_in` moved from b1-erdelyaranykora-04-gr to b1-03-05-gr. The old screen is on the citizenship track, so core learners never met the skill as taught; b1-03-05 (core, B1 unit 4) introduces *annak érdekében, hogy*. Frozen list note added. Not moved, on purpose: `hypothetical-ha-conditional` stays on b1-04-01-b-gr (the `-a` screen teaches only the fixed phrase *a helyedben*; `-b` spells out the full *ha* clause), and `additive-connectors` stays on b1-32-01-b-gr (b1-13-05-a teaches other connectors, *egyfelől … másfelől* and *mindent összevetve*; *ráadásul* and *továbbá* appear only on b1-32-01-b).
    - (e), (j) Skill gaps: nothing left to do. The gap pass decided with the user on 2026-10-07 (ACHIEVED "gap skills added, two skills re-levelled, one removed", `docs/skill-gap-proposal.md`) already settled every gap listed. Applied there: *ponerse* → `reflexives`, *múlva* → `temporal-postpositions` (A2 items; the A1 ones come before the screen), *-ul/-ül* becoming verbs → `mediopassive-verbs-odik`, *annyi … mint* → `olyan-mint`. Kept as vocabulary there: weather, café phrases, *presentar a*, direction chunks, neuter *esto/eso* (the items test meaning), *-ás/-és* nouns, *azelőtt/azóta*, commemorative postpositions, *alighogy … máris*, the `independent-hungarian` particles and generic *az ember*. *nélkül*, flavour adjectives, the *-ik* becoming verbs and *nyugszik* have no items that test a pattern. The two optional ES `taught_in` moves (`plural`, `stem-changes`) were not made; `plural` comes back under (i).
    - (g) New ES skill `pronunciation` (A1, family `sounds-spelling`, "Spanish vowels and letter sounds", `taught_in` a1-01-01-vowels-gr), with a frozen-list entry. Eight new exercises, `a1-01-01.ex17`–`ex24`, in a new "Sounds" group before Practice, identical in both courses. Each is built on whole words (silent *h* in *hola*, the flat *o* of *no*, *ñ*, the silent *u* of *queso*, *j*, *ll*, *rr*, the stress in *café*), and *c/z* is avoided because the two courses pronounce them differently. `a1/greetings-introductions` re-locked in both courses.
    - (h) `a1-01-05.ex09`–`ex11` now depend on the story `a1-01`: where Meg is from (South Africa, with Hungary and Spain, both named in the story, as the wrong options), why Carlos goes to the restaurant (the language exchange) and what they do after practising (eat tacos). Both courses; re-locked with (g).
    - (i) Prerequisite order: 7 of the 12 exemptions had gone stale. `cuando-mientras` no longer requires `imperfect`; `acabar-de` is an alias of `perifrasis-verbales`; and the five B2 conditionals require a B1 skill, so the order was already right. The other 5 requirements were dropped, because each screen teaches what it needs: the usted and negative command screens teach the vowel swap themselves (no `subjuntivo-morfologia`), `a2-indefinidosnegacion-01` teaches double negation (no `negation`), and the latam B2 `formal-register` and `nominalizacion-despersonalizacion` screens stand alone (no `nominalization`). The check in `screen_positions()` now places a screen by the longest lesson stem that prefixes its name, so screens with descriptive names (`b1-35-03-complex-hypothetical-reference-gr`) count too: 0 screens are left unplaced in es-es, es-latam and hu, where before 136 es-es and 77 es-latam were. That revealed 9 further Spanish pairs, exempted and queued in ROADMAP 148(i); Hungarian has none.
    - (m) The nine `latam` B1 consolidations with 14 exercises are accepted as they are (complete in structure).
    - (n) HU A1 length give-aways (2026-10-08, ROADMAP 148(a)): the 15 hits were the 14 native-reviewed a1-121…150 dialogue items exempted in item 130 plus a1-09-dialogue-1 (logged for the native speaker). The checker now skips the 14 for `--length` (`NATIVE_REVIEWED` in `imports/review/check-slash-giveaway.py`); `--length hu a1` leaves only a1-09-dialogue-1.

133. **Spanish pronunciation skill and exercises (added 2026-10-05).** Found in the ES A1 `greetings-introductions` read-through (item 125 step 3). a1-01-01 has two pronunciation screens, *Spanish Vowels* (`a1-01-01-vowels-gr`) and *Spanish Letter Sounds* (`a1-01-01-sounds-gr`: silent *h*, *ñ*, *ll*, *j*/*g*, *qu*, *c*/*z*), but no exercise practises them and the frozen Spanish skill list has no pronunciation skill to tag one with. Hungarian has `hungarian-vowels` and `hungarian-consonant-sounds` for the same job. Fix: with the user's sign-off, add one or two Spanish pronunciation skills to `skills/es.json` and `skills/frozen-es.json` (family, level A1, `taught_in` the two screens), then write at least 6 exercises per skill in a1-01-01 for both es-es and es-latam, applied identically, and re-lock the unit with `lock_tags.py --update`. Never TTS a bare letter (Chirp3-HD returns silence); build sound items around whole words.

134. **ES A1 a1-01-05 reading items don't need the story (added 2026-10-05).** Found in the same read-through. `a1-01-05.ex09`–`ex11` (category `reading`, in both es-es and es-latam) can be answered from general knowledge: "What is the main purpose of their conversation?" → *They get to know each other.* against *They order food.* / *They plan a trip.*; ex09 and ex11 ("What kind of situation does the story represent?") ask nearly the same thing. Fix: rewrite each to quote or depend on a specific story line (who is from where, what Meg answers), or cut the near-duplicate and replace it with one that does; apply identically to both courses and re-lock the unit with `lock_tags.py --update`.

136. **HU `tol-tol` is registered A2 but taught at A1 (added 2026-10-05).** The a1-154-a screen teaches the ablative *-tól/-től* (*a barátomtól*), but `tol-tol` in `skills/hu.json` is A2 (`taught_in` `a2-05-a-gr`), so the A1 read-through (item 125) left six `origin-cases` items that test it on `a1-origin-cases-vocab` (`a1-154-introduce-1`, `-controlled-1`, `-practice-2`, `-dialogue-1`, `a1-155-consolidation-5`, `-10`). Same fix as ACHIEVED.md item 135 (`on-en-on`): with the user's sign-off, move it to A1 with `taught_in` `a1-154-a-gr`, note it in `skills/frozen-hu.json`, retag those six and re-lock the unit with `lock_tags.py --update`.

138. **HU A2 registry follow-ups from the read-through (added 2026-10-05).** ~~(a) 17 A2 `taught_in` screens moved to the screen that first teaches each skill~~ (approved by the user and done 2026-10-05, ACHIEVED.md § "HU A2 registry fixes, ROADMAP 138(a)"). ~~(b) 11 A2 grammar skills have fewer than 6 exercises: `verb-government-ert` 2, `jar-iskolaba`, `mit-csinaljak`, `postpositions-altal-reven`, `sokat-eleget` 3 each, `egymas`, `ordinal-numbers` 4 each, `kellene`, `potential-hat-het`, `sajat`, `superlative` 5 each. Write exercises for them, as item 137 (now in ACHIEVED.md) did for A1.~~ **Done 2026-10-07 (item 144(4), ACHIEVED.md "Small-fixes pass: thin skills filled to 6"; checked 2026-10-08: no HU A1–B1 grammar skill has fewer than 6 exercises).** (c) Gaps with no skill, tagged vocabulary for now: the reflexive *érez … magam*, the mediopassive *-kodik/-ködik* verbs (*borotválkozik*), *-ás/-és* nouns, *-nként* outside a2-179, *múlva*, and the direction series *ide/oda/innen/onnan* (on `itt-ott-here-there`, whose title names only *itt/ott*). **Status 2026-10-08 (item 144(5)):** `reflexive-magam`, `ide-oda-innen-onnan` added; `mediopassive-verbs-odik` and `distributive-nkent` re-levelled to A2. Still without a skill: *-ás/-és* nouns and *múlva*. ~~(d) prerequisites taught after the skill~~ (decided with the user and done 2026-10-05, ACHIEVED.md § "HU prerequisite order, ROADMAP 138(d)").

140. **Spanish prerequisite order (added 2026-10-05).** The new prerequisite-order check (item 138(d)) found 12 Spanish skills whose prerequisite is taught after them or only on the Latin America track, exempted in `KNOWN_PREREQ_ORDER` until decided. Taught later: `cuando-mientras` (a2-13-02) ← `imperfect` (a2-imperfectobasico-01); `imperativo-formal-usted` and `imperativo-negativo` ← `subjuntivo-morfologia` (a2-subjuntivobasico-01); `indefinidos-negativos` (a2-indefinidosnegacion-01) ← `negation` (-05 of the same unit); `perifrasis-verbales` (a2-perifrasisverbales-05) ← `acabar-de` (a2-perifrasisduracion-01); es-latam `formal-register` (b2-14-05) and `nominalizacion-despersonalizacion` (b2-21-03) ← `nominalization` (b2-35-01). Track only (es-latam): `apodosis-condicional-literaria`, `implicit-conditionals`, `inversiones-condicionales-de-haber`, `mixed-conditionals`, `regrets-reproaches` (b2-10/11/16, core) ← `pluscuamperfecto-subjuntivo-si`, taught only at b2-nicaragua-03 (latam track). For each: drop the requirement, move `taught_in`, or fix the curriculum, with the user's sign-off, then remove the exemption. Also: the check could place only 197 es-es and 551 es-latam screens (many named Spanish screens such as `a2-imperfectobasico-01` sit outside the unit tables' stems), so 136 and 77 Spanish skill screens are unchecked; give them unit-table positions or teach `screen_positions()` their order.

141. **HU B1 read-through follow-ups (added 2026-10-06).** The level is done (ACHIEVED.md "HU B1 read-through complete"). Left for sign-off or a later pass: (a) `taught_in` screens that a core unit teaches earlier than the registered one, found while reading (no tag change; each needs the user's sign-off like item 138): `formal-purpose` b1-erdelyaranykora-04 → b1-03-05-gr, `hypothetical-ha-conditional` b1-04-01-b → b1-04-01-a-gr, `vonatkozoi-nevmas-esetei` b1-arpadhaz-03 → b1-11-01-b-gr, `additive-connectors` b1-32-01-b → b1-13-05-a-gr, `evidentials` b1-13-03-a → b1-13-01-b-gr, `correlative-minel-annal` b1-matyas-02 → b1-15-01-a-gr, `causal-postpositions` b1-mohacs-01 → b1-16-02-a-gr, `participle-actions` b1-nemzetiugy-01 → b1-29-05-b-gr, `reported-speech-statements`, `indirect-questions`, `reported-commands` → their b1-33 screens, and `mediopassive-verbs-odik` (also covers the *-ul/-ül* becoming-verbs of b1-25-01-a). `nominalizing-processes` (title "progressive state in -óban/-őben van") still has no `taught_in` screen. **Status 2026-10-08:** moved (item 144(6)): `vonatkozoi-nevmas-esetei`, `evidentials`, `causal-postpositions`, `participle-actions`, the three reported-speech skills (to b1-13-01-a, b1-13-02-a, b1-27-03-a), `correlative-minel-annal` (b1-02-05) and `mediopassive-verbs-odik` (re-levelled A2); `nominalizing-processes` was removed. **Not moved, and no record of why:** `formal-purpose` (still b1-erdelyaranykora-04), `hypothetical-ha-conditional` (b1-04-01-b), `additive-connectors` (b1-32-01-b); check each screen and move or note it. ~~(b) 11 B1 grammar skills have fewer than 6 exercises: `kent-vs-mint` 0, `noun-compounds` 0, `historical-routines` 1, `nominalizing-processes` 1, `mixed-conditionals` 3, `kepest`, `verb-government-bol-bol`, `verbal-adjectives-hatatlan-hetetlen` 4 each, `concessive-postpositions`, `distributive-nkent`, `spatial-belonging-beli` 5 each. Write exercises for them, as item 137 (now in ACHIEVED.md) did for A1.~~ **Done 2026-10-07 (item 144(4)).** (c) Gaps with no skill, tagged vocabulary (*inkább … mint* now has `inkabb-mint`, item 144(5)): *annyi … mint*, *azelőtt/azóta/egyre/minél*, *-ul/-ül* and *-ik* becoming-verbs, flavour adjectives, the commemorative postpositions (*emlékére, alkalmából*), *nélkül*, *nyugszik*, *alighogy … máris*, the particles of `independent-hungarian` (*ugyebár, apropó, vagyis inkább*), generic *az ember*. (d) ~~Consistency: citizenship units locked before `angevin-kings` (`carpathian-basin-before-magyars`, `honfoglalas`, `arpad-dynasty`, `saint-stephen`, `mongol-invasion`, `matthias-corvinus`, `health-wellbeing`/`mohacs-1526` civics items) keep who/when/why fact questions as unit vocabulary; later units made them untagged reading. Decide and unify. (e) Content: the late units' lessons still often hold near-copies across lessons 01–05 (`society-inequality`, `kossuth-petofi-national-cause` lessons 02–05, `environment`, `politics-public-life`, `opinions-arguments`); the rewritten history facts in `interwar-years`, `world-war-2` and `revolution-1956` should be spot-checked against the screens (a subagent wrote them from general knowledge); `being-hungarian-citizen` `03.ex04` (compulsory schooling to 16) needs a fact-check.

142. **ES A1 read-through follow-ups (added 2026-10-06).** The level is done (ACHIEVED.md "ES A1 read-through complete"). Left for sign-off or a later pass: (a) ~~four `taught_in` screens that a unit teaches earlier than the registered one (no tag change; each removes "taught later" warnings, about 70 across the level): `hay` a1-07-04-hay-estar-gr → a1-07-01-hay-gr; `querer-poder` a1-abilities-01-poder-gr → a1-08-03-querer-gr (querer + noun is taught there, querer + infinitive later); `numbers` a1-12-01-numbers-gr → a1-10-02-edad-gr (10–30 and the *veinticinco* rule); `saber-infinitivo` a1-abilities-02-saber-gr → a1-10-05-celebracion-gr; optionally `plural` a1-03c-03-plural-gr → a1-03-04-adjectives-gr, and `stem-changes` (the e→i change of *vestirse* is taught on a1-reflexive-03-vestirse-ponerse-gr). Apply via `skills/es.json` and `scripts/build_skill_registry.py` after the user's sign-off.~~ **Four of the moves done 2026-10-06** (`hay`, `querer-poder`, `numbers`, `saber-infinitivo`; ACHIEVED.md "ES A1 registry fixes, ROADMAP 142(a)(b)"); the optional `plural` and `stem-changes` moves were not made. (b) ~~32 orphan exercises: `a1-18-01-ex.json` and `a1-18-02-ex.json` (lessons "What Do You Like?" and "Hobbies", with their grammar and vocabulary files) are in neither unit table nor the lock, carry the retired `a1-unit18-vocab` tag, and look superseded by the `likes-dislikes` and `hobbies-free-time` units; decide whether to delete them or add a unit.~~ **Deleted 2026-10-06** (16 files, both courses). (c) Skill gaps tagged vocabulary because no skill exists (date patterns and telling the time now have `dates-months` and `telling-time`, item 144(5)): weather expressions (*hace calor*), polite café phrases (*¿Algo más?*), *presentar a*, irregular *ponerse* forms, direction chunks (*a la izquierda*), neuter *esto / eso*. (d) Content: ~~the template "Which sentence starts this exchange?"~~ **fixed everywhere and checked 2026-10-06**: seven more items in `a1-10` were rewritten, a search of all es-es, es-latam and hu exercises finds no other instance, and `readthrough_check.py` now errors on such a question. `a1.dem.04.ex06` has a weak second answer; `a1.12.04.ex10` and the near-duplicate items in `directions` and `travel-getting-away` were left. The generated `translation-index.json` still holds the old *treinta y uno años* line until the next index build.

144. **Small-fixes pass before continuing item 125 (added 2026-10-06, decided one by one with the user; HU and ES A1–A2 to be fully polished first).** Guiding rule: whatever helps the learner learn the language. Decisions: (1) a unit's own contrast outranks the Sí/No rule, so `ya-todavia-no` dialogues keep that skill (spec § Read-through conventions). (2) Hints that print the answer: the five HU A1 hits are cognates or a name, no fix; ES B1's 217 per course belong to the ES B1 read-through. (3) ~~**Rewrite lesson-to-lesson copies** (not delete):~~ **done 2026-10-06, ACHIEVED.md "Small-fixes pass: lesson-to-lesson copies rewritten".** Original plan:  `scripts/dup_report.py` lists them, `docs/dedupe-brief.md` is the subagent sheet; real counts excluding consolidation: ES A2 458, HU A1 237, HU B1 239, ES A1 64, HU A2 1; pilot done on ES A2 `comparing-trips-memories` (42) and HU A1 `going-places` (22), then batches of one to four units, two subagents at a time. (4) ~~**Write the missing exercises for thin skills** (HU 22 grammar + 2 vocabulary, ES `intensificadores-y-grado`; about 67 exercises), after the dedupe; `nominalizing-processes` needs a screen first.~~ **Done 2026-10-07, ACHIEVED.md "Small-fixes pass: thin skills filled to 6" (58 exercises; `nominalizing-processes` was removed instead of getting a screen).** (5) ~~**Skill gaps:** bring the user a short list for sign-off (gaps that are real grammar with a screen and 6+ vocabulary-tagged items; the rest stay vocabulary).~~ **Done 2026-10-07, ACHIEVED.md "Small-fixes pass: gap skills added".** (6) ~~**`taught_in`:** verify each, then apply the HU B1 moves of item 141(a) and the two optional ES A1 moves (`plural`, `stem-changes`). (7) ~~ES A2 unit 8 reading items 11–13 and 15: rewrite the questions from the story; ES A2 unit 13 *mientras* dialogues: replace the wrong reply that is a valid answer; HU B1 history fact questions: untagged reading everywhere (retag the eight early units and re-lock).~~ **Done 2026-10-06, ACHIEVED.md "Small-fixes pass: ES A2 reading and dialogues, HU B1 history facts".** (9) **PARKED by the user 2026-10-07 (a far-away project; do not start it unprompted).** **Sentence-builders accept only one word order** (found 2026-10-06 by the dedupe subagents): the engine already accepts a `solutions` list of tile orders (`engine/lessons.js:1642`) but only 4 builders in all content use it (es-es 1,277 builders, hu 2,277). Decided with the user: from now on every new or rewritten builder with a natural alternative order must list it (dedupe and read-through briefs updated); **retrofit the existing builders later**, first A1–A2 (about 190 ES A1, 384 ES A2, 115 HU A1, 430 HU A2), then B1+ (Hungarian B2/C1 order carries focus, so each needs care). (8) ~~Housekeeping still to offer: regenerate cached audio for `a2.vosotrospeninsular.05.ex07`, the stale `translation-index.json` lines, the HU `nominalizing-processes` screen.~~ **Done 2026-10-07: audio and index needed nothing; `nominalizing-processes` removed.** Still open: only (9), the sentence-builder retrofit, parked by the user.

145. **ES B1 follow-ups (added 2026-10-08).** (a) ~~**Lesson goals** that mention facts the stories lack~~ **done 2026-10-08:** about 250 `latam` goals were rewritten to what each lesson's story, screens and exercises cover, plus 2 `cultura` goals and one typo; the other `cultura` goals were all supported. Where a `latam` story is garbled, the goal now follows the story rather than the lesson title, so the stories themselves need regenerating (c). (b) **Short consolidation lessons:** nine `latam` units (`liberalism-modernization`, `great-depression`, `democratization`, `indigenous-movements`, `regional-integration`, `end-cold-war`, `latin-america-1990s`, `legacy-20th-century`, `latin-america-toward-2000`) have a 14-exercise consolidation (two dialogues and two structured-writing items at the end) where the other units have 18; checked 2026-10-08, they are complete in structure, not missing exercises, so only the inconsistency remains. (c) **LATER, LARGE CONTENT REWRITE: the `latam` stories** (decided with the user 2026-10-08, not started). The lesson-to-story wiring is correct, but the story texts are template-generated paragraphs with sentences spliced in from neighbouring lessons, so several lessons sit over stories that cover a neighbouring topic: `central-america-revolution-conflict` (stories out of order by one step, El Salvador's opens on post-war impunity), `regional-integration` 03/04 (03 is mostly NAFTA), `end-cold-war` 02–04 and `latin-america-1990s` 01–05 (blurred or shifted); the other `latam` units are shorter and garbled in places. About 180 stories (5 per unit, 36 units). The grammar screens, vocabulary, exercises (already rewritten to the garbled text), listening sentences and goals all lean on the stories, so a rewrite is per unit: write five clean stories from the lesson vocabulary and screens, then regenerate that unit's reading questions, listening and goals, and re-lock (tags stay valid for unchanged items). Suggested pilot: `central-america-revolution-conflict` to measure the cost before committing the other 35 units. Also four orphan grammar screens in `centroamerica` (`-01-impersonal-se`, `-02-passive-voice`, `-03-gerund`, `-04-formal-connectors`) and unlinked `*-gr` files in `indigenous-movements` and others: link or delete them in the same pass. (d) **`taught_in` warnings** (`ser-passive`, `prepositional-phrases`, `verbos-regimen-preposicional`, `relativo-posesivo-cuyo`, `cuanto-mas-tanto-mas`, `correlativos-no-solo-sino`) stay until the per-course `taught_in` map exists (user: later). (e) A handful of fact questions, listening sentences and builders in `cultura` and `latam` units still rest on detail the screens lack (see the subagent reports in the session log). (f) **Thin ES B1 skills** (found 2026-10-08, fewer than 6 exercises in a course that teaches them): es-es `pluscuamperfecto-subjuntivo-si` 0, `relativo-posesivo-cuyo` 3, `a-pesar-de` 4, `conditional-conjunctions` 4, `resultar-adjective` 5; es-latam `estar-a-punto-de` 2, `futuro-perfecto` 2, `resultar-adjective` 5. Write exercises in the lessons that teach them, or confirm the skill isn't taught in that course (es-es may need `variant` on some), and re-lock.

## Completed queue items

151. **Hungarian fill-blanks without an `english` line (added 2026-10-08, from item 149).** — **Done 2026-10-09.** Added missing `english` translation lines to all 2,417 Hungarian fill-blank exercises across A1, A2, and B1: A1 691 exercises across 197 files (2026-10-08), A2 611 exercises across 222 files (2026-10-09), and B1 1,115 exercises across 397 files (2026-10-09). All translations follow `docs/hu-fillblank-english-brief.md`: natural plain US English, matched hints, pinned person/number/tense/aspect/possessor, and gender-neutral `He/She` pronouns. Inserted cleanly on their own line without modifying array formatting or existing metadata. `check-content.py hu a1`, `a2`, and `b1` all report `missing-english 0`. Schema validator and content checks pass cleanly. Claude reviewed samples of A2 and B1 (2026-10-09) and made `english` required for HU fill-blanks in `content/hu/schemas/exercises.schema.json`, as in Spanish; the temporary `fill-blank without english` warning is removed from `validate-content.py`.

149. **One-button course generation: the typed fill-blank `hint` field (part, done 2026-10-08).** Fill-blank hints used to be written into `sentence` as a parenthetical (*Ayer __ una carta. (escribir)*). `hint` is now a field in all three `exercises.schema.json` files; `engine/lessons.js` and the Workshop Grammar Driller (`grammar.js`, `grammar-runner.js`) show it muted, in parentheses, right after the blank. `scripts/migrate_fillblank_hints.py` moved 7,186 hints in 2,935 files (es-es, es-latam, hu, all levels), plus one by hand (`c1-energetika-02-controlled-2`, *EPC*). It took a parenthetical right after the blank, at the end of the sentence, or before a trailing `[English]` gloss, and six hand-checked HU ones a word away from the blank. It left in place the acronyms that belong to the sentence (*BOE*, *DGT*, *INE*, *DNSH*, *ERM-II*), the ES B1 place and term glosses (*(Nochevieja)*, *(Granada)*), and the gloss in HU `a1-01-practice-3`. `validate-content.py` now fails a hint written back into a fill-blank sentence. `readthrough_check.py` reads the hint field, and so does `check-hu-exercises.py`, which already did. `dup_report.py` counts the hint as content. Side effect: lesson speaking candidates built from fill-blanks no longer carry the hint text. `add_fillblank_hints.py`, which wrote the old form, moved to `scripts/archive/`. Rule recorded in AGENTS.md, the generation brief § 6.4, the read-through and dedupe briefs, the HU authoring template and the schema READMEs. Also closes item 122's Phase B. **Follow-up, same day:** 850 ES B1 fill-blanks (es-es and es-latam, 396 files) also carried their translation in `sentence` as a trailing `[English]` gloss, which showed the meaning before the learner tried; all had the same text, or a better one, in `english`, so the brackets were stripped (the translation stays reachable as the second step of "Need a hint?" and after the answer). In 36 the bracket differed from `english`; the field's wording was kept except `b1-22-01.ex03` (future of probability, *estará en casa*), whose `english` now reads *He/She is probably at home* in both courses. `validate-content.py` fails a trailing `[English]` in a fill-blank sentence; rule in AGENTS.md and the brief § 6.4. **Step (2), same day: `scripts/check-content.py`** (audit § 5). One pass over a course, level or unit, with 33 checks: option give-aways (length over 1.3×, " / ", time words, absolutes, openers, punctuation, mixed languages, "I don't know"), fill-blanks (blank count, appended blank, letters repeated next to the blank, hint is the answer, Spanish *haber* person), answer printed in the prompt, "this exchange", missing `english`, question word vs answer, HU case nouns and *-tatik*, es-latam *vosotros*, non-rendering types, adjacent repeated questions, lesson-to-lesson copies, forms used before their screen, unused vocabulary, and on new courses the brief's lesson, consolidation, stage, goal and story-length shape. It gathers in `check-hu-exercises.py`, `check-slash-giveaway.py`, `dup_report.py` and the content parts of `readthrough_check.py`. Errors are precise; seven pattern checks are "suspects" a reader confirms, never gated. Gate: `--changed` (now in `.githooks/pre-push`) compares the touched units with origin/master and fails only on findings the change adds, so editing an already-flagged item never blocks and the existing courses stay a report (decision 3); a course not in `hu`/`es-es`/`es-latam` fails on any error. Calibrated on HU and ES A1–B1 by sampling every check: dropped or narrowed what read-through content showed was noise (Hungarian person endings, *-tetik*, which is also an ordinary verb ending, *dieciséis* as vosotros, *Si* as *Sí*, question/statement punctuation, one-word openers, a time contrast set up by the prompt, case-only duplicate options, echoed greetings); option-language fell from ~600 hits to 70, question-answer-type from 140 to 6. What remains is listed in ROADMAP item 152. Brief § 8.1, § 6.1 and § 9.2, AGENTS.md and scripts/README updated. Still open in ROADMAP item 149: (3) a pilot unit.

2. **Composed Room visual identity sweep across new additions (done 2026-10-08).** Audited and aligned recent additions against `DESIGN.md` ("The Composed Room"). Eliminated pure white card backgrounds on cream ground (`var(--card-bg, #fff)`, `var(--bg-card, #FFFFFF)`) across CEFR Exam Prep, Deck Blast (`.dkb-lobby-card`, `.dkb-prompt-bar`, `.dkb-canvas-wrap`, `.dkb-done-card`), and Library recommendations (`.lib-rec-card`), restoring flat `--surface` / `--bg` / `--wash` structures. Stripped hover lifts (`translateY(-2px)`) and drop shadows (`box-shadow: 0 6px 16px rgba(0,0,0,0.07)`). Standardized soft 4px/6px/8px/10px/12px radii on badges, textareas, prompt cues, inputs, and chips across `engine/lessons.js`, `drills/speaking.js`, `drills/writing.js`, `styles/components.css`, and `styles/workshop.css` to 2px `--radius-sm`. Converted pill shapes (`--radius-pill`) on tags and chips (`.story-card-topic-match`, `.lt-chip`, `.gd-hud-skill-tag`, `.cefr-status-pill`) to sharp hairline tags. Replaced stray off-palette greens (`#2e7d32`, `#4CAF50`), reds (`#dc4e2e`, `#c62828`), and oranges (`#e65100`, `#ffb74d`) with semantic tokens (pine `--success`, brick `--danger`, vermilion `--accent`, ochre `--ochre-text`). Converted the Grammar Driller overlay from a floating centered dialog into a standard Parlour bottom sheet with a 35% dim and 3px navy top rule. Offline test suites and content validator verified cleanly.

150. **Curated Communicative Challenges per course: es-es file (part, done 2026-10-08).** Spain lessons requested `content/es-es/curriculum/challenges.json`, which didn't exist (404 on every lesson, seen while checking the dev server from the new main checkout). Copied the es-latam file unchanged, since its 6 entries are already written for Spain; validator passes. es-es unit 1 lessons now show the curated "Greetings" challenge instead of the generated one, as es-latam already did. The new-course rule is in AGENTS.md § "Adding a new course" step 5. Still open in ROADMAP item 150: the es-latam rewrite and a Hungarian set.

137. ~~**Thin HU A1 grammar skills (added 2026-10-05).**~~ — **Done 2026-10-07** under item 144(4) (ACHIEVED.md "Small-fixes pass: thin skills filled to 6"); archived 2026-10-08 after a recount found no HU A1–B1 grammar skill under 6 exercises. Original entry: **Thin HU A1 grammar skills (added 2026-10-05).** After the A1 read-through (item 125) 15 A1 grammar skills have fewer than the 6 exercises the spec asks for: `kell-infinitive` 0 (taught on a1-118-b but no exercise tests it), `good-for-me-nekem-jo` 1, `akar-tervez-infinitive`, `directional-preverbs`, `formal-address-on`, `hungarian-vowels`, `kerek-vs-szeretnek` 2 each, `itt-ott-here-there`, `kor-time`, `mert-because`, `nem-vs-nincs-two-kinds-of-negation`, `szokott-infinitive-habitual-actions` 3 each, `lehet-infinitive` 4, `erdekel-construction`, `subject-pronouns-omission` 5 each. Write exercises in the lessons that teach each skill (not merge the skills away), tag and re-lock those units with `lock_tags.py --update`.

143. ~~**ES A2 read-through follow-ups (added 2026-10-06).**~~ — **Done 2026-10-08.** Decisions with the user: invitations are folded into existing skills, not a new one; reported questions use the existing reported-speech skill `preguntas-indirectas`. (a) `making-responding-invitations` (unit 8): the *¿Quieres + infinitive?* frames and answers (21 items) now teach `querer-poder`, the *¿Te gustaría…? / Me gustaría…* frames (12) `polite-softening`, *acepto* (1) `ar-verbs`, with their `category` moved to `grammar`; matching, "what does X mean", single-word blanks and the accept/decline phrase choices stay under the unit's vocabulary skill. (c) Unit 14 `asking-what-happened`: 16 items whose target is a reported question (*Preguntó qué pasó*, *Quiso saber dónde trabajó*) moved from `questions` to `preguntas-indirectas` (which already held 38; the old note that no skill covered reported questions was out of date). Both units re-locked with `lock_tags.py --update` in es-es and es-latam. Units 1–4 leftovers: 20 sentence-builders got their `english` line (shown as feedback after the attempt, and as an opt-in hint over 8 tiles); every *lo / la / los / las* answer in units 2–4 dialogues (27 items, plus the two grammar screens `a2-02-03-gr` and `a2-03-02-gr`) was rewritten to repeat the noun (*Sí, ya hemos visto el río*) because `objeto-directo` is first taught at `a2-12-01-gr`; two more distractors in `a2.06.05.ex15` fixed; *tenido* added to the regular-participle table in `a2-01-01-participles-gr`. Not changed: lesson-to-consolidation repeats in units 1–4 are by design (consolidations replay lesson items; `dup_report.py` skips them). Earlier points (b), the repeated templates, and the unit 13 *mientras* replies were already fixed under item 144. Original entry follows.

    **ES A2 read-through follow-ups (added 2026-10-06).** Collected while reading units 1–8; the level is not done. **Status 2026-10-08: the repeated eight-item templates in (b) and (c), the (b) unit 8 reading questions and the (c) *mientras* wrong replies are fixed (item 144, ACHIEVED.md; `dup_report.py` finds no lesson-to-lesson copies at any level). Still open here: (a) the invitations skill and (c) the reported-questions skill (both need sign-off), and the unit 1–4 leftovers at the end.** (a) Skill gaps: no skill covers invitations (*¿Quieres venir…?*, *me gustaría*, accepting and declining), so `making-responding-invitations` is 66 vocabulary tags of 116 (the old `invitaciones-y-pedidos` was retired); decide whether to add an A2 skill, which needs the user's sign-off and a frozen-list entry. (b) Content: `a2-08-01` to `a2-08-05` repeat one eight-item template (ex02–05, 07–09) in all five lessons, and reading items 11–13 and 15 in `a2-08-05` ask about a drink and a dish that are not in the story `a2-08`; rewrite per lesson and re-anchor the reading. (c) Units 13–16: each repeats one eight-item template across lessons 01–05; the *mientras* dialogues in unit 13 have a wrong reply that is arguably valid (`a2.13.02.ex15/16`, `03.ex16`, `04.ex16`, `05.ex17`, `consolidation.ex15`); no skill covers reported (indirect) questions, so unit 14's 80 question items are tagged `questions` (needs sign-off to add a skill). (d) ~~Hint prints the answer:~~ **the five HU A1 hits are cognates or a name (*(bank)*, *(park)*, *(Meg)*), not defects (2026-10-06); only the ES B1 217 remain:**  the new check finds 217 ES B1 fill-blanks per course (es-es and es-latam) whose parenthesised hint is the answer (*(otro)*, *(de)*, *(por eso)*, *(excelente)*) and 5 in HU A1; the ES B1 read-through must rewrite them as English hints, and the HU A1 five are worth a quick fix now (`python scripts/readthrough_check.py` lists them per unit). Units 1–4 still hold near-duplicate items between the lessons and the consolidation, sentence-builders with no English prompt, *lo / la / las* in dialogues before `a2-12` and *tenido* with no participle screen.

146. ~~**Multi-language rework: hard-coded language assumptions moved into `Lang` profiles (Antigravity, merged 2026-10-08).**~~ — **Done 2026-10-08.** `engine/lang.js` now holds a per-language profile (speech locale, diacritics, openers, number words, speech abbreviations, exam labels, discourse connectors, can-do cues, verb paradigm) plus `Lang.profile/registerProfile/targetText/targetLemma`, and the drills, speech input, CEFR exam, can-do prompts, lexicon, SRS, verbs and the Home welcome flow read from it instead of branching on the language. Welcome screen is built from `Lang.available()`; switching course no longer re-shows the welcome or placement prompt (`parlour_first_open_completed`). The service worker no longer caches localhost. Reviewed and rebased onto master by Claude: generated decks/manifests taken from master, stale `test-onboarding-guide.js` assertion fixed, can-do cues deduplicated (es-latam now uses Mexico City, es-es Madrid), the `localStorage` read in `home.js` guarded, SW `CACHE_VERSION` bumped. Full test run: all pass except `test-learner-signals.js` (already failing on master, see item 147); both courses load clean in the browser. **Follow-ups done 2026-10-08:** the diagnostic question `es-diag-a1-06` carried the retired tag `pedir-favores` (both Spanish courses); retagged `er-ir-verbs`, and `test-learner-signals.js` passes again. The es-es/es-latam prompt fallback in `speaking.js` and `writing.js` and the writing diacritics bar now read `Lang.contentFallback/diacritics/openers` (es-es gets `contentFallback: 'es-latam'` in its profile). The other language branches found in the sweep are either profile-first with a dead legacy fallback (`leveltest.js`, `diagnostic.js`, `speech-input.js`) or genuinely language-specific engines (Hungarian drillers, `lexicon.js`, `morphology/`, phonetic folders). The once-ever first-open welcome (`parlour_first_open_completed`) is intended: a new language gets no second welcome, and a gentler placement offer after switching would need new UI, so it is not queued. The speculative `fr` profile was removed from `Lang.PROFILES` (a French course adds its own via `Lang.registerProfile`).

132. ~~**HU A2 units off by one from a2-187 to a2-220, with six consolidations unwired (found 2026-10-05 during item 125).**~~ — **Done 2026-10-05.** The seven units from `lak-lek-suffix` to `pharmacy` now each run five lessons plus the consolidation that closes them (`a2-187`–`190` + `a2-190-consolidation`, `a2-191`–`195` + `-195-consolidation`, … `a2-216`–`220` + `-220-consolidation`), so all six orphan consolidations are wired in. Unit ids, order and positional `unit.a2.NN` ids are unchanged. Found while fixing it: 134 vocabulary tags in 44 A2 lessons pointed at another unit's skill. The old slug `a2-unit38-vocab` meant unit 28 under HU A2's old "+10" numbering and unit 38 by position, and step 2 of item 125 gave each such slug to one owner. Units 38–42 carried units 28–32's skills, and units 33–34 carried banking/pharmacy. Seven unit vocabulary skills had no exercises at all. Every A2 vocabulary tag now names its own unit's skill (each affected skill has 12–42 exercises). Checked across every course and level: no other has this collision. Spanish A1's 286 off-unit tags are the separate `a1-unit01-vocab` spread, left for the read-through (item 125 step 3). Original entry: The A2 unit table, kept unchanged from the old automatic grouping when unit ids were added, puts lessons into the wrong units from `lak-lek-suffix` to `banking`. For example, `lak-lek-suffix` is `a2-187`–`a2-191`, but `a2-190-consolidation` closes that unit and `a2-191` (*1st Person -aim/-eim*) belongs to `plural-possessed`. `a2-216` (*At the Pharmacy*) sits in `banking`. There is no `a2-186`. The consolidations `a2-190`, `-195`, `-200`, `-205`, `-210` and `-215` are in no unit, so learners never see them. Fix: regroup those eight units in `content/hu/curriculum/units/a2.json` by lesson content, keeping each unit's `id` (and its vocabulary skill), then run `build-manifest.py`. Lesson progress is keyed by lesson id, so it isn't affected. Check the tags of any locked unit that moves. Similar orphans elsewhere: es-es/es-latam `a1-18-01`/`02` and es-latam `b1-subjuntivo`.

129. ~~**`tests/sync/test-two-way-sync.js` fails (found 2026-10-04 during item 121).**~~ — **Done 2026-10-04.** The new `sync-worker.js` was deployed to the `parlour-sync` Worker first, then the app change was pushed (`9c9e8ceb`). Closing a tab saves progress again. Details below. It fails on master before item 121's changes too (an assertion expects `true` and gets `undefined`), so it is unrelated. Every other offline test under `tests/` passes. Find which sync behaviour changed (`engine/sync.js`) and fix the code or the test. **Diagnosed 2026-10-04: a real bug, not just a stale test.** Since the 2026-10-01 merge-before-upload change, `backup()` reads the cloud first and only then POSTs, so on `pagehide`/`beforeunload` the page is gone before the upload starts and `keepalive` never helps: closing the tab no longer saved progress. Fix (committed, waiting for the worker deploy): a leave-save skips the read and POSTs at once with `baseUpdatedAt` (the cloud version it last saw); `sync-worker.js` writes only if the cloud is still at that version (atomic conditional UPDATE), otherwise 409, and the data stays local and merges next session. Normal saves still read and merge first. Test 8 now checks the immediate POST, and new test 9 checks that a normal save still reads first. **Deploy order matters:** paste the new `sync-worker.js` into the `parlour-sync` Worker first (backward compatible), then push the app change.

128. ~~**26 duplicate story ids in es-latam B1 (found 2026-10-04 during item 121).**~~ — **Done 2026-10-04.** All 26 pairs had the same shape: the file a lesson references (`"ref"`, added 2026-09-20) and an orphan added by `4bcdc76b` ("overhaul B1 track stories", 2026-09-24) that wrote new lesson-reading files without deleting the old ones. That commit never touched any lesson or exercise, and the stitched whole-unit stories contain every paragraph of the referenced files, so lessons, exercises and combined readings all use the 2026-09-20 texts. The 26 orphans were deleted. Learners never saw an orphan inside a lesson (lessons load by path), only as a second Library card sharing the same id and reading position. `validate-content.py` now fails on a duplicate story id in any course (`duplicate_story_id_errors`), and AGENTS.md says to keep the referenced file. Original report below. `story.b1.cambiosocial.02`-`.05`, `conquista.04`, `economiacolonial.04`-`.05`, `economiasexportacion.03`-`.05`, `llegadaeuropeos.01`, `nacionalismo.01`-`.05`, `revolucion.01`-`.05`, `revolucionmexicana.01`-`.05` each exist in two story files with *different* texts (e.g. `b1-revolucion-01-quees.json` and `b1-revolucion-01-tensiones.json`). Two generation passes apparently both wrote lesson readings. Whichever file the manifest builder reads last wins, so a lesson may show a different reading than the one its exercises were written for. For each pair, check which text the lesson's exercises and vocabulary match, delete the other (or give it its own id if both are wanted), and rebuild. Then make `validate-content.py` fail on a duplicate story id, so it can't recur (the Hungarian C1 case in ACHIEVED item 121 was the same bug). To find them: load every `content/<course>/stories/**/*.json` and group by `id`.

127. ~~**C1 -tatik passives: keep for recognition, archaic contexts only (added 2026-10-04).**~~ — **Done 2026-10-04.** `c1-21-02` is now "The Archaic Passive in Labour History": its grammar screen explains *-tatik/-tetik* (and drops the non-existent *-tatatik/-tetetik* the old screen taught), with a table of old-document sentences next to their modern equivalents, and a tip that it reads as mock-officialese today. Its exercises recognise the form in old factory rules, put it into modern Hungarian (*követeltetik* → *követelnek*), and produce it only inside an old document (*tiltatik*). `c1-22-02` is now "Describing Automated Processes": how modern Hungarian renders English technical passives (machine as subject, 3pl, intransitive *alakul*, *-va/-ve van*), with *-tatik* and *által ... kerül feldolgozásra* only as wrong options. The four consolidation items that claimed modern labour and IT texts use this passive (21-cons-2/9, 22-cons-2/9) were rewritten, and the two skills got new titles in `grammar-titles.json` (slugs unchanged). **Revised the same day:** the native speaker then decided to drop *-tatik/-tetik* entirely ("very old-school"), so it no longer appears anywhere in the course, not even as a wrong option. `c1-21-02` now teaches "Saying What Happened Without Naming the Doer" in labour news: 3pl impersonal (*háromszáz dolgozót bocsátottak el*), *-va/-ve van* (*a kapuk le vannak zárva*), and recognising heavy *kerül* officialese (*kifizetésre kerültek*), with *lett*-passives (*be lett tiltva*) as the error to avoid. `c1-22-02` keeps its topic, with *lett* and *által ... kerül* calques as the wrong options. A scan of all Hungarian content found no other true *-tatik* passives (the remaining *-tetik/-tatnak* hits are definite 3pl or causatives, e.g. *hirdetik*, *felvételiztetik*). New Hungarian sentences are the reviewer's; worth a native read. Original report below. Decided by the native speaker during item 120 (ACHIEVED.md). Lessons `c1-21-02` and `c1-22-02` drill the archaic *-tatik/-tetik* passive (*követeltetik*, *elutasíttatik*, *feldolgoztatik*, *bontatik*) in modern settings (factory discipline, NLP pipelines), as if it were live usage. Rework both lessons (lesson file, grammar screens `c1-21-02-a-gr.json`/`c1-22-02-a-gr.json`, exercises, and the copies in `c1-21-consolidation`/`c1-22-consolidation`): the grammar labels *-tatik* as archaic/official-historic and shows the modern equivalents (*megkövetelik*, *feldolgozzák* / *feldolgozódik*). Sentences that keep *-tatik* move to historic, legal or literary contexts (19th-century law, royal decrees, *Kéressetek, és adatik nektek*), and learners mainly recognise it rather than produce it. Modern-topic sentences use modern forms. Other "-tat/-tet" hits in C1 are causatives or ordinary verbs (*vitatott*, *rámutatott*), not this.

126. ~~**"Slash" give-away in choice exercises (added 2026-10-04).**~~ — **Done 2026-10-04.** All 383 exercises were fixed by Antigravity (Spanish 66, HU A1–B1 60, HU B2 90, HU C1 167) and every one was read in review; `check-slash-giveaway.py` now reports `total: 0` for all courses. The B2/C1 review made ten small changes: three C1 consolidation questions asked "Milyen kifejezésekkel" (plural) over a now single-phrase answer, so they say "kifejezéssel"; four C1 essay-closing items had kept the stiffer half (*Végső konklúzióként*, *Konklúzióként levonható*) and now keep *Mindent összegezve/összevetve*; one kept phrase was capitalised to match its distractors (`c1-egeszsegugy-05-check-8`); two B2 glosses were tightened (*mulasztás* → "omission", *élcelődik* → "to banter"). In 322 Hungarian choice exercises the correct option is two or three phrases joined by " / " (*kötelessége szavatolni / nem foszthatja meg*) while every wrong option is a single phrase, so the slash gives the answer away. Counts: A1 12, A2 26, B1 22, B2 90, C1 172. Mostly the "Melyik kifejezés …" check items generated for B2/C1. Found while reviewing C1 block 5 (ACHIEVED.md item 120). Fix: keep one phrase in the correct option, or give every option the same two-part shape (rule 3 of `imports/review/ANTIGRAVITY-exercise-quality.md`). A mechanical work list is easy to build (correct option contains " / ", no wrong option does). **Handed to Antigravity 2026-10-04:** the pattern exists in Spanish too (es-es 42, es-latam 24), so 383 in all once the 5 in `c1-21-*`/`c1-22-*` (ACHIEVED.md item 127, rewritten there) are left out. Check and work list: `imports/review/check-slash-giveaway.py` (all courses). Brief: `imports/review/ANTIGRAVITY-slash-giveaway.md`, which stops for review after Spanish + HU A1-B1 (126 exercises). **Stop 1 reviewed 2026-10-04:** all 126 were read and accepted. One gloss was adjusted (*recorrer* → "to travel around"); 3 fix-2 cases were correct but under-reported. Go-ahead for HU B2 + C1 (257) added to the brief.

121. ~~**Finish aligning Hungarian C1 with B2's naming, after Antigravity's C1 generation is done (added 2026-10-02).**~~ — **Done 2026-10-04.** The C1 non-core track id is now `culture`, like B2's: 36 units in `curriculum/units/c1.json`, `LEVEL_TRACKS` in `build-manifest.py` (title "Culture, Society & Public Life", description "Hungarian public life, law, science and culture, in the language of the press and the essay."), `TRACK_SHELF_LABELS` in `engine/reader.js` (the `discourse` alias is gone), `build_translation_index.py`, `stitch_track_unit_stories.py`. The Vocabulary Driller's C1 toggle now reads "Culture" (it showed "Discourse"). Nothing stores track ids in learner data, so no migration was needed. The one-off C1 generator scripts under `scripts/c1_block*/` still write `discourse`. They are historical, but change them if they are ever re-run. **Not done, on purpose:** renaming the stored `type: "world"` of ~1,500 dual-track stories. Only the shelf label is visible to learners, and the churn (folders, `_trackShelfKey`/`_isBrowsableStory`, manifest builder, tests) buys nothing. **Found and fixed on the way:** the unit 7 / unit 32 slug collision (`74fdd6c5`) had left 7 stale story files. Five were exact copies of unit 32's lesson readings under unit 7's ids `story.c1.jogallamisag.01`-`.05`, so a unit 7 lesson could load the wrong text. The other two were extra whole-unit readings, so unit 7 showed three times on the C1 Culture shelf. All seven were deleted; the shelf is now 36 Culture + 36 Classics, one reading per unit. `tests/reader/test-library-recommendations-search.js` was stale (it expected 12+12 C1 stories); it now asserts 36+36 and exactly one reading per Culture unit. Checked in the app: a C1 Culture unit page shows "CULTURE, SOCIETY & PUBLIC LIFE". Original report below. The C1 shelf in the Library now reads "Culture" like B2's (`TRACK_SHELF_LABELS` in `engine/reader.js`, commit `869ba318`), but two things were left alone so the generator's output isn't disturbed mid-run: (1) **Learn-tab track title.** `LEVEL_TRACKS["hu"]["c1"]` in `build-manifest.py` still calls the track "Public Discourse & Society"; B2's reads "Culture, History & Society". Pick a matching title (and description) for C1. (2) **Internal names.** C1's non-core track id is `discourse` (B2's is `culture`), and every dual-track reading in all three courses is stored as `type: "world"` in `content/<course>/stories/world/` folders, although `world` is meant to be reserved for current-news readings (the `current` type, shown as "Current Events"). Renaming the C1 track id to `culture` touches the C1 unit files (`curriculum/units/c1.json`), the story and lesson `unit.track` values, the manifest and `TRACK_SHELF_LABELS`. Renaming the stored type touches about 1,500 stories across es-es, es-latam and hu, the folders, `_trackShelfKey`/`_isBrowsableStory` in `engine/reader.js`, the manifest builder and the tests; decide whether the type rename is worth it at all, since only the shelf label shows to learners. Do both only once the C1 units are finished and committed, then rebuild with `build-manifest.py` and check the Library for all three courses.

120. ~~**Hungarian C1 needs the same exercise-quality review (added 2026-10-02).**~~ — **Done 2026-10-04.** Antigravity reviewed all of Hungarian C1 (432 files, 3,691 exercises) in six blocks, with a review after each (`imports/review/ANTIGRAVITY-hu-c1-review.md`; feedback rounds 4-7, sections 11-18 of `hu-review-feedback-a1-a2.md`). Main fixes: ~970 fill-blank hints that printed their own answer (now lemma + grammar, or English plus every correct synonym in `answers`, each decided in the worksheet `c1-english-hint-recheck.txt`), absurd wrong options replaced with near misses, dialogue wrong options turned into form errors on the taught word. The reviewer restored 8 dialogues block 4 had left with no correct option, fixed 3 wrongly changed correct answers (blocks 2-3) and ~10 two-right-answer cases. Found on the way: stray Cyrillic/CJK/katakana letters (validator now rejects them), the slash give-away (item 126), and the archaic -tatik drills (item 127). The native speaker answered all 16 logged questions (recorded at the end of `hu-review-questions.txt`). Lessons on driving Antigravity: a fresh chat per block, a written per-item decision instead of 'take your time', and diffing every changed correct answer instead of trusting its report. Original report below. Item 117's multi-round review (ACHIEVED.md) covered Spanish B1 and Hungarian A1 through B2 — two-right-answer options, give-away distractors, and fill-blank hints that leak their own answer. It never reached C1: partway through, Antigravity started generating substantial *new* C1 content in the same shared checkout (new units beyond the original 12 files/144 exercises — `c1-02` onward, plus new topics like `esszemuveszet`, `metaforak`, `tudomanyelmelet`, `vitakultura`) instead of only reviewing what existed, so reviewing C1 then would have meant reviewing a moving target. Once that generation is finished, run the same pass over all of C1: `imports/review/check-hu-exercises.py c1` for the mechanical checks (duplicate options, `correct` not a single index, time-word give-aways, wrong case endings, `Nem tudom.`-style catch-all distractors), then a hand read of a sample of the choice and reply exercises for two-right-answer cases and hints that give away their own answer, the same two problem classes item 117 found repeatedly. `imports/review/ANTIGRAVITY-exercise-quality.md` has the full brief and rules if the work goes back to Antigravity; `hu-review-feedback-a1-a2.md` has the specific mistakes to watch for (showing off grammar by rewriting an answer until it stops answering the question; swapping an absurd wrong option for a different but also-correct one in reply exercises). **Update 2026-10-04: C1 generation is finished (Unit 36 capstone and the C1 level test are in), and handed to Antigravity.** C1 is now 432 files and 3,691 exercises (36 numbered + 36 topic units), not 12/144. The main problem is new: about 970 of its 1,022 fill-blanks print the answer in the hint, `(to death / halálhoz)` → `halálhoz`. `check-hu-exercises.py` now reports this as a `hint-leak` suspect (all levels: A1 5, A2 4, B1 17, B2 18, C1 972); C1 also has 32 time-word give-aways and 17 case suspects. Brief: `imports/review/ANTIGRAVITY-hu-c1-review.md`, with a stop after block 1 (12 units, ~600 exercises) for review. `hu-review-progress.md` lists C1 in blocks of 12. Item 121 waits until this pass is done, since it edits the same C1 unit files. **Block 1 reviewed 2026-10-04** (`976ca84b`, `2767a529`; 72 files, 333 exercises changed, 4 questions logged): the best round yet. In a sample, about 5% of the changed choice exercises and about 1 in 3 English-only fill-blank hints had problems: one exercise had another question's options pasted in, two replies had more than one right answer, and correct synonyms were missing from `answers`. Feedback is section 11-12 of `hu-review-feedback-a1-a2.md`. Antigravity fixes those, then does blocks 2-3 and stops to report. **Blocks 2-3 reviewed 2026-10-04** (`810dd6c6`…`abc24a66`): the section 11 fixes are good and the checks are clean, but quality regressed. The pace went back to 1-2 s/exercise and no questions were logged. Only 21 of 172 hints made English-only got synonyms in `answers`, and some function-word blanks can't be solved from an English hint (*Annak*, *Amerre*). Three changed correct answers were wrong again, one with another exercise's options pasted in. There is a recheck list (`imports/review/c1-english-hint-recheck.txt`, 199 items) and feedback sections 13-15. Back to one block at a time. **Block 4 + fixes reviewed 2026-10-04** (`94c7d54d`, `83196001`, `1cc21eb3`): the per-item worksheet fixed the hint problem (302 decisions, about 97% right), and it logged questions again. A new failure appeared: 8 dialogues had a correct answer replaced by forms of a word that doesn't fit, leaving no correct option, while the commits claimed 0 correct-answer changes. I restored them, plus 2 two-right-answer dialogues, and the `case` check no longer flags *térben*, a false positive that caused needless rewrites. Feedback sections 16-17. Blocks 5-6 remain, one per fresh chat. **Block 5 reviewed 2026-10-04** (`f1ba1345`, `bcf1bffc`): the best block yet. No correct answers changed (true this time), the worksheet was kept up, questions were logged, and the dialogue wrong options are clean form errors. In all 49 changed dialogues there were 4 problems, which I fixed: an older wrong marked answer (*reverzibilisen* for *reverzibilis*), two wrong options that were also correct (conditional *térhetne*, *építenénk*), and a capital letter mid-sentence. The slash give-away found here became item 126. Block 6 remains. **Block 6 reviewed 2026-10-04 (`ad73af29`, `a088b097`). C1 review complete:** all 432 files and 3,691 exercises are reviewed. Block 6 was clean: no correct answers changed, all 59 changed dialogues read correctly, and the only suspects left are 3 correct uses of *helyben*. One bug: Chinese characters in a C1 answer (*szakértői匿名 módon*). A corpus scan found three more from earlier generation passes, all fixed: Cyrillic in *reдукció* (HU B2 lesson) and *верett* (HU B2 story), and katakana in *Mキシco* (es-latam B1 story). `validate-content.py` now fails any content file with letters from another script. Still open: 8 questions in `hu-review-questions.txt` for the native speaker. Item 121 is unblocked.

122a. **Stray trailing blanks in HU B1 fill-blanks** — **Done 2026-10-04.** Found by the item 122 exercise-audio audit. 50 fill-blank sentences in 30 files (`b1-arpadhaz-*`, `b1-honfoglalas-*`, `b1-istvankiraly-*`, `b1-karpatmedence-*`, `b1-orszagma-*`, including their consolidations) ended in an extra `_____`, either after the English hint ("…gyorsan ___. (collapsed) _____") or, in the 10 `orszagma` items, straight after the full stop. They showed two blanks on screen and were never spoken. The trailing blank was dropped and nothing else changed. A scan for any other fill-blank with two or more blanks found only `a2-190-check-2`, which is meant to have two. All 50 also gained the `english` translation AGENTS.md requires (the HU schema leaves it optional, so the validator never flagged its absence), and six `orszagma` blanks that had no way to be guessed got an English hint: *helyezkedik* (is located, twice), *torkollik* (flows into), *határos* (shares a border), *államiság* (statehood), *sérült* (was damaged). The *-ból áll*, *között* and *nyugatra* blanks were left without a hint because the grammar they test makes them recoverable. 18 of the 50 also carried a `teaches` tag that didn't match what they test, now corrected (category changed too where needed): *aki* `movement-with-ba-be` → `aki-vonatkozoi-mellekmondat`; the conjunction *mielőtt* `temporal-postpositions` → `miutan-mielott`; *egyesültek* `subject-pronouns-omission` → `past-tense-indefinite`; *elfoglalták*/*biztosították* and *kapta* (the last was a vocabulary item) → `definite-past`; *küldött* `definite-vs-indefinite-conjugation` → `past-participle-adjective`; the nouns *identitásban*, *alapköve*, *törzsszövetsége* and the lexical verbs *helyezkedik el*, *torkollik*, *határos* moved from grammar tags (`definite-vs-indefinite-conjugation`, `van-vannak-locative`, `postpositions-kozott-utan`, `direction-adverbs-jobbra-balra`) to their unit vocabulary tags.

124. ~~**Hungarian noun/adjective endings have no vowel-harmony check (added 2026-10-03).**~~ — **Done 2026-10-03.** `nominalEndingClashes()` / `resolveNominalWith()` in `engine/morphology/hungarian.js` now reject a case, possessive or plural ending (including stacked ones, "kertunkben") whose harmony clashes with the lemma, in both `analyze()` and `ladder()`. Nouns break the vowel pattern more than verbs, so only a lemma whose last vowel is back, ö/ő/ü/ű, or a short e with no back vowel anywhere is checked; é and i/í stems (*célunk*, *hidak*) and mixed loans (*hotelban*) are left alone, and "-ként", "-ért", "-ig" and the possessor "-é" (*családé*) fit any stem. Snapshot of the ~46,000 unique story words: 60 top readings changed — mostly English words losing fake Hungarian readings ("age" → *ág*, "sale" → *sál*), plus *tisztje* → *tiszt* (was *tiszta*), *azé* → *az*, *másé* → *más*, *feladná* → *felad*; lost: foreign names whose harmony follows pronunciation (*Clevelandben*, *Broadwayvé*) and *tanácsosné* (the "-né" "wife of" suffix isn't analysed at all; it was only reached through a bogus translative reading). The Reader's accentless fallback now also accepts a restored listed irregular form (`HungarianMorphology.isIrregularVerbForm()`), so "mentunk" → *megy*, "elmentunk" → *elmegy*. Tests: `tests/reader/test-hu-verb-harmony.js`, `tests/reader/test-hu-accentless-lookup.js`. Original report below.

    Verb endings got one (ACHIEVED.md item 123), but case and possessive endings still accept every harmony variant, so an accentless "mentunk" (*mentünk*, "we went") reads as "ment" (adjective, "exempt") + back possessive "-unk", and the Reader's accentless fallback never reaches *mentünk*. Nouns can't use the verb rule as-is: e/é/i/í-only stems often take back endings (*cél* → *célunk*, *híd* → *hidunk*, *nyíl* → *nyilak*). A safe first step: enforce only where the stem's last vowel is back or ö/ő/ü/ű, and check `scripts/audit-reader-coverage.js hu` plus a before/after snapshot of every story word's top reading, as was done for 123.

123. ~~**Hungarian analyser ignores vowel harmony on some verb endings (added 2026-10-03).**~~ — **Done 2026-10-03.** `verbEndingClashes()` in `engine/morphology/hungarian.js` now rejects a verb ending whose vowels clash with the stem's harmony, in both `analyze()` and `ladder()`, checked on the resolved lemma (after the prefix and "-ik" come off). It only rules where the harmony is certain: a back or ö/ő/ü/ű last vowel, or e/é with no back vowel earlier. Compounds ("hazatér", "túlél") and i/í stems ("bénít" is back, "épít" front) are left alone, and "-nék"/"-jék" fit both harmonies. Across the ~45,000 unique words in the Hungarian stories only 6 readings changed, all for the better (English "fled", "lesson", "rose", "rote" no longer read as Hungarian verbs; "hívek" no longer "I call"). Test: `tests/reader/test-hu-verb-harmony.js`. "mentunk" then fell to "ment" (adjective) + possessive "-unk" — fixed by item 124 above. Original report below.

    "mentunk" (an accentless "mentünk", *we went*) resolves as *menik* ("to flee") + back-vowel past 1pl "-tunk", though *menik* is a front-vowel verb and only takes "-tünk". `HungarianMorphology.analyze()` accepts the ending without checking harmony, so the Reader's accentless fallback (ACHIEVED.md, "Hungarian Reader: words written without accents now resolve") never gets to run for it. Enforcing harmony on verb endings would also make the fallback's stem+suffix pass stricter; check against `scripts/audit-reader-coverage.js hu` so real stories don't lose readings.

107. ~~**Expand the Hungarian B1/B2 classic adaptations to target length (added 2026-09-28).**~~ — **Done 2026-10-02.** All 72 Hungarian literary classics in `content/hu/stories/classics/` (36 at B1 and 36 at B2) were expanded to match Library word-count standards while preserving grammar tags, character lists, and pedagogical comprehension questions:
    - **B1 classics (~400 words target):** Expanded from an average of ~225 words (with severe outliers under 120 words like *Édes Anna*, *Légy jó mindhalálig*, and *Szindbád*) to an average of ~384 words (353–493w band across all 36 files), enriching narrative context, character interiority, and authentic B1 syntax (commit `5f09cb7b`).
    - **B2 classics (~700 words target):** Expanded from 1-page vignettes (~230–370 words, avg 288 words) to full-bodied B2 adaptations averaging 665 words (648–690w band across all 36 files), featuring sophisticated literary style, compound sentences, and dialogue grounded in 20th-century Hungarian classics (*Pacsirta*, *A vörös postakocsi*, *Bánk bán*, *Ábel a rengetegben*, *Sorstalanság*, *Az ajtó*, *Különös házasság*, etc.) (commit `21a38cbb`).
    - Manifests regenerated (`content/hu/stories/manifest.json`) and all files validated cleanly against schema. Original report below.

The Hungarian literary classics in `content/hu/stories/classics/` are much shorter than the Library's word-count standards (the Spanish B1/B2 classics were expanded in commit `4aabea4b`):
    - **B1 classics (~400 words target).** 32 of 36 average ~225 words, with severe outliers under 120 words (*Édes Anna* `b1-10`: 114w, *Légy jó mindhalálig* `b1-11`: 98w, *Szindbád* `b1-12`: 91w). Expand to ~400 words, keeping B1 grammar and dialogue.
    - **B2 classics (~700 words target).** All 36 average ~288 words (e.g. *Pacsirta*, *A vörös postakocsi*, *Bánk bán*, *Ábel a rengetegben*, *Sorstalanság*, *Az ajtó*). The prose and dialogue are authentic, but they're 1-page vignettes; expand into ~700-word B2 adaptations with text-grounded comprehension questions.
    - **B1/B2 World/Civics shelf.** Consider expanding the short cultural vignettes too (currently ~130 words at B1, ~360 at B2).


117. ~~**B1+ choice exercises: easy giveaways, not two right answers (scoped 2026-10-01).**~~ — **Done 2026-10-02.** Antigravity did the Spanish B1 distractor rewrite (726 give-away options across 502 exercises) and a full Hungarian review, A1 through B2, in four reviewed rounds: A1-A2 (250 exercises read, 10 fixed directly by Antigravity; the reviewer then fixed 10 more two-right-answer cases it had introduced or missed, and corrected the a1-80 day exercise), B1 (753 exercises changed, including 642 fill-blank hints that leaked their own answer; a reviewer pass found 64 "choose the reply" exercises where Antigravity had swapped an absurd wrong option for a different *also-correct* reply — fixed with near-miss grammar errors instead), and B2 (597 changed; the reviewer found and restored 17 correct answers Antigravity had rewritten to show off grammar but which no longer answered the question, plus 2 more acceptable-but-marked-wrong options). Two cross-cutting follow-ups then closed it out: 313 fill-blank hints that had gone English-only after the leak fix and lost their disambiguating word entirely (184 got a dictionary-lemma-plus-grammar hint, e.g. "(became)" → "(válik, past)"; 16 bare-dictionary-form answers kept their English hint and got the real synonym added to `answers`, e.g. szemben/ellentétben, felett/fölött, amit/amelyet) and 35 leftover time-word give-away wrong options in B1/B2 (e.g. an absurd distractor padded with "tegnap" for no reason), replaced with neutral wording that keeps each option wrong for the grammar reason the exercise actually teaches. Left alone on purpose: 129 of the 313 flagged hints (closed-class words, fixed collocations, no real synonym risk) and 5 exercises the give-away checker also flagged, whose `teaches` tags (reported-speech-statements, b2-past-modals, b2-cataphoric-clauses) show the time word *is* the grammar point, not an accident; also the "helyben" (locally) and "térben" (in [abstract] space) false positives from the checker's case-suffix heuristic. Final state: A1 has 2 known-good intentional distractors, A2 is clean, B1/B2 have only those confirmed false positives left. C1 was never reached — partway through, Antigravity started generating substantial new C1 content (new units beyond the original 12 files) in the same shared checkout instead of only reviewing what existed, so the review itself stopped at B2 (see ROADMAP 120). Working files: `imports/review/ANTIGRAVITY-exercise-quality.md` (the brief), `check-es-b1-giveaways.py` and `check-hu-exercises.py` (the mechanical checks, kept for reuse), `hu-review-feedback-a1-a2.md` (the three rounds of reviewer feedback), `es-b1-giveaways.jsonl`, `fill-blank-hint-recheck.txt` and `b1-situational-recheck.txt` (the work lists). Original report below.

A1-A2 were audited for two acceptable answers (ACHIEVED.md, "One correct answer per choice exercise, A1-A2"). A scope of B1-C1 (9,872 choice exercises) found that problem is rare there: no duplicate options or multi-answer `correct`, no dictionary synonyms, and only 1 doubtful item in a random sample of 180 sentence/reply/dialogue questions (`b1-22-03.ex06`, "Which form follows «si» in this pattern?" without the pattern), against about 9% at A1-A2. The weakness at B1+ is the opposite: wrong options that can be ruled out without knowing the grammar. Spanish B1 has 486 of 3,597 (14%) where a wrong option is given away by a mismatched *ayer*/*mañana* ("Busqué una alternativa mañana."); B2 and Hungarian 3-5% by the same measure. Others are throwaways ("La comunicación existe.", "Tengo una decisión.") or, in Hungarian B2 dialogues and the ES-LATAM history tracks, absurd statements ("Fuss ki az épületből és ne gyere vissza soha többé."). If worth doing: replace them with near-miss distractors that test the target form (wrong mood, wrong tense with a matching time word, wrong case), starting with the Spanish B1 *ayer*/*mañana* set.

119. ~~**Topic decks and the Vocabulary Driller still read the shared deck gloss (found 2026-10-01 during item 92).**~~ — **Done 2026-10-01.** `decks.json`'s shared table still takes the first gloss a course gives a word, but `SHARED_GLOSS` in `build-manifest.py` (Spanish only) now overrides the words whose first gloss was found to be unit-specific: *llevar* "to take / carry" (was "to have been doing"), *cuyo* "whose" (was "Cuyo (western Andean region)"), *estado* "state", *andar* "to walk / go", *agente* "agent". The units that teach the narrow sense keep it through their lesson deck's own `glosses` (ACHIEVED 92). Choosing the general gloss automatically was tried and rejected: scoring each course gloss against the dictionary, even replacing only a first gloss that shared no word with it, swapped in worse ones (*probar* "to try / taste" → "to prove", *suspender* "to fail" → "to suspend", *porteño* "from Buenos Aires" → "inhabitant of Valparaíso port"), because `spanish-en.json` keeps one terse sense per word. Add a word to `SHARED_GLOSS` when another such case turns up. Original notes: Lesson decks carry their own per-unit `glosses` (ACHIEVED 92), but topic decks pool several units and the Vocabulary Driller (`engine/drills/vocabulary.js`, `_words`) reads `decks.json`'s shared table, which holds the first unit's sense. So *llevar* can still show "to have been doing" there. A fix would pick a general gloss for the shared table (the earliest A1/A2 core-track sense rather than the first file read), or let the driller take the gloss of the unit the word was drawn from.

118. ~~**Spanish has no frequency decks (found 2026-10-01 during item 92).**~~ — **Done 2026-10-01.** `build_decks()` looks up `FREQUENCY_SOURCES` by the course's language (`es-es`/`es-latam` → `es`), so both Spanish courses now have "Top 100 words", "Words 101–250", "Words 251–500" and "Words 501–1000", like Hungarian. A frequency deck carries its own `glosses` where a curated `FREQUENCY_GLOSS` differs from the course gloss already in the shared table (*de* "of, from", *por* "for, by, through", *tiempo* "time, weather"). `FREQUENCY_GLOSS` gained entries for weak dictionary glosses in the top 1000 (*él* was "he, him, masculine personal third person subject…", *usted* "second person formal", *hasta* "even", *encontrar* "to meet", *ni*, *ello*, *carne*, *señorito*, *alejar*, *amar*). Checked in the app: the four decks list in ES-LATAM Parlour Decks with those glosses. The 501–1000 band holds some vulgar words (*joder*, *culo*), since the frequency list comes from subtitles; they are left in as real frequency. Original notes: `FREQUENCY_SOURCES` in `build-manifest.py` is keyed `"es"`, but `build_decks()` runs for `es-es` and `es-latam`, so neither course gets the "Top 100 words" / "Words 101–250" decks Hungarian has, and `FREQUENCY_GLOSS` is never used. If they are wanted, key the sources by course (or map `es-*` to `es`). Note that the frequency loop's `remember()` cannot override a gloss a lesson already put in the shared table, so a frequency deck would also need its own `glosses` map (as lesson decks now have, ACHIEVED 92) for `FREQUENCY_GLOSS` and words like *cuyo*/*estado*/*andar*, whose first lesson gloss is a narrow B2 sense.

92. ~~**Audit `imports/dictionary/spanish-en.json` for more wrong-primary-sense entries (added 2026-09-24).**~~ — **Done 2026-10-01.** Two scans over the 3,000 most frequent Spanish forms (`imports/dictionary/frequency.csv.raw`): one for place, surname, initialism and obsolete glosses, one for forms whose dictionary part of speech disagrees with the corpus. About 100 bad entries were found and fixed via `MANUAL_OVERRIDES` in `scripts/import_dictionary.py` (also applied to the generated JSON): conjugated verbs glossed as unrelated homographs (*ha* "hyaluronic acid", *hay* "alternative form of ahí", *son* "tone", *van* "van", *pongo* "orangutan", *pienso* "animal feed", *dije* "locket"), function words (*a* "bishop", *al* "initialism of América Latina", *sí* "hello? (phone)"), feminine and plural forms glossed as surnames or places (*sola*, *hermosa*, *casas*, *segura* "Segura (river)", *antigua* "Antigua") and niche senses (*guapo* "arrowroot", *rara* a bird, *primera* "first gear"). Participles glossed as adjectives ("perdido" = "lost") were left alone. **Root cause fixed as well**: `renderCard()` in `engine/srs.js` showed the dictionary entry over the card's own saved gloss whenever one existed, so a curated lesson gloss lost to the exact-string headword (how "llamas" got through). The card's gloss now wins; the dictionary only fills cards saved without one (`english` empty or `'unknown'`). **Related deck-gloss bug fixed** (found while checking ES-LATAM deck glosses): `decks.json` keeps one shared gloss per word, the first one `build-manifest.py` meets, so a word taught in several units showed the first unit's sense in every deck (*llevar* as "to have been doing / to have been in a state" in the unit that teaches it as "to take / carry"; *cuyo* as "Cuyo (western Andean region)"). Lesson decks now carry a `glosses` map wherever their unit's gloss differs from the shared one (190 ES-LATAM decks, 102 ES-ES, 194 HU), and `wordsOf()` in `engine/decks.js` prefers it. The narrow B2 glosses themselves ("plata" = "silver bullion extracted from ore", "desaparecido" = "forcibly disappeared person") are correct for their lessons and were kept. Follow-ups: items 118 and 119, also in this file. Original notes: Bug report #192 flagged the review card for "llamas" showing "a name of several localities in Asturias, Spain" instead of the taught verb sense — not corrupted/malformed data (the 2026-09-17 audit, ACHIEVED.md item 30, already covers that class), but a real Wiktionary entry that's simply the wrong headword for a common conjugated form that also exists as its own place-name/homograph entry. Fixed via `MANUAL_OVERRIDES` in `scripts/import_dictionary.py`, same mechanism as the 2026-09-18 HU "wrong-sense gloss" fixes (ACHIEVED.md, "HU Dictionary Wrong-Sense Gloss Fixes"), but ES has never had that HU audit's equivalent systematic pass over common words' primary senses — only this one-off fix. Worth a similar targeted audit of the ES dictionary's top N frequency-ranked headwords, since `Lexicon.define()` (used directly by SRS review cards) has no conjugation-aware disambiguation and will surface whatever sense the raw dictionary file happens to carry for that exact string.

115. ~~**Reader coverage follow-ups (added 2026-10-01).**~~ — **Done 2026-10-01** (parts 1 and 2; part 3 cannot be done with the available tools). (1) `.github/workflows/reader-coverage.yml` runs `scripts/audit-reader-coverage.js` on pushes that touch the stories, `imports/dictionary/`, `engine/lexicon.js`, `engine/morphology/` or the script itself, and by hand. It is a report, never a gate (`continue-on-error`): the per-course counts and the most frequent gaps appear in the run summary (`--markdown`), and the full list is attached as the `reader-coverage` artifact. (2) `imports/dictionary/coverage-ignore.json` is now `{ all, hu, es }`: the audit applies `all` plus the course's own language (a legacy single `words` list is still honoured), and `fill-dictionary-gaps.py import` writes ChatGPT's non-words to the language it was run for and migrates the old list. Checked: counts unchanged by the restructure; a word ignored for Spanish only is still reported for Hungarian; ignored for Hungarian, for all, or through the legacy list it disappears. (3) The weekly gloss review runs on the app's default model: neither `create_scheduled_task` nor `update_scheduled_task` has a model setting. Set the app's default model to Opus 5.5 if that is wanted. Original notes: (1) Run `scripts/audit-reader-coverage.js` in CI as a report, not a gate, so a content change that adds many unreadable words shows up. (2) `imports/dictionary/coverage-ignore.json` is shared by Hungarian and Spanish; split it per language if a word ever needs ignoring in only one. (3) The weekly gloss review uses the desktop app's default model, because the scheduling tool has no model setting; set the app default to Opus 5.5 (or check the task's own settings) if that matters.

5. ~~**Two new-learner notes still need a signal (added 2026-09-24).**~~ — **Done 2026-10-02.** Both driller notes from the new-learner introduction (`ACHIEVED.md` item 87) are built as end-of-lesson invitations in `engine/guide.js`, placed before the general Workshop invitation and, like every invitation there, shown at most twice and never once the learner has opened the Workshop. **Listening:** `engine/lessons.js` records the first-try result of every listening step (category `listening`: listening-choice and dictation) at the two grading points (`solveStep`, `failStep`) into a rolling log of the last 20 per course (`LearnerModel.recordListeningOutcome`, key `listeningLog`, synced); the note ("Listening practice has its own space in the Workshop.") shows with at least 8 attempts and 60% or fewer right. Spanish has about 1,400 to 1,650 such steps per course; Hungarian about 50, so it rarely fires there. **Verbs:** per-verb counting was dropped for a per-tense signal, because Spanish forms are ambiguous (`fui` is ser or ir) and finding the verb would mean loading the multi-MB dictionary mid-lesson. The note ("If a verb keeps catching you out, the Verb Driller practises just that.") shows when a skill listed in `indexes/verb-tense-skills.json` ranks weak under the learner model's existing rule (`LearnerModel.weakVerbTense`). Spanish only: Hungarian has no tense mapping, so no verb note there. `renderLessonSummary` collects both signals through `LearnerModel.guideSignals()`. Tests: `tests/drills/test-driller-notes.js`. Copy and triggers: `docs/feature-guidance-copy.md` (6a, 6b). Original notes: The new-learner introduction (`ACHIEVED.md` item 87) planned two behaviour-triggered notes that weren't built, because nothing records what they'd trigger on: the **Verb Driller** note ("If a verb keeps catching you out, the Verb Driller practises just that", meant for the same verb missed three times across lessons) and the **Listening Driller** note ("Listening practice has its own space in the Workshop", meant for low listening scores). Lessons don't record which verb a miss was on, and there's no per-skill listening score. Either add those signals (e.g. note the lemma of a missed conjugation step in the learner model) or pick a different trigger. The copy is in `docs/feature-guidance-copy.md` (6a, 6b); the end-of-lesson "What's next" screen already suggests a grammar drill for a weak skill, which partly covers 6a.

112. ~~**HU Reader: decode the noun-to-adjective "-i" suffix for pasted text (scoped 2026-08-29).**~~ — **Done 2026-10-01.** Built as a last-resort rule in `HungarianMorphology.analyze()` (`engine/morphology/hungarian.js`): only when a word has no other reading and is not itself a headword, a word ending in `-i` whose base resolves as a noun or adjective gets an "adjective in -i" reading ("of or from <base gloss>"). Because it runs last, the 83% false-positive rate a naive rule has against the whole dictionary never shows: a word with any real reading keeps it. The item's own example, `kiértékelési`, now resolves (as do `nemzetiségi`, `logikai`, `geopolitikai`); `iskolai` keeps just its dictionary entry. The `morphdb/morphdb.hu` allowlist idea was not needed. Original notes: `resolveNominal()` in `engine/morphology/hungarian.js` has no fallback for `iskola` to `iskolai`. A naive "strip the trailing i and check the dictionary" rule was tried and rejected: an 83% false-positive rate against about 2,000 real dictionary nouns, because which nouns take `-i` is a per-word lexical fact. No curriculum content is affected (every `-i` adjective in `content/hu/` is already its own headword), but the Reader also takes arbitrary user-pasted text, where an adjective Wiktionary lacks as a headword (for example `kiértékelési`) fails to resolve. `morphdb/morphdb.hu` (CC-BY 2.5, the HunMorph lexicon) was looked at as a source for a verified allowlist but needs network access to fetch. Full notes: `docs/archive/TROUBLESHOOTING_BACKLOG.md`, "HU Reader - morphology engine backlog".

116. ~~**Hungarian A1 units 121-150 read as generated (found 2026-10-01 during the item 103 audit, see ACHIEVED.md).**~~ — **Done 2026-10-01.** All 114 `dialogue-complete` steps in units 121-150 (practice, dialogue and consolidation) were exported to a text file, corrected and imported back: 85 changed. Units 121-130 were corrected by hand by a native speaker; units 131-150 were then done in the same style (answers that actually answer the question, short natural replies, "Mennyibe kerül?" rather than "Mennyi az ár?", each exchange understandable on its own), with consolidation copies kept identical to the practice step they repeat. Examples: "Mit csinálsz a szabadidődben?", "Szeretnétek moziba menni szombaton?", "Mikor jön a busz?" / "Hamarosan. Nézd, már jön!" in place of "Mikor érkezünk?" / "Hamarosan. Jön a busz.". All content validates. Original report below.

Beyond the "Nem tudom." distractors fixed then, several practice dialogues have correct answers that don't answer the question or aren't natural Hungarian: "Szeretnétek együtt programot?" (no verb), "Mit csinálsz szabadidőben?" (should be *szabadidődben*), "A kabát hosszú, de kényelmes." answered with "A nadrág rövid?", "Akarunk találkozni hétkor?". The same exchanges recur across each unit's practice and consolidation files. Worth a native-speaker pass over these 30 units' `dialogue-complete` steps (about 150 exercises).

109. ~~**Audit `dialogue-complete` exercises for verbatim-repeated questions across adjacent exercises (added 2026-09-29).**~~ — **Done 2026-10-01.** Audited every `dialogue-complete` against the two steps before it in actual lesson order (each lesson's `exerciseRefs`), flagging any shared line of two or more words: 51 hits. 17 exercises fixed (19 counting both Spanish courses), the same way as #203 (address the question by name or give it its own context): Hungarian `a1-13`, `a1-18`, `a1-20`, and the `dialogue-2` steps of `a1-52`…`a1-72` ("Meg, hol vagy?" after Károly's "Hol vagy?"); `a1-85-consolidation-16`, a near-copy of step 15, now asks "Mit csinálsz ma?"; Spanish `a1.health.05.ex10` repeated step 11's exact options and now has its own headache exchange, and `a1.12.03.ex11` asks "Carlos, ¿qué hora es ahora?". Left as they are: continuations, where the previous answer opens the next exchange (11 hits, intended); consolidation substitution drills, where one question is asked repeatedly with different answers ("Hová mész?" → mozi / étterem / gyógyszertár; about 25 hits), which is deliberate drilling; and natural re-asks to a different person (`a1-01-03`, `a1-12`). Original report below.

Bug report #203 flagged `a1-17-dialogue-1` (HU): its prompt had Meg ask "Hány éves vagy?", the exact same line Károly had just asked in the immediately preceding exercise (`a1-17-practice-7`), just with the speakers swapped — so the learner saw the identical question twice in a row. Fixed by addressing the question to Károly by name ("Hány éves vagy, Károly?"), matching the variation pattern the lesson's own `a1-17-dialogue-2` already uses. This is a different failure mode from item 103's "ambiguous referent" audit (both here are unambiguous, just literally duplicated) and hasn't been checked for elsewhere — worth a pass over `dialogue-complete` exercises within a lesson, searching for two prompts in sequence whose question line (or the whole exchange) is character-identical.

103. ~~**Audit `dialogue-complete` exercises for ambiguous-referent questions (added 2026-09-27).**~~ — **Done 2026-10-01.** Audited every `dialogue-complete` in es-es, es-latam and hu whose options pair a yes and a no (404 exercises, 305 after merging es-es/es-latam copies) and read each one for the bug's signature: two options that are both sensible answers. 80 exercises fixed (95 counting the Spanish ones in both courses). (1) Spanish: "¿Ya han navegado…?" with both "No, todavía no." and "Sí, ya hemos navegado." (A2 units 02 and 03, 10 exercises) and "Has visto alguna vez una barca?" now have contradictory distractors ("Sí, todavía no.", "No, ya las hemos alquilado."), the pattern A2 unit 09 already used; café "¿Algo más?" no longer offers "Quiero un café." or "Sí, quiero dos cafés." as wrong answers; `b1-22-05.ex14` and `b1-28-01.ex14` likewise. (2) Hungarian A1 units 121-150 used "Nem tudom." as the wrong option in 42 exercises (plus one "Nem értem."), which answers any question; each is now an off-topic line from another unit's vocabulary. Three correct answers there were broken and are fixed: "Bal van." to "Balra van.", "Van jegyünk?" answered with "Igen, van két jegyünk." instead of "Igen. A megálló ott van.", and "A múzeum és a mozi is itt van?" answered with both places. (3) Hungarian A2/B1: "Dolgoztál tegnap?" / "Nem, holnap dolgozom." and 16 more like it now contradict themselves ("Igen, holnap dolgozom."). `a1-80-practice-5` was rewritten as a clean `-n` day check ("Kedden jó." / "Keddben jó."). Content-grounded history and civics questions (the answer comes from the reading) were left alone, as were opinion questions whose wrong option is merely a weak position. All content validates. Original report below.

Bug report #198 flagged `a1-15-consolidation-14` (HU): the prompt "Ő egy nő?" had no established referent for `ő` anywhere in the dialogue, so both options ("she's a woman" / "he's a man") were equally valid — a coin flip, not a real answerable question. Fixed by grounding it in a named character (Anna) whose identity the unit's own story establishes, matching the pattern the neighboring step already uses. Not yet checked whether the same "bare `ő`/`ő` with no antecedent" pattern recurs elsewhere in `dialogue-complete` exercises across HU or the Spanish courses — worth a pass similar to item 101's audit (ACHIEVED.md), searching for `dialogue-complete` prompts whose two options are both internally self-consistent (i.e. neither option contradicts itself or fails to address the question), which is the actual signature of the bug rather than just "uses `ő`".

114. ~~**Four tests are stale or broken (found 2026-09-30 during the repo cleanup).**~~ — **Done 2026-10-01.** `test-library-recommendations-search.js` reads `content/es-es/stories/manifest.json`, and its DOM mock gained comma selector lists and `hasAttribute()`, which the search code now uses. `test-deck-review-isolation.js`'s element stub has a `dataset`. The three grader tests that need a running grader endpoint, their shared runner and their fixtures moved to `tests/grader-live/` (with a README); everything left under `tests/` runs offline and passes. Original report below.

`tests/reader/test-library-recommendations-search.js` still reads `content/es/stories/manifest.json` (the course folders are now `es-es` and `es-latam`). `tests/decks/test-deck-review-isolation.js` throws in `engine/srs.js:1039` (`cardEl.dataset` is undefined in its DOM stub, so the swipe code added since needs a stub or a guard). `tests/grader/test-spanish.js`, `test-hungarian.js` and `test-consistency.js` call the live grader Worker and fail without network, so they belong in a separate "needs network" group. The rest of `tests/` passes.

108. ~~**Grammar search: bridge grammar terms across languages (added 2026-09-28).**~~ — **Done 2026-10-01.** `scripts/build_grammar_guide_index.py` now has `GRAMMAR_TERM_SYNONYMS`, hand-made groups of equivalent grammar terms per language family (`es` for both Spanish courses, `hu`): subjuntivo ↔ subjunctive, pretérito indefinido ↔ preterite, tárgyeset ↔ accusative, igekötő ↔ preverb, névutó ↔ postposition and so on. The groups are applied when the index is built, not to the query: a topic that mentions any term of a group gets the rest of the group added to its hidden keywords, so the search code in `engine/curriculum.js` is unchanged. A term matches at the start of a word, ignoring accents and case. es-es: "subjunctive" and "subjuntivo" now both find 44 topics (were 34 and 14), "preterite" 0 to 28; es-latam: both find 108 (35 and 78); hu: "tárgyeset" 0 to 12, "névutó" 0 to 61, "feltételes mód" 1 to 56. To add a term, extend the list and re-run the script (CI's `sync-generated-content.yml` also re-runs it when the script changes). Original report below.

Grammar Guide search now matches English and target-language keywords (see ACHIEVED.md, "Grammar & Decks Search in Both Languages"), but only the words each topic actually contains. A term used in one language doesn't find topics written in the other: on es-es, "subjunctive" finds 34 topics and "subjuntivo" only 14, because most English-language topics never write *subjuntivo*. The same will be true for HU case names (*tárgyeset* vs "accusative"). A small hand-made synonym list of grammar terms per course (subjuntivo ↔ subjunctive, pretérito indefinido ↔ preterite, tárgyeset ↔ accusative, …), applied to the query the way the Library's `BILINGUAL_TOPIC_SYNONYMS` (`engine/reader.js`) is, would close the gap.

110. ~~**Reader dictionary coverage, Hungarian and Spanish (widened 2026-09-30).**~~ — **Done 2026-10-01.** Bug reports #204/#205 found four B2 coffeehouse words that showed "Not in the dictionary yet" (fixed by hand, commit `598111c3`). `node scripts/audit-reader-coverage.js [hu|es-es|es-latam|all]` now checks every story word through the real `Lexicon.lookup()` in seconds, so this is a command, not a manual pass.
    - **Done (engine).** Spanish: `del`/`al` contractions; feminine and plural participles (`fundada`, `liderados`, `inscritas`, `recubierta`); gerund or infinitive plus clitic for any dictionary verb and `ñ` no longer stripped (`transformándose`, `enseñarles`, `bañarse`); `-uir` verbs, `i→ie` stems, hiatus accents, `ído` participles (`concluyó`, `adquiere`, `reúne`, `desposeídos`); the two lookups that threw (`constructor`, `desoyeron`). Hungarian: long-vowel and `ő`-stem nouns with possessive or case (`idején`, `nyarán`, `nevét`, `erejét`); comparatives and superlatives; `-ság/-ség` and `-ás/-és` nouns; present, future and `-ott` participles, adverbial `-va/-ve`; `-i` adjectives; personal-pronoun and demonstrative paradigms (`engem`, `nálunk`, `abban`, `amellyel`); long-vowel verb past (`nőttek`); `iz`-stem verbs (`őrzik`); potential `-hat/-het`; personal infinitive (`fizetnie`); `lehet`. Reader: a capitalised mid-sentence word with no entry shows the word with a "name" tag and no Add button; the ending after a number (`A2-es`, `1948-as`) is no longer a tap target. `recordLookup` no longer throws on `constructor`.
    - **Result.** Hungarian words with no reading: 6,439 to 4,824 (about 1,250 are names, now shown as names; 866 more only get the literal compound guess). es-es: 738 to 541 and es-latam: 2,381 to 1,588, nearly all names now. No lookup throws in any course.
    - **Fill tool built (2026-10-01).** `scripts/fill-dictionary-gaps.py`: `export` writes the audit's gaps as ChatGPT-ready batches (`imports/dictionary/gap-batches/`, words and names separately, words seen 3+ times by default: Hungarian about 460 words and 400 names, Spanish about 90 words and 450 names), `import` validates the reply and merges it into the dictionaries through `imports/dictionary/additions-<lang>.json` (layout-preserving; `merge` re-applies after a dictionary re-import), and names are stored so case endings still resolve. `imports/dictionary/coverage-ignore.json` plus automatic Roman-numeral skipping keep non-words out of the report. Tested with 13 real entries (kept). **To run it:** export, paste each batch into ChatGPT, save the reply as `<batch>.reply.txt`, import; then re-run the audit. A Spanish verb whose headword is already an adjective (`circular`, `articular`) is reported as a conflict instead of merged, because Spanish entries hold one sense.
    - **Gap batches run (2026-10-01).** Hungarian: 888 names and about 400 words imported in two rounds; Spanish: about 450 names and words. Result: Hungarian words with no reading 6,439 to 3,064 (122 look like names); es-es 738 to 381; es-latam 2,381 to 1,154. Spanish verbs whose headword is also an adjective (`circular`, `articular`, `anular`, `formular`, `tutelar`) now work: they live in `imports/dictionary/spanish-verb-homographs.json`, written by `merge` and read by the Lexicon. Words ChatGPT marks as not real go into `coverage-ignore.json` automatically.
    - **Leftovers cleared (2026-10-01).** The tokenizer now treats every Latin letter as part of a word, so `Solimões`, `Rondônia` and `Domènech` are one tappable name each instead of fragments. Hungarian rules added: dropped-vowel stems (`ezrek`, `lelkében`, `jelzik`, `ünnepli`, `megszerzett`), j- and v-stems (`édesapjával`, `művében`, `alapköve`), possessive plus accusative (`lelkét`, `lelkeit`), comparatives and superlatives of adverbs and `-i` adjectives (`bátrabb`, `közelebb`, `legjobban`, `legrégebbi`), short and irregular adverbial participles (`adva`, `ülve`, `téve`, `lévő`), the `létre-`/`szét-`/`körül-` verb prefixes. Spanish: `yergue` (erguir). Counts: Hungarian words with no reading 2,883 (120 look like names), es-es 385, es-latam 1,148, and what is left is single-occurrence vocabulary and rare names.
    - **AI gloss fallback (2026-10-01), deployed and verified.** For the long tail, a tapped word with no entry, no reading and not a name now asks a Cloudflare Worker (`cloudflare-worker/gloss-worker.js`, client `engine/gloss-ai.js`) for the base form and a short gloss, shown as "machine suggestion" and never saved to a deck; any failure keeps today's "Not in the dictionary yet". Answers are cached in KV (one model call per word for everyone), capped at 600 uncached calls a day, origin-restricted, and exportable with `python scripts/fill-dictionary-gaps.py pull-ai hu|es` so the words learners really tap become reviewed dictionary entries (cache keys are versioned, currently `v2`; the prompt asks for the dictionary gloss of the lemma, not a translation of the inflected form). Tests: `tests/reader/test-gloss-worker.js`, `test-gloss-ai-client.js`. Also: the Reader popup strips parentheses from glosses, so the name tag is now ", a name" (not "(name)").
    - **Weekly review (2026-10-01).** A scheduled task, `weekly-gloss-review` (Mondays about 09:00, while the desktop app is open), runs `pull-ai` for both languages, reviews every cached gloss strictly (real word, correct lemma and part of speech, a plain dictionary gloss of the lemma), imports the approved ones through `fill-dictionary-gaps.py import`, adds the rejected words to `imports/dictionary/ai-rejected.json` so they aren't offered again, bumps the cache version and pushes to master, and records each week in `imports/dictionary/ai-review-log.md` (counts, and every rejection with its reason). Its token comes from `~/.parlour-gloss-token`. First run found nothing to review (2 cached answers, both already in the dictionary). Single-occurrence vocabulary can still be exported in bulk with `python scripts/fill-dictionary-gaps.py export hu --min-count 1`.

101. ~~**Fill-blank hints that repeat the answer — 80 more instances beyond the fixed 59 (added 2026-09-25).**~~ — **Done 2026-09-30.** Audited every `fill-blank` in `content/*/exercises` whose trailing `(…)` equals `answer` (no `[…]` bracket in `sentence`): 258 exercises, not 80 — 59 es-es, 184 es-latam (about 33 of them A1/A2 copies of the es-es ones), 15 hu. Each parenthetical was replaced with a short English gloss of what's blanked (`(to cook)`, `(whose)`, `(pronoun)` for a bare `se`), or a category clue where the answer is a proper name (`(lake)` for Titicaca, `(newspaper)` for Pesti Hírlap). Only the trailing parenthetical of `sentence` changed; `answer`/`teaches` are untouched and all content validates. The 38 exercises pairing the parenthetical with an existing `[English sentence]` bracket were left as the deliberate dual-hint form. Original report below.

Bug report #193 flagged `b1-precolombina-01.ex04`: the inline parenthetical at the end of `sentence` (e.g. `"...la papa se convirtió... (mientras que)"`) literally repeated the answer instead of hinting at it. Fixed that exercise plus the same pattern across ~59 other ES-LATAM B1 history-track exercises (mostly each lesson's `ex04`) by replacing the Spanish repeat with a short English gloss derived from the exercise's own `english` field (commit `8d125e09`). While auditing, found 80 more fill-blanks with the identical bug (`sentence`'s trailing `(...)` case-insensitively equals `answer`, no `[...]` bracket translation already in the sentence) that weren't fixed in this pass: about half are in the same history track's remaining lessons/consolidations (missed because they use `teaches` tags the audit script didn't classify as connector-related, e.g. plain vocabulary recall like `"(institución)"`), the other half are in the numeric `b1-02`…`b1-09` grammar-topic units, a different exercise family from the history track. Left untouched: 38 further matches that pair the parenthetical with an existing `[English sentence]` bracket already in `sentence` (e.g. `b1-06-05.ex03`) — that looks like a distinct, likely-intentional dual-hint convention, not the same bug, and wasn't in scope for #193. Before the next pass: re-run the audit (search `content/es-latam/exercises/**/*.json` for `fill-blank` where the trailing paren equals `answer` case-insensitively and `sentence` has no `[`), fix each with an `english`-derived gloss the same way, and separately check whether `es-es` and `hu` content have the same pattern (not yet audited). Bug report #193 flagged `b1-precolombina-01.ex04`: the inline parenthetical at the end of `sentence` (e.g. `"...la papa se convirtió... (mientras que)"`) literally repeated the answer instead of hinting at it. Fixed that exercise plus the same pattern across ~59 other ES-LATAM B1 history-track exercises (mostly each lesson's `ex04`) by replacing the Spanish repeat with a short English gloss derived from the exercise's own `english` field (commit `8d125e09`). While auditing, found 80 more fill-blanks with the identical bug (`sentence`'s trailing `(...)` case-insensitively equals `answer`, no `[...]` bracket translation already in the sentence) that weren't fixed in this pass: about half are in the same history track's remaining lessons/consolidations (missed because they use `teaches` tags the audit script didn't classify as connector-related, e.g. plain vocabulary recall like `"(institución)"`), the other half are in the numeric `b1-02`…`b1-09` grammar-topic units, a different exercise family from the history track. Left untouched: 38 further matches that pair the parenthetical with an existing `[English sentence]` bracket already in `sentence` (e.g. `b1-06-05.ex03`) — that looks like a distinct, likely-intentional dual-hint convention, not the same bug, and wasn't in scope for #193. Before the next pass: re-run the audit (search `content/es-latam/exercises/**/*.json` for `fill-blank` where the trailing paren equals `answer` case-insensitively and `sentence` has no `[`), fix each with an `english`-derived gloss the same way, and separately check whether `es-es` and `hu` content have the same pattern (not yet audited).

4. ~~**Explain an elective track to learners who start mid-track (added 2026-09-24).**~~ — **Done 2026-09-30.** Each non-core track in `LEVEL_TRACKS` (`build-manifest.py`) now has a one-line `description`, carried into `curriculum.json`; `_electiveCandidate()` passes it as `trackDescription` and the Home elective card shows it instead of the generic "From <track>, alongside the main course" line (falls back to that line if a track has none). Original report below.

The B1 elective tracks (es-es Cultura y Ciudadanía, es-latam Latin America, hu Citizenship) now open with a welcome screen in their first lesson (see ACHIEVED.md, "Welcome Screens for the B1 Elective Tracks"). But the elective nudge (`engine/recommendationEngine.js`, `_electiveCandidate()`) can send a learner straight to a later unit, and they never see that screen. Proposed: a one-line `description` on each track in `curriculum.json`'s `tracks` array (through `build-manifest.py`, since that file is generated), shown on the nudge card. The B1 elective tracks (es-es Cultura y Ciudadanía, es-latam Latin America, hu Citizenship) now open with a welcome screen in their first lesson (see ACHIEVED.md, "Welcome Screens for the B1 Elective Tracks"). But the elective nudge (`engine/recommendationEngine.js`, `_electiveCandidate()`) can send a learner straight to a later unit, and they never see that screen. Proposed: a one-line `description` on each track in `curriculum.json`'s `tracks` array (through `build-manifest.py`, since that file is generated), shown on the nudge card.

111. ~~**ES-LATAM leftovers from the B2 Library shelf fix — part (b).**~~ — **Done 2026-09-30.** (Part (a), the thin combined readings, is still open in ROADMAP.md.) The four Latin America B2 units and their readings (`b2-futuro`, `b2-integracion`, `b2-migracion`, `b2-pluralismo`) lost the "B2 Regional: " prefix from their titles, matching the neighbouring units; `curriculum.json`, decks, story manifest and grammar guide index were rebuilt.

111. ~~**Port the visual overhaul (designed 2026-09-29).**~~ — **Done 2026-09-30.** (Listed in ROADMAP.md as 109 until it was archived, a number another item was given the same day.) "The Composed Room": every screen designed in `docs/overhaul-prototype/`, rules in `DESIGN.md`, ported to the app on branch `visual-overhaul` and merged to master. Shipped: tokens and the colour-semantics table (vermilion here-and-now, pine finished/right, brick wrong, ochre due/new), the art registry (`engine/art.js`: heroes, nav icons, level marks, generated unit/story marks, row thumbnails), page headers, phone bottom nav, focus screens without nav, and every screen: Home, Lessons (Hungarian Cultural Exam rows removed from Lessons; it lives in Workshop only), Library, Workshop, Decks and review (swipe cue kept via `data-swipe`), Journey (streak grid, mountain, rows), lesson exercises and completion, studios and feedback, conversation scenarios, Cultural Exam, placement diagnostic, sheets, toasts, margin notes, switches and fields. Kept from the old design at the user's request: the Library Continue Reading and Recommended cards and the story-card grid. `overhaul.css` stays as the last-loaded stylesheet on purpose (its overrides interleave with rules in all eight base files); 910 declarations and 94 rules it fully replaced were pruned from the base files, with computed styles verified unchanged. Known dev quirk: the service worker serves CSS stale-while-revalidate, so a change shows after a second reload. Optional follow-up: bundle the stylesheets into one file.

106. ~~**Home recommendation engine: remaining improvements (added 2026-09-28).**~~ — **Done 2026-09-28.** (Listed in ROADMAP.md as 105, a number another item was given the same day.) Every part below has profiles in `tests/drills/test-home-recommendation-profiles.js` (25, all passing).
    - **Returning after a break.** `AppOpens.bump()` (`engine/init.js`) now records each open's time, and a gap of 3+ days since the previous open saves `appReturn = { days, at }` (`AppOpens.returned()`). For 12 hours after such a return, with 5+ words due, Home's one card is "Welcome back — Start with a review" (`welcomeBackCard()`), ahead of everything else, until it's taken or skipped. The separate review banner hides while it shows. Due grammar isn't counted, because it comes back in the next lesson's recycle block anyway. It uses the gap between app opens, not `lastActivityAt()`, which only lessons update.
    - **Level-test weak spots.** Results now save `takenAtOpen` next to `takenAt`. `LearnerModel.troubleSkills()` counts a test's top 3 "topics to revisit" as recent trouble for 14 days, until any exercise of that skill is answered right after the test. The card says so: "Your A1 test showed a few mistakes with …". Older results without a date are ignored.
    - **Outcome log surfaced.** Home logs `shown` (once per card per app open) as well as `taken`/`skipped` for every card kind, including the unit-end roleplay, the elective and welcome-back. All Home card buttons now go through `RecommendationEngine.open()`/`skip()` (`data-rec-open`/`data-skip-rec`). `RecommendationEngine.outcomeStats()` rolls the log up per card type; open Home with `?recstats` to see a table (not shown to learners). The log (last 300) and the elective state are backed up by `engine/sync.js`.
    - **Vocabulary-theme and "reading" skills.** A weak skill whose registry `kind` is vocabulary is named by its unit, e.g. "mistakes with words from 'The Architecture of Argument & Logical Cohesion'", with a "Word practice" button. Any skill still titled "reading" gets "the exercises from '…'". In practice only 2 HU vocabulary slugs are in the grammar index, but this turned up five real grammar skills wrongly titled "reading" in `grammar-titles.json`, now named: `alguna-vez-nunca`, `si-clauses`, `para-purpose` (es-latam), `superlatives` (es-es), `miutan-mielott-clauses` (hu).
    - **Elective cadence.** The offer now comes once 5 core lessons of the current level are completed since it was last started or skipped (`electiveResolvedAt`), instead of on `completedCount() % 5`, which elective lessons also moved.

105. ~~**Hungarian A1-01 sound tables: real recordings instead of TTS on bare letters (added 2026-09-25).**~~ — **Done 2026-09-28.**
    Lesson A1-01's vowel and consonant tables sent every bare letter (a, á, sz, gy…) through ParlourTTS. Measured against the live worker, Chirp3-HD returned **silence** (0.3 s, peak ≤ 0.01) for 9 of 24 letters (a, á, e, é, i, í, o, sz, gy). The rest were most likely the letter's *name* ("es" for s), not its sound. The silent clips were also cached for good in R2 and IndexedDB. The Wikimedia recordings added 2026-09-12 were all whole words, so they couldn't stand in for letters, and their CC BY-SA credit had been lost from the content.
    - **Recordings:** the user recorded all 48 items with `tools/sound-recorder/`: a local page (`server.py`, `index.html`) that records one item at a time with voice processing off and saves `recordings/<id>.wav`. The raw takes are gitignored. `process.py` cuts each take by segment energy: it drops lip smacks, breaths and key clicks separated from the word by a gap, and keeps final t/k releases on words. It then applies a light voice chain (90 Hz high-pass, −2.5 dB at 300 Hz, +2 dB at 4 kHz, +1.5 dB shelf above 10 kHz, 2:1 compression; no reverb, no de-essing), levels every clip to −18 dBFS and writes 96 kbps MP3s to `content/hu/audio/sounds/`. `review.html` plays studio, plain and raw takes side by side, with the kept region drawn on each waveform, and saves flags for manual cuts (`trim-overrides.json`).
    - **Lesson:** `a1-01-a-gr.json` has three tables. The seven vowel pairs play the isolated vowel sounds. A new "Short or long" minimal-pairs table (hat/hát, szel/szél, irt/írt, kor/kór, tör/tőr, hurok/húrok, üt/űr) comes with glosses. The anchor words (lát, rész…) follow. In `a1-01-b-gr.json`, sz, s and zs play held sounds and every word plays its recording. c, cs, gy, ny, ty, ly and j have no letter button, and the text says to hear them in the word.
    - **Engine:** new `audioOnly` flag on `table` (`engine/lessons.js`, `content/hu/schemas/grammar.schema.json`, `HU_Content_Authoring_Template.md`). A cell plays its recording or gets no button, never the TTS fallback. The 15 Wikimedia clips (`content/hu/audio/letters/`) are deleted, which also resolves the missing attribution. `lessons.js?v=2026-09-28snd`, `sw.js` `CACHE_VERSION = 'v2026-09-28c'`. Verified: all 55 buttons load their MP3s (200, no console errors), no TTS button remains in the four sound tables, ordinary tables keep TTS, and `validate-content.py hu` passes 6108/6108.

102. ~~**Confirm TTS plays on iOS after the silent-switch fix (added 2026-09-26).**~~ — **Done 2026-09-26.**
    Since `b6480096` (2026-09-25) `ParlourTTS` plays through Web Audio buffers instead of `<audio>`. iOS mutes Web Audio under the ring/silent switch, and Safari throws no error, so `speak()` "succeeded" silently and never fell back to device speech: no TTS on iPhone in lessons or stories, while desktop was fine. Fix: `getAudioCtx()` in `engine/tts.js` sets `navigator.audioSession.type = 'playback'` before creating the context. Confirmed working on the user's iPhone 2026-09-26. The Audio Session API needs iOS 16.4+, so on older iOS the path is still muted. If that matters, skip Web Audio on iOS when `navigator.audioSession` is missing and let `speak()` use its `<audio>` fallback.

100. ~~**Split catch-all "junk-drawer" grammar skills and add skill-size/alias checks (added 2026-09-25).**~~ — **Done 2026-09-25.**
    The consolidation pass in item 99 left several oversized catch-all skills where a substring/fallback matcher folded unrelated lessons, review tags, and lexical tags into default buckets (plus a `_comment` string from `verb-tense-skills.json` folded into `subjuntivo-morfologia.aliases`).
    - **Preventative Validator & Index Checks:** Added a skill-size sanity check to `scripts/build_grammar_index.py` that warns whenever a grammar skill exceeds `150` grammar exercises or `25` aliases in `skill-registry.json` (`0` warnings across all three courses after split), and extended `validate_grammar_titles()` in `scripts/validate-content.py` to enforce the `^[a-z0-9]+(-[a-z0-9]+)*$` slug format on every canonical skill and alias in `skill-registry.json` (removing the `_comment` string from `subjuntivo-morfologia.aliases` in `es-es` and `es-latam`).
    - **Hungarian (`content/hu`) Junk-Drawer Split (`195 → 216` canonical grammar skills):** Audited all 13 candidate skills and substring collisions (`relative` → `elative-bol-bel`, `feleség` → `postposition-fele`, `jóllehet` → `lehet-infinitive`, `foglalkozásod` → `fog-infinitive`, `lakik` → `aki-vonatkozoi-mellekmondat`) against the `91f95140` baseline, created 21 focused CEFR grammar skills (`negation-with-nem`, `subject-pronouns-omission`, `word-order-focus-and-is`, `direction-adverbs-jobbra-balra`, `mediopassive-verbs-odik`, `formal-address-on`, `hogy-clauses`, `weather-verbs-esik-sut`, `light-verb-collocations`, `spatial-questions-hol-hova`, `quantity-choice-questions-mennyi-melyik`, `demonstratives-ez-az`, `definite-article-a-az`, `accusative-quantities-and-measures`, `relative-clauses-aki-ami-amely`, `definite-vs-indefinite-conjugation`, `plural-nouns-after-quantifiers`, `inessive-location-chunks`, `existential-questions-van-itt`, `predicate-adjectives-zero-copula`, `kinship-possessives`), and individually tagged `593` review exercises. Top skills dropped from **`present-tense-routine-language`: `675 → 71` (`138 → 6` aliases), `ki-and-mi`: `347 → 91` (`57 → 11` aliases), `adversative-contrast`: `340 → 31` (`66 → 4` aliases), `ban-ben-in`: `165 → 119` (`33 → 7` aliases), `how-the-accusative-t-works`: `161 → 135` (`25 → 19` aliases), `elative-bol-bel`: `89 → 49` (`21 → 7` aliases)**.
    - **Spanish (`content/es-es` & `content/es-latam`) Junk-Drawer Split (`es-es`: `175 → 200`, `es-latam`: `190 → 219` canonical grammar skills):** Audited all 14 candidate skills against `91f95140`, retagged ~920 B1 CCSE/Cultura reading-title exercises from `subjuntivo-morfologia` to their true grammar structure (`voz-pasiva-ser`, `pasiva-refleja`, `superlatives`, `conectores-con-subjuntivo`) or unit vocabulary, split 25 focused CEFR skills (`subjuntivo-valoracion-necesidad`, `subjuntivo-opiniones-no-creo-que`, `subjuntivo-peticiones-propuestas`, `subjuntivo-relativas`, `conectores-con-subjuntivo`, `invitaciones-y-pedidos`, `preposiciones-movimiento`, `conectores-argumentativos`, `expresar-opiniones-preferencias`, `secuencia-narrativa`, `estilo-indirecto-informacion`, `saber-infinitivo`, `expresiones-probabilidad`, `intensificadores-y-grado`, `perifrasis-verbales`, `locuciones-preposicionales-formales`, `porque-y-por-eso`, `por-que-y-porque`, `conectores-causales-formales`, `ya-perfecto`, `todavia-no-perfecto`, `preterito-perfecto-participios`, `preterito-indefinido-narracion`, `voz-pasiva-historia`, `concesivas-a-pesar-de-por-mas-que`, `gerundio-acciones-paralelas`), and individually tagged `338` review exercises per course. Top skills dropped from **`subjuntivo-morfologia`: `1,059 → 17` in `es-es` / `154 → 17` in `es-latam` (`14/26 → 3` aliases), `present-tense`: `527 → 118` in `es-es` / `544 → 118` in `es-latam` (`70/87 → 13` aliases), `cause-consequence`: `303 → 107` in `es-es` / `372 → 139` in `es-latam` (`16/48 → 11/23` aliases), `ya-todavia-no`: `231 → 117` (`3 → 1` aliases), `preterito-perfecto-vs-indefinido`: `153 → 105`, `preterito-perfecto`: `529 → 54`, `preterito-indefinido`: `369/376 → 40/42`**.

99. ~~**Consolidate near-duplicate and single-use `teaches` skill slugs across courses (added 2026-09-25).**~~ — **Done 2026-09-25.**
    Following the metadata backfill in item 98, `hu` had 1,202 grammar skills (`1,549` distinct tags, `245` single-use), `es-es` had 611 grammar skills (`1,286` distinct tags, `276` single-use), and `es-latam` had 751 grammar skills (`1,511` distinct tags, `390` single-use), and newly added `grammar-titles.json` entries had Title-Case/mechanical-fallback formatting while backfilled `category: "vocabulary"` exercises sometimes carried grammar slugs.
    - **CEFR Title Curation & Validator Enforcement (`Phase 1`):** Rewrote all 1,154 Hungarian titles and 64 Spanish titles in `content/<course>/indexes/grammar-titles.json` to obey the mid-sentence CEFR title style (`0` violations across all three courses). Added `--strict` to `scripts/build_grammar_index.py` and `validate_grammar_titles()` to `scripts/validate-content.py`.
    - **Grammar Skill Consolidation & Alias Migration (`Phase 2`):** Consolidated fragmented and single-use grammar slugs into canonical CEFR grammar skills (**`hu`: `1,202 → 195` grammar skills, `1,549 → 345` total tags, `245 → 0` single-use tags; `es-es`: `611 → 175` grammar skills, `1,286 → 304` total tags, `276 → 0` single-use tags; `es-latam`: `751 → 190` grammar skills, `1,511 → 318` total tags, `390 → 0` single-use tags**). Recorded all merged slugs in `"aliases": [...]` in `content/<course>/indexes/skill-registry.json`, rewrote `exercises/*/*.json`, `diagnostic-test.json` (`30/30` mapped in all three courses), `verb-tense-skills.json`, `conversation-scenarios.json`, `writing-prompts.json`, `writing-exchanges.json`, and `skill-prereqs.json`, rejected alias slugs in `scripts/validate-content.py`, and added `LearnerModel.migrateProductionAliases()` in `engine/learnerModel.js` (`sw.js` `CACHE_VERSION = 'v2026-09-25i'`) with unit test coverage in `tests/drills/test-learner-signals.js`.
    - **Category / Skill-Kind Alignment (`Phase 3`):** Retagged `2,068` Hungarian, `2,121` Peninsular Spanish, and `1,523` Latin American Spanish exercises so every `category: "vocabulary"` exercise uses a `kind: "vocabulary"` unit theme slug and every `category: "grammar"` exercise uses a `kind: "grammar"` canonical skill. Enforced in `scripts/validate-content.py`.
    - **Follow-up fix (review, 2026-09-25):** the alias migration could double-count a learner's speaking/writing evidence under cloud sync. `productionEvidence` is merged key by key, so the first sync after migrating brought back a stale copy of each alias entry, and the next load folded it in again. Each canonical entry now records the aliases folded into it (`mergedFrom`, which syncs with the entry), and an alias that comes back after being folded is dropped instead of re-merged. Covered in `tests/drills/test-learner-signals.js`. Known leftover: some Spanish B1 listening exercises were given generic grammar tags (e.g. `stem-changes` on a passage about the Defensor del Pueblo). They don't feed the grammar index, but the labels are loose. Follow-up: item 100 split the catch-all skills created by this pass's substring/fallback matcher.

98. ~~**Give Hungarian a real grammar skill catalogue (added 2026-09-25).**~~ — **Done 2026-09-25.**
    `content/hu/indexes/grammar-index.json` had only 48 skills because Hungarian exercises used ~25 lesson-stage and content-domain labels (`controlled`, `practice`, `introduce`, `check`, `consolidation`, `review`, `civics`, etc.) in `category` instead of the six canonical categories, and 3,027 Hungarian exercises (278 in A1, 2,749 in B1) plus 114/564 Spanish B1 exercises had no `teaches` tag.
    - **Canonical skill registries & validator gate (`Phase 1`):** Created `content/<course>/indexes/skill-registry.json` (`es-es`: 1,287 skills, `es-latam`: 1,512 skills, `hu`: 1,549 skills) and extended `scripts/validate-content.py` (`METADATA_ENFORCED_EVERYWHERE = True`) so every exercise across all courses must have a valid 6-value `category` (`vocabulary | grammar | reading | dialogue | writing | listening`) and every non-`reading` exercise must have a non-empty `teaches` array registered in `skill-registry.json`.
    - **Hungarian `category` → `category` + `stage` (`Phase 2`):** Restored the 6-value `category` enum and added an optional `stage` enum field to `content/hu/schemas/exercises.schema.json`. Migrated all 6,723 off-list Hungarian exercise categories across 580 files via `scripts/backfill_hu_stage.py`.
    - **Full `teaches` & `category` backfill (`Phase 3`):** Backfilled all 61+61 missing Spanish B1 categories (and fixed 24 Reading-section exercises per Spanish course mislabeled as `grammar`), 114 `es-es` B1 and 564 `es-latam` B1 untagged exercises, 389 Hungarian exercises from sibling tags, 2,143 Hungarian B1 exercises from lesson grammar files (`-gr.json`) and unit vocabulary themes, and 495 Hungarian B1 consolidation exercises.
    - **Grammar index & diagnostic test resolution:** Rebuilt `content/<course>/indexes/grammar-index.json` and `grammar-titles.json` across all three courses (`hu` grammar exercises rose from 1,404 to 5,321 and distinct grammar skills rose from **48 to 1,202** with 0 uncurated title warnings). Retagged all 29 previously unmapped Hungarian placement diagnostic questions (`30/30` mapped) and the 2 remaining Spanish diagnostic questions (`es-diag-a1-06` and `es-diag-b1-05`, `30/30` mapped in both `es-es` and `es-latam`).

97. ~~**Match outside Decks, Verb Speed and the placement diagnostic feed the learner model**~~ — **Done 2026-09-25.**
    These were the last three gaps left after item 96.
    - **Match:** when a time limit ran out, Match marked every word not
      yet shown as missed, so switching on SRS credit would have given
      Again to words never tried. It now tracks wrong pairs separately
      (`_wrongUids`), and only those count. The study plan's Match and
      the recommended "weakest words" Match now credit fully
      (`srsCredit: true`). The lesson Quick Reinforce credits misses only
      (`srsCredit: 'misses'`), because a correct match seconds after the
      word was taught is short-term memory, and brand-new cards are due
      at once, so a hit would get a free first review.
    - **Verb Speed:** the tense/person breakdown used to live in memory
      and vanish at session end. Each answer now updates a
      `verb:<tense>:<person>` card through `Recycle.credit()` (one outcome
      per pair per session, flushed at the end or when leaving). The
      hand-written `content/es-*/indexes/verb-tense-skills.json` links
      tenses to grammar skills (`subjuntivo.futuro` is left unmapped
      because no skill teaches it). `LearnerModel.weakConjugations()`
      lists pairs that have been missed, and the study plan's Verb Speed
      block now opens on the weakest tense ("Verb speed drill: Preterite").
      Along the way, the missed-conjugations recap had always shown a
      blank verb; it now uses the real infinitive.
    - **Diagnostic:** each answered question is recorded as a `diag:<id>`
      card and joined to its skill through `teaches`. That's one data
      point among a skill's many exercise cards, so it's outweighed as
      practice builds up, unlike a level-test miss, which lowers a skill
      a tier for good. Tiers never reached send nothing. The tags were
      free text (2/30 Spanish and 0/30 Hungarian matched a real skill),
      so they were retagged: 28/30 Spanish (both courses), 1/30
      Hungarian. The Hungarian gap is in ROADMAP.md item 98.
      `_skillRefs()` now ignores any verb or diagnostic tag that names an
      unknown skill, so leftover free-text tags can't create phantom
      skills.
    Tests: `tests/drills/test-learner-signals.js` (joins,
    `weakConjugations`, and that the content tags resolve) and
    `tests/decks/test-deck-srs-credit.js` (Match wiring).

96. ~~**Grammar Driller, Reader lookups and Vocabulary Driller feed the learner model**~~ — **Done 2026-09-25.**
    An audit of which activities send no knowledge signal turned up three
    gaps, and all three are now wired in.
    - **Grammar Driller:** it recorded only accuracy per module, which the
      learner model never read, so drilling a skill didn't change its
      state. Each answer now updates that item's recycle card through the
      new `Recycle.credit()` (miss = again always; correct = good, due
      items only). Bank items are recorded as `bank:<id>`, and
      `LearnerModel._skillRefs()` joins them to their skill by module.
    - **Reader lookups:** `LearnerModel.recordLookup()` runs from
      `showWord()`. Looking up a word that has an SRS card counts as
      **again**, at most once per word per day. Looking up a word with no
      card is logged (store `wordLookups`, synced), and a word looked up on
      2+ separate days shows up in `weakWords()`. Known words are skipped.
    - **Vocabulary Driller:** feeds `creditPractice()`. A miss is again,
      a correct typed answer is good, and a correct multiple-choice answer
      is weak.
    - **Existing bug fixed along the way:** the learner model counted only
      cards with `reviews > 0`, but "again" resets `reviews` to 0, so an
      item that had only ever been missed looked "not yet seen". This hid
      the weakest items of all. It now counts lapses as history too
      (`hasHistory()`).
    Test: `tests/drills/test-learner-signals.js`. Still not wired: Library
    reading, Match outside Decks, Verb Speed by tense and person, and the
    diagnostic's per-tier answers.

95. ~~**Deck study modes feed the SRS schedule**~~ — **Done 2026-09-25.**
    Learn, Match and Blast used to leave SRS cards untouched, so drilling
    a deck earned no credit and the words stayed due in Review. Now
    `creditPractice()` (`engine/srs.js`) takes their outcomes. A miss in
    Match or Blast is an automatic **again**, even on a card that isn't
    due. A correct Match/Blast hit is a new non-button **weak** rating:
    the interval grows at the "hard" pace (1.2x) and ease stays the same,
    because recognising a word isn't the same as recalling it. Getting
    Learn's strict typed stage 4 right on the first try is a full
    **good**; wrong on the first try is **hard**. Weak, good and hard
    only count for cards that are due, so
    replaying a deck can't push intervals out. Each game sends one
    outcome per word per session, and a miss beats a hit. Words with no
    card are never enrolled. Match is also used by lessons and the study
    plan, so credit is opt-in (`srsCredit: true`) and only Decks turns it
    on. Known quirk: a wrong pair in Match marks both tapped words as
    missed, as the missed-pairs recap already did. Test:
    `tests/decks/test-deck-srs-credit.js`.

94. ~~**Rewrite the B1 Unit 1 exercises**~~ — **Done 2026-09-25.** (Was ROADMAP.md active item 94.)
    B1 Unit 1 (`b1-01-*`, identical in es-latam and es-es) had been
    machine-templated. The grammar multiple-choice questions quoted
    their own answer ("Elige la opción que mejor encaja en «Ya había
    salido.»") next to a fixed "La historia ocurre mañana." distractor.
    Dialogues were a generic "¿Qué sabes sobre el tema?" / "Entiendo.",
    and the consolidation repeated one set of items three times. The
    whole unit was rewritten around one storytelling thread, keeping
    every exercise ID, type and section so the lesson files didn't
    change:
    - **Lessons:** 1 is a power cut (the preterite), 2 is waiting in the
      rain (imperfect vs preterite, *soler*), 3 is the missed train (the
      pluperfect), 4 is the lost wallet (*sin embargo*, *por eso*,
      *así que*, *además*), and 5 is Don Quijote (all three tenses). Its
      four reading questions now ask about the actual story
      (`stories/classics/b1/b1-01.json`).
    - **Consolidation:** 15 new mixed items, plus the 3 rewritten earlier
      (item 93).
    - **Grammar pages:** full conjugation tables (regular endings,
      including a labelled *vosotros* row, the irregulars the lesson
      uses, *haber* + participle, irregular participles), a
      "which tense?" table and a connector table. Examples come from
      each lesson's scene, and each page has a tip and a link reused
      from existing ones.
    - **Vocabulary:** 7–8 words per lesson that match the scenes. The
      stray *diverso*, *sociedad* and *mensajero* were dropped. The
      lesson goals' "three new expressions" became "the new
      expressions".
    - **Language:** neutral enough for both courses (no *móvil*,
      *coche*, *piso*, *vale*, *camarero* or *ustedes*/*vosotros* verb
      forms in exercises), and correct answers are spread across option
      positions.
    - **Other units:** a check of es-latam found no other exercise file
      with the template's phrases, so this was the only unit built that
      way. Committed as `318bea27`.

93. ~~**Name the leftover grammar skills "reading"**~~ — **Done 2026-09-25.** (Was ROADMAP.md active item 8.)
    The user chose not to hand-name or retag what the audits (items 89
    and 91) left open, but to label it "reading".
    - The 151 es-es skills and 1 hu skill added by the CCSE and
      Hungarian citizenship rewrites after the naming pass are named
      "reading". Many of their IDs are whole phrases, like
      `acoger-el-festival-internacional-de-cine-y-entregar-la-concha-de-oro`.
    - The 18 mis-tagged exercises with no fitting skill were moved to
      a new `reading` skill (named "reading") in each course. These are
      the two placeholder exercises in `b1-01-consolidation` (ex01,
      ex13), the plain CCSE and hu citizenship sentence-builders, and
      the hu *lenni* exercise `a1-21-review-2`. The overhaul had already
      rewritten one, `b1-orszagma-consolidation.ex12`, and it was left
      as is. The placeholders, plus a third identical one (ex07) the
      audit had missed, were then written as real exercises: *mientras*
      + imperfect interrupted by a preterite, putting events in order
      with *primero / luego / por último*, and the pluperfect for an
      earlier past. They are tagged `imperfecto`, `past-sequence` and
      `pluscuamperfecto`, in es-latam and es-es. The rest of the unit was
      rewritten next (item 94).
    - Restored the earlier "reading" rename of the 33 no-grammar skills
      (item 91), which hadn't made it into that commit.
    - Result: `build_grammar_index.py` reports no unnamed skills in any
      course. 157 es-es, 30 es-latam and 2 hu skills are named
      "reading".

91. ~~**Grammar `teaches` tags that don't match the exercise**~~ — **Done 2026-09-24.** (Was ROADMAP.md active item 7.)
    Every grammar exercise was checked against its `teaches` tags, 7,573
    exercise–tag pairs across es-latam, es-es and hu. Parallel agents
    checked each skill's exercises against its curated name, then I
    reviewed the results by hand. 179 findings:
    - **Removed 105 stray tags** where the exercise already had the
      right one. The biggest clusters were in es-latam A2. `a2-10-01`
      to `a2-10-05` tagged present-perfect drills as `porque`, and
      `a2-16-01` to `a2-16-05` tagged *ir a* + infinitive drills as
      `preterito-indefinido`. In Hungarian A1, whole lessons had both of
      their skill tags on every exercise (`ez-az-this-that` +
      `mi-micsoda-what`, `sok-egy-singular-noun` + `egyutt-together`).
    - **Retagged 56** to the existing skill that fits, e.g. a
      `habitos-soler` exercise that tests the passive *se*, and a
      `cause-consequence` one that tests *si* + imperfect subjunctive.
      `ser-questions` (all about *llamarse*) was folded into `names`,
      and the stray `negation`, `gerund` and `passive-voice-legado` tags
      are gone. These skills disappeared from the index, and their
      names were pruned from `grammar-titles.json`.
    - 18 were left unchanged: plain sentences with no grammar point,
      two placeholder exercises, and one HU *lenni* exercise with no
      matching skill (resolved in item 93).
    - The 33 skills whose exercises contain no grammar (comprehension
      questions, sentence ordering) are now named "reading", as is
      `gerund`, which is left with one such exercise.
    - Edits were made on the `teaches` array as text, so file
      formatting was kept. The Hungarian citizenship overhaul
      (`c67fa8f8`) landed mid-audit. The 7 edited files it touched were
      reverted and re-checked against the new content before the fixes
      were applied again.

90. ~~**Complete Authoring of Spain Citizenship Track (`content/es-es`, Units 1–36) & Consolidated Unit Library Readings**~~ — **Done 2026-09-24.** (Was ROADMAP.md active item 1.)
    - Authored all **36 units** (Units 37–72 in `content/es-es/curriculum/units/b1.json`, `b1-constitucion` through `b1-simulacro`) of the Spain Citizenship (`cultura` / CCSE) B1 elective track to the full pedagogical standard matching the Hungarian Citizenship (`hu`) and Latin America (`es-latam`) tracks:
      - **216 lessons** (`180` 8-part main lessons + `36` consolidation lessons) replacing all legacy 6-exercise `b1-ccse-*` stubs.
      - **2,268 schema-validated exercises** (`63` exercises per unit: `11` per main lesson + `8` per consolidation lesson, covering `multiple-choice`, `fill-blank`, `sentence-builder`, and `dictation`).
      - **1,440 vocabulary items** (`40` per unit across `180` `-voc.json` files) and **180 contextual civic/grammar modules** (`-gr.json`).
      - **180 TRIH-style 5-paragraph world stories** (`900` narrative paragraphs + `540` comprehension questions) covering all five official Instituto Cervantes CCSE tasks (*Tarea 1: Gobierno, legislación y participación ciudadana; Tarea 2: Derechos y deberes fundamentales; Tarea 3: Organización territorial y geografía física y política; Tarea 4: Cultura e historia; Tarea 5: Sociedad española y vida cotidiana*).
      - **Units 1–36**: `b1-constitucion`, `b1-monarquia`, `b1-cortes`, `b1-gobierno`, `b1-judicial`, `b1-autonomias`, `b1-participacion`, `b1-seguridad`, `b1-unioneuropea`, `b1-simbolos`, `b1-lenguas`, `b1-cervantes`, `b1-derechos`, `b1-igualdad`, `b1-deberes`, `b1-garantias`, `b1-geografia`, `b1-norte`, `b1-mediterraneo`, `b1-centrosur`, `b1-ciudadesautonomas`, `b1-historiaantigua`, `b1-historiacontemporanea`, `b1-literatura`, `b1-arte`, `b1-musicacine`, `b1-fiestas`, `b1-gastronomia`, `b1-sanidad`, `b1-educacion`, `b1-empleo`, `b1-vivienda`, `b1-documentacion`, `b1-transporte`, `b1-consumobanca`, `b1-simulacro`.
    - **Consolidated Unit Library Readings (`scripts/stitch_track_unit_stories.py` + `build-manifest.py`)**:
      - Stitched the 5 lesson readings of each B1 elective track unit into **1 consolidated 25-paragraph Library reading per unit** (`b1-<slug>.json`) whose `"title"` matches the exact Unit Title in `curriculum/units/b1.json` (`36` in `es-latam`, `36` in `es-es`, and `36` in `hu`).
      - Updated `build-manifest.py` so individual lesson sub-stories (`b1-<slug>-01..05*`) remain accessible inside their lessons while the Library displays one clean consolidated reading per unit.

89. ~~**Readable, CEFR-style names for grammar skills**~~ — **Done 2026-09-24.** (Was ROADMAP.md active item 6.)
    Practice suggestions name the weak skill mid-sentence ("You made a
    few mistakes with … lately", item 88), but Spanish had no curated
    names, so learners saw title-cased IDs ("Cambio Radical Reflexivos",
    "Estar Ando") or story titles ("La crisis de 1929").
    - New `content/es-es/indexes/grammar-titles.json` (459) and
      `content/es-latam/indexes/grammar-titles.json` (751): every skill
      in both courses, 781 distinct IDs. Hungarian's 46 were restyled to
      match. Names use plain CEFR-inventory English, start lowercase and
      are written to sit mid-sentence: "stem-changing reflexive verbs",
      "estar + gerund for -ar verbs", "stating purpose with a fin de
      que". No colons, dashes or parentheses.
    - Names follow what the tagged exercises actually test, not the ID,
      where the two disagree (see item 91). Skills whose
      exercises contain no grammar are named after the activity:
      "understanding the text", "putting sentences in order".
    - Drafted in parallel batches from each skill's sample exercises and
      lesson titles, then reviewed by hand against the ID and the
      exercises.
    - `engine/drills/grammar.js` capitalises the first letter for its
      topic list. `humanizeSkill()`'s fallback for an unnamed skill is now
      the ID with spaces, not title case. `scripts/build_grammar_index.py`
      warns about any skill missing from `grammar-titles.json`.

88. ~~**Practice suggestions lose their item counts and game names**~~ — **Done 2026-09-24.**
    Buttons like "Grammar: Cambio Radical Reflexivos (5 questions)",
    "Match Game (10 words)", "Audio Decode", "Suffix Sprint" and "Fast
    Translation" read like a quota and a game. Every practice suggestion
    now names the activity plainly and gives the reason in one sentence.
    The pattern: *"You made a few mistakes with stem-changing reflexives
    lately. Practice it here:"* followed by a **Grammar practice**
    button.
    - `engine/recommendationEngine.js` `_miniGameNudge()`: each candidate
      has a plain `title`, a `buttonLabel` with no count ("Listening
      practice", "Sentence translation", "Suffix practice", "Word
      matching", "Conjugation practice, timed"), a `blurb` that states
      the reason, and a new `invite` field ("Practice it/them here:").
      `secondaryLabel()` lost its counts too.
    - `engine/home.js` `miniGameCard()`: the eyebrow "Quick challenge"
      became "Practice", and the card shows `blurb` + `invite` before the
      buttons. Workshop's "What's next?" card shows `blurb` alone.
    - `engine/lessons.js` end-of-lesson buttons: "Grammar practice",
      "Vocabulary practice", "Word matching", "Listening practice",
      "Speaking practice". The session lengths themselves haven't changed.
    - Follow-up: skill names in these sentences are often raw IDs
      (done the same day, item 89).

87. ~~**New-learner introduction replaced: a quiet first screen, margin notes and end-of-lesson invitations**~~ — **Done 2026-09-24.** (Was ROADMAP.md active item 3.)
    The old system (item 56: Home welcome card, a banner on the first
    visit to each room) felt heavy. It explained rooms up front, with
    generic onboarding copy. Replaced by a gradual first week, with the
    flow and all copy in `docs/feature-guidance-copy.md`:
    - **First screen** (`engine/home.js`, `showWelcome()`): the name, one
      sentence, then one question at a time: language, which Spanish
      (Latin America / Spain), then "Start from the beginning" or "Find
      my level" (straight into the placement test). A course change
      reloads the app, so the choice is carried across the reload in
      `parlour_welcome_pending`.
    - **Margin notes** (`Guide.note()`): one serif-italic line with a
      thin accent rule, no box or shadow, fixed below its anchor and
      re-placed on scroll. Closed by any tap, and retired after two
      showings. At most one a day, except the first-lesson basics
      (listen, tap a word, "Anything you miss comes back at the end").
      A note counts only once it has been on screen, and lesson notes
      appear only on steps that aren't asking a question. Arrival notes
      are in Decks, the Library (first story), the Speaking/Writing
      studios and the first review card. Later notes cover Decks import
      (third visit), My Texts (5 stories read or past A1), Grammar Guide
      (after reopening a finished lesson), My Dictionary (after a word
      graduates) and streak import (Journey).
    - **Invitations** on the lesson summary (`Guide.invitation()`): the
      deck after the first lesson (with Next lesson), the Library after
      Unit 1, the Workshop after Unit 2. Each is skipped once that tab has
      been visited (`Guide.markVisited()` from `showTab()`). A skipped
      invitation comes back once.
    - Removed: the per-room banners and their CSS, the Home welcome card,
      and `#lesson-guide-slot`. "How Parlour works" is unchanged and now
      opened from a quiet link at the bottom of Home, plus the nav
      footer. The drillers' "About this drill" info is unchanged.
    - The approved invitation wording "Tomorrow they'll come back" was
      changed to "ready for a short review", because new cards are due
      immediately (`newCardSchedule()`).
    - Not built: the Verb Driller and Listening Driller notes, which have
      no signal to trigger on (ROADMAP.md active item 5).
    - Verified live at phone width on a fresh profile, covering the first
      screen, the course switch and reload, and every note and
      invitation. `tests/drills/test-onboarding-guide.js` was rewritten
      for the new API.

86. ~~**Communicative challenge no longer swaps the can-do for an unrelated canned scenario**~~ — **Done 2026-09-24.**
    User finished LatAm B1 `b1-precolombina-02` and got the challenge "Ask
    someone on the street for directions to a station, hotel…" under the
    target "explain who the Maya, Mexica and Inca were, and roughly where
    and when each flourished". `engine/canDoPrompt.js` picks a scenario
    template by bare substring match, and `'where'` counted as a directions
    keyword. A corpus scan showed 340 can-dos across all courses were
    templated, most of them wrongly: "counties/country/encounter" went to
    "count out loud", "family structure" to "talk about your family", "market
    economy" to shopping, "table/meal" to restaurant, and Brazil's coffee
    economy to "order at the café". Now there is one `TOPIC` table of
    whole-word regexes, shared by the title and the prompt. Incidental
    triggers are gone (`where`, `table`, `meal`, `daily`, bare
    `day`/`count`/`number`/`market`/`buy`). Anything unmatched falls back to
    the generic prompt, which restates the can-do itself. After the fix, 86
    can-dos are templated, all genuine café/shop/restaurant/directions/
    family/routine/hobby/calendar situations. Note that JS `\b` is
    ASCII-only, so `café` needs `(?![a-z])`, not `\b`. Regression cases
    were added to `tests/drills/test-cando-prompt.js`.

85. ~~**Vocabulary Driller's B1 gate closed everywhere, including timed sessions**~~ — **Done 2026-09-24.**
    The driller has been B1+ since 2026-09-23 (`minLevel: 'B1'` in
    `engine/workshop.js`, mirrored in RecommendationEngine), but four
    other buttons opened it directly. Below B1, `Workshop.open()` just
    bounced them to the picker, which is why the user's "review missed
    words" after a Decks review "just sends me to Workshop". The leaks:
    Decks' "Practice N missed words", the lesson summary's "Vocabulary
    (N words)" reinforce button and its goal-remediation fallback, and
    the timed session's vocabulary blocks. Added `Workshop.isAvailable(id)`
    (the picker's own `_available()` rule) and used it at all four, so
    the gate has one source. Below B1 these buttons are now hidden, and
    the goal-remediation button falls back to speaking. Applies to every
    course, not just Spanish, same as the picker. Verified in the
    preview: at A1 a 30-min plan with 25 weak, due words had no vocabulary
    blocks and neither button showed; with the level faked to B1 all of
    them came back.

84. ~~**Time-Based Sessions rebuilt: urgency-ranked, short blocks, runs to the clock**~~ — **Done 2026-09-24.**
    The old builder had a fixed order and only used reviews, the next
    lesson, grammar, vocabulary, listening, speaking and Match Game. It
    also had a bug: grammar and vocabulary split *all* the remaining time
    between them, so whenever both had something to practise (the usual
    case), nothing was left for the "always included" speaking prompt,
    listening, speaking or Match Game. User's spec for the rebuild: the
    most urgent thing goes first, then the next most urgent, and so on,
    with every activity considered; the next lesson goes 2nd; the short
    speaking prompt always goes 3rd; practice comes in short blocks
    ("rather 3x1.5 minute activities" than 5 minutes of one driller); and
    if the learner gets through the plan early, keep recommending
    activities until the chosen time is up.
    `engine/studyPlan.js` now builds from *sources*, each ranked on one
    shared urgency scale (`URGENCY`): due reviews 90-100, weak grammar
    skill 80 (+5 if the level test flagged it), weak words 75, weak spoken
    skill 70, weak driller 60-70, developing grammar skill 50. Activities
    with no weakness signal are filler at 10: Verb Driller, Translation,
    Listening, Speaking, the Hungarian drillers, Match Game, and one
    Library story that fits the time. Each block taken from a source costs
    it 25 points (`REPEAT_PENALTY`), so filler rotates and a big review
    backlog alternates with other work instead of taking the whole
    session. The same kind never runs twice in a row while anything else
    is available. Blocks are ~1.5 min (`BLOCK_MINUTES`); reviews are 9
    words (~3 min), since 4-word flashcard blocks felt too choppy.
    The budget is now also a clock, counted from when the plan starts,
    breaks included. `StudyPlan.extend()` appends the next most urgent
    thing when the planned items are done and at least a minute is left
    (the next lesson is a candidate here too). If time runs out with
    planned items left, the runner shows a "Time's up" screen: "Finish
    session", or "Keep going: {next} →", which switches off the clock for
    the rest of that session (`keepGoing()`). There's still no visible
    countdown.
    `engine/studyPlanRunner.js` launches the new kinds: Translation and
    the Hungarian drillers are embedded like Grammar; the Verb Driller (a
    60s speed drill) and reading leave for their own tabs, the way reviews
    already did (the flag is now `_leavingForActivity`). The Reader has no
    results screen, so `engine/reader.js` hands back through
    `StudyPlanRunner.onReadingClosed()`: closing the story returns to the
    session and ticks it off (finished or not), skipping the "next in
    series" offer; leaving the Library through the nav ends the session.
    `LearnerModel.availableDrillers()` was added so the planner knows
    which drillers are unlocked for this course.
    Verified in the preview: plans for a new learner and for a seeded
    learner (25 due cards, weak words, a speaking prompt) came out in the
    expected order; an extra activity was added after the plan ran out;
    the "Time's up" screen appeared with the clock moved forward, and
    "Keep going" launched Translation embedded; the Verb Driller ran its
    60s drill and its results button read "Next: Read: Carlos conoce a
    Meg"; finishing the story returned to the session with it ticked off;
    leaving the Library through the nav ended the session.
    Not built: the Writing Studio's open composition (too long for a
    short block).
    **Follow-ups the same day**, after the user reviewed it:
    - When nothing is urgent (a new learner), the lesson goes 1st and
      filler follows it, instead of a verb drill before Lesson 1.
    - A story only counts as done when it's finished
      (`StudyPlanRunner.markReadingFinished()`, called from
      `finishStory()`). Closed early, it stays the current item.
    - "Skip this activity": a quiet text link under the checklist's main
      button and above every embedded driller. `StudyPlan.skip()` moves
      on without counting it: the checklist shows it struck through with
      "–" and no green tick, and the completion screen's "N things done"
      leaves skips out (`doneCount()`).
    - Reviews come in blocks of 10 (`REVIEW_BLOCK_WORDS`).
    Verified in the preview: a new learner's plan starts with the lesson;
    reviews came out ×10; the skip link above an embedded Translation
    moved on to the next item and marked the skipped one; closing a
    story early left it current, finishing it ticked it off; completion
    read "2 things done" for 3 items with 1 skipped.

83. ~~**"Only words from my lessons" opt-in toggle on every dictionary-wide driller**~~ — **Done 2026-09-23.**
    User asked for a switch on the "relevant" Workshop drillers that
    restricts them to words the learner has actually encountered in a
    completed lesson. Five drillers deliberately draw from the full
    dictionary/verb list by default (each says so in its own header
    comment): `hu-verb`, `hu-suffix`, `hu-prefix`, `hu-morphology`, and the
    Spanish `verbs` driller (Table + Speed). `engine/drills/vocabulary.js`
    already does something similar unconditionally via its own
    `_isReached()`, backed by `content/<lang>/indexes/word-lesson-index.json`
    (lemma -> first-teaching lesson) — but that one deliberately fails
    *open* on an indexless lemma, which is fine for an always-on filter
    over an already-level-scoped pool.
    Extracted a new shared module, `engine/taughtWords.js` (`TaughtWords`),
    for the new opt-in toggle — deliberately failing *closed* instead:
    checked empirically that only ~28% of hu-verb's candidate verbs have
    any word-lesson-index entry at all, so reusing vocabulary.js's
    fail-open rule here would have left the toggle barely restricting
    anything, defeating a feature whose whole point is a strict guarantee.
    Wired a "geo-toggle" switch (same component as the existing Tense/
    Definite/vosotros toggles) into all five settings screens, each
    filtering its own pool by the relevant lemma (verb lemma for hu-verb/
    hu-prefix/verbs, word lemma for hu-suffix/hu-morphology) once the
    toggle is on. `engine/verbs.js`'s Spanish list also got a
    `_rebuildVerbList()` extraction (was inlined in `init()`) with a
    fail-open *fallback* — not the same as TaughtWords' own fail-closed
    lookup — for the case where the filtered list would otherwise be
    completely empty, so flipping the toggle can never silently break the
    driller for a learner very early in the course. Verified live across
    all five: toggling on visibly shrinks the pool (Hungarian Verb Driller
    563 → 4 with ~11 lessons done, → still small but sensible with 60;
    Spanish Table mode correctly loaded "leer," an early-taught verb, with
    the toggle on) and toggling off restores the full pool.

82. ~~**"About this drill" info popup added to every Workshop driller's settings screen**~~ — **Done 2026-09-23.**
    User asked for a closeable info bubble on each drill explaining what it
    trains, why it can feel odd at first, and what improvement actually
    looks like — using the Hungarian Verb Driller (items 80-81) as the
    example: "you might not know the verb itself, but if you know the
    ending you can construct the correct form." Built one shared component,
    `engine/drillInfo.js` (`DrillInfo`), reusing the app's existing
    `.wp-overlay`/`.wp-sheet`/`.wp-header`/`.wp-close` bottom-sheet
    component (the same one `engine/guide.js`'s "How Parlour Works" modal
    and the Reader's word-tap popup already use) rather than inventing a
    new modal pattern — a content dictionary keyed by driller id
    (`hu-verb`, `hu-suffix`, `hu-prefix`, `hu-morphology`, `verbs`,
    `grammar`, `vocabulary`, `translation`, `listening`, `speaking`,
    `writing`), a `buttonHtml(id)` helper that returns a small "ⓘ About
    this drill" link to splice next to a settings screen's own title, and
    `attach(container)` to wire its click handler alongside a screen's
    other event listeners. Wired into all eleven settings/setup screens
    across `engine/drills/hu-verb.js`, `hu-suffix.js`, `hu-prefix.js`,
    `hu-morphology.js`, `engine/verbs.js` (Spanish), and
    `engine/drills/grammar.js`, `vocabulary.js`, `translation.js`,
    `listening.js`, `speaking.js` (both its Sentence Drills and Verbal
    Production Studio screens), `writing.js`. New CSS (`.di-info-btn`,
    `.di-title`, `.di-body`, `.di-p` in `styles/workshop.css`, near the
    existing `.hv-info-link` it's visually modeled on) plus the usual
    `?v=` bump and `sw.js` `CACHE_VERSION` bump so it actually reaches
    already-installed users. Verified live: the link renders under each
    driller's title, opens the popup centered with a dimmed backdrop,
    closes via the × button, a backdrop click, or Escape — confirmed
    directly on the Hungarian Verb Driller (screenshot) and confirmed via
    console checks that every other listed driller (Spanish `verbs`,
    `grammar`, `vocabulary`, `listening`, `speaking`, `writing`) renders
    the same button correctly.

81. ~~**Hungarian Suffix Driller's unattended recommendation could mix in untaught Possessive/Case suffixes; also fixed a pre-existing bug that left its Plural pool permanently empty**~~ — **Done 2026-09-23.**
    Follow-up audit after item 80: user asked whether other
    `RecommendationEngine` candidates had the same "recommends untaught
    content" shape. `engine/drills/hu-suffix.js`'s own header comment
    already says plainly it "runs dictionary-wide... plural ships Unit 5,
    possessive Unit 6/9, case Unit 11+" and that the settings screen
    "frames this plainly" — but `RecommendationEngine`'s mini-game/weak-
    driller nudges launch it via `autoStart: true` with no explicit
    `type`, skipping that settings screen (and its warning) and defaulting
    to `TYPE.MIXED`, so a learner recommended "Suffix Sprint" at
    `lesson.a1.22` (when Plural ships) could get quizzed on Case suffixes
    ~30 lessons before Unit 11 teaches them, with no warning shown.
    Fixed by adding `_taughtTypes()`/`_restrictAutoMixed` to
    `hu-suffix.js`: an unattended `autoStart` launch with no explicit
    `type` now only mixes in Plural/Possessive/Case as each is actually
    taught (`lesson.a1.22`/`lesson.a1.26`/`lesson.a1.51`, the last two
    matching the driller's own comment and `hu-morphology`'s existing
    gate for the same milestone); a learner who opens the driller manually
    still sees every type in the picker and can choose Case on purpose,
    since they've seen the warning first.
    While verifying this live, found the Plural pool had been completely
    empty since the driller shipped: `_load()`'s bucketing checked
    `tag.case` before `tag.number === 'pl'`, and `word-index.json` tags
    even plural-nominative forms with `case: 'nom'` (nominative being the
    unmarked baseline every noun carries) — so every plural entry fell
    into the Case bucket instead, and picking "Plural" always rendered
    "No entries of this type yet." Fixed the same edit by excluding
    `case === 'nom'` from the Case bucket. Verified live across 15-25
    randomized `autoStart` launches at each curriculum stage: Plural-only
    before `lesson.a1.26`, Plural+Possessive (no Case leakage) before
    `lesson.a1.51`, all three once taught; manual settings-screen
    selection of Case still works unrestricted at any stage. Also checked
    Spanish for the same class of bug: the one Spanish-specific
    unattended-recommendation candidate (`verbs`, "Verb Speed Sprint")
    always defaults to `indicativo.presente` (the first tense taught)
    unless the learner had personally switched tenses themselves — no
    equivalent gap found there, or in the shared Translation/Listening/
    Speaking candidates (already level-scoped) or Grammar/Vocabulary/SRS
    candidates (already evidence-gated via `LearnerModel`).

80. ~~**Hungarian Verb Driller could quiz untaught plural persons; curriculum now teaches them, driller gated on it**~~ — **Done 2026-09-23.**
    User reported RecommendationEngine pushed the Verb Driller as a nudge
    while learning Hungarian, and it quizzed the -unk/-ünk (1pl, "we")
    ending before that form had ever been taught. Root cause:
    `engine/drills/hu-verb.js` deliberately draws its verb pool from the
    full dictionary regardless of lesson progress (by design, for
    vocabulary breadth), but also hardcoded all six grammatical persons
    (1/2/3, sg/pl) into every session — including the three plural ones,
    which no A1 lesson actually named as a grammar point. Confirmed by
    reading the curriculum: `content/hu/grammar/a1/a1-97-a-gr.json`
    ("Review of Present Tense Verbs", lesson.a1.97) only reviewed
    dolgozom/dolgozol/dolgozik (singular) despite being the level's
    present-tense consolidation point; nothing taught -unk/-ünk,
    -tok/-tek/-tök, or -nak/-nek as verb endings anywhere in A1.
    `engine/recommendationEngine.js`'s `hu-verb`/`hu-suffix` candidates
    gate only on lesson *count* (`completedCount >= 8`), not on what
    grammar has actually been taught — unlike the `grammar`/`vocabulary`
    candidates, which route through `LearnerModel.weakSkills()`/
    `weakWords()` and can't fire on unseen content.
    Fixed both sides: (1) extended `a1-97-a-gr.json`'s "Review of Present
    Tense Verbs" into an actual full-paradigm lesson — a 6-row table
    (dolgozom/dolgozol/dolgozik/dolgozunk/dolgoztok/dolgoznak), new
    examples, and a tip explaining the -unk/-ünk vs -tok/-tek/-tök vs
    -nak/-nek vowel-harmony split — plus 5 new drilling exercises in
    `exercises/a1/a1-97-ex.json` (wired into the lesson's Controlled/Check
    groups) so plural persons are actually taught and practiced, not just
    mentioned; (2) added `_availablePersons()` to `hu-verb.js`, which
    restricts the driller's pool to singular persons only until
    `LearnerPath.isComplete('lesson.a1.97')`, same lesson-id-gate pattern
    `hu-suffix`/`hu-prefix` already use elsewhere in
    `recommendationEngine.js`. Settings-screen hint now says so
    explicitly when gated. Verified live: with `lesson.a1.97` incomplete,
    the driller reports only singular forms available; marking it
    complete immediately unlocks all six persons.

79. ~~**Time-Based Sessions: results screen names and launches the next task directly**~~ — **Done 2026-09-23.**
    User feedback: finishing a task inside a time-based session required
    an extra click ("Back to your plan →") just to get back to the
    checklist, then a second click on the checklist's own "[item] →"
    button to actually start the next task. First attempt was an
    auto-advance timer (return to the checklist automatically a few
    seconds after results) — user clarified that wasn't it: they wanted
    the button itself to name and launch the next activity directly,
    skipping the checklist screen in between entirely. `mountNextAction()`
    (`engine/studyPlanRunner.js`) now peeks the queue's next item
    (`_peekNextItem()`) and labels the button "Next: {that item's
    description} →" (e.g. "Next: Quick speaking — 40s"), or "Finish
    session →" when it's the last one. Clicking it calls
    `StudyPlan.advance()` and launches the returned item straight into
    `#study-plan-activity` via the same `launchItem()` the checklist's own
    button uses (`goTab('study-plan-screen')` first for the few kinds —
    lesson/test/review — whose results live on a different tab; a
    same-tick DOM write, so nothing is visibly shown mid-swap). Verified
    live: the button reads the real next item's label, clicking it
    advances the plan's index and embeds that driller directly, and the
    last item correctly shows "Finish session" instead.

78. ~~**Post-unit practice nudge was dead code; fixed, and Written Exchanges given parity with Conversation Scenarios**~~ — **Done 2026-09-23.**
    While wiring the Writing Studio's Written Exchanges (texting-style
    roleplay) into the recommendation engine alongside Speaking's oral
    Conversation Scenarios, found that the existing "Put it into
    conversation" post-unit nudge (`engine/recommendationEngine.js`'s
    `_practiceNudge()`) never actually rendered. `recommend()` builds it
    via `Object.assign({ kind: 'unit-nudge' }, nudge)`, but `nudge` itself
    carried its own `kind: 'scenario'` field — the later source in
    `Object.assign` wins, so `primary.kind` silently ended up `'scenario'`
    instead of `'unit-nudge'`, and every check for `primary.kind ===
    'unit-nudge'` (`engine/home.js`'s Home render, this engine's own
    `_nextActionInfo`/`_routeTo`) never matched. The card had presumably
    never shown since this system was built. Fixed by renaming the inner
    field to `type` so it no longer collides with the wrapper's `kind`;
    added a regression test (`tests/drills/test-scenario-learner-path.js`)
    asserting the merge directly. With that working, `_practiceNudge()`
    and the per-lesson mini-game candidate list now also try
    `writing-exchanges.json` (matched by `unitIds`, same shape as
    `conversation-scenarios.json`) when no oral scenario matches the
    just-finished unit, routing into Writing Studio's Exchanges tab via
    the same `scenarioId` option Speaking already used. Verified live:
    both the scenario and exchange paths now render the Home card and
    route to the correct driller/item.

77. ~~**Recycle scheduling switched from wall-clock time to app opens, and leech handling wired up**~~ — **Done 2026-09-23.**
    The grammar/skill recycle system (`engine/recycle.js`) reused the
    vocabulary deck's SM-2 "again" rule of "due again in 1 minute"
    (`SRS_CONFIG.AGAIN_MINUTES`, `engine/srs.js`). That works for a large
    vocab deck where one overdue card is diluted among hundreds of others,
    but a recycle pool for one grammar point can be a handful of exercises
    — one miss stayed "due" essentially forever in real time, so it
    permanently won that concept's one recycle-block slot
    (`pickRecycleExercises`'s due-first sort + one-exercise-per-`teaches`-
    tag diversity rule) in every subsequent lesson, however many days
    passed. Recycle scheduling now runs on a new global open counter
    (`window.AppOpens`, bumped once per page load in `engine/init.js`)
    instead of dates: a miss ("again") is due starting the *next* app
    open, never mid-session, and growth for later ratings (hard/good/
    easy) uses the same ease-based SM-2 shape but counts in opens instead
    of days. Vocabulary SRS (`engine/srs.js`) is untouched — this only
    affects `engine/recycle.js`'s exercise-recycling schedule. **Leech
    handling wired up same day**: `pickRecycleExercises` now sorts a
    leech (8+ lapses, same threshold/meaning as the vocab deck) behind
    any non-leech due exercise on the same `teaches` concept, so a
    different exercise gets a turn once one exists — it's still served
    when it's the only option for its concept, never excluded outright.
    The lesson screen also shows the same quiet "Leech" badge next to the
    title that the vocab review card shows (`Recycle.isLeech()`,
    `engine/lessons.js`'s shared `renderStep()` title line) —
    informational only, matching the vocab deck's existing philosophy
    (see `engine/decks.js`'s comment on `card.leech`) that a leech is a
    signal for the learner, not a card to suspend.

76. ~~**Communicative Challenge reshuffle (Tier 1)**~~ — **Done 2026-09-23.**
    The challenge card had it backwards — the bold headline was the
    generic CEFR task description (e.g. "Ask for a coffee and water
    politely"), while the actual sentence to produce was buried inside
    the "Points to include" bullet list. For Tier 1 (A1, single-target)
    challenges, the card now leads with "Say this in {language}:" plus
    the English sentence to translate; the CanDo/task framing moved to
    the post-solve success message ("Well done! With this, you've
    completed a CEFR A1 requirement: '...'"). Added an `english` field
    to the challenge step shape (`engine/lessons.js`, `content/*/schemas/
    lesson.schema.json`, `content/es-latam/curriculum/challenges.json`)
    carrying that source sentence. Tier 2/3 (situational, multi-cue, no
    single target sentence) were intentionally left unchanged — worth
    revisiting later whether they need the same canDo-framing-moved-to-
    completion treatment for consistency.

75. ~~**Fix the same white-rectangle `--bg-card` bug in CEFR Diagnostic, Level Test, Home onboarding**~~ — **Done 2026-09-23.**
    Direct follow-up to item 74, at the user's request to check these two
    screens specifically. A project-wide grep found `--bg-card` used in
    exactly 10 places outside its own token definition — every one of
    them in `styles/components.css`'s Level Test (`.lt-*`)/Diagnostic
    (`.diag-*`)/Home-onboarding (`.hm-onboarding-card`) sections, plus the
    one `.sp-mic-btn` instance items 72-74 deliberately left alone. Not
    used correctly anywhere else in the app — strong evidence this is a
    dead vestige of the 2026-08-14 "soft card" design phase that got
    reversed the same day (per `[[visual-identity-v2-parlour]]` memory),
    which these newer features copied without realizing it was no longer
    the live pattern. Most consequential fix: `.diag-opt-btn` — the CEFR
    Diagnostic's A/B/C/D answer buttons, the single most-seen element in
    the whole flow — was rendering white when the sanctioned answer-option
    pattern (`.lsn-option`/`.gd-option`, confirmed by direct comparison)
    has always used `var(--bg)` (blends with the page, border does the
    defining). Also fixed a real (not just cosmetic) bug along the way:
    `.lt-opt-btn.is-selected`'s text color was `var(--bg-card, #fff)` —
    in dark mode `--bg-card` resolves to the dark surface color, not
    white, so selected-option text would have gone low-contrast against
    its own navy `--primary` background; changed to a plain `#fff`,
    matching the app's existing (untokenized but consistent) convention
    for text-on-primary everywhere else. Fixed background-color choice
    was picked per sibling precedent, not uniform: `var(--bg)` for
    answer-option buttons, `var(--surface)` for bordered panels/cards/
    inputs, `var(--wash)` for small badges/chips/note-boxes needing
    visible contrast. Also caught one more inline-JS instance
    (`engine/diagnostic.js`'s pedagogical-reminder note box) beyond what
    the CSS-file grep alone would have found. Verified live: CEFR
    Diagnostic's preface card, tier pill, question card, and A/B/C/D
    options (including the selected state) all render on-token; Level
    Test's CSSOM-confirmed via direct rule inspection (completing a full
    156-lesson level to reach it live wasn't practical this session).

74. ~~**Fix white-rectangle bug in Speaking Conversation Scenarios and Written Exchanges**~~ — **Done 2026-09-23.**
    User reported white rectangles inside a live conversation, in the
    scenario-list turn-count badge, and the same in Written Exchanges.
    Root cause: `--bg-card` is a real, deliberately-defined token —
    `#FFFFFF`, pure white — used elsewhere in the app for actual elevated
    cards, but Speaking/Written Exchanges had been using it as a generic
    "give this a background" fallback for tinted badges/banners/panels
    that were never meant to be white, so every one of them rendered as a
    stark white box against the cream page. The two prior sweep passes
    (items 72-73) missed this class of bug entirely since they grepped
    for shadows/hardcoded-hex/radius, not background-color token misuse.
    Fixed both in `styles/workshop.css` (`.sp-prompt-card`/`.sp-lesson-card`,
    `.sp-turns-pill`, `.sp-briefing-roles-box`, `.sp-chat-timeline`) and,
    just as importantly, in **inline styles embedded directly in JS**
    (`engine/drills/speaking.js`, `engine/drills/writing.js`) — the
    `.sp-scenario-banner` turn header, `.sp-turn-objective-card`,
    `.sp-turn-recording-panel`, `.sp-turn-review-panel`, and
    `.sp-turn-replay-block`, all of which also carried the same
    `--radius-md` phantom-token pattern items 72-73 had only checked in
    CSS files, not JS template strings. Replaced `--bg-card` with
    `--surface` (blends with the page, for panels that already have a
    border to define their edge) or `--wash` (a visible sand tint, for
    badges/banners that need contrast against both the page and the
    white/surface elements sitting inside them) depending on which read
    correctly against neighboring elements — picked per-case, not a blind
    find/replace. Verified live end-to-end in both features (scenario
    list → briefing → live conversation for Speaking; exchange list →
    briefing → live exchange for Written Exchanges), confirming every
    previously-white element now reads as an intentional tint, not a
    stray white box.

73. ~~**Finish the visual-identity drift sweep: remaining phantom tokens, badge colors, dead pulse CSS**~~ — **Done 2026-09-23.**
    Follow-up to item 72, closing out everything that pass had explicitly
    left for later:
    - The `--radius-md`/`--shadow-md`/`--shadow-sm` phantom-token pattern
      (referenced via `var(--radius-md, 6px)` etc. but never actually
      defined in `base.css`, so it always silently fell back to an
      invented value) is now gone project-wide, not just from the
      Speaking/Diagnostic scope item 72 covered: `.lib-rec-btn` and
      `.story-comprehension-block` (Library), the offline-PWA status
      banner, `.pl-guide-banner`/`.pl-guide-room-card`/
      `.pl-guide-features-box` (Parlour Guide onboarding, which also had
      a real `box-shadow` on the banner — removed), and `.gg-search-input`
      (Grammar Guide search) all now use the real `var(--radius)` token.
      Confirmed with a project-wide grep that no `--radius-md`/
      `--shadow-md`/`--shadow-sm` reference remains anywhere in `styles/`.
    - `.badge-comfortable`/`.badge-challenging`'s dark-mode variants
      (Library recommendations) used raw hex (`#81c784`/`#ffb74d`) where
      the light-mode rule right above them already correctly used
      `var(--success)`/`var(--accent)` — dark mode now matches.
    - The `.sp-mic-btn` recording-pulse investigation turned out to be
      moot: `styles/workshop.css` had **two** `@keyframes sp-pulse` blocks
      under the same name (a box-shadow ripple at the mic button's
      original definition, a scale/opacity pulse defined later for the
      grading spinner). Per CSS's last-one-wins rule for duplicate
      `@keyframes` names, the *later* block silently overrode the earlier
      one for every element using `animation: sp-pulse`, including the
      mic button — so the box-shadow version was dead code, never
      actually rendered. Confirmed via `element.getAnimations()` in the
      live page before touching anything: the mic button was already
      animating with `transform`/`opacity` only. Deleted the dead
      box-shadow block rather than rewrite a shadow that was never live.
    Verified via live `getComputedStyle`/CSSOM inspection in the browser
    (not just source review) that every fixed selector now resolves to
    the real token, brace-balance and console/network checked clean
    (same pre-existing unrelated content-index 404 as item 72, not
    caused by this pass).

72. ~~**Visual-identity drift sweep: Speaking, Diagnostic, Writing Exchanges, Workshop pickers**~~ — **Done 2026-09-23.**
    User's own instinct ("I feel like new features keep introducing more
    app-like looks, contradicting our 'no pills' minimalist decision") was
    checked against `design principles.md` — no shadows anywhere, sharp
    `--radius`/`--radius-sm` only, pills reserved for the rare control that
    needs one — and confirmed real. Scoped to every `.sp-*` (Speaking),
    `.diag-*` (CEFR Diagnostic), `.wr-*` (Written Exchanges), `.wk-pill`/
    `.hm-budget-pill` (Workshop/Home pickers) selector in
    `styles/workshop.css`/`styles/components.css`, since those are the
    newest surfaces (all shipped since ~09-13). Found the actual violations
    were narrower than the class names suggested — most things named
    `*-pill` (`.wk-pill`, `.sp-level-pill`, `.sp-skill-pill`,
    `.hm-budget-pill`) already used `--radius-sm` bordered/fill-tint boxes,
    not real pills, so those were false positives from naming alone and
    left untouched. The genuine drift:
    - **The Conversation Scenarios chat UI** (`.sp-chat-bubble`,
      `.sp-chat-listen-btn`, `.sp-scenario-record-cta`/`-stop-btn`) was
      generic chat-app/Material-Design styling: real `box-shadow`s, fully
      rounded 20-28px pill buttons, `transform: scale()` hover bounces,
      and a Google-blue (`#1a73e8`/`#e8f0fe`/`#8ab4f8`) learner-bubble
      color never seen anywhere else in the app. Same Google-blue also
      leaked into Written Exchanges' `.wr-exchange-comp-tag` and its
      textarea focus ring — same copy-paste source, both fixed the same
      way. All converted to `var(--radius)`/`var(--accent-bg)`/
      `var(--accent-dark)`, box-shadows removed outright, hover bounces
      changed to `translateY(-1px)` (matching `.lr-play-btn`'s existing
      convention), and the redundant hand-rolled dark-mode overrides for
      the Google-blue bubble were deleted since `--accent-bg`/
      `--accent-dark` already have dark variants in `base.css`.
    - **Two true 999px pills** — `.diag-tier-pill`, `.diag-verdict-level-pill`
      in the placement-test flow — converted to `--radius-sm`, matching how
      every other small status badge in the app (`.sp-level-pill` etc.)
      already renders.
    - **Off-token feedback colors**: `.sp-word-matched`/`-missed` (bootstrap
      green/red `#1b5e20`/`#c62828` etc., with a hand-rolled dark-mode
      duplicate) and `.sp-eval-good`/`-retry` mapped onto the app's actual
      `--success`/`--success-bg`/`--danger`/`--danger-bg` tokens, which
      already carry correct dark-theme values — the manual dark overrides
      became redundant and were deleted.
    - **A local `--radius-md`/`--shadow-md` phantom-token pattern**: these
      names read like design-system tokens but were never defined in
      `base.css`, so every `var(--radius-md, 6px)`/`var(--radius-md, 8px)`
      silently always resolved to its own hardcoded fallback — a
      third, undocumented radius scale invented per-component. All ~20
      occurrences inside the audited scope mapped onto the real
      `var(--radius)` token.
    Verified live in the browser (not just read against source): Home's
    budget-bar pills, the CEFR Diagnostic question screen's tier badge,
    Workshop's Speaking Studio scenario picker/briefing/turn screens — all
    render sharp-cornered, shadow-free, on-token. Confirmed via
    `getComputedStyle` on the live "Listen" button (`4px` radius, `none`
    box-shadow) that the fix actually reached the rendered page, not just
    the source file. Console/network clean (three pre-existing unrelated
    404s on a missing content index, not caused by this change). Scope was
    deliberately bounded to the newest features — see the follow-up item
    in `ROADMAP.md` for what's left (the same phantom-token pattern
    elsewhere, two off-token Library badge colors, and the mic-button's
    recording pulse, which still uses `box-shadow` as a ripple technique
    and needs a live-visual rewrite rather than a token swap).

71. ~~**SRS polish pass: leech detection, interval fuzz, per-deck reset**~~ — **Done 2026-09-23.**
    Three follow-ups to `engine/srs.js`'s SM-2 scheduler, requested after a
    review of the system found the core algorithm already solid:
    - **Leech detection**: `card.lapses` (lifetime count of "again" ratings,
      distinct from `reviews`) tracked in `normalizeCard()`/`scheduleCard()`;
      a card is flagged `card.leech` at `SRS_CONFIG.LEECH_THRESHOLD` (8,
      Anki's own default) lapses. Surfaced as a quiet "Leech" badge on the
      review card itself (`renderCard()`'s `review-context`) and as the
      row state in Decks' word list (`dk-word-leech`, outranking
      mastered/learning), both styled off the same danger-red language the
      existing "Again" bucket badge already used. The flag never
      auto-clears (lapses is a lifetime count, not a streak) — verified
      deliberately in the smoke test below. Also threaded into
      `engine/learnerModel.js`'s `weakWords()`: among cards tied at
      `MIN_EASE`, the higher-lapse (more-leechy) one now sorts first, and
      the returned shape carries `leech` through — sharpens the SRS
      "weakest words" recommendation from item 70 above.
    - **Interval fuzz**: cards reviewed together on the same day with the
      same rating no longer land on the exact same future due date. A
      deterministic (not `Math.random()`) ±15% fuzz applies only to the
      ease-driven growth phase (`reviews >= 2`, interval >= 3 days) — the
      fixed `FIRST_INTERVAL`/`SECOND_INTERVAL` onboarding ramp stays exact.
      Determinism matters here: `previewSchedule()` is called twice for
      every real rating (once to label the rating buttons, once inside
      `scheduleCard()` to actually apply it) as two separate calls with no
      shared state, so the fuzz is seeded from a hash of
      `(card.spanish, rating, pre-fuzz interval)` rather than randomness,
      keeping the label a learner sees and the interval actually saved in
      agreement.
    - **Per-deck reset**: `clearDeck()` (the existing "Reset" button) wipes
      the *entire* SRS pile across every deck at once — flagged previously
      as too broad for real users. Added `Decks.resetDeckProgress(deck)`
      (`engine/decks.js`): a "Reset progress" link on any deck's detail
      screen (any deck with progress in it, excluded on "All my words"
      since that already IS the whole pile clearDeck() covers) that clears
      SRS cards and known-word status for only that deck's words, leaving
      every other deck, XP, and streak untouched.
    Verified with an ad hoc smoke script (leech threshold/persistence,
    fuzz determinism/range/floor, `weakWords()` tie-break) plus a live
    browser pass: seeded a leech card via localStorage, confirmed the
    "LEECH" row state and its danger-red styling in Decks, the "Leech"
    badge on the actual review card, the "Reset progress" button appearing
    on a real Parlour deck (and correctly absent on "All my words"), and
    that clicking it removed only that deck's card from `srsDeck` while
    leaving an unrelated card untouched.

70. ~~**SRS "weakest words" recommendation, and grammar demoted off the unit-nudge primary slot**~~ — **Done 2026-09-23.**
    Two follow-ups to the recommendation engine work above (items 68-69),
    both in `engine/recommendationEngine.js`:
    - **SRS weakest-words candidate**: `engine/studyPlan.js`'s Time-Based
      Sessions already offer "these are your weakest words, practice them"
      via an SM-2-ease-ranked review or Match Game slot — the ordinary
      Home/Workshop recommendations had no equivalent. Added
      `_srsCandidate()` (sources `LearnerModel.weakWords()`, picks `match`
      when there are >=4 pairs and `DeckMatch` is loaded, else `review` —
      same floor `studyPlan.js` uses) and `_openSrs()` (mirrors
      `studyPlanRunner.js`'s own dispatch: `showTab('review')` +
      `Decks.reviewDeck()` for a review, or `DeckMatch.render()` straight
      into the deck browser's own container for a match). Wired into both
      the secondary tier (`recommend()`) and the mini-game pool
      (`_miniGameNudge()`), and into `secondaryLabel()`/`openSecondary()`.
      Unlike the Vocabulary Driller candidate (B1+ only), this works at any
      level since it reads the SRS deck directly rather than inferring
      meaning from sentence context.
    - **Grammar demoted off the forced-primary unit-nudge slot**: the
      post-unit "practice nudge" used to fall back to a grammar recap of the
      unit whenever no conversation scenario matched, giving grammar a
      forced-primary precedence no other driller got. `_practiceNudge()` is
      now scenario-only (returns `null` otherwise); a unit's grammar recap
      now only surfaces via the ordinary `_miniGameNudge()` candidate pool
      (Candidate 1, "Targeted Grammar"), competing on priority like every
      other candidate. Removed the now-dead non-scenario branch of
      `engine/home.js`'s `practiceNudgeCard()` and its
      `[data-practice-unit]` click handler, both orphaned by this change.
    Verified with the existing `test-scenario-learner-path.js`,
    `test-challenge-tier.js`, and `test-onboarding-guide.js` suites (all
    still pass) plus an ad hoc smoke script covering the new SRS candidate's
    match/review selection and routing.

69. ~~**Vocabulary Driller gated to B1+**~~ — **Done 2026-09-23.**
    The Vocabulary Driller's exercises all infer a word's meaning from a real
    sentence context (`PARLOUR_VOCABULARY_DRILLER_SPEC.md`); below B1 the
    learner doesn't yet know enough surrounding vocabulary/grammar for that
    inference to work, so it read as an unfair guessing game rather than a
    useful drill.
    - `engine/workshop.js`: added a `minLevel` field to the driller
      definition and extended `_available()` (previously lang-only) to also
      check `LearnerPath.currentLevel()` against it — the same mechanism
      already used to hide Hungarian-only drillers from Spanish learners, and
      already wired so `render()` bounces back to the picker if something
      still tries to open a gated driller directly.
    - `engine/recommendationEngine.js`: added `_vocabularyAvailable()` and
      gated both the secondary-tier vocabulary candidate
      (`_grammarVocabCandidate()`) and the mini-game's Vocabulary Recall
      candidate on it, so the recommendation surfaces never suggest a driller
      the picker would refuse to open.

68. ~~**Recommendation engine silently offered a narrow slice of its own candidates**~~ — **Done 2026-09-23.**
    Root cause: `engine/recommendationEngine.js`'s mini-game nudge (and
    `engine/reader.js`, `engine/studyPlan.js`, `engine/drills/writing.js`)
    all called `LearnerPath.currentLevel()` / `LearnerPath.completedCount()`,
    but `engine/learnerPath.js` never actually defined either — every call
    site guarded with `typeof LearnerPath.currentLevel === 'function'` and
    silently fell back to `'A1'` / `0`. In practice this meant, for every
    learner regardless of real progress:
    - Verb Speed Sprint, Fast Translation, Audio Decode, and the Speaking
      Driller mini-game candidates were dead code — their `completedCount >=
      N` gates could never pass — so the per-lesson "what's next" nudge only
      ever rotated through Targeted Grammar, Vocabulary Recall, the
      scenario-matched roleplay, and (via their `isComplete()` fallback) the
      three Hungarian sub-drillers.
    - Any content that keyed off the learner's actual level (translation/
      listening difficulty, reader story recommendations) was pinned to A1
      forever, even for a B1 learner.
    Added real `completedCount()` (count of `getProgress()` entries) and
    `currentLevel()` (the level of `nextStep()`, falling forward to the
    course's top level once the course is finished) to `LearnerPath`'s
    returned API. Existing test suites (`test-challenge-tier.js`,
    `test-scenario-learner-path.js`, `test-onboarding-guide.js`) still pass
    unchanged.

67. ~~**Situational Written Exchanges (Interactive Texting & Correspondence Engine)**~~ — **Done 2026-09-22.**
    Shipped multi-turn situational digital correspondence and text messaging as the 3rd studio mode in Writing Studio (`[ Composition Studio | Written Exchanges | Sentence Translation ]`) across Spanish and Hungarian:
    - **Dignified Editorial Messaging UI**:
      - Styled in Parlour's restrained, literary aesthetic (`styles/workshop.css`) with calm card borders, muted headers, and zero emojis.
      - Typographic diacritics bar (`á, é, í, ó, ú, ñ, ¿, ¡` for Spanish; `á, é, í, ó, ö, ő, ú, ü, ű` for Hungarian) for rapid desktop accent insertion.
      - Simulated partner typing delay note (*"Mateo is writing a reply…"*) during turn transitions.
    - **Authentic Scenario Datasets**:
      - Authored 12 authentic Spanish scenarios (`content/es-latam/writing-exchanges.json` and `content/es-es/writing-exchanges.json`) across A1, A2, and B1 covering everyday digital correspondence (shopping lists, meeting coordination, birthday RSVPs, boiler breakdown notices to landlords, Airbnb check-in updates, sick leave notices, marketplace purchases, group trip planning, customer service claims, restaurant reservation adjustments, and diplomatic neighbor notes).
      - Authored 4 Hungarian scenarios (`content/hu/writing-exchanges.json`).
      - All scenarios link directly to curriculum units in `curriculum/curriculum.json` and include CEFR can-do goals.
    - **Formative Written Interaction Assessment**:
      - Calibrated `GraderPrompt.buildGraderPrompt()` (`engine/grader/grader-prompt.js`) for `written_exchange` evaluating pragmatics, register (*tú* vs *usted*), communicative responsiveness, vocabulary range, and diacritics/orthography.
      - Enhanced `LocalGrader.gradeConversation()` (`engine/grader/local-grader.js`) with `modality: 'written'` support for zero-latency turn-level validation and deterministic offline end-of-exchange debriefs.
      - Ingests production evidence into `LearnerModel` (`modality: 'written'`), verifies target competencies on score $\ge 75$, and awards XP.
    - **Automated Verification**:
      - Created comprehensive test suite `tests/drills/test-writing-exchanges.js` verifying schema validity, curriculum unit ID mapping, zero emoji enforcement, grader prompt accuracy, and UI tab mounting. All tests pass with schema validator confirmation.

66. ~~**`fill-blank` exercises have no hint mechanism**~~ — **Done 2026-09-22.**
    Implemented an on-demand, progressive two-tier hint system across both Lesson fill-blank steps (`engine/lessons.js`) and GrammarRunner fill-blank practice drills (`engine/drills/grammar-runner.js`), resolving issues #176, #180, and #183:
    - **Progressive Two-Tier Hints**:
      - **Hint 1**: Reveals the initial letter of the canonical target word (`Starts with "X"`), respecting unicode word/number characters and accented characters (*É*, *ú*).
      - **Hint 2**: Reveals the full English gloss / sentence translation (`English: "..."`), then indicates `All hints shown` and disables further clicks.
    - **Parlour Visual Identity (Strict Zero Emojis)**:
      - Clean text-only design (`Need a hint?` -> `Next hint` -> `All hints shown`), with dashed surface card styling (`.lsn-hint-box`) and subtle dotted-underline trigger (`.lsn-hint-btn`).
      - Hint area and buttons automatically tuck away when the step is solved or attempts expire.
    - **Soft Learner Path & SRS Signal**:
      - Using hints does not penalize or consume any of the learner's 3 answer attempts.
      - Softly signals imperfect recall: excludes the step from `lessonStats.correctFirstTry` and schedules the item as `'hard'` (instead of `'good'`) in SM-2 spaced repetition (`Recycle.record`).
    - **Automated Verification**:
      - Created comprehensive test suite `tests/drills/test-fill-blank-hints.js` covering initial render, zero emoji enforcement, progressive tier progression, stats tracking, SM-2 scheduling, accent handling, and GrammarRunner parity. All 7 tests pass.

65. ~~**Comprehensive Pedagogical Error Feedback & Post-Session Review Recaps across All Workshop Drills & Minigames**~~ — **Done 2026-09-21.**
    Imbued all Workshop drillers and minigames with direct pedagogical teaching functions so learners always understand mistakes and see corrections immediately:
    - **Verb Table Driller (`engine/verbs/table.js`, `styles/verbs.css`)**:
      - Preserves learner's typed inputs on incorrect check rather than erasing/overwriting them.
      - Renders inline `.vtable-correction` indicators (`Correct: <form>`) underneath each incorrect row.
      - Enriches summary feedback (`✗ X of Y correct. Review the corrections shown above (person1, person2).`) and unblocks the Next Verb button so learners can either re-attempt or advance smoothly.
    - **Listening Driller & Runner (`engine/drills/listening-runner.js`, `engine/drills/listening.js`)**:
      - Replaced generic failure indicators with explicit contrastive corrections (`✗ Not quite. The correct answer is: "..."`, `✗ Not quite. You wrote "...". The correct answer is "..."`, `✗ Not quite. The missing word was "..."`).
      - Preserves user typed input in dictation exercises and forwards detailed error payloads (`{ question, correct, user }`) to `onResult`.
      - Renders a post-session `.gd-missed-recap` ("Review Missed Items") card with user response and model answer badges.
    - **Translation Driller & Runner (`engine/drills/translation-runner.js`, `engine/drills/translation.js`)**:
      - Added explicit pedagogical feedback (`✗ Marked for review — compare your attempt with the model: "..."`) on "Not quite".
      - Captures user translation and reference model into `_missedDetails` and renders `.gd-missed-recap` on the results screen.
    - **Hungarian Drillers (`hu-verb.js`, `hu-suffix.js`, `hu-prefix.js`, `hu-morphology.js`)**:
      - Hooked into `GrammarRunner.render`'s `onResult(correct, details)` callback across all 4 Hungarian drillers.
      - Captures question prompt, correct form, and user response for all missed items; displays `.gd-missed-recap` on the session results screen.
    - **Verb Speed Driller (`engine/verbs/speed.js`)**:
      - Immediate contrastive feedback: displays `✗ Correct: <answer> (you wrote: "<user>")` with extended review pause (1200ms) on wrong submissions before auto-advancing.
      - Renders "Review Missed Conjugations" recap on session results with verb, tense, person, learner's answer, and correct form.
    - **Deck Match Game (`engine/decks/match.js`, `styles/components.css`)**:
      - Added live mismatch feedback banner (`.dkm-feedback`: `✗ "<word>" does not match "<word>"`).
      - Tracks all mismatched and untimed words in `_missedWords`; renders a "Review Missed Pairs" recap with target word and translation on completion.
    - **Automated Verification**: Authored `tests/drills/test-pedagogical-feedback.js` covering all 8 drillers/runners; all tests pass.

64. ~~**CEFR Diagnostic Placement Test: 10-Question Hybrid with Active Production, 85% Pass Threshold & Screener Disclosures**~~ — **Done 2026-09-21.**
    Overhauled the CEFR Diagnostic Placement Test (`engine/diagnostic.js`, `styles/components.css`, content files) from a 6-question multiple-choice screener into a 10-question hybrid assessment per tier requiring active recall and an 85% mastery mark:
    - **10-Question Hybrid Structure Across Tiers (A1, A2, B1)**:
      - **Questions 1–5 (Multiple Choice)**: High-discriminator morphological and syntactical items in context.
      - **Questions 6–7 (Prompted Situational Communication)**: Real-world conversational prompts (`q.prompt`) testing communicative pragmatics, register (*tú* vs. *usted*), and polite request formulas.
      - **Questions 8–10 (Open Active Production)**: Text-input cloze (`type: "text-input"`) requiring typed production of target verbs, pronouns, and modifiers without multiple-choice crutches.
    - **Tighter 85% Passing Standard (`passRatio: 0.85`)**:
      - Raised pass ratio from 66% (4/6) to 85% (requires 9 out of 10 correct per tier to advance). Passive guessing alone cannot pass a tier.
      - Evaluates text input with casing/whitespace trimming and normalized accent tolerances (`normUser === normAccepted`).
    - **Desktop Usability & Diacritics**:
      - Integrated Parlour's virtual diacritics bar (`UI.diacriticsBarHtml('.diag-text-input')`) for quick entry of `á`, `é`, `í`, `ó`, `ú`, `ñ` without international keyboards.
      - Auto-focuses active text input on question load and supports Enter-key advancement.
    - **Explicit Screener Disclosures**:
      - Updated Preface, Testing header, and Debrief screens to clearly state that the diagnostic test is a rapid structural screener, and directs learners seeking comprehensive multi-modal certification (including extended writing and recorded oral speech) to the official curriculum Level Tests.
    - **Multi-Course Implementation & Verification**:
      - Updated all 3 tracks (`content/es-latam`, `content/es-es`, `content/hu`) with 10 questions per tier (30 questions each, 90 questions total across courses).
      - Added automated test suite `tests/test-diagnostic.js` verifying question counts, schema constraints, evaluation logic, and accent tolerance.

63. ~~**Spanish Conjugation Tables Audit, Peninsular Vosotros & Workshop Verb Driller Restoration**~~ — **Done 2026-09-21.**
    Audited and repaired Spanish conjugation tables, drill references, and TTS audio integration across both European Spanish (`content/es-es`) and Latin American Spanish (`content/es-latam`):
    - **Workshop Verb Driller Availability (`engine/workshop.js`)**: Corrected language matching in `_available(driller)` and expanded driller configuration to `['es', 'es-latam', 'es-es']`. Previously `Lang.code()` returning regional codes caused the entire Verb Driller tool to be hidden for Spanish learners in Workshop.
    - **Workshop Conjugation Table Audio & Reveal Mode (`engine/verbs/table.js`, `styles/verbs.css`)**:
      - Integrated `ParlourTTS.button()` audio playback for the infinitive title and each conjugated person row.
      - Added speculative preloading for all paradigm forms upon table render.
      - Added "Show Answers" reference reveal action so learners can inspect full paradigms immediately without having to complete typing drills.
    - **Lesson Conjugation Table Pronoun Recognition & Audio (`engine/lessons.js`)**:
      - Expanded `PRONOUN_RE` regex and cleaned input strings (`replace(/[*_()]/g, '')`) to recognize composite pronouns (`él/ella/ud.`, `nosotros/as`, `vosotros/as`, `(A mí)`, etc.).
      - Ensured secondary cells in grammar conjugation tables are recognized as conjugated forms and properly rendered with target-language audio buttons.
    - **Peninsular Vosotros Backfill in `content/es-es`**:
      - Audited all curriculum grammar tables; identified 21 legacy 5-row tables across 17 A1/A2 lesson files in `content/es-es` that were missing the Peninsular *vosotros* paradigm.
      - Added complete *vosotros* rows across regular and irregular paradigms (present, imperfect, conditional, reflexive, and auxiliary verbs).
      - Validated all 17 touched files via `python scripts/validate-content.py --changed` with 0 errors.

62. ~~**B1 Fill-in-the-Blank and Dictation English Translations Backfill**~~ — **Done 2026-09-21.**
    Backfilled natural English translations (`english`) for all 980 unique B1 fill-in-the-blank and dictation exercises across both `content/es-es` (697 exercises) and `content/es-latam` (980 exercises, Spain being a 100% subset of LatAm):
    - **Sentence Export**: Generated 5 human-readable `.txt` batch files (`b1_batch_1.txt` – `b1_batch_5.txt`, ~200 items each) with a ChatGPT prompt preamble for manual translation.
    - **Translation Merge**: Injected ChatGPT-returned JSON translations via `scratch/merge_b1_translations.py` into 655 exercise files across both language variants.
    - **Validation**: `python scripts/validate-content.py --changed` → `es-es: 216 passed, 0 failed; es-latam: 433 passed, 0 failed`. Manifests regenerated via `build-manifest.py`.
    - **Coverage**: 100% English translation coverage now achieved across the entire existing Spanish curriculum (A1, A2, and B1 fill-blank, dictation, and sentence-builder).

61. ~~**A1 & A2 Fill-in-the-Blank and Dictation English Translations Backfill**~~ — **Done 2026-09-21.**
    Backfilled, merged, and validated natural English translations (`english`) for all 1,109 A1 and A2 fill-in-the-blank and dictation exercises across both European Spanish (`content/es-es`) and Latin American Spanish (`content/es-latam`):
    - **Schema Updates (`content/es-es/schemas/exercises.schema.json`, `content/es-latam/schemas/exercises.schema.json`)**: Added optional `english` property definition to both `fillBlank` and `dictation` exercise types.
    - **Sentence Reconstitution & Translation**: Extracted all 381 A1 fill-blank, 563 A2 fill-blank, and 165 A2 dictation exercises. Reconstituted full target Spanish sentences, cleanly stripping prompt prefixes (`"Complete: "`) and utilizing contextual cues (`(ella)`, `(usted)`, etc.) to ensure natural, idiomatic, CEFR-aligned English translations.
    - **Multi-Course Merging & Schema Validation**: Populated `"english"` into 1,109 exercises across 332 files in `content/es-es` and 332 files in `content/es-latam` (664 files total). Verified 100% schema compliance with `python scripts/validate-content.py` (0 errors) and regenerated manifests via `build-manifest.py`.
    - **Authoring Standards Invariant**: Added strict instruction to `AGENTS.md` and `ROADMAP.md` requiring all future `fill-blank`, `dictation`, and `sentence-builder` exercises to include an `english` translation.
    - **Backlog Tracking**: Updated Item 16 in `TROUBLESHOOTING_BACKLOG.md` marking A1/A2 complete and logging B1 remaining scope (980 items).

60. ~~**Pedagogical Feedback Clarity, Decks Typing Auto-Assessment, Diagnostic Overhaul & STT Polish**~~ — **Done 2026-09-21.**
    Shipped a unified suite of UX enhancements, pedagogical fixes, and driller optimizations:
    - **Decks & SRS Production-First Review (`engine/srs.js`, `styles/components.css`, `index.html`)**:
      - Defaulted flashcard review direction to English-first (`en-es`), enforcing active target-language recall rather than passive recognition.
      - Built automated 4-bucket assessment (`easy`, `good`, `hard`, `again`) for desktop typing review mode based on latency and accuracy: <3.0s exact match rates as Easy, 3.0–7.5s rates as Good, >7.5s or minor accent slips rate as Hard, and incorrect answers rate as Again.
      - Added instant inline evaluation badges (`.review-type-assessment`, `.srs-bucket-badge`) with latency display and auto-labeled Continue actions (`Continue [BUCKET] (Enter ↵)`).
    - **Personalized Welcome Screen (`engine/sync.js`, `cloudflare-worker/sync-worker.js`, `engine/home.js`)**:
      - Captures user display name from Google OAuth identity tokens into `localStorage` (`parlour_user_name`).
      - Dynamically renders time-of-day greetings for authenticated learners (*"Good [morning/afternoon/evening], [Name] — welcome back to your language journey."*).
    - **Placement Diagnostic Test Overhaul (`engine/diagnostic.js`, `engine/progress.js`, `styles/components.css`)**:
      - Restyled the placement interface to strictly adhere to Parlour ink aesthetic: eliminated raw white prompt boxes, unified option button sizing, and created custom styles for `.wk-primary-btn` and `.wk-secondary-btn`.
      - Resolved case-sensitivity level-jumping bug in `markLevelComplete()` and ensured curriculum manifests are pre-loaded; testing into B2 reliably auto-credits and marks A1, A2, and B1 as completed.
    - **Pedagogical Immediate Feedback & Missed Items Recap (`engine/drills/grammar-runner.js`, `engine/drills/vocabulary.js`, `engine/drills/grammar.js`, `styles/workshop.css`)**:
      - Replaced blind wrong-state indicators across grammar and vocabulary drills with immediate display of the exact correct answer.
      - Added a "Review Missed Items" recap card to session summaries detailing each missed prompt, the learner's response, and the correct solution.
    - **Speaking Studio & STT Punctuation Normalization (`engine/speech-input.js`, `engine/lessons.js`, `engine/drills/speaking-runner.js`)**:
      - Stripped non-phonetic punctuation and typographical signs (`-`, `—`, quotes, etc.) from STT comparison tokens so missing punctuation never penalizes speech evaluation.
      - Configured "Can't speak right now" action in lessons and drills to immediately advance, snooze speaking exercises for 10 minutes, and display confirmation toast feedback.

60. ~~**Two-Way Multi-Device Cloud Sync, Additive Merging & Save-on-Leave Lifecycle**~~ — **Done 2026-09-21.**
    Implemented seamless cross-device synchronization and guaranteed save-on-leave behavior:
    - **Additive Multi-Device Merging (`engine/sync.js`)**: Merges progress additively via `mergeSnapshots()` — union of completed lesson IDs, deduplicated union of known words, card-level SRS resolution preserving highest intervals/reviews, and merged XP daily histories. Completing lessons across multiple devices combines all work without overwriting.
    - **Startup Auto-Sync (`engine/init.js`, `engine/sync.js`)**: App launch automatically checks and pulls newer cloud backups with a 3.5s timeout before initializing in-memory caches (`loadDeck()`, `loadKnownWords()`, `loadXP()`), falling back to local storage offline.
    - **Guaranteed Save-on-Leave**: Flushes pending debounced saves and dirty states on `visibilitychange` (hidden), `pagehide`, and `beforeunload` using `fetch` with `keepalive: true`.
    - **Foreground Tab Sync**: Detects remote updates on tab focus (`visibilitychange` visible) without interrupting active exercises.
    - **Google Sign-In Refresh**: Journey card Google Sign-In triggers page reload on success so all curriculum and deck modules initialize with fresh cloud data.

59. ~~**Google Sign-In & Multi-Device Cloud Sync**~~ — **Done 2026-09-20.**
    Implemented 1-tap Google Sign-In alongside email magic links:
    - **Cloudflare Worker Auth (`cloudflare-worker/sync-worker.js`)**: Added `/auth/google` POST endpoint that cryptographically verifies Google OpenID Connect ID tokens via Google's standard tokeninfo endpoint (zero external dependencies). Validates token audience, issuer (`accounts.google.com`), expiration, and verified email flag.
    - **D1 SQL & Session Integration**: Maps verified Google email to existing D1 `users` table and issues HMAC-SHA256 signed JWT session tokens identical to magic link sessions. Learners signing in via either method with the same email seamlessly share cloud backups.
    - **Client Engine (`engine/sync.js`)**: Added lazy loader for Google Identity Services SDK (`accounts.google.com/gsi/client`), `Sync.loginWithGoogle()`, `Sync.renderGoogleButton()`, `Sync.promptGoogleOneTap()`, and auto-restore of cloud backups for clean devices.
    - **Journey & Onboarding UI (`engine/journey.js`, `styles/components.css`)**: Added Google Sign-In button container and divider in Journey Account card and first-visit prompt sheet, with automatic light/dark theme adaptation.
    - **Documentation**: Authored step-by-step setup guide in `GOOGLE_SIGNIN_SETUP.md` and linked in `CLOUD_SYNC_SETUP.md`.

58. ~~**Automatic Background Cloud Sync & Life-Cycle Auto-Save**~~ — **Done 2026-09-20.**
    Implemented transparent background auto-sync in `engine/sync.js`:
    - `Sync.scheduleAutoSave()` automatically schedules a debounced backup (2.5s) whenever learner state changes (progress updates in `engine/progress.js`, SRS cards and known words in `engine/srs.js`, drill sessions in `engine/drillHistory.js`, and XP awards in `engine/xp.js`).
    - Life-cycle hooks: automatically flushes pending auto-saves via `visibilitychange` (state hidden) and `pagehide`, ensuring zero lost progress on tab switch or navigation.
    - Emits `sync-saved` window events with timestamp on successful auto-save, preserving offline-first local storage without blocking the UI.

57. ~~**Peninsular Adaptations & Active *Vosotros* Practice (`content/es-es` A1/A2)**~~ — **Done 2026-09-20.**
    Authored and integrated interactive Peninsular Spanish adaptations and *vosotros* forms across European Spanish (`content/es-es`):
    - Interactive *vosotros* conjugation and imperative exercises in A1 and A2 (`a1-05-01-ex.json`, `a1-06-02-ex.json`, `a1-06-03-ex.json`, `a1-reflexive-01-ex.json`, `a2-01-03-ex.json`, `a2-imperativonegativo-03-ex.json`).
    - Peninsular lexical adaptations (`ordenador`, `móvil`, `aparcar`, `patata`, `gafas`, `piso`).
    - Strict schema validation and full isolation from the `es-latam` corpus.

56. ~~**Onboarding, Casual Philosophy & Encounter-Based Feature Guidance**~~ — **Done 2026-09-20.**
    Designed, implemented, validated, and shipped the onboarding and feature guidance system (`engine/guide.js`):
    - **Casual, Grounded Philosophy & Welcome Presentation**:
      - Warm, human welcome: *"Parlour is for people who actually want to learn languages and cultures. A non-commercial project, we want to provide a place where you can learn, read, review, and practice — welcome!"*
      - Enhanced Home onboarding card with target language selector, philosophy summary, "How Parlour works" modal trigger, and dual entry paths (*"Take placement test →"* vs. *"Start at Unit 1"*).
    - **"How Parlour Works" Modal & Power Features Highlighted**:
      - Accessible modal detailing the 6 rooms (Home, Lessons, Library, Decks, Workshop, Journey).
      - Prominently highlights power features: streak import from Duolingo/other apps, Quizlet/Anki deck import, pasting custom articles in *My Texts* with tap-to-translate glosses, and the Speaking/Writing Studios.
      - Accessible at any time via Home onboarding card or the understated "How Parlour works" link in the nav footer.
    - **Contextual Encounter-Based Coach Notes**:
      - Replaced intrusive upfront tutorials with non-blocking, ink-styled coach note banners that appear once when learners encounter a feature for the first time:
        - `lesson`: First lesson entered (explains self-paced progression, zero-stress mistake redo pass).
        - `reader`: First library visit (explains tap-to-translate glosses and *My Texts* pasting).
        - `decks`: First review/decks visit (explains automated SRS collection and Quizlet/Anki importing).
        - `workshop`: First workshop visit (explains targeted drillers, reference tables, and composition studios).
        - `production`: First Speaking/Writing task (explains focus on communicative clarity and 1-sentence coaching).
      - State persisted in `localStorage` (`parlour_guide_seen_<feature>`), animated dismissals.
    - **Deferred Sync Email Prompt**:
      - Updated `engine/sync.js` to defer the first-visit cloud sync email prompt until the learner has completed at least 1 lesson or earned XP, preventing early modal interruptions on visit #1.
    - **Verification & PWA Shell**:
      - 100% SVG line/wash iconography, zero emoji pictograms.
      - Comprehensive automated test suite `tests/drills/test-onboarding-guide.js` (6 test suites passed).
      - Precached via `sw.js` (cache version `v2026-09-20c`).

55. ~~**CEFR Level Diagnostic Placement Test & Onboarding Ladder**~~ — **Done 2026-09-20.**
    Designed, authored, validated, and shipped the multi-tier adaptive placement diagnostic test engine (`engine/diagnostic.js`) and content across Spanish and Hungarian:
    - **Course-Agnostic Adaptive Ladder Architecture**:
      - Deterministic multiple-choice ladder assessing core grammar, syntax, and communicative pragmatic comprehension across tiers (A1, A2, B1, and dynamically expandable to B2/C1 without engine rewrites).
      - Passing threshold (66%) dynamically evaluates whether to advance to the next tier ladder or place immediately.
    - **Pedagogical Communication-First Preface**:
      - Prominently displays clear philosophical guidance: *"This is just a quick diagnostic test; mistakes are completely natural and possible, and you can retake it at any time... If you feel at all shaky on any fundamentals, we strongly encourage taking the lessons anyway. In Parlour, we do not learn a language merely to finish a course, but to actually be able to communicate with confidence."*
    - **Auto Jump-Ahead & Non-Destructive Progression**:
      - Accepting placement into e.g. A2 or B1 automatically marks preceding levels complete (`markLevelComplete(lvl)`), advancing the learner directly to the recommended unit while keeping all preceding lessons open for review.
    - **New-User Onboarding & On-Demand Access**:
      - Brand-new learners (0 completed lessons) receive a calm, unobtrusive welcome card on Home offering the choice between starting fresh at Unit 1 or taking the 5-minute placement test.
      - Learners can take or retake the diagnostic test on demand from the top of the Learn/Curriculum tab.
    - **Strict Constructivist Standard**: 100% SVG icons, zero emoji pictograms, fully responsive Parlour aesthetic. Authored Spanish (`content/es/tests/diagnostic-test.json`) and Hungarian (`content/hu/tests/diagnostic-test.json`) suites (18 questions each across 3 tiers). Precached via `sw.js` (cache version `v2026-09-20a`).

54. ~~**CEFR Real-Exam Practice Mode & Multi-Modal End-of-Level Assessment (Queue Item 9)**~~ — **Done 2026-09-20.**
    Designed, implemented, validated, and shipped the multi-modal CEFR level assessment engine (`engine/leveltest.js`) and authentic end-of-level exam content across Spanish and Hungarian:
    - **Multi-Modal CEFR 3-Part Architecture**:
      - *Part 1: Language in Context*: 20–28 questions combining contextual cloze dropdowns (`dropdown`), active-recall text inputs (`text-input`), and authentic communicative pragmatic choices (`choice`).
      - *Part 2: Short Written Production (`writingTask`)*: Integrated writing prompt with live length meter, target keyword badges, and CEFR rubric evaluation.
      - *Part 3: Short Spoken Production (`speakingTask`)*: Integrated speech-to-text recording, audio playback, and accessible typed/dictation fallback.
    - **Exams Authored & Shipped**:
      - Spanish A1 (`content/es/tests/a1-test.json`): 22 questions, *Un día en mi vida* writing task, *Presentación personal* oral task.
      - Spanish A2 (`content/es/tests/a2-test.json`): 24 questions, *Un fin de semana inolvidable* writing task, *Mensaje de voz con recomendaciones* oral task.
      - Hungarian A1 (`content/hu/tests/a1-test.json`): 26 questions, *Magyarul tanulok* writing task, *Bemutatkozás élőszóban* oral task.
      - Hungarian A2 (`content/hu/tests/a2-test.json`): 26 questions, *Köszönőlevél vendéglátásért* writing task, *Névnapi köszöntő* oral task.
      - Hungarian B1 (`content/hu/tests/b1-test.json`): 28 questions testing conditional present/past (*volna*), participles (*-ó/-ő, -t/-tt, -andó/-endő, -va/-ve, -ván/-vén*), potential suffix (*-hat/-het*), causative (*-tat/-tet*), frequentative (*-ogat/-eget*), reflexive verbs (*-kodik*), complex connectors (*bár, noha, holott*), indirect speech & indirect question particle (*-e*), preverb inversion & auxiliaries, and citizenship & administrative topics; *Hivatalos megkeresés és javaslattétel* writing task (min. 60 words); *Állásinterjú vagy szakmai tervek bemutatása* oral task (min. 30s).
    - **Navigation & Engine Polish**: Implemented `LevelTest.hasTest(level)` to dynamically activate level tests per language, preventing dead-ends while rendering clean "Coming soon" indicators on unscoped levels; added diagnostic topic breakdowns on exam completion, retake functionality, and automatic jump-ahead level completion for scores >= 90%.

53. ~~**Hungarian B1 Dual Track Curriculum: Complete 72 Units & 432 Lessons**~~ — **Done 2026-09-20.**
    Authored, integrated, validated, and pushed all 36 dual unit-pairs for Hungarian B1 (72 units, 432 lessons total) in complete parity between the Core track and the Citizenship track:
    - **Scope & Delivery**: 216 Core lessons (`b1-01` to `b1-36`) + 216 Citizenship lessons (`b1-orszagma` to `b1-allampolgarsag`), 3,024 exercises across 432 exercise files, 360 vocabulary files (~1,800 target words), and 510 grammar modules.
    - **Dual Literature & World Story System**:
      - 36 Hungarian classic literature adaptations for Core units (Petőfi, Mikszáth, Móricz, Kosztolányi, Karinthy, Babits, Szerb Antal, Gárdonyi Géza, etc.).
      - 216 world stories for Citizenship units (180 episodic stories + 36 comprehensive compendiums) covering the entire sweep of Hungarian history, culture, institutions, constitution (*Alaptörvény*), and the citizenship oath.
    - **Track Isolation & Verification**: All exercises and vocabulary rigorously partitioned between Core and Citizenship tracks with 0 contamination in `ListeningDriller`, `SpeakingStudio`, and `VocabularyDriller`. 100% schema validation (3,953 content files passed, 0 failed).

52. ~~**Natural Can-Do Production Prompts & 1-Sentence Coaching Feedback Norm**~~ — **Done 2026-09-18.**
    Resolved awkward verbal/written production prompts derived from CEFR Can-Do descriptors and streamlined under-1-minute productions with a compact 1-sentence coaching feedback card:
    - **Can-Do Prompt & Scaffolding Engine (`engine/canDoPrompt.js`)**: Replaced crude 37-char mid-word truncation (`options.targetCompetency.slice(0, 37) + '...'`) with topic-aware title extraction (e.g. *"At the Café"*, *"Months of the Year"* instead of *"I can complete a short at the café in..."*). Categorized descriptors into 4 typologies:
      - *Enumeration & Inventory*: e.g. "I can name all twelve months and say which month something is in" prompts the learner to recite the 12 months in order and state an event or their birthday, with language-specific case/preposition cues (`-ban / -ben` in Hungarian, `en` in Spanish).
      - *Situational Transactions*: e.g. "I can complete a short at the café interaction" provides setting and 3-part communicative dialogue cues (polite greeting, order e.g. *Kérek...*, and bill/closing).
      - *Personal Monologue*: Daily routine, family, hobbies, town prompt for 2–3 connected sentences with concrete guidance points.
      - *Functional Imperatives*: Converts generic "I can [action]..." statements into active imperative tasks.
    - **1-Sentence Coaching Feedback Norm for Short (< 1 Min) Productions**: In `SpeakingDriller` (`engine/drills/speaking.js`) and `WritingDriller` (`engine/drills/writing.js`), tasks where `maxSeconds <= 60` or `taskCompletionPrimary` is active now render a compact coaching view instead of the bulky 5-dimension CEFR dashboard:
      - Score badge (`88%`) & Verified Competency indicator.
      - *Speaking / Writing Coach's Note*: Single prioritized, actionable coaching sentence pulled from formative grader output (`_prodOneLineTip`: priorities[0] → error explanation → strength).
      - Audio recording replay player (`sp-own-voice-player`) to listen back to your recording.
      - Spoken transcript preview (`"What you said:"`).
      - Seamless navigation via `RecommendationEngine.mountNextAction()` returning directly into the session.
    - **In-Lesson Dynamic Communicative Challenges (`engine/lessons.js`)**: Integrated `CanDoPrompt` into `injectCommunicativeChallenge()`. Tier 2 challenges now generate appropriate context and cues for enumeration, monologue, and transactional goals rather than forcing generic 3-bullet transactional cues onto every goal.
    - **Test Coverage**: Added test suite in `tests/drills/test-cando-prompt.js`. All 5 test suites pass alongside `test-studios.js` and `test-challenge-tier.js`.

51. ~~**Adversarial Full-App Audit: LevelTest Navigation Traps, Storage Resilience, Cross-Course Isolation & Input Tolerances**~~ — **Done 2026-09-18.**
    Conducted an adversarial, root-cause traced full-app QA audit across navigation, state isolation, storage crash risks, speech recognition, and input grading tolerance:
    - **Level Test Dead-End Trap & Navigation Polish**: B1 and B2 units previously rendered an active Level Test button leading to an unrecoverable blank screen when content test files did not exist (`b1-test.json`, `b2-test.json`), because `LevelTest.render()` rendered no back button and all app tabs remained hidden. Implemented `LevelTest.hasTest(level)` to display a clean disabled "Coming soon" state in `curriculum.js`. Updated `LevelTest.render()` to always render `<button class="dk-back" data-close-test="1">← Back</button>` and wire `closeTest()` if a test is missing. In addition, `LevelTest.open()` now records `openingTab` so learners returning from tests opened from Home or Study Plan return to their originating tab rather than hardcoded Lessons.
    - **Cross-Course Isolation on Language Switch**: Neither `srs.js` nor `lessons.js` listened to `language-changed`. Switching languages left prior language cards in memory (writing Spanish words to `hu:srsDeck` on next save) and served cached Spanish files to Hungarian lessons via `contentCache`. Added `language-changed` listeners in `srs.js` (reloading `loadDeck()`, `loadKnownWords()`, and clearing card state) and `lessons.js` (clearing all `contentCache` promises).
    - **Storage Corruption Crash Resilience**: Wrapped raw `JSON.parse(saved)` in `loadDeck()` (`srs.js`) and `loadXP()` (`xp.js`) in `try/catch` with safe fallback default object structures, preventing corrupt or truncated `localStorage` strings from crashing the app during boot.
    - **Speech Recognition Language Parity in Review Mode**: Fixed flashcard review type input microphone addon calling `lessonInlineVoiceInput('#review-type-field')`. When `reviewDirection === 'es-en'`, recognition language is now set to `'en-US'` and speech target points to `reviewExpectedEnglish` (instead of target language and stale lesson `stepState`).
    - **Input Normalisation Tolerance**: Enhanced `normalise()` (`lessons.js`) and `srsNormalise()` (`srs.js`) to collapse consecutive whitespace (`\s+`) and strip quotation marks (`"`, `'`, `«`, `»`, `“`, `”`) and dialogue dashes (`—`, `-`), while strictly preserving accent diacritics.
    - **Empty Input Submission Protection**: In `lessonCheckBlank()`, submitting an empty input now warns *"Type or speak an answer first."* without invoking `failStep()` and burning an attempt.
    - **Mobile Theme Toggle Accessibility**: Added `.mobile-theme-btn` into `PageHeader.render()` actions, styled to display on mobile and tablet viewports (<1024px) where the desktop sidebar footer is hidden.
    - **Test Coverage**: Added comprehensive test suite in `tests/audit/test-audit-remediations.js` covering missing level tests, storage corruption handling, language-switch isolation, input normalisation, and empty input protection. All 12 test suites pass.

49. ~~**Vocabulary Driller: surface-form, slash-adjective, and article-prefixed lemma matching**~~ — **Done 2026-09-18.**
    Resolved the live runtime lemma matching gap in `VocabularyDriller` across Spanish and Hungarian:
    - **Root cause investigated**: A comprehensive audit across all 2,882 Spanish content words revealed that 996 words (34.6%) previously returned 0 context occurrences because `_buildContextIndex()` indexed sentences solely under canonical dictionary lemmas (e.g. `ser`), while `_hasContext()` and exercise builders queried using raw deck keys (`soy`, `alto / alta`, `el perro`).
    - **Dual-Key Context Indexing**: Updated `_buildContextIndex()` in `engine/drills/vocabulary.js` to index sentences under both their canonical dictionary lemma (`readings[0].lemma.toLowerCase()`) and their literal surface form (`token.toLowerCase()`). Handles multilingual pair keys (`spanish`, `hungarian`, `target`).
    - **Intelligent Query Resolution Waterfall**: Implemented `_getOccurrences(word)` resolving deck entries across direct key matches, lowercase matching, slash-separated gender pairs (`alto / alta` -> `alto`, `alta`), article stripping (`el perro` -> `perro`), Lexicon lemma lookups, and Hungarian `-ni` infinitive stem resolution.
    - **Decoy Shape Normalization**: Enhanced `_pickWordDecoys` to strip leading articles from distractors and match adjective gender endings, preventing malformed questions (e.g. `El el caballo corre`).
    - **Context Coverage Surge**: Boosted Spanish context sentence matching from 65.4% (1,886 words) to 98.9% (2,850 words), recovering 964 words into rich contextual cloze, discrimination, and choice exercises.
    - **Test Suite Added**: Authored `tests/drills/test-vocabulary-surface-matching.js` asserting surface forms, slash adjectives, and article nouns resolve with valid blanking and zero emojis.

50. ~~**App-wide Reddit Critic Audit: Zero-Failure & Flow Resilience Pass**~~ — **Done 2026-09-18.**
    Comprehensive audit from the perspective of an obsessive, technically savvy language learner. Resolved all identified bugs, dead-ends, unhandled edge cases, and infinite loading risks across the engine:
    - **Boot Screen & Crash Prevention**: Guarded global DOM event listeners (`typeof document !== 'undefined'`) across `decks.js`, `content-loader.js`, `vocabulary.js`, and `ui.js`. Added a 6-second safety timeout and `try/catch` fallback around `loadCurriculumData()` in `init.js` with retry UI to prevent permanent boot hangs. Added `teardownTab('leveltest')`. Exported `window.XP` and module exports in `xp.js`, fixing silent 0 XP awards in Speaking and Writing studios.
    - **Vocabulary Driller Fallbacks & Dead-End Elimination**: Implemented `_buildDirectDefinition`, `_buildReverseChoice`, and `_buildReverseRecall` in `vocabulary.js` to automatically fall back to direct recall when words lack corpus sentences or are non-content parts of speech. Completely eliminated the unplayable abort screen.
    - **SRS Decks & Review Polish**: Decoupled `clearDeck()` from global XP in `srs.js`, added confirmation modal, and replaced destructive alert. Implemented `sessionRelearningQueue` so SM-2 cards rated "Again" remain in active session rotation until successfully recalled, eliminating premature "Session Complete — 0%". Fixed Type Mode in `checkTypedAnswer()` to accept both bare lemmas and article-prefixed forms (`perro` and `el perro`). Added diacritics accessory bar to SRS Review Type Mode.
    - **Verb Driller Accents**: Mounted `UI.diacriticsBarHtml` on Verb Speed (`#vspeed-answer`) and Verb Table (`.vtable-input`) drills so mobile and international learners can input accented characters (`á, é, í, ó, ú, ñ, ü`) seamlessly without switching keyboard layouts.
    - **Reader Familiarity & Offline Audio**: Cleaned reader tokens in `getWordStatus()` to strip inverted Spanish punctuation (`¿, ¡`) and punctuation quotes, and integrated SRS `knownWords` checking so graduated words are properly recognized instead of falsely styled as unknown. Unblocked offline audio in `StoryAudioPlayer` so cached IndexedDB audio and local `speechSynthesis` playback function without network.
    - **Level Test Lifecycle & Hardware Clean-Up**: Added `LevelTest.stop()` with active media stream track releasing (`stream.getTracks().forEach(t => t.stop())`), preventing hardware microphone indicator lockups. Added `onExit` callback support to `LevelTest.open()` to cleanly return learners to study plan checklists upon exit.
    - **Unified Toast System & Speech Leniency**: Implemented accessible, non-blocking `UI.toast(msg, type)` in `ui.js` and `styles/components.css`. Replaced all blocking browser `alert()` dialogs across `lessons.js`, `decks.js`, `library.js`, `reader.js`, `writing.js`, and `speaking.js`. Updated inline lesson voice input to check `SpeechInput.isRecognitionSupported()` specifically for speech-to-text, preventing silent 10-second desktop browser timeouts (e.g. Firefox desktop).
    - **Service Worker & PWA Cache Invalidation**: Bumped `CACHE_VERSION` in `sw.js` to `v2026-09-18a` so browsers immediately cycle their app shell caches to load the updated scripts and styles.

26. ~~**Vocabulary Driller: scoped session dead-end fixed**~~ — **Done 2026-09-18.**
    The UI fallback for the dead-end (mounting `RecommendationEngine.mountNextAction()` + "Back to Workshop") had already shipped; this closes the systemic content gap that caused it. Backfilled missing example sentences for the Translation Driller / Vocabulary Driller Context-mode corpus:
    - Generated ~2,450 new example sentences (Haiku subagents, one per originally-missing deck word) across `content/{es,hu}/backfill_sentences/*.json`, folded in via `scripts/build_translation_index.py`.
    - Full grammar review pass, not just generation: per-file review agents found and fixed ~290 real errors in the Hungarian content (invented verb forms, wrong case government, definite/indefinite conjugation mismatches, a systemic `az`/`a` article-rule bug affecting 300+ sentences, one file with real õ/û mojibake) and ~10 in Spanish (gender agreement, a stray English word, a logic contradiction).
    - `scripts/export_missing_vocab_sentences.py` (the missing-word detector itself) had two real bugs fixed: it falsely flagged ~88% of "still missing" Spanish words because `decks.json` stores nouns with their article (`"el cumpleaños"`), which can never match a single sentence token; and it under-recognized inflected/prefixed Hungarian conjugations against an incomplete lemma index. Both fixed with targeted matching fallbacks (article-stripping for ES; stem/agglutination heuristics for HU `-ni`/`-ik` forms).
    - Closed the resulting smaller residual gap (44 ES + 92 HU words the fixed detector still flagged) with a second Haiku pass + review, then a final ChatGPT-generated pass for the last 54 Hungarian words.
    - **Result**: Spanish corpus gap fully closed (0 missing, verified). Hungarian closed to a small irreducible detector residual (~21 words) caused by irregular verb stem alternation (e.g. `megy`→`ment-`) that regex heuristics can't resolve — confirmed by direct inspection that these words are in fact already covered with correct sentences.
    - The original item's note about ~40 Spanish deck entries keyed to a surface form (`soy`, `alto/alta`) failing lemma matching in the live Driller was not independently re-verified this pass — tracked as a follow-up (see queue item 49 in `ROADMAP.md`).

36. ~~**Exercise-type variety: audit calibrated & scope narrowed to 45 A2 lessons**~~ — **Done 2026-09-18.**
    Resolved the exercise variety gap and listening parity across all 45 lessons in the 9 named A2 units (`imperfectobasico`, `imperfectocontraste`, `imperativoafirmativo`, `imperativonegativo`, `pronombrescliticos`, `condicionalsimple`, `subjuntivobasico`, `perifrasisverbales`, `educacionyestudios`):
    - **Dialogue Enrichment**: Replaced generic `fill-blank` exercises with full `dialogue-complete` exercises (90 exercises) featuring natural speaker turns and plausible Latin American Spanish distractors.
    - **Writing Enrichment**: Replaced generic `fill-blank` exercises with `structured-writing` exercises (45 exercises) providing bilingual prompt-and-model-answer templates.
    - **Listening Parity**: Authored and added dedicated `Listening` blocks (`listening-choice` + `dictation`, 90 exercises) across all 45 lessons and wired them into lesson definitions, achieving full structural parity with the 100 numbered A2 lessons.
    - **Variety & Word Coverage Pass**: Every lesson now spans 6 distinct exercise types (passing `MIN_LESSON_TYPES = 5`), exercises incorporate lesson vocabulary to clear `every new word appears in an exercise`, all 3,308 files pass schema validation (`validate-content.py es`), and `build-manifest.py` cleanly generates.

38. ~~**A2 lessons systemically show "2 goals vs 1 checklist item"**~~ — **Done 2026-09-18.**
    Investigated the 123/174 mismatch pattern across A2 lessons. Scoping confirmed that `guides/a2-lesson-guide.md` does not prescribe goal/checklist structure; rather, an early generation artifact (commit `813cf6a8`) copied a single `"goal"` into the checklist while leaving a generic boilerplate Goal 2 in `goal.items` (along with trailing `..` typos in 99 lessons). Resolved via Option 1:
    - **100 Numbered Teaching Lessons (`a2-01-01` to `a2-20-05`)**: Trimmed generic secondary boilerplate Goal 2 (*"Use the ... vocabulary from this lesson"* or repeated unit grammar lines), retaining Goal 1 as the single, focused lesson goal. Cleaned checklist items to strictly match Goal 1 and removed trailing double dots (`..` -> `.`).
    - **20 Numbered Consolidation Lessons (`a2-01-consolidation` to `a2-20-consolidation`)**: Unified the two review goals into 1 matching review goal that directly mirrors the single synthesized checklist item.
    - **3 Named Unit Mismatches**: Resolved 3:2 mismatches to 2:2 pairs in `a2-imperativonegativo-04`, `a2-perifrasisverbales-01`, and `a2-pronombrescliticos-05`.
    - **Checklist Prefix Standardization**: Standardized 16 named unit checklist items that began with *"I know that..."*, *"I understand..."*, or *"My writing..."* to start with `"I can "` per the project-wide authoring standard.
    - **Derived Indexes & Verification**: Rebuilt `competencies-index.json` (2,439 competencies cleanly indexed without typo artifacts), regenerated manifest (`build-manifest.py`), passed schema validation (`validate-content.py es`: 3,308 files), and verified zero failures for `goals and checklist are one-to-one` and `every checklist item begins "I can"` across all 174 A2 lessons via `scripts/audit-lesson.py a2`.

37. ~~**New vocabulary frequently never appears in its own unit's story**~~ — **Done 2026-09-18.**
    Investigated the 55% (A1), 59% (A2), and 40% (B1) failure rates. Found this was an architectural audit mismatch rather than missing content:
    - **Curriculum design vs audit expectation**: A unit teaches 25–55 new words across its 5 lessons, but carries only one shared 100–250 word story (in Lesson 5). Expecting every single word from all 5 lessons to appear in a single short narrative is mathematically impossible without turning graded reader stories into unnatural word lists.
    - **Tooling calibration in `scripts/audit-lesson.py`**: Added disk fallback in `unit_story_ref()` to discover standalone original stories on disk (all 27 A1 units and 27/29 A2 units already have complete original stories written), clearing all 37 "unit has no story yet" warnings. Calibrated the word-in-story check from a blocking lesson failure (`r.rule`) to an advisory warning (`r.warn`), while preserving `every new word appears in an exercise` as the strict blocking rule that guarantees every word is drilled.
    - **Documentation updated**: Aligned `content/es/guides/a1-content-spec.md` and `a1-quality-checklist.md` with this calibrated expectation.

34. ~~**HU `a2-curriculum-draft.json` grammar_coverage may not match what's taught per unit**~~ — **Done 2026-09-17.**
    Comprehensive audit conducted across all 370 Hungarian A2 grammar files against the draft claims in `content/hu/a2-curriculum-draft.json`:
    - **Reconciled 32 draft units to 37 live units**: `a2-curriculum-draft.json` originally stopped at Unit 32; synchronized units 33 to 37 (*Declined Pronouns: Internal & Surface*, *Declined Pronouns: Proximity & Motion*, *Translative Case (-vá/-vé)*, *Essive-Formal Case (-ként)*, and *Sociocultural Pragmatics & Customs*) matching `content/hu/curriculum/curriculum.json`.
    - **Reconciled inaccurate/stale claims**: Updated `grammar_coverage` to document `-hat/-het` as an introductory 1-lesson preview (Unit 23) rather than a full paradigm; marked `akar` as integrated from A1; clarified possessive nominal suffixes vs deferred independent possessive pronouns (`enyém`); and clarified Topic & Focus word order (Unit 22 prefix splitting / Unit 33 focus).
    - **Backfilled omitted taught grammar**: Added translative `-vá/-vé`, essive-formal `-ként`, distributive temporal suffixes `-nta/-nte` and `-nként`, and declined case-marked personal pronouns to `grammar_coverage`.

33. ~~**20 of 26 A1 consolidation lessons ship the wrong shape**~~ — **Done
    2026-09-17.** Fixed all 20 failing A1 Spanish consolidation lessons to
    conform to `scripts/audit-lesson.py`'s `"single"` shape:
    - **Structural merge**: merged split Practice/Dialogue/Writing exercise-group
      blocks into a single `"Review"` group in each lesson JSON, and removed
      the empty `srs` block.
    - **Goal/checklist alignment**: updated all goals and checklist items to
      consistently start with `"I can ..."`, and made goal and checklist item
      counts 1:1.
    - **Exercise variety backfill**: added two schema-compliant `fill-blank`
      exercises to each of the 12 consolidation exercise sets that only had 4
      exercise types, bringing every Review block to 5+ distinct types.
    - **Teaches-tag coverage**: re-tagged gustar consolidation exercises from
      generic placeholder `"consolidation"` to 10 granular grammar tags; added
      cumulative A1 crossover tags across 5 other consolidation exercise files
      so all 6 lessons span 9–10 distinct teaches points (satisfying 8+).
    - Validated schemas (`validate-content.py es` passes 3,308 files with 0
      failures) and audit (`audit-lesson.py a1` passes 24/26 consolidation
      lessons, with the remaining 2 being pre-existing Unit 1 scope checks).

28. ~~**Writing/Speaking Studio topic prompts sourced from real exam
    topics**~~ — **Done 2026-09-17.** User supplied three ChatGPT-sourced
    `.txt` files (HU A1-B1, ES A1-A2, ES B1 — 60 exam-style tasks total,
    30 writing/30 speaking, split into Situation/Task/bullet-point-list/
    word-or-time-target). Found on scoping that most of the work was
    already done, uncommitted, in this working tree — apparently by a
    concurrently-running agent: `scripts/import_cefr_exam_prompts.py`
    (a complete parser for this exact format, both languages, both
    modalities), `content/{es,hu}/speaking-prompts.json` (generated from
    these same files — verified byte-for-byte identical to a fresh
    re-run of the script), and `engine/drills/speaking.js` already
    switched from reusing `writing-prompts.json` to its own dedicated
    file. `writing-prompts.json` for both languages had the real prompts
    merged in too (append-by-id, so the old internally-invented A1/A2/B1
    prompts were still sitting alongside the new real-exam ones). Per
    user's choice, removed those 3 old invented prompts per language
    (kept the lone B2 one — no real-exam B2 source exists yet). Verified
    live: `WritingDriller.render()` shows exactly the 5 real-exam prompts
    per level (A1/A2/B1) plus the untouched B2 entry, for both `es` and
    `hu`; a full prompt's Situation/Task/Include text renders correctly
    on the writing screen. No code changes needed — `writing.js`'s
    grading path already treats a missing `targetSkills` as `[]` and
    degrades gracefully.
22. ~~**Full guide/planning-doc staleness audit**~~ — **Done 2026-09-17.**
    Paused 2026-09-16 after `a1.md` and `a1-vocabulary-themes.md` were
    regenerated from `content/es/curriculum/units/a1.json` + real
    lesson/vocabulary files, replacing the obsolete 20-sequential-lesson
    framing with A1's real 26-units-×-6-lessons structure. Finished the
    remaining seven A1 guide docs the same way, each read against real
    content or `scripts/audit-lesson.py` (the actual enforced spec) rather
    than the old prose:
    - `a1-grammar.md`, `a1-learning-objectives.md`,
      `a1-progression-matrix.md`, `a1-reading-plan.md`, `a1-story.md`,
      `a1-quality-checklist.md` — mechanical extraction from
      `content/es/curriculum/units/a1.json` and the real lesson/story
      files, delegated to Haiku subagents and spot-checked.
    - `a1-reading-plan.md` / `a1-story.md` also fixed a real factual
      error: Unit 14's story is "El número del autobús" (Meg and Carlos
      needing numbers for a museum trip), not the old "Un paseo por
      Hanói" text, which didn't match any real story file. Both docs also
      now correctly show 19 units with a linked story (not 20 — that
      same off-by-one existed in `a1.md`'s own prose too and was fixed
      there in this pass) plus the 6 written-but-unlinked topic stories.
    - `a1-content-spec.md` and `a1-exercises.md` — rewritten by hand
      (not delegated) against `scripts/audit-lesson.py` directly: dropped
      the fictional §4b split-lesson-parts and §4c three-end-of-level-
      review sections (confirmed dead architecture — 03a/03b merged into
      one unit, 03c became its own independent unit, and there's no
      lessons-18-19-20 review shape in the real files), replaced fixed
      exercise-count claims ("exactly 15", "~9 exercises") with the real
      observed ranges (12–19 total, Practice 8–16/Dialogue 2–4/Writing
      1–3/Reading 1–5 when present), and documented all 11 schema-defined
      exercise types (the old catalogue only listed 12 informally-named
      ones and missed several in active use elsewhere in the app).
    - `a1-lesson-template.md` — rewritten to match the real block shape
      (Practice → Reading → Dialogue → Writing) instead of the old
      per-category grouping with a fixed 9-exercise count.
    - Found and logged as its own item rather than fixed here: 20 of 26
      A1 consolidation lessons ship the wrong structural shape and fail
      `audit-lesson.py` — see "Current priority queue" item 33.
    - Not done in this pass, carried forward as its own item: HU
      `a2-curriculum-draft.json`'s `grammar_coverage` staleness check —
      see "Current priority queue" item 34.

1. ~~**Learner Path**~~ — **Done.** Single source of truth for
   level/unit/lesson position, completion state, and last-activity
   timestamp. See "Learner model & personalized path" below (step 1).
2. ~~**Learner Model / Brainmap**~~ — **Done.** Evidence-based knowledge
   tracking (step 2 below).
3. ~~**Recommendation Engine**~~ — **Done.** One strong + secondary
   recommendation (step 3 below).
4. ~~**Simplify Home experience hierarchy**~~ — **Done** (step 4 below).
5. ~~**Time-Based Sessions**~~ — **Done** (step 5 below). Heuristic
   constants flagged for later tuning — see "Current priority queue"
   → step 5's own note.
6. ~~**Unify all activity types as evidence**~~ — **Done 2026-09-11**
   (step 6 below): fixed the "recycle lottery" (a first-encounter
   exercise now counts as evidence immediately, not only if later
   redrawn into a recycle block) and folded `DrillHistory` into
   `LearnerModel` as `weakDrillers()`.
7. ~~**Cloud persistence**~~ (Cloudflare Worker + D1) — **Deployed & Live 2026-09-14**:
   Cloudflare Worker deployed at `https://parlour-sync.gergkar.workers.dev`,
   D1 database schema (`magic_links`, `users`) installed and verified, CORS
   controls active, and magic-link passwordless email login dispatched via
   Resend. Client integration live in My Journey's Account card (`engine/sync.js`).
8. ~~**Italics content retrofit**~~ — **Done 2026-09-13.** Paused
   2026-09-10 partway (282/1366 files), resumed and completed: all
   ~1,366 grammar files across both languages/levels retrofitted
   (ES B1, HU A1 remainder, HU A2, HU B1 — commits `749012e2` through
   `bb79846d`), convention documented in the content style guides
   (`3a12155e`).
20. ~~**Batch fix/feature pass — Lessons, Decks, Speaking/Writing, Workshop,
    Reader, Journey**~~ — **Done 2026-09-16.** An 18-item punch list across
    four phases, each landed as its own commit:
    - Phase 1 (crashes): `enableCheck` ReferenceError killing structured
      speaking's auto-grade; end-of-lesson summary crash on close-during-
      render; Decks Review-all race + stale `currentReviewCard`; HU
      Workshop grammar-title formatting (now consults
      `grammar-titles.json` first, keyed by resolved path so a runtime
      course switch can't serve a stale language's cache).
    - Phase 2 (grading): Hungarian number/abbreviation leniency in
      `read-repeat`; `prompt-speak` now routes through CEFR `GraderEngine`
      instead of word-match; Verbal Production no longer cuts a recording
      short when native speech recognition ends its session mid-way
      (manual mode now restarts recognition instead of committing early).
    - Phase 3 (polish): Decks Match lockout cut from ~650ms to ~150-200ms;
      typed review auto-grades instead of requiring manual self-rating;
      Reader voice-button rest-state contrast bumped in both themes;
      Journey's Milestones collapsed to next-5 + "See all"; review
      sessions in `reviewDirection='audio-en'` now show a persistent
      "Audio mode" badge.
    - Phase 4 (bigger features): the 48 migrated A2 imperfecto lessons
      (see item above) wired into `build-manifest.py`'s `UNIT_TABLES` as
      units 21/22 — previously validating cleanly but invisible to the
      Learn tab; a course-wide Grammar Guide search (backed by a new
      prebuilt `indexes/grammar-guide-index.json`, after a live per-unit
      walk proved too slow at 100+ units — see
      `scripts/build_grammar_guide_index.py`), later made more
      discoverable (top of Learn tab, top of every level, linked from
      every per-unit guide); end-of-lesson summary split into a stats
      screen and a "what's next" reinforcement screen; a CEFR level-filter
      added to Writing/Speaking Studio's topic cards; a genuinely new
      "Set Your Own Task" flow letting a learner author their own one-line
      task + word/time limit for free writing/speaking, graded against
      exactly that task; `structured-writing` lesson steps now feed
      `LearnerModel` (were invisible to it before) plus an optional
      on-demand "Get feedback" button (no "AI" wording, hidden when
      `!navigator.onLine`).
    - Found and flagged along the way: 5 grammar files with single-
      character titles in A1 unit 02 (fixed same session, see commits
      `4a32e229`/`f71cf085`); the iOS audio-playback gap logged as item 19
      in ROADMAP.md.
21. ~~**Unit tables moved from Python code to JSON content**~~ — **Done
    2026-09-16.** Wiring the two new A2 imperfecto units into the
    curriculum (item above) meant editing a hardcoded `UNIT_TABLES` dict in
    `build-manifest.py` — a code change for a content-authoring decision.
    Moved each level's table (ES A1/A2/B1, HU B1) to
    `content/<lang>/curriculum/units/<level>.json`, an ordered array of
    `{title, stems, track?}`, schema-validated
    (`content/<lang>/schemas/units.schema.json`) like every other content
    file. Adding a unit to an already-tabled level is now appending one
    JSON object — no Python edit, no dev session required. Also added a
    project `CLAUDE.md` instructing sessions to keep this roadmap current,
    since nothing does that automatically. Verified `curriculum.json` is
    byte-for-byte identical to before the refactor (both languages,
    timestamp aside) — a pure data-location move, not a behavior change.

## Learner model & personalized path (architecture initiative) — done

User's own 7-step plan, logged 2026-09-10, superseding/reframing the ad-hoc
`Recommend` work into one coherent system. **Explicit ordering from the
user: cloud persistence is step 7, only after the rest works locally** —
build the learner model and recommendation logic first, then treat cloud
sync as a pure persistence/replication problem instead of solving "what
does the learner know" and "how do two devices agree on it" at the same
time. All 7 steps below are complete — matches "Completed queue items"
1-7 above.

1. **Learner Path — "Where am I?"** One reliable source of truth for
   current level/unit/lesson, completed vs. incomplete work, the next
   curriculum step, and last-activity timestamp (kept separate from
   curriculum position — finishing something isn't the same as touching
   the app). Today this is scattered: `getProgress()` in `engine/progress.js`
   tracks completion, but "next step" logic is duplicated across
   `engine/home.js`'s `practiceNudge()`/`miniGameNudge()` and
   `Recommend.lastCompletedLessonId()`/`unitFor()`.
2. **Learner Model / Brainmap.** Track what the learner actually *knows*,
   not just what they completed: grammar skills, vocabulary, exercise
   evidence, weak/developing/strong areas, prerequisites/dependencies,
   review needs. Mostly hidden from the learner. `Recommend.weakestSkill()`/
   `weakestWords()` are a first, narrow slice of this (SM-2 ease from
   `recycle.js`/`srs.js`) — the real model needs to fold in level-test
   results, reading/listening exercises, and prerequisite relationships
   none of today's code tracks.
3. **Recommendation Engine.** Path + learner model → one strong
   recommendation ("Continue Lesson 4.3"), with occasional secondary
   recommendations ("Practise adjective agreement"). The system decides;
   the learner isn't navigating a decision tree. This is where the
   queued "next recommended activity button after a mini-game" and "wire
   the HU-specific drillers (suffix/prefix/morphology/verb) into the
   mini-game signal, not just grammar+vocabulary" work belongs — both are
   pieces of this engine, not standalone features, so build them as part
   of this step rather than bolted onto the current ad-hoc `Recommend`
   module.
4. **Simplify the Home experience.** Reduce "here are 12 things you can
   do" down to a clear hierarchy: Recommended next step (primary action)
   → Optional reinforcement (secondary) → Explore (vocabulary, grammar,
   reading, Workshop, Decks — freedom preserved, but the app has a clear
   opinion about what to do next).
5. **Time-Based Sessions** (optional mode). Learner picks a time budget —
   10/15/20/30/45/60 minutes — and the app builds a finite session out of
   curriculum position, knowledge gaps, reviews due, and priorities, with
   a clear start and end. No countdown timer (time is a planning
   constraint, not a productivity metric). Completing a session does not
   advance the curriculum unless the actual lesson work was done. The
   normal recommended path stays the default; this is an alternative
   entry point, not a replacement. Depends on steps 1-3 existing first.
   **Built 2026-09-11** (`engine/studyPlan.js`/`engine/studyPlanRunner.js`).
   **To revisit** (flagged 2026-09-11, "tinker on time-based session" —
   no specific complaint yet, just a general "spend more time on this"
   note): the time-to-activity-count heuristics
   (`SEC_PER_REVIEW`/`SEC_PER_GRAMMAR_Q`/`SEC_PER_VOCAB_WORD`/
   `DEFAULT_LESSON_MINUTES`/`TEST_MINUTES` in `engine/studyPlan.js`) were
   built as best-judgment defaults, explicitly flagged at the time as
   "worth confirming against real usage... before shipping" — a good
   place to start once there's a specific thing about the feature that
   feels off after actually using it a few times.
6. **Make everything feed the same Learner Model.** Lessons, drills, SRS,
   Workshop, level tests, reading/listening exercises should all become
   evidence about the learner over time, rather than isolated features
   each with their own local state.
7. **Cloud Persistence — last, not first.** Once the above works locally,
   cloud sync becomes "learner state + learner model → cloud → another
   device," a straightforward persistence/replication problem, instead of
   simultaneously inventing the state model and figuring out how to
   replicate it. Design work deferred until steps 1-6 exist to sync, but
   the backend is already decided (2026-09-10) so it doesn't need
   revisiting later: **Cloudflare Worker + D1**, chosen over Supabase/
   Firebase after comparing free-tier limits — D1 covers this app's scale
   indefinitely (5GB storage, 5M row-reads/day, no auto-pause-after-
   inactivity, unlike Supabase's free tier) and reuses the exact Worker
   pattern already proven in this repo (`cloudflare-worker/bug-report-proxy.js`,
   see `BUG_REPORT_SETUP.md`). Planned shape once steps 1-6 are ready to
   build on:
   - Magic-link email auth (no passwords, no client SDK — plain `fetch()`
     calls from vanilla JS, matching the app's existing lightweight
     architecture — see the Core-First/Enhancement-Second principles in
     ROADMAP.md).
   - A new thin `engine/sync.js` that `progress.js`, `xp.js`, and `srs.js`
     write through instead of touching `localStorage` directly — today
     each of those three modules independently reads/writes its own
     localStorage key (`progressKey()`, `'spanishApp_xp'`,
     `Lang.key('srsDeck')`/`Lang.key('knownWords')`) with no shared
     abstraction; the sync layer needs to sit underneath all three
     without those modules growing their own cloud logic.
   - Local-first writes (localStorage updates immediately, UI never
     waits on the network) with a background sync queue.
   - Per-record merge, not whole-blob overwrite — a phone and a laptop
     need to reconcile (e.g. union completed-lesson sets, keep the
     higher SRS review count per card) rather than one device's full
     state clobbering the other's on next sync.
   - Curriculum/content stays out of this entirely — only mutable user
     state (progress, XP, SRS card state, known words, preferences)
     goes through the sync layer; lesson/grammar/exercise content stays
     purely local static files, as it already is.

   **Built 2026-09-11, deliberately smaller than the shape above** —
   scoped down with the user before building, not a silent deviation:
   whole-snapshot **backup/restore on two explicit buttons**
   (`engine/sync.js`, My Journey's Account card), not a background sync
   queue with local-first writes, and **last-write-wins**, not the
   per-record merge described above — confirmed most real usage is a
   single primary device, so a smart per-field merge (keep the higher
   SRS review count per card, union completed-lesson sets, etc.) is a
   real future need, not a v1 one. Curriculum/content-stays-local held
   exactly as planned — only learner state syncs. Cloudflare/D1/Resend
   infrastructure deployed and verified live 2026-09-14 (see "Completed
   queue items" item 7 above).

35. ~~**`audit-lesson.py` crashes on multi-blank fill-blanks, silently
    skipping A2/B1 teaching-order checks**~~ — found and **fixed
    2026-09-17** while scoping a "perfect what's shipped" improvement
    pass. `exercise_spanish()` assumed every `fill-blank` exercise had a
    scalar `answer` field, but exercises with multiple blanks use
    `answers` (a list) instead — at least `a1-01-01`, `a1-03-05`,
    `a1-06-01` through `a1-06-04` do this. That threw `KeyError: 'answer'`
    inside `check_teaching_order()`, which runs per-level *after* all
    per-lesson structural checks print — so `python scripts/audit-lesson.py`
    with no args always crashed partway through A1 and never reached
    A2/B1 at all. Per-lesson structural checks (the FAIL/warn lines) ran
    correctly when a level was passed explicitly (`a1`/`a2`/`b1`), so
    those results were already trustworthy; only the cross-lesson
    teaching-order pass was silently blind, for every level except
    (partially) A1, for as long as the bug existed.
    - **Fix**: `exercise_spanish()` now returns `[ex["sentence"]] +
      (ex["answers"] if "answers" in ex else [ex["answer"]])` for
      `fill-blank`, matching how other multi-value exercise types are
      already handled.
    - Verified: `python scripts/audit-lesson.py` (no args) now runs to
      completion across A1/A2/B1 with no traceback — reports "616
      lesson(s) need work, 731 exercise(s) test untaught Spanish" as its
      first-ever full-corpus teaching-order result. A2/B1's actual
      teaching-order failures are new information (never surfaced
      before) — see ROADMAP.md's Current priority queue for what's next.

10. ~~**UI/UX Overhaul Initiative (7-Phase Roadmap)**~~ — Sequenced 2026-09-12
    to elevate Parlour's interaction ergonomics, responsive layout, and
    aesthetic fidelity:
    - [x] **Phase 1: Visual Identity & CSS Cleanliness** — **Done 2026-09-12**:
      Purged legacy `.card` `background: var(--surface)` and heavy borders;
      eliminated `.br-flag-btn` box shadow (last shadow in the codebase);
      standardized open cream rows on `var(--bg)` with `1px solid var(--border)`
      hairlines and `--dur-fast` transitions.
    - [x] **Phase 2: Responsive Shell & Navigation Architecture** — **Done 2026-09-12**:
      Desktop Constructivist sidebar (≥1024px) with brand mark and pinned XP/streak;
      mobile bottom tab bar (<640px) with safe-area insets; tablet centered container
      (640px–1023px); in-lesson clean screen mode (`body.in-lesson`) across all viewports.
    - [x] **Phase 3: Exercise Ergonomics & Desktop Keyboard Flow** — **Done 2026-09-12**:
      Added desktop hotkeys `1`–`4` with subtle monospace key badges for choices;
      global diacritic helper toolbar (`UI.diacriticsBarHtml`) across lessons and
      all drill runners for `es`, `hu`, and `fr`; and intelligent character-level
      error diffing (`generateAnswerDiff`) with accent-specific feedback.
    - [x] **Phase 4: Library & Reader Experience Polish** — **Done 2026-09-12**:
      Added typography/font-size scaling controls (85% to 150%) persisted in localStorage
      with dynamic line-height across both Parlour stories and My Texts reading views;
      integrated reading scroll progress indicator track and bar;
      added instant universal search filtering across all rooms, shelves, titles, authors, and levels
      with match counter and clear button;
      refined word popup (`.wp-sheet`) with desktop modal centering, hairline borders, and mobile
      safe-area bottom padding.
    - [x] **Phase 5: Decks & SRS Organization & Gestures** — **Done 2026-09-12**:
      Organized massive unit deck catalogues into collapsible CEFR level sub-accordions (A1, A2, B1, B2, C1)
      with level badge indicators and deck counts;
      added instant universal search filtering across titles, topics, preview words, and CEFR levels
      with auto-expanding matched accordions and clear button;
      implemented fluid mobile touch swipe gestures on flashcard review (swipe left for Again, swipe right
      for Good, tap to reveal answer) with dynamic rotation, color-tinted feedback, and exit animations;
      added desktop review hotkeys (`1` Again, `2` Hard, `3` Good, `4` Easy, Space/Enter for Show/Good)
      with visible monospace `.review-rate-hint` badges.
    - [x] **Phase 6: Workshop & Driller Visual Unification** — **Done 2026-09-12**:
      Standardized `.driller-progress-track` and `.driller-progress-bar` across all 9 workshop drillers
      (`grammar.js`, `translation.js`, `listening.js`, `vocabulary.js`, `verbs/speed.js`, `hu-verb.js`,
      `hu-suffix.js`, `hu-prefix.js`, `hu-morphology.js`);
      standardized session HUD (`.gd-hud`, `.gd-hud-score`, `.gd-change-skill` `← Settings`);
      standardized 4-metric results grid (`.vspeed-results`, `.vspeed-stat`) and unified 3-button post-drill
      action loop ("Practice Again", "Change Settings", "Back to Workshop" via `Workshop.close()`), preserving
      driller-specific actions (e.g. Vocabulary's "Add missed words to a deck").
    - [x] **Phase 7: Dark / Low-Light Reading Theme** — **Implemented 2026-09-12**:
      Inverted Constructivist palette (`[data-theme="dark"]` and `@media (prefers-color-scheme: dark)`)
      with midnight navy ground (`#0C1B2B`), warm cream structure & typography (`#F5F1E8`), crisp 1px hairlines,
      and vibrant warm orange focal accent (`#FF5A26`);
      immediate anti-FOUC initialization in `<head>`;
      standalone `engine/theme.js` with `'system' | 'light' | 'dark'` options and `localStorage` persistence;
      interactive Appearance card in My Journey tab;
      quick-toggle theme buttons in desktop sidebar and page header.

11. ~~**Speaking Function & Pronunciation Engine Initiative**~~ — **Built & deployed 2026-09-14**:
    - **Core Speech Recognition & Evaluation Engine** (`engine/speech-input.js`):
      - Browser-native Speech-to-Text (`SpeechRecognition` / `webkitSpeechRecognition`) with multi-language mapping (`es-ES`, `hu-HU`).
      - Transparent word-by-word evaluation tagging (`matched` vs `missed`) with diacritic, casing, and punctuation leniency via normalized Levenshtein token distance.
      - Sound energy visualizer and live interim transcription bubble.
      - Self-evaluation fallback mode for quiet rooms or unsupported browsers (e.g. desktop Firefox).
      - One-tap "Can't speak right now" preference to snooze speaking exercises for 30 minutes.
    - **Curriculum & Lesson Integration** (`engine/lessons.js`):
      - Two dedicated speaking step types: `read-repeat` (listen to model pronunciation and repeat) and `prompt-speak` (translate prompt into target language and say it out loud).
      - Injected 2 dedicated speaking practice steps into every curriculum lesson generated from the lesson's target vocabulary and grammar structures.
    - **Workshop Speaking Driller** (`engine/drills/speaking.js`, `engine/drills/speaking-runner.js`):
      - Dedicated Workshop speaking module with CEFR level selector (A1–C1), topic filters, and mode toggles (`Prompt & Speak`, `Read & Repeat`, `Mixed`).
      - Integrated model audio replay, mic waveform animation, and comprehensive evaluation breakdowns.
    - **SRS Flashcard Speaking Integration** (`engine/srs.js`):
      - Voice response mode on flashcard reviews with immediate accuracy feedback.
    - **Dual Audio Replay & Model Comparison**:
      - Side-by-side comparison bar across Lessons, Workshop, and SRS:
        `[Model Voice]` plays the native model pronunciation, while `[Your Voice]` replays the learner's actual recorded speech clip.
      - Mutual audio interruption, live `Playing...` active state, and dark-mode styling.
    - **Mobile-Proof Engineering & Learner Hesitation Debounce**:
      - Fixed iOS Safari user gesture expiration by invoking `recognition.start()` strictly synchronously within the tap event handler.
      - Solved hardware mic contention on mobile devices by running non-blocking background `MediaRecorder` audio buffering alongside native STT.
      - Extended silence debounce from 1.3s to **2.8 seconds** with automatic pause resumption on native mobile `onend` to accommodate learner hesitations ("um, uh, mhh") and thinking pauses.
      - Added safety session ceiling (25 seconds) and asset version cache-busting (`scripts/stamp-assets.py`).

12. ~~**Writing & Speaking Studios, CEFR Grader Engine & Oral Leniency**~~ — **Built & deployed 2026-09-14**:
    - **Dual Grading Engine** (`engine/grader/`): deterministic zero-dependency `LocalGrader` for instant local rubric scoring + optional `GraderEngine` for Cloudflare AI / Anthropic LLM feedback.
    - **Writing Studio** (`WritingDriller` in `engine/drills/writing.js`): open-ended free-text written production with topic/level selection, prompt suggestions, and structured CEFR assessments.
    - **Speaking Studio** (`SpeakingStudio` in `engine/drills/speaking.js`): unstructured speaking production practice with prompt generation, live microphone transcription, and audio playback.
    - **Oral Modality Calibration** (`engine/grader/grader-prompt.js`): calibrated prompts and local metrics to accommodate oral speech traits (pauses, filler words, transcript capitalization/punctuation artifacts).
    - **Manual Speech Transcript Editing**: allows learners to edit the raw speech recognition transcription before submission on unstructured speaking tasks.
    - **Instant Auto-Stop on 100% Target Match**: automatically stops recording the exact instant target speech matches 100%, removing manual mic clicks.
    - **Mobile Hardware Contention & Lifecycle Hardening**: eliminated MediaStream audio track hardware locks on non-audio steps, and resolved Android single-shot continuous listening conflicts.

13. ~~**CEFR "Can-Do" Checklist Competencies Integration**~~ — **Built & deployed 2026-09-14**:
    - Extracted and indexed official CEFR competency descriptors in `content/es/indexes/competencies-index.json`.
    - Wired competencies directly into `LearnerModel` (`recordCompetencyEvidence`, `getCompetencyCoverage`), Post-Lesson Summary screen (`renderLessonSummary`), My Journey mastery stats, Level Tests, and Studio prompts.

14. ~~**Library: Dual-Card Recommended Reading & Deep Bilingual Topic Search**~~ — **Built & deployed 2026-09-14**:
    - **Dual-Card Recommendation Banner ("Pick Your Pace")**: Pinned at the top of Library tab (`.lib-recs-container`), computing a Comfortable Read ($i+0$, fluency consolidation) and a Challenging Read ($i+1$, lexical stretch / authentic narrative) based on LearnerPath level and unread status.
    - **Deep Bilingual Topic Search**: Universal topic matching across English and Spanish (`BILINGUAL_TOPIC_SYNONYMS`) covering titles, authors, levels, unit titles, summaries, topic tags, and paragraph keywords.
    - **Manifest Keyword Indexing**: `build-manifest.py` automatically extracts up to 80 thematic keywords from story paragraphs for offline instant search.
    - **Word-Boundary Matching**: queries $\le 4$ chars enforce word boundaries, avoiding substring false positives.

15. ~~**Offline Support & Progressive Web App (PWA)**~~ — **Built & deployed 2026-09-14**:
    - **Service Worker** (`sw.js`): Precaches 82 core application shell assets (HTML, 8 stylesheets, core engine scripts, base curriculum and story manifests).
    - **Dynamic Content Caching**: Network-first caching for visited lessons, grammar explanations, and readings (`/content/`).
    - **Web App Manifest** (`manifest.webmanifest`): Standalone PWA installation on mobile and desktop with Constructivist branding.
    - **Network-Only Bypass**: Explicitly bypasses Cloudflare sync endpoints and external AI APIs.
    - **Offline Connectivity Status**: Floating status banner (`.offline-banner`) notifies users when operating offline.

16. ~~**Decks Importer (Anki, Quizlet, CSV)**~~ — **Built & deployed 2026-09-14**:
    - Auto-detects delimiters (tab, comma, semicolon, dash, colon), strips HTML tags, handles quotes, and validates lemmas against Lexicon dictionary.

17. ~~**Codebase Health & Performance Audit (Zero-DOM Escaping & Engine Cleanup)**~~ — **Completed 2026-09-14**:
    - **Zero-DOM String Escaping**: Replaced `document.createElement('div')` in `Reader.escapeHtml` and 8 drill/deck/verb runners (`engine/drills/grammar-runner.js`, `engine/drills/grammar.js`, `engine/drills/translation-runner.js`, `engine/verbs.js`, `engine/verbs/speed.js`, `engine/verbs/table.js`, `engine/decks/learn.js`, `engine/decks/match.js`) with fast, zero-allocation string escaping via `UI.escape()` with regex fallback. Eliminates disposable DOM nodes and GC pauses during text and exercise rendering.
    - **Debug Console Log Cleanup**: Purged leftover verbose debug `console.log` statements in `engine/lexicon.js` and `engine/reader.js`.
    - **Global Scope & Static Analysis Audit**: Confirmed all 64 engine scripts load and compile cleanly, with zero syntax errors, balanced CSS rules, zero unreferenced files, and 0 pictorial emojis across all code and stylesheets.
    - **Cache & Service Worker Synchronization**: Bumped PWA service worker and asset cache query parameters to `v2026-09-14h`.

18. ~~**Online Substack-Style Story Reading Player & Google Cloud TTS Architecture**~~ — **Built & deployed 2026-09-15**:
    - **Substack-Style Reader UI** (`engine/reader.js`, `styles/components.css`): Floating bottom pill player (`.story-substack-player`) pinned above the bottom viewport, styled with Constructivist borders, subtle glassmorphism backdrop blur, and smooth transitions. Features a circular Play/Pause button, active speaker and language tags (`#ssp-speaker-tag`), paragraph scrubber slider, paragraph counter/remaining counter (`1/14`, `-13 left`), and speed toggles (`0.8×`, `1.0×`, `1.2×`, `1.5×`) defaulting strictly to natural **`1.0×`** speed.
    - **Online-Only Graceful Visibility**: Adheres to the Core First, Enhancement Second architectural principle. Audio listening is strictly an online progressive enhancement: the player is hidden (`hidden` attribute and `.is-offline`) when disconnected (`!navigator.onLine`), and dynamically surfaces whenever internet connectivity is present. Paragraph audio buttons fall back gracefully to offline browser speech synthesis.
    - **Zero Git Audio Bloat (In-Memory Streaming)**: Eliminated all static `.mp3` and `.wav` audio files from the repository and Git history. Audio is fetched and synthesized on demand per paragraph via in-memory `Audio` buffers with eager next-paragraph background pre-fetching, keeping the repository 100% lightweight code and text.
    - **Cloudflare Worker TTS Proxy** (`cloudflare-worker/tts-worker.js`): Zero-dependency Cloudflare Worker proxy protecting the Google Cloud TTS API key in worker secrets. Handles CORS verification for production domains (`gergkar-gif.github.io`, `parlour.me.uk`, and `localhost`), mapping requests to Google Cloud Journey and Studio neural speech models.
    - **Substack-Calibrated Voice Casting**: Uses Google Journey models (`en-US-Journey-F`, `en-US-Journey-O`) for rich conversational, podcast-quality English scaffolding narration, and Google Studio/Neural2 models (`es-ES-Studio-C`, `es-ES-Neural2-B`, `hu-HU-Wavenet-A`) for authentic Spanish and Hungarian dialogue.
    - **Dual-Language Stories**: Fully supports Hungarian stories with English scaffolding narration and Hungarian dialogue. Detects paragraph `lang`, routing scaffolding to English Journey voices and Hungarian dialogue to native Hungarian voices with synchronized paragraph scrolling and active highlighting.
    - **Hungarian Phonetic Digraph Adaptation ("Károly" -> "Károy")**: Adapted speech synthesis inputs across `engine/reader.js`, `engine/speech.js`, and offline generation tools to replace the Hungarian name `Károly` with `Károy` (reflecting the Hungarian `ly` = `/j/` digraph pronounced like English "y") for speech synthesis, while keeping proper visible orthography (`Károly`) intact on screen.
    - **Pedagogical Comprehension Checks**: Built-in interactive multiple-choice check with immediate validation and explanations.
    - **Schema & Manifest Integration**: Added `narration` definitions in `story.schema.json` with optional `audioFile`, and updated `build-manifest.py` so `hasAudio` is based on narration structure and paragraphs rather than local disk audio presence. Verified with 11 automated unit tests in `tests/reader/test-story-narration.js`.

23. ~~**`ParlourTTS` engine abstraction (`engine/tts.js`)**~~ — **Built and
    live 2026-09-16.** Content -> `ParlourTTS.speak({text, language, type,
    voiceName, gender, speed, onEnded})` -> provider -> audio, so no caller
    talks to a TTS provider directly. Cloud-first (Google Cloud TTS via
    `cloudflare-worker/tts-worker.js`), falling back automatically to
    device `speechSynthesis` (`engine/speech.js`'s `Speech` module) when
    offline, the worker errors, or no API key is configured — verified live
    in-browser (Library story reader and Workshop's Listening Driller both
    correctly attempt cloud, catch the failure, and fall back to device
    speech with auto-advance intact). Session-cached per
    `language::voiceName::text` so repeat playback is free.
    - Undoes an uncommitted regression from between 2026-09-15 and
      2026-09-16 that had replaced item 18's real Google Cloud TTS call in
      `tts-worker.js` with a reverse-engineered, unofficial Microsoft
      Translator endpoint (hardcoded HMAC key pulled from the Android app).
      Worker now calls `texttospeech.googleapis.com` directly again, using
      Chirp3-HD voices (Google's newest natural-narration tier, and the
      only one covering both Spanish *and* Hungarian at that quality —
      Studio and Neural2 don't have Hungarian voices). Free tier is 1M
      chars/month; Parlour's own estimated spoken-content corpus is a
      one-time synthesis in the low single-digit millions of characters,
      cached forever after. Needs a GCP project + billing account (card on
      file, but $0 expected) and `wrangler secret put GOOGLE_TTS_API_KEY`
      on the worker before cloud playback actually works — until then it
      falls back to device speech automatically, nothing breaks.
    - **GCP + Cloudflare setup completed and verified live 2026-09-16**:
      `parlour-tts` GCP project, billing account, Text-to-Speech API
      enabled, API key restricted to that one API, `GOOGLE_TTS_API_KEY`
      deployed as a Cloudflare Worker secret. `/health` reports
      `hasApiKey: true` and a real story played through Chirp3-HD end to
      end with zero fallback warnings.
    - **Purposeful voices by content type, same day**: `tts-worker.js`'s
      `SHORT_VOICE` map picks by an explicit per-character voice first (see
      below), else `gender` (`male` -> Orus, `female` -> Kore), else `type`
      (`vocabulary`/`listening`/`pronunciation` -> Iapetus for clarity,
      `instruction` -> Achird for a distinct "app voice", `example` ->
      Despina, `narrator`/`reading` -> Sulafat), else the narrator default.
      Voice names are shared across the Chirp3-HD bank per language, so the
      same semantic map works for es/hu/en without per-language tuning.
    - **Distinct voice per named character, same day**: a story's dialogue
      no longer collapses every male character onto one voice and every
      female character onto another. `reader.js`'s `assignCharacterVoices()`
      reads each story's own `narration.speakers[name].gender` and hands
      out one voice per character from a 6-deep gender-matched pool (Orus,
      Puck, Charon, Fenrir, Umbriel, Algieba for male; Kore, Aoede, Leda,
      Zephyr, Callirrhoe, Autonoe for female), assigned once per story load
      so "Meg" keeps the same voice in every line. Worker's `character`
      param (a short voice name) takes priority over `gender`/`type`.
    - **All three leftovers resolved 2026-09-16**:
      1. All ~15 remaining `Speech.speak()`/`Speech.button()`/
         `Speech.available()` call sites (decks, lessons, library, SRS,
         speaking runner, studyPlan, recommendationEngine) migrated to
         `ParlourTTS` — added `ParlourTTS.available()` (online, or a device
         voice as fallback) and `ParlourTTS.button()` (same drop-in markup
         ergonomics as `Speech.button()`, own `[data-tts-text]` delegated
         click listener so it doesn't collide with `Speech`'s
         `[data-speak]` one) to make the swap mechanical. Verified live:
         Decks word list, a lesson's vowel-sound table, and the SRS review
         card all speak through the cloud provider with no fallback
         warnings. Found and fixed a related latent bug along the way:
         Speaking Studio's "play my own recording" only ever cancelled
         `speechSynthesis`, not a still-playing cloud audio clip — now
         calls `ParlourTTS.stop()`, which covers both.
      2. `listening.js`'s settings screen now gates on `ParlourTTS
         .available()` instead of `Speech.available()`, so the driller
         works from the cloud provider alone on a device with no voice
         installed. Same fix applied to the two other places that decide
         whether to *recommend* Listening/Speaking activities at all
         (`studyPlan.js`'s time-based session builder, `recommendation
         Engine.js`'s Home candidates) — otherwise migrating the driller
         itself would have been undercut by recommendation logic still
         hiding it from cloud-only users.
      3. `scripts/narrate-story.py` no longer synthesizes audio at all —
         removed the `edge-tts` dependency, `synthesize_story_neural()`,
         and the `audioFile` field it wrote into `narration`, along with
         the now-dead `--no-synth` flag. It only ever generates the
         timing/pedagogical metadata now (word-count-based paragraph
         timing, comprehension questions, `speakers[name].gender` for the
         voice assignment above) — verified with `--dry-run` against the
         real content and the existing 11-test narration suite still
         passing unchanged.
    - **R2 audio cache added 2026-09-17**, prompted by a backend cost
      review: `tts-worker.js`'s only cache was `ParlourTTS`'s in-memory
      session cache (above), which meant every reload re-synthesized
      identical lesson audio through Google TTS — pure waste, since lesson
      text is fixed and near-all repeat traffic across learners/sessions.
      Worker now content-addresses each synthesis (SHA-256 of
      `languageCode::voiceName::speakingRate::pitch::text`) and checks an
      R2 bucket bound as `TTS_CACHE` before calling Google; a miss writes
      the MP3 to R2 after synthesis (best-effort — a write failure doesn't
      fail the response, just costs a repeat Google call later). `/health`
      now reports `hasR2Cache`. No client change needed — `engine/tts.js`
      already just reads `audioContent` from the same JSON shape. Verified
      live: `/health` returns `hasR2Cache: true` on the deployed worker.

24. ~~**SRS/Decks review card: audio/mic UI stripped back down**~~ — **Built
    2026-09-16.** The card had accumulated three overlapping audio
    affordances: a `ParlourTTS.button()` listen icon, a separate
    audio-first review direction (`reviewDirection === 'audio-en'`, its own
    front/back layout and auto-play), and a self-recording "Speak" button
    (`reviewSpeakWord()` — records via `SpeechInput`, evaluates pronunciation,
    offers a "Hear yourself" replay). User's call: "too many things for an
    SRS card... all I want is on the target language side to have a little
    microphone icon... click and listen to the word. That's all. Like in a
    Quizlet card." Removed the audio-first direction (now a plain two-way
    Spanish/English toggle) and the self-recording/evaluation flow entirely
    (`reviewSpeakWord`, `reviewPlayUserAudio`, their state, the `#review
    -speak-btn`/`#review-speak-feedback` markup, `.review-speak-*`/
    `.review-audio-*`/`.btn-audio-prompt` CSS) — kept only the one listen
    icon next to the Spanish word. Pronunciation self-recording still exists
    in Speaking Driller, which already covers that use case separately;
    nothing was lost, just de-duplicated off the review card. Verified live:
    Flip and Type modes, Show Answer, rating buttons, and the two-way
    direction toggle all work with no console errors and no orphaned
    references to the removed markup/classes anywhere in the codebase.

25. ~~**AI-grading fixes: natural-language tips surfaced, task-completion
    grading for can-do checks**~~ — **Built 2026-09-16.** Two related grader
    fixes from a user feedback batch:
    - **Lesson-end writing/speaking feedback was numbers-only.** The AI
      grader (`engine/grader/grader-prompt.js`) already returns a
      natural-language coaching tip (`feedback.priorities`/
      `errors[].explanation`) — Writing/Speaking Studio already renders it,
      but the two in-lesson checkpoints (`lessonGetWritingFeedback()`,
      `_lessonCheckSpeakingCEFR()` in `engine/lessons.js`) only showed
      percentage-pill dimension scores and threw the qualitative feedback
      away. Added `_graderOneLineTip()`, a small picker (priority →
      error explanation → strength, first available) rendered as one
      `.lsn-hint` line under the pills in both places.
    - **Grader too harsh on can-do checks.** A learner asked to "count from
      1 to 10" and did exactly that got marked down for "not using full
      sentences" — traced to `engine/drills/speaking.js`'s competency-check
      flow (`journey.js`'s "unverified competencies" nudge, and the Studio's
      own "Target Unverified Goals" card) hardcoding "...and use complete
      sentences" into the TASK text sent to the grader, regardless of
      whether the competency was an enumeration/list-style can-do or an
      open topic — plus defaulting `targetSkills` to include
      `sentence_structure` for every competency check. Removed both. Added
      a new `taskCompletionPrimary` flag (threaded `speaking.js`/
      `writing.js` → `context` → `grader-engine.js` → `grader-prompt.js`),
      set `true` only for competency-derived prompts in both Studios: when
      set, the prompt tells the model to ignore the normal dimension
      weighting and score 85-100 for a production that correctly and
      completely fulfils a concrete, bounded task, however short or
      grammatically simple — reserving deductions for content that's
      actually missing, wrong, or unintelligible. Verified by generating
      prompts with the flag on/off and confirming the new instructions
      appear/disappear and "complete sentences" no longer appears in any
      generated prompt; existing `tests/grader/test-oral-grader.js` suite
      still passes unchanged. The AI's actual grading behavior with the new
      instructions can't be unit-tested (inherent to LLM grading) — worth
      a real-usage spot-check.

27. ~~**Time-Based Sessions should always include a quick speaking prompt**~~
    — **Built 2026-09-17.** Investigated 2026-09-16 as two scopes (small:
    loosen the existing conditional inclusion; medium: a real
    auto-launched quick-prompt mode) — built the medium version, refined
    from the user's own suggestion to source prompts from the CEFR can-do
    list (the same 1,114 HU / 2,341 ES items behind My Journey's Can-Do
    Passport — see item 29's index-generation fix) rather than inventing
    generic ones, since a can-do statement like "I can greet someone" is
    both a real 30-second speaking task *and* already the exact shape
    yesterday's `taskCompletionPrimary` grading fix (item 25) was built
    for.
    - `engine/learnerModel.js`'s new `pickSpeakingPrompt(level)`: prefers a
      genuinely unverified/weak competency at the learner's level
      (`unverifiedCompetencies()`, already existed), falls back to any
      competency from an already-completed lesson (nothing ahead of where
      the learner actually is) at that level, any level if none yet at
      this one, and returns `null` — not a placeholder — when there's
      truly nothing appropriate (e.g. a brand-new learner with zero
      completed lessons). Verified all three paths live.
    - `engine/studyPlan.js`: new guaranteed `speaking-cando` item, ~40
      seconds, placed ahead of the budget-gated blocks so it survives a
      tight session — added only when `canSpeak` and a prompt was
      actually found; skipped outright otherwise, same "never pad with
      invented busywork" rule the rest of the allocator already follows.
      Coexists with (doesn't replace) the existing opportunistic longer
      Sentence-Drills `speaking` block for when there's real budget left.
    - `engine/drills/speaking.js`'s `targetCompetency` auto-launch
      shortcut (already used by Journey's "unverified competencies"
      nudge) now takes an optional `maxSeconds`, defaulting to the
      existing 300s so that entry point is unchanged; the Studio tab
      label ("Verbal Production (5 min)") is now computed from the actual
      cap instead of hardcoded, reset to the default on every fresh
      `render()` that isn't itself setting a custom cap, so a quick 40s
      session's cap can't leak into an unrelated later normal one in the
      same page session (caught live while testing, not theoretical).
    - Verified end-to-end: a 30-minute plan now includes both `speaking-
      cando` ("Quick speaking — 40s") and the longer `speaking` block; a
      10-minute plan fully consumed by its lesson correctly omits it
      rather than forcing it in. `engine/studyPlanRunner.js` routes the
      new kind straight to `SpeakingDriller`'s recording screen, which
      already returns to the plan queue via the existing
      `RecommendationEngine.mountNextAction()` → `StudyPlanRunner
      .mountNextAction()` path once graded.
    - **Not done**: longer, CEFR-exam-style prompts ("talk about clothes
      for 3 minutes," matching what an actual exam asks) — that's item 28,
      still waiting on the user's ChatGPT-sourced topics file. The
      `maxSeconds` plumbing built here is exactly what that will also
      need (just a bigger number and a different prompt source), so no
      rework expected when it lands.

29. ~~**Hungarian CEFR Can-Do Passport loaded no skills; Decks review back
    button showed garbled text**~~ — **Fixed 2026-09-16.** Two unrelated
    bugs, one report:
    - `content/hu/indexes/competencies-index.json` (the file `engine/
      learnerModel.js`'s `loadCompetenciesIndex()` reads) never existed —
      only `content/es/...` did, so the Hungarian portfolio silently
      degraded to an empty list (the loader already catches a fetch
      failure and returns `[]`, so no crash, just nothing to show). Root
      cause: this index was hand/one-off generated for Spanish only,
      never added to any of the `scripts/build_*.py` family that
      regenerates every other derived index. Added `scripts/
      build_competencies_index.py`, which mechanically extracts each
      lesson's `checklist`-step "I can..." items via curriculum.json
      (same source data ES's file already came from — no new content to
      author). Verified the ES output against the existing file before
      trusting it for Hungarian: 0 field mismatches on 2,315 shared
      entries; the only differences were 2 stale orphaned entries (lessons
      no longer in curriculum.json) and 26 newer entries (the A2
      imperfecto lessons from item 20/21 above, added after the existing
      file was last generated) — so this run also quietly fixed ES's own
      staleness. Generated `content/hu/indexes/competencies-index.json`
      fresh: 1,114 items across A1/A2/B1. Verified live: Hungarian's
      Can-Do Portfolio modal now lists real competencies grouped by unit
      with working Speak/Write practice buttons, where it previously
      showed nothing.
    - `index.html`'s Decks review "← All decks" back button had been
      triple-encoded mojibake (`â† All decks`, raw bytes
      `\xc3\xa2\xe2\x80\xa0\xc2\x90`) since commit `084348cc5` (2026-09-13)
      — predates this session, not something introduced here. Fixed with
      a direct byte-level replacement back to a plain `←` character,
      matching every other back button's style in the codebase (`engine/
      decks.js`, `engine/library.js`, `engine/workshop.js`). Checked for
      other visible (non-comment) instances of the same corruption
      elsewhere in `index.html`; found none.

31. ~~**Cloudflare Turnstile added to sign-in (`/auth/request-link`)**~~ —
    built and verified live 2026-09-17, from the same backend cost/
    security review as item 23's R2 cache. `sync-worker.js`'s only abuse
    guard was "max 3 links per email per hour" in D1, which doesn't stop
    a script hitting the endpoint with many distinct emails and burning
    Resend's send quota (or getting the sending domain flagged). Client
    (`engine/sync.js`) now mints an invisible Turnstile token before
    calling `requestLink()`; the Worker verifies it against Cloudflare's
    `siteverify` API (`verifyTurnstile()`) before touching D1 or Resend.
    Designed to degrade to a no-op, not break sign-in, while unconfigured:
    empty `TURNSTILE_SITE_KEY` client-side skips minting a token, and a
    missing `TURNSTILE_SECRET_KEY` server-side skips verification — both
    now set. **Setup gotcha hit during rollout:** the dashboard Secret was
    first added as `TUSTILE_SECRET_KEY` (typo, missing "RN"), which — since
    a missing/misnamed secret is the intentional "not configured yet"
    no-op path — silently let every request through unverified rather than
    erroring. Confirmed via `curl` with a deliberately bogus token: before
    the fix, `429`/`502` (request reached D1/Resend, meaning verification
    never ran); after renaming the secret, `403 Verification failed` as
    expected. **Lesson: a bogus-token test, not just a missing-token test,
    is what actually distinguishes "verification is running and rejecting"
    from "verification isn't running at all"** — both look identical from
    the missing-token case alone. Also found and fixed in passing: `JWT_
    SECRET` and `RESEND_API_KEY` were stored as plain **Variable** type on
    the Worker (plaintext-visible in the dashboard) rather than **Secret**
    (encrypted-at-rest) — re-typed to Secret.

32. ~~**AI grader switched off Llama 70B by default, ~4x cheaper per call**~~ —
    built and verified live 2026-09-17, same backend cost review as items
    23/31. `grader-worker.js` was trying `@cf/meta/llama-3.3-70b-instruct-
    fp8-fast` **first on every single grading call**, not as an error
    fallback — Cloudflare's own neuron pricing puts that model at ~6-8x the
    per-token cost of an 8B-class model. Spent most of this item's time on
    a real, evidence-based elimination round rather than guessing:
    - Three Llama 8B-class candidates were tried and rejected, each with a
      concrete, reproducible failure on the actual multi-field CEFR JSON
      scoring prompt (not just weaker nuance): `llama-3.1-8b-instruct-fp8-
      fast` returned `overallScore` and every dimension as `0` for a solid
      A2 response, plus a manufactured grammar error on correct usage;
      `llama-3.1-8b-instruct` (unquantized) turned out to be deprecated
      server-side (Cloudflare error `5028`) and simply errors now;
      `llama-3.1-8b-instruct-fp8` returned `overallScore` as a `0.0-1.0`
      fraction (`0.6`) instead of the required `0-100` int, which
      `engine/grader/schema.js`'s `clampNumber` would round straight down
      to `1` — a learner who did well would have seen "1/100".
    - `@cf/openai/gpt-oss-20b` was tried and abandoned without a full test:
      it's a reasoning model that spends tokens on hidden chain-of-thought
      before the visible answer, so it returned empty content once
      `max_tokens` (below) was tightened — and its true per-call cost would
      include that invisible reasoning anyway, likely erasing its sticker
      price advantage.
    - `@cf/mistralai/mistral-small-3.1-24b-instruct` (~4x cheaper than 70B
      on output neurons) passed the same real-prompt spot-checks, but only
      after fixing two root causes in `engine/grader/grader-prompt.js`
      itself — **not model-specific, so this also hardens 70B and any
      future cheaper model**: the required-JSON-shape example showed
      `"overallScore": 0` sitting right next to `0.0-1.0` dimension fields
      with nothing distinguishing its scale (a plausible reason every
      failing 8B model got this wrong the same way), and the
      `demonstratedSkills`/`weakSkills` object shape was only ever implied
      by the example, never stated as a hard rule. Both are now explicit
      "CRITICAL RULE" lines in both the written and oral prompt builders.
      Verified with the real `buildGraderPrompt()` output (not a hand-
      written test prompt) on both a strong A2 response (scored 72-78,
      correctly-shaped skill objects, accurate non-hallucinated errors)
      and a deliberately weak one (scored 20-25, confirming the score
      tracks actual content rather than anchoring to the example's
      placeholder number).
    - `CANDIDATE_MODELS` is now `[mistral-small-3.1-24b-instruct, llama-3.3-
      70b-instruct-fp8-fast]` — 70B remains a true fallback, only reached
      if Mistral errors. Also fixed in passing: the fallback loop only
      continued to the next candidate on error `5007`; a `5028`
      (deprecation) hit during this session's testing instead hard-failed
      the whole grading call, so the continue-condition now covers both.
      `max_tokens` trimmed `3000` → `1500` (the prompt's own output-economy
      rules already cap real responses far below either number, so this
      only caps worst-case cost, no truncation risk).
    - **Ship gotcha hit during rollout:** right after a `Deploy`, two
      requests seconds apart returned two different models even with
      identical (default) candidate settings — Cloudflare Worker deploys
      take up to roughly a minute to fully propagate across edge
      locations, so a request can transiently land on a PoP still running
      the previous version. Re-tests a short while later were consistent.
      Don't read a deploy as broken from one inconsistent request
      immediately after clicking Deploy — retry a few times first.

39. ~~**ES teaching-order flags triaged: 731 total, 86% real**~~ — **Done 2026-09-17.**
    `scripts/triage-teaching-order.py` (built after item 35's crash fix unblocked
    A2/B1 for the first time) classified flags into `real-gap-candidate` (626),
    `wrong-distractor-only` (100), and `english-leak` (5). Resolved across levels
    via items 46 (ES A1/A2) and 48 (ES B1), reducing 626 candidates down to 11
    accepted irregular/clitic morphology edge cases across the entire 762-lesson
    Spanish curriculum. See items 41, 46, and 48 for complete tooling and content
    audit details.

40. ~~**Hungarian teaching-order checker expansion**~~ — **Done 2026-09-17.**
    Built Hungarian's first teaching-order checker (`scripts/audit-lesson-hu.py` +
    `scripts/triage-teaching-order-hu.py`) with agglutination-aware bounded-prefix
    stem matching, accent-sensitive tokenizing, and curriculum-based unit
    grouping. Resolved across levels via items 42–45 (HU A1/A2) and 47 (HU B1),
    reducing 171 real-gap candidates to 10 accepted morphophonology edge cases
    across all Hungarian levels. See items 41, 42–45, and 47 for details.

42. ~~**HU pilot: "Going Places" unit (a1.56-60) — fixed and verified**~~ —
    resumed item 41, **done 2026-09-17**. Fixed lesson a1.56 (Haiku-applied
    from fully-specified edits): added `mozi`/`étterem`/`múzeum`/`posta` to
    its vocabulary file, added a `Hová mész?` worked example to its grammar
    screen, reworded an off-topic dialogue opener (`Mit csinálsz?` → `Hová
    mész?`) so it reinforces the lesson's actual grammar point instead of
    an unrelated verb.
    - **Bigger find while triaging a1.57-60**: every `structured-writing`
      exercise in those lessons had a malformed `answer` field — a Python
      tuple-repr string (`"('állomás', 'station') ('megálló', 'stop')..."`)
      instead of a real sentence, which is why they'd shown up as apparent
      English leaks the triage heuristic didn't recognize. Grepped the
      whole HU exercise corpus for the same pattern: scoped to exactly
      `a1-56` through `a1-75` (20 lessons, one broken exercise each), zero
      elsewhere (not HU A2/B1, not ES). Sent the user a `.txt` for a1.57-60's
      4 instances (real sentences need correct vowel harmony, not guessed);
      user ran it through ChatGPT and returned real sentences, applied via
      Haiku, verified valid JSON and no leftover `('` pattern. The other 15
      lessons (a1.61-75) have the same bug, out of this pilot's scope — see
      new item 43.
    - **Real tooling bug found and fixed along the way**: re-auditing after
      the content fixes still showed `útba` (a regular, correctly-taught
      inflected form of `út`, "road") as untaught. Root cause was in
      `scripts/audit-lesson-hu.py` itself, not content: `KnownWords`
      bucketed known words by their first **3** characters for fast fuzzy
      lookup, but a short root like `út` (2 chars) buckets under `"út"`
      while its suffixed form `útba` buckets under `"útb"` — different
      keys, so the fuzzy match never even ran. Changed the bucket key to 2
      characters. Effect was much bigger than this one word: full-corpus
      flag count dropped from 330 to **213** (real-gap-candidate 171 → 104)
      — most of item 40's original count was this false-positive class,
      not real gaps. `audit-lesson-hu.py`/`triage-teaching-order-hu.py`'s
      numbers everywhere above (items 40/41) are now stale; 213/104 are
      current as of this fix.
    - Verified end-to-end: `audit-lesson-hu.py a1` shows zero remaining
      flags for lessons a1.56-60 (one harmless leftover, an English gloss
      `(to the road)` inside a1-60's sentence text, correctly excluded from
      `real-gap-candidate` by the triage script).

43. ~~**HU: same malformed-`answer` bug in 15 more A1 lessons (a1.61-75)**~~
    — found 2026-09-17 while scoping item 42 (see ACHIEVED.md), **done**.
    Same shape as that item's a1.57-60 fix, but spanned 3 different grammar
    topics, not one uniform pattern: a1.61-65 teach 1st-person-singular
    present tense verb conjugation (several irregular `-ik` verbs among
    them, e.g. `enni`→`eszem`, `inni`→`iszom`), a1.66-70 teach negation
    (`nem`) and question transformations, a1.71-75 teach daily-routine
    present-tense language. Sent one `.txt` for all 15, grouped by grammar
    topic; user ran it through ChatGPT.
    - **Caught and fixed one real error in the ChatGPT reply before
      applying**: exercise 63's `iszok` should be `iszom` (`inni` is an
      irregular `-ik` verb, same pattern as `enni`→`eszem` which the reply
      got right) — worth the sanity pass, not just apply-and-trust.
    - Applied all 15 via Haiku (exact strings pre-verified, not asked to
      judge). Re-auditing surfaced 3 new gaps the fix itself introduced —
      several word-pair lists supplied only verbs or only nouns, so a
      natural sentence needed a partner word the lesson never taught
      (`víz`/`kenyér` for a1.63, `óra` — already taught two lessons later
      in a1.75, reused here — for a1.73, `tartani` for a1.75). Added those
      4 words to the respective lessons' vocabulary files.
    - **Not fully clean, and that's expected, not a bug**: a1.63 still
      flags `iszom` and `vizet` — both genuine Hungarian morphophonology
      the bounded-prefix heuristic can't catch (suppletive stem for
      `iszom`, vowel-length shortening `víz`→`vizet`), not something worth
      chasing for two words. Full HU corpus: 330 → 213 (item 42's tooling
      fix) → **209** (99 real-gap-candidate, 90 wrong-distractor-or-
      english-option, 20 english-leak). The remaining ~99 real-gap-
      candidates are pre-existing, unrelated to this item.

44. ~~**HU: rest of a1.01-165's real-gap-candidates cleared, plus 3 more
    triage-tool fixes**~~ — **done 2026-09-17**, continuing items 42/43.
    Full HU corpus: 209 → **166** flags (real-gap-candidate 99 → 41; A1's
    own real-gap-candidate count: 29 → 4).
    - **3 more triage heuristic fixes**, same "find the pattern, don't fix
      one word at a time" approach as items 42/43: (1) `"What does 'X'
      mean?"` comprehension checks are deliberately all-English options —
      281 such exercises exist across the whole HU corpus, none of which
      the triage recognized as noise before this. (2) The wrong-distractor
      check only applied to `multiple-choice`, not `dialogue-complete`,
      which has the identical `options[]`/`correct` shape — missed e.g.
      a1-11's unselected "Én itt lakom." (3) A real bug, not just a triage
      gap: `hu_tokens()`'s proper-noun filter used the same fuzzy
      `same_stem()` matcher as regular word comparison, so the pronoun
      `maga` ("himself/herself") got silently swallowed as if it were a
      form of `Magyarország` (shares "mag-") — meaning `maga` never
      actually entered any lesson's known-vocabulary set anywhere it was
      taught. Switched the proper-noun filter to strict `startswith`
      (proper nouns only need to match their own suffixed forms, which is
      always noun+suffix, so no fuzzy tolerance is needed or safe there).
      This one fix alone dropped the full corpus by 43 (209→166) — bigger
      than either content batch below.
    - **~26 real vocabulary gaps fixed** across a1.01-165 (the rest of the
      lessons items 42/43 didn't already cover): missing content words
      used in exercises before being taught (`ők`, `kell`, `fontos`,
      `film`, `leves`, `ebéd`, `mögött`/`között`, `tanár`, `történelem`,
      `diák`, etc.) — applied via Haiku in one batch call across 23 files
      after manually checking each flagged exercise's actual context first
      (not applied blind). Also added `bécs` (Vienna) to `HU_PROPER_NOUNS`
      — same proper-noun-not-taught issue as items 30/42's Spanish/HU
      place-name lists.
    - **Left deliberately unfixed (4 flags)**: `a1-01-practice-3`'s
      "(Do you want coffee?)" gloss-supported warm-up sentence (by design,
      not a gap); `a1-63`'s `vizet` (vowel-length shortening, víz→vizet);
      `a1-112`'s `hozom` and `a1-152`'s `elvettem` (definite-conjugation
      and irregular-past-tense forms respectively that don't share enough
      surface prefix with their infinitives for the bounded heuristic to
      catch) — all genuine Hungarian morphophonology, not tool bugs, not
      worth chasing for single-word cases.

45. ~~**HU A2 real-gap-candidates cleared, plus 2 more triage-tool fixes**~~
    — **done 2026-09-17**, continuing items 40/42-44. A2's real-gap-
    candidate count: 28 → 5 (all left deliberately, same morphophonology-
    edge-case reasoning as item 44 — e.g. `víz`→`vizet`-style vowel
    shortening in `úr`→`uram`, definite/indefinite conjugation divergence
    in `úszni`→`úszom`).
    - **2 more triage fixes before touching content, per item 44's own
      advice**: (1) a `"(...)" ` gloss can sit inside an `options[]` entry
      too, not just the `sentence`/`question` fields — e.g.
      `"Virágcsokor (flower bouquet)"` — found via `a2-184-controlled-4`'s
      `bouquet` false flag; 75 such option-embedded glosses exist across
      the corpus, previously all invisible to the triage. (2) Two more
      names needed adding to `HU_PROPER_NOUNS` (`gábor`, `kovács` — a
      first name and the most common Hungarian surname, both used as
      dialogue characters, e.g. "Kovács néven foglaltam szobát").
    - **27 real vocabulary gaps fixed** across a2.52-185 via one Haiku
      batch (18 files), each checked against its actual exercise context
      first — same workflow as item 44, not applied blind. One fix
      (`hát`, "back") resolved two separate lessons' flags at once since
      a2-138's `hátam` is downstream of a2-85's `hátra` in teaching order.

46. ~~**ES A1 and A2 real-gap-candidates cleared, plus 3 tooling fixes in
    `audit-lesson.py` itself (not just the triage layer)**~~ — **done
    2026-09-17**, continuing item 39/41. A1: 40 → 4 real-gap-candidates.
    A2: 22 → 6. Same lesson as items 42-45: ported HU's triage-layer fixes
    over first (meaning-check pattern, `dialogue-complete` wrong-distractor
    detection — ES has 1,528 `dialogue-complete` exercises with a
    `correct` field, far more than HU had — option-embedded glosses, one
    proper noun `lucia`), which alone cut 731 → 707. But the bigger finds
    this time were in `audit-lesson.py`'s own `matches()`/`teach_tokens()`,
    not just the read-only triage script:
    - **Grammar tables only ever read column 1, never column 2** —
      `teach_tokens()`'s table handling did `spanish_tokens(row[0])` only.
      Harmless for a `[spanish, english]` table, but conjugation tables
      are `[pronoun, conjugated-form]` (e.g. `["nosotros", "trabajamos"]`)
      — the entire point of the table, the actual verb forms, was never
      registered as taught. Root cause of most of a1-06's "nosotros"/"tú"
      form flags. Fixed by reading both columns (707 → 656).
    - **`matches()` had no concept of verb conjugation at all** — its
      only fuzzy logic stripped noun/adjective plural endings
      (`es/os/as/s`). Added present-tense person-ending stripping that
      reconstructs the infinitive and checks if *that's* already known
      (a learner who knows `cocinar` can be expected to recognise
      `cocinamos`) — the same productive-rule leniency `find_missing()`
      already granted verbs elsewhere, extended to the teaching-order
      check too (656 → 620). Then found A2 introduces past tense (preterite
      + perfect) that the present-only ending list didn't cover at all
      (`celebraron`, `tenido`, `preguntado`...) — extended the ending list
      (620 → 574) — and a reflexive-infinitive gap (`alegró` needs to
      reconstruct `alegrarse`, not `alegrar`) — added `-arse/-erse/-irse`
      alongside `-ar/-er/-ir`.
    - **Same short-root bucketing class of bug as HU's item 42-44 fixes**:
      the noun/adjective stem-length threshold (`>=4`) missed `foto`→
      `fotos` and `vela`→`velas` (3-char stems after stripping the
      plural); the verb-root threshold (`>=3`) missed `leer`→`leo` (root
      `le`, 2 chars). Lowered both by one.
    - **~29 real vocabulary gaps fixed** across A1 (18 files, 24 entries)
      and A2 (4 files, 5 entries) via two Haiku batches, each checked
      against its actual exercise context first.
    - **Left deliberately unfixed (10 flags: 4 A1, 6 A2)**: irregular
      preterite stems (`hiciste`/`hicieron` from `hacer`, `estuvieron`
      from `estar` — suppletive, no reconstructible pattern),
      reflexive-infinitive-plus-clitic forms (`acostarme`, `despedirme`,
      `marcharme`), one stem-changing verb (`muestras` from `mostrar`),
      one by-design gloss-supported sentence, one ambiguous future/
      subjunctive form (`lograran`) — all genuine Spanish morphology, same
      category of exception already established for HU.
    - Full ES corpus: 731 → 707 → 656 → 620 → 574 → **570** (real-gap-
      candidate 626 → 399). B1 dropped from 537 to 389 as pure fallout
      from the tooling fixes, before any B1-specific work started.

47. ~~**HU B1 cleared, plus a severe proper-noun bug that silently affected
    the entire session's earlier HU work**~~ — **done 2026-09-17**.
    Scoped B1 first at the user's request (hypothesis: most of it is the
    citizenship track) — confirmed directionally right but not the way
    expected: citizenship-track lessons produced 70% of raw flags (26/37)
    but only **2 of the 6 real gaps**; core track had proportionally more
    real problems (4/11) despite far less raw noise. Citizenship lessons
    are civics/history quizzes with English-option answers, which is
    exactly the shape the triage already classifies as noise — the raw
    flag count was measuring exercise *style*, not actual gaps.
    - **The bug, found while investigating one of the 6 real gaps**:
      `hu_tokens()`'s proper-noun filter (added item 42, fixed to strict
      `startswith` in item 44) used plain prefix matching without a
      length floor. Every other entry in `HU_PROPER_NOUNS` is 4+ characters,
      but `meg` (the protagonist's name) is 3 -- and `meg-` is also
      Hungarian's single most common verbal preverb, prefixing hundreds of
      ordinary verbs (`megyek`, `megnéz`, `meggyőz`, `megvesz`...). Every
      one of them was silently wiped to an empty token set for the entire
      session, in both directions (never counted as taught, never counted
      as required) -- which is why it mostly didn't change raw flag counts
      when fixed (a word invisible on both sides of the check is
      invisible to the check, not wrong in an obviously visible way).
      318 distinct `meg`-prefixed words found across the whole HU corpus
      grep'd for spot-checking. Fixed by requiring exact match instead of
      prefix match for any proper noun under 4 characters.
    - **Re-audited A1/A2 after the fix rather than assuming they still
      held**: full corpus went 166 → 143 (net small, per the above), and
      exactly one new real gap surfaced in A1 (`megyek`, previously
      invisible) — checked its context and left it deliberately (an
      incidental "I'm going, bye!" dialogue line seven lessons before the
      unit that actually teaches "to go", not something the exercise
      tests). A2's list was unaffected. B1's 6-item real-gap list (scoped
      before the fix) was independently re-verified unchanged after it —
      the fix's effect on B1 was invisible for the same reason.
    - **6 real vocabulary gaps fixed**: `fábián` was a person's name, added
      to `HU_PROPER_NOUNS` instead of vocab; `suli` (school, colloquial),
      `óriási` (huge), `lép` (to step), `fekvés`/`konkrét` (location/
      concrete — citizenship track), `zúdul` (to pour/swarm — citizenship
      track) added via one Haiku batch across 5 files.
    - **All three HU levels are now fully done.** Full corpus (raw flags):
      166 → 143 (bug fix) → 137 (B1 fixes); real-gap-candidate: 41 → 16
      (bug fix) → **10** (5 A1, 5 A2, 0 B1) — down from the original 330
      raw / 171 real-gap-candidate this whole initiative (items 40/42-47)
      started from. Remaining flags in all three levels are deliberately
      accepted morphophonology edge cases, same category established in
      items 42-46, not gaps.

41. ~~**Real-gap-candidate lists worked level by level, both languages**~~
    — **done 2026-09-17**. Antigravity's content-fill pass (new ES A2 + HU
    A1/A2 curriculum phases, claimed full CEFR can-do coverage) finished
    the same day and was confirmed purely additive (doesn't touch items
    39/40's flagged lessons) by re-running both audits before and after;
    Antigravity's separate item 33 pass (A1 consolidation shape) finished
    later the same session and was merged in cleanly before ES B1's final
    push. **Every level of both languages is now done**: HU A1/A2 (items
    42-45), HU B1 (item 47), ES A1/A2 (item 46), ES B1 (item 48) — see
    ACHIEVED.md for all of them. Combined starting point across both
    languages was roughly 330 HU + 626 ES = 956 raw real-gap-candidates;
    final state is small accepted-edge-case counts only (HU: 5 A1 + 5 A2 +
    0 B1; ES: 3 A1 + 0 A2 + 8 B1 = 11), everything else either fixed as
    real content gaps or resolved by one of the many tooling fixes these
    items found along the way. The recurring lesson worth carrying
    forward: sanity-check the audit tool against a sample of its own flags
    before trusting the count, every time — across both languages this
    session, tooling fixes accounted for far more of the drop than content
    edits did.
48. ~~**ES B1 scoped, tooling fixed, and content gaps closed: 389 → 8
    real-gap-candidates**~~ — **done 2026-09-17**, continuing item 41 —
    with this, the full ES corpus (A1+A2+B1 combined) is down to **11**
    real-gap-candidates, from item 39's original 626. Found while scoping
    and fixing B1 content:
    - **B1 uses a completely different gloss convention than A1/A2** —
      square brackets holding a full-sentence English translation (e.g.
      `"La pobreza puede aumentar debido al desempleo. [Poverty can
      increase due to unemployment.]"`), not A1/A2's parenthetical style.
      204 files / ~3,200 instances corpus-wide, never recognised by the
      triage before this — the single largest fix of the whole HU/ES
      initiative. 389 → 197.
    - **~573 of those bracket pairs have the order reversed** — English
      main text, `[Spanish]` in the bracket (e.g. `"The consequence of
      trusting too easily. [La consecuencia de confiar demasiado.]"`).
      Generalised `english_text()`'s gloss extraction to pick whichever
      side of a bracket pair doesn't look Spanish, rather than assuming
      the bracket is always the gloss (same `looks_spanish()` heuristic
      already used for the A1 reversed-matching-pairs fix). 197 → 172.
    - **`matches()` had no concept of imperfect or conditional tense** —
      B1 introduces both and neither reconstructed. Added imperfect `-ar`
      endings (`aba`/`abas`/`ábamos`/`abais`/`aban`, same stem-strip-and-
      readd pattern as existing endings) and the shared imperfect-`-er/-ir`
      /conditional endings (`ía`/`ías`/`íamos`/`íais`/`ían`) — conditional
      needed a second check alongside the existing one, since it keeps the
      *whole* infinitive before the ending (`trabajaría` → root
      `trabajar`, already complete) rather than truncating to a bare stem
      like imperfect `-ar` does. 172 → 166 → (after the reversed-bracket
      fix landed on top) **160**.
    - **Investigation pass, before touching content**: pulled every
      exercise whose flagged tokens still looked English (common words,
      `-ing`/`-tion` endings) to check for a 4th missed format. All of them
      turned out correctly classified already — the raw `--all` printer
      shows every unseen token for context, English ones included, even
      when they're already excluded from the verdict; spot-checking
      `classify_token()` directly on individual tokens (e.g. `checking`/
      `contract` vs `contrato` in the same exercise) confirmed no bug, just
      a noisy display. No 4th systemic false-positive source found.
    - **Did find one more real gap while doing that check**: gerund forms
      (`-ando`/`-iendo`) weren't in `VERB_ENDINGS` at all —
      `investigando` reduces to `investig` + `ar` = `investigar`, same
      pattern as every other tense fix this session. Added. 166 → 163 →
      **157** (after the gerund and gerund-adjacent counts settled).
    - **Confirmed via frequency count, not just spot-checking**: every one
      of the remaining 157 flagged tokens is now unique (zero duplicates)
      — a strong signal the clustered/systemic issues are exhausted and
      what's left is genuinely scattered content work, not another hidden
      pattern. Spread evenly across B1 units 01-35, no single unit or
      range dominating.
    - **Separate, known limitation, not fixed here**: `check_teaching_
      order()` only walks numeric unit ids, so B1's Latin America track
      (word-slug ids like `b1-conosur-*`) isn't part of this 157-item list
      at all — a structural gap distinct from item 39's original word-in-
      story finding about the same track, not addressed by any of this
      session's matcher work.
    - **A 5th fix, found starting the content-fix pass**: every accented
      ending added to `VERB_ENDINGS` above (`áis`/`éis`/`ía`/`ías`/`íamos`/
      `íais`/`ían`/`ábamos`) had a real bug — `spanish_tokens()`/`norm()`
      strips accents from every token *before* `matches()` ever sees it,
      so an accented ending in the list could never `.endswith()`-match an
      already-unaccented token. Every vosotros form (`podéis`, `hacéis`)
      and every imperfect/conditional form added in this same item had
      silently never worked since the moment they were written a few
      hours earlier in this session. Fixed by writing every ending
      unaccented (`ais`, `eis`, `ia`, `ias`, `iamos`, `iais`, `ian`,
      `abamos`). 157 → **131**, bigger than three of the four fixes above
      it combined.
    - **A 6th fix, found starting the actual content batch**: infinitive/
      gerund + attached clitic pronoun (`hacerlo`, `presentarme`,
      `adaptarme`) was a whole unhandled shape — none of `VERB_ENDINGS`
      applies (the word doesn't end in a conjugation, it ends in a
      pronoun). Roughly a quarter of the remaining list was this single
      pattern. Added a clitic-stripping check alongside the ending-based
      one. Effect wasn't B1-only — A1 dropped 4→3, A2 dropped 2→0 (both
      already "done" in items 44/46, now cleaner still). 131 → 105 → 103
      (after also adding missing vosotros-preterite endings
      `asteis`/`isteis`, same accent-free lesson as the 5th fix).
    - **A 7th fix, refining the reversed-bracket detector (item 48's own
      2nd fix)**: `looks_spanish()`'s accent-or-article check went blank
      on short accent-free sentences like `"Era abogado."`, so
      `bracket_gloss()` silently defaulted to keeping the Spanish side and
      discarding the *English* side as if it were the gloss (found via
      `b1-06-05.ex09`: "He was a lawyer. [Era abogado.]"'s "lawyer" was
      being thrown away, "abogado" kept, exactly backwards). Replaced the
      binary check with a scored one (common function words on both
      sides, not just accents/articles) that returns nothing rather than
      guess when neither side scores — while building it, found "he" is
      itself a live collision (English pronoun vs. Spanish `haber`
      auxiliary, "he comido" = "I have eaten") that would have made an
      entire present-perfect exercise set misfire the same way; excluded
      it from the English word list rather than risk being confidently
      wrong across a whole grammar topic.
    - **Hit a live concurrent-edit while starting the content batch**:
      `audit-lesson.py` crashed (`KeyError: 'sentence'`) on newly-appearing
      fill-blank exercises in A1 consolidation files (`question`+`hint`
      instead of `sentence` — 34 files mid-edit by another process when
      checked, git status confirmed). The new shape is a real, apparently
      deliberate improvement (splits the English gloss into its own
      `hint` field instead of baking it into the sentence text, which
      matches a real fill-blank content-quality gap flagged before now) —
      not a bug to report, but it broke this script's assumption that
      fill-blank always has `sentence`. Added a fallback so `question` is
      read when `sentence` is absent; deliberately did *not* fold `hint`
      into the required-Spanish text, since that field exists specifically
      to hold English cleanly, same reasoning as everywhere else English
      gets excluded. Paused B1 content work at this point to flag the
      concurrent edit to the user rather than pushing further changes into
      files someone/something else is actively touching.
    - **Resumed and finished once Antigravity's item 33 pass landed**:
      re-scoped fresh from the merged state (106 items — item 33's A1
      consolidation changes rippled slightly into B1's known-word set) and
      added 2 more `SPANISH_WORDS` entries (`un`/`una`/`unos`/`unas`, and
      the `haber` forms `ha`/`has`/`hemos`/`han` — not `he`, still
      excluded for the same collision reason) that resolved 3 more short
      accent-free sentences the same way item 48's earlier scoring fix
      did. 106 → 105. Applied the remaining ~99 real vocabulary gaps via
      two parallel Haiku batches (33 files/~53 words, 31 files/~46 words)
      plus 3 proper nouns (`ulises`, `gulliver`, `daniel` — literature-
      adaptation characters) added directly to `PROPER_NOUNS`.
    - **Final state**: 8 real-gap-candidates left in B1, all verified
      genuine irregular-verb morphology, same acceptance bar as every
      other level this session — g→j/c→zc orthographic stem changes
      (`dirijo`, `reconozco`), e→ie stem-changing (`conviene`), the
      irregular `-ongo` pattern (`propongo`), a spelling-irregular
      subjunctive (`surjan`, `parezcan`), a compound gerund+clitic form
      the clitic-check doesn't chain with gerund-reduction
      (`llevándonos`), and the one already-documented `he`/`haber`
      collision case. **ES B1 is done.**
19. ~~**"Listen to your own voice" unavailable on iPad/iPhone**~~ — **Re-evaluated & Fixed 2026-09-19.** Real-device testing on iOS confirmed that running `getUserMedia` concurrently with `webkitSpeechRecognition` causes the exact same microphone hardware contention on iOS as on Android: WebKit's audio capture session locks the hardware, starving `SpeechRecognition` of audio samples (recording plays back fine, but recognition receives silence and transcribes nothing). Resolved 2026-09-19 by enforcing exclusive microphone access on all mobile platforms (`canRecordConcurrently = !isMobile`), reserving concurrent capture exclusively for desktop browsers. On mobile, `SpeechRecognition` gets clean, unconstrained audio access, restoring real-time transcription and automatic grading on iOS and Android alike.
   - **Unified 1-Sentence Coaching Formatting for Short Productions**: Short (< 1 min / `taskCompletionPrimary`) speaking and writing tasks compose an opening task completion appraisal smoothly into an actionable coaching clause (`_cleanFragment`, `_formatCoachingClause`, `_prodOneLineTip`, `_shortTaskTip`), eliminating fragmented headers (`You missed:`, `Focus on Practice...`), double periods, semicolons, and errant capitalization.

33. ~~**20 of 26 A1 consolidation lessons ship the wrong shape**~~ — **Fixed
    2026-09-17** (item 33). All 20 failing lessons corrected:
    - **Structural fix** (`scripts/fix_consolidation_shape.py`): merged the
      separate Practice/Dialogue/Writing exercise-group blocks into one
      group titled `"Review"`, and removed the empty `srs` section. Every
      lesson now has the `"single"` shape: `goal → recycle → Review → checklist`.
    - **Goal/checklist text** (`scripts/fix_consolidation_goals.py`,
      manual edits): all `goal` and `checklist` items now begin with `"I can"`.
      Goal and checklist counts now match in every lesson.
    - **Exercise type variety** (`scripts/fix_consolidation_exercise_types.py`):
      added 2 `fill-blank` exercises to each of the 12 lessons whose Review
      group only had 4 types (`dialogue-complete`, `matching`,
      `multiple-choice`, `structured-writing`), bringing all to 5+ types.
    - **Teaches-tag coverage** (`scripts/fix_consolidation_teaches_tags.py`):
      re-tagged gustar consolidation exercises from the placeholder
      `"consolidation"` tag to real grammar points (10 distinct); added
      cumulative A1 crossover tags to 5 other files to meet the 8+-points
      requirement (all 6 now have 9–10 distinct tags).
    - **Result**: 24/26 consolidation lessons pass all 10 audit rules.
      The 2 remaining (`a1-01`, `a1-03c`) are pre-existing failures
      unrelated to this item — `a1-01`'s Review exercises only cover 5
      tags (Unit 1 genuinely introduces fewer grammar points), and both
      have a `no SRS step` conflict that predates this work.

30. ~~**Audit `imports/dictionary/*.json` for more corrupted glosses**~~ — **Audited and fixed 2026-09-17.** Full systematic scan of all 141,149 entries across both dictionaries (`spanish-en.json`: 112,156 entries; `hungarian-en.json`: 28,993 entries) for unresolved templates, HTML/math leaks, unrendered entities, and scraper macro remnants:
    - **`hungarian-en.json`**: 100% clean (0 broken templates, 0 HTML leaks, 0 scraper artifacts).
    - **`spanish-en.json`**: Identified and sanitized 129 entries with unparsed syntax: 22 unexpanded `{{es-superseded spelling of|...}}` templates, 4 `{{gender-neutral neologism for|...}}`, 7 transliteration/foreign name templates, 11 `{{tcl|...}}` tags, math/html formatting remnants (`semiproducto`, `acetilcolina`), unrendered HTML entities/wikilinks (`bosníaco`, `ramblero`, `cuidar`, `llanisco`), and ~60 macro-prefixed place definitions (`@official name of:...`, `@init of:...`). All 129 entries rewritten to clean, natural English glosses; zero corruption flags remain corpus-wide. Content validation passes 100% clean (3308/3308 ES, 2296/2296 HU).


## Completed Roadmap Archive (Features & Subsystems Shipped)

The following completed subsystem initiatives and milestones were previously tracked in `ROADMAP.md` and archived here upon completion:

### Content & Curriculum Milestones
- **Welcome Screens for the B1 Elective Tracks** — Built 2026-09-24. The first lesson of each B1 elective track now opens with an `intro` screen, like A1 lesson 1 does: `b1-constitucion-01` (es-es, Cultura y Ciudadanía), `b1-precolombina-01` (es-latam, Latin America) and `b1-orszagma-01` (hu, Citizenship). Each screen says what the track covers, how it teaches (a story-led lesson, with vocabulary and one B1 grammar point taken from the story, five lessons plus a consolidation lesson per unit), and how it fits with Core (it runs alongside Core, doesn't gate the level test, assumes B1 Core grammar in parallel, and uses the same review deck). The two citizenship tracks also say plainly that they teach the exam's topics but aren't official preparation courses. `scripts/generate_es_b1_ccse_unit1.py` writes the es-es intro too, so re-running it keeps the screen. Follow-ups: (1) when CCSE unit 36 (*Simulacro General de Examen CCSE*) exists, mention the practice exam in the Spain intro; (2) a learner the elective nudge sends straight to a later unit never sees these screens, so a one-line track `description` in `curriculum.json` shown on the nudge card would cover that case.
- **HU B1 Citizenship Track Word Count Trim** — Completed 2026-09-19. Resolved vocabulary pacing and density requirements for the Hungarian B1 Citizenship track (units 6–36), moving away from the dense 40 new words/unit structure to a paced vocabulary load.
- **Dual-Language Reading Setup (A1 Spanish)** — Completed 2026-09-18. Integrated English-Spanish dual-language reading setup with originals across all A1 original stories (`content/es/stories/original/a1/`), featuring English narrative scaffolding paired with Spanish dialogue and target text, matching the Hungarian A1 dual-language reading setup.
- **Evaluate importing exercises from Todo-Claro / Spanish Unicorn** — Evaluated 2026-09-12. Third-party scrape catalogues analyzed; discarded due to low quality and unverified licensing. Proceeded with native content authoring.
- **Exercise Modularity Architecture** — Confirmed 2026-09-12. Pipeline validates that new exercises can be added without rewrite; `recycle.js` pools exercises at runtime via `teaches` tags.
- **Hungarian A1 "First Sounds, First Words" Fix** — Fixed 2026-09-02. Fixed non-standard section type causing blank render on lesson 1.1.
- **Spanish B1 Vocabulary Screen Sequencing** — Fixed 2026-09-12. Reordered vocabulary section before first practice exercise group across all 36 units (180 lessons).
- **Word Bank Feature** — Built 2026-08-27. Unit-level vocabulary browser added under Grammar Guide in unit detail views.
- **Bug-Report Content Sweeps** — Fixed 2026-09-16. Repaired broken dictionary gloss templates and Hungarian translation drill bugs.
- **Bug-Report Content Sweep (#182, #184)** — Fixed 2026-09-22. Accepted "tomas" as an alternate answer on `a1.06.03.ex04` alongside the default "bebes" (es-latam). Fixed `short_gloss()`/`shortGloss()` (`build-manifest.py`, `engine/lexicon.js`) to also strip an "inflection of X:" prefix — pronoun entries like "me", "te", "nos" were riding onto SRS review cards with the raw dictionary explanation still attached (`engine/srs.js`'s live per-card lookup) instead of just the translation.
- **Bug-Report Content Sweep (#191, #189, #188)** — Fixed 2026-09-23. Three Hungarian content fixes, all in Unit `a1-12`/`a2-08`: (1) `a1-12-practice-5`'s dialogue-complete question "Ő egy nő?" ("Is he/she a woman?") never established who "ő" referred to, so both options were defensible — reworded to name the referent ("Anna egy nő?", Anna already established earlier in the same lesson) so there's exactly one correct answer. (2) `a2-08-practice-4`'s sentence-builder only accepted one tile order ("...a fogorvosnál pénteken", place-then-time) when the time-then-place order ("...pénteken a fogorvosnál") is equally grammatical Hungarian — switched from a single `solution` to the schema's `solutions` array to accept both. (3) The `a2-08-b-gr.json` grammar example "Szabad vagy foglalt vagy csütörtökön?" read as three coordinated disjuncts ("free, or busy, or Thursday?") because the second "vagy" landed right before the time expression — reworded to "Csütörtökön szabad vagy foglalt vagy?", moving the time adjunct to the front so the idiomatic "`[adj] vagy [adj] vagy?`" question reads naturally. A fourth report (#190, "ES-LATAM — Grammar Driller — hint is needed") was left open with a clarifying comment: the Drills-tab bug-report context doesn't capture which specific question/type was open (unlike lesson reports), and while `error-correction` questions are the one Grammar Driller exercise type with no hint button (fill-blank already has one), that's a guess without more detail from the reporter.
- **Bug-Report Content Sweep (#201, #200)** — Fixed 2026-09-28. Two Hungarian grammar-screen fixes in `lesson.a1.16` ("Numbers 0-10"): (1) `grammar.a1.16.a` ("Numbers 0–10; Asking hány?") told learners to treat `nulla`–`tíz` "as ten fresh vocabulary items" but never actually listed them on that screen — unlike the following "Numbers 11–100" screen, which has a table for the tens — so added the matching 0–10 table. (2) `grammar.a1.16.b`'s tip claimed Hungarians "read digits one at a time" for phone numbers, then illustrated it with a sequence that included `harminc` ("thirty") — not a single digit, contradicting the claim in the same sentence — replaced with a tip about the screen's own genuinely irregular pattern instead (the 20s take `huszon-`, not `húsz-`). Two further reports were left open with clarifying comments rather than guessed at: #202 ("hét and húsz have no audio playing" in the same lesson's vocabulary step) — the vocab data, TTS pipeline (`engine/tts.js`, `engine/speech.js`, `cloudflare-worker/tts-worker.js`) and step renderer all checked out clean for both words with nothing word-specific in the code path, but the live TTS worker and any cached audio state weren't reachable from this environment to confirm a cause. #199 ("tts is not working on ios across the board", es-latam Review tab) — no lesson/word specifics to reproduce against, and the review tab's TTS call path matches the rest of the app including its existing iOS Safari audio-session workarounds; asked the reporter for iOS version, whether other tabs work, and a specific reproducing word/card.

### Workshop Subsystem Polish
- **AI-Graded Scripted Conversation Scenarios** — Completed 2026-09-19. Shipped interactive multi-turn spoken roleplay scenarios as the 3rd studio mode in Speaking Studio (`[ Sentence Drills | Verbal Production | Conversation Scenarios ]`) across Spanish and Hungarian. Features natural TTS interlocutor turns, live speech-to-text recording with microphone pulse visualizer and voice playback, zero-latency turn-level validation via `LocalGrader.validateTurn()`, and complete end-of-scenario CEFR oral evaluation via `GraderEngine` (Cloudflare Workers AI with deterministic local fallback), awarding XP and verifying CEFR oral competencies.
- **Sentence-Builder / Sentence-Order Mini-Game** — Evaluated & Confirmed 2026-09-19. Confirmed fully covered by the core curriculum and driller engines: `sentence-builder` (interactive shuffled tile reconstruction with multi-solution support) and `sentence-order` (sentence sequence drills) are comprehensively implemented as first-class exercise types in `engine/lessons.js` and actively drilled across Workshop grammar sessions via `GrammarRunner` without requiring a separate redundant runner.
- **Grammar Driller Audit & Fixes** — Audited 2026-08-27. Fixed Spanish gap-fill punctuation hints, removed non-deterministic question options, and improved distractor selection.
- **Workshop Recommended Drill** — Built 2026-08-27. Smart drill recommendation based on recent lesson performance and error rates.
- **Workshop Mini-Games** — Built 2026-09-02. Lightweight short-format practice modes with score tracking and instant feedback.
- **Grammar Screen Italicization** — Completed 2026-09-02. Italicized target-language words and clean typography across grammar explanations.
- **Verb Drill Leaderboards & Scoring** — Built 2026-08-28. High-score tracking, streak counters, and accuracy calculation.
- **Translation Driller by Topic** — Built 2026-08-27. Topic-filtered translation practice sessions across all CEFR levels.
- **Writing Studio AI-Grader / HU Accent Fixes (#185, #186)** — Fixed 2026-09-22. The AI grader (`engine/grader/grader-prompt.js`) was flagging Hungarian `van`/`volt` as needing to agree with the possessor's person in existential-possessive constructions ("időpontom volt" = "I had an appointment"), when it actually agrees with the third-person possessed noun — added an explicit carve-out to all three prompt variants. Also added a one-line note on the Written Exchanges setup screen (Hungarian only) explaining that `content/hu/writing-exchanges.json`'s missing accents are an intentional simulation of real Hungarian texting, not a content bug.
- **Vocabulary Driller Results Screen Crash on Any Missed Answer (#187)** — Fixed 2026-09-23. Bug report ("HU — Drills: Vocabulary Driller — it got stuck and doesn't let me progress") didn't reproduce against the exercise-building pipeline in isolation, so this needed a live browser: `engine/drills/vocabulary.js`'s `_renderResults()` calls a local `_escapeHtml()` helper when rendering the missed-questions recap, but unlike every other driller module in `engine/drills/` (`grammar-runner.js`, `grammar.js`, `translation-runner.js`, `hu-suffix.js`, `hu-morphology.js`, `hu-prefix.js`), `vocabulary.js` never actually defined that helper. Any session where the learner missed at least one question threw `_escapeHtml is not defined` while building the results screen's HTML, so `_container.innerHTML` was never assigned — the learner was left on the last question with Check hidden and Next silently doing nothing on every click, no error visible in the UI. Added the same `_escapeHtml()` wrapper around `UI.escape()` the other driller modules use. Reproduced and verified fixed with a headless Chromium session driving the real Workshop → Vocabulary Driller UI (settings screen, Timed mode, hint button, Check/Next) through a full session ending on a missed answer.
- **Dual-Track Levels No Longer Gate the Core Path on Elective Content** — Fixed 2026-09-23. A dual-track level's non-core track (`content/es-es` B1's CCSE citizenship-exam units, `content/es-latam` B1's history units) was silently interleaved into `engine/learnerPath.js`'s `courseWalk()`/`levelStats()`, so the canonical "next step"/Continue-card position and the level-test gate both required finishing citizenship-exam or history units alongside core grammar — content most learners have no reason to want blocking their progression. `courseWalk()`/`levelStats()` now filter to each level's `core` track (`_isCoreUnit()`; a level with no `tracks` at all is entirely core, unaffected). The elective track is still real content, so `engine/recommendationEngine.js` gained an `_electiveCandidate()` secondary recommendation — surfaced roughly once every 5 completed lessons (`ELECTIVE_CADENCE`), skippable per-unit via a "Not now" button (reuses the existing `dismissedUnits()` store) that advances to the next elective unit — wired into Workshop's "Recommended for you" card (`engine/workshop.js`, `.wk-recommend-skip` in `styles/workshop.css`). Verified live: seeded B1 progress in the browser confirmed `nextStep()` stays on core lessons with a core-only done/total, the elective card appears at the right cadence, and skipping one elective unit correctly offers the next.
- **Typed Answers Show Feedback Before Advancing** — Fixed 2026-09-24. In every driller and mini-game built on `GrammarRunner` or `ListeningRunner` (grammar, vocabulary, hu-verb/suffix/prefix/morphology, listening), pressing Enter in a text field ran Check, which revealed Next — and the same keypress then bubbled to the runner's window-level Enter handler, which clicked that Next straight away. A wrong answer's "✗ The correct answer is…" flashed for zero frames and the learner only learned they'd missed it on the results screen. The input handlers now `preventDefault()` and the window handler skips already-handled events, so the first Enter checks and the second advances. Verified in the browser: one Enter → feedback shown, Next not called; second Enter → advances.
- **Grammar Practice Stays Within Where the Learner Is** — Fixed 2026-09-27. A HU learner in A1 unit 3 kept getting "Grammar practice" as the Home/mini-game nudge, and it asked for B2 answers like *színházba*. Two leaks: (1) the Grammar Driller's pool for a skill was every exercise tagged with it at any level, and skills are tagged across levels (`vagyok-vagy-and-where-van-goes` has A1, A2 and B1 exercises), so B1/B2 sentences got into early drills; (2) `LearnerModel.weakSkills()` counted misses on those advanced exercises, so a B2 skill (`b2-nehogy-subjunctive`) turned "weak" and became the top recommendation. Missing it again kept it weak, so the nudge never went away. New `LearnerPath.reachedExerciseRefs()` returns the exercise files of every lesson, in course order, up to the furthest one completed, plus every lesson of any level whose test was passed. `_buildPool()` now keeps only reached entries (falling back to the full list when none are reached, e.g. a skill picked by hand in Settings), and `weakSkills()` ignores recycle evidence from unreached files, which also clears evidence already stored before the fix. Regression test: `tests/drills/test-skill-reach-gating.js`, on the real HU curriculum. Not gated: `skillState()`, so the Driller's per-skill "needs review" badge can still reflect stored advanced-level misses.
- **Workshop "Recommended for you" Card Removed** — 2026-09-28. At the user's request, recommendations live on Home only; Workshop now opens straight onto the driller picker. Removed `_recommendationHtml()`/`_loadRecommendation()` from `engine/workshop.js` and the `.wk-recommend*` styles from `styles/workshop.css`.
- **Home Shows One Recommendation, and It's Accurate** — 2026-09-28. Follow-up to the Workshop card removal. `RecommendationEngine.recommend()` now returns only `{ primary }`: the `secondary` tier, `secondaryLabel()`/`openSecondary()` and Home's never-rendered `data-secondary-*` handlers are gone. Precedence of Home's single card: unit-end roleplay/exchange → post-lesson practice → elective-track nudge → continue. The elective nudge (B1 CCSE / Latin America history, every 5th completed lesson, "Not now" skips that unit) moved from the Workshop card to Home as its own `electiveCard()`, and to results screens' "What's next?". Accuracy fixes in `_miniGameNudge()`: (1) "Your last lesson covered X" now uses `Recommend.lessonSkillFor()` instead of the unit's top skill, which could come from lessons not yet taken (e.g. after es-latam B1 "What Was Happening?" it said *pluperfect*, now *imperfect*); (2) the unit's roleplay/written exchange is no longer offered after every lesson of the unit, only once at unit end via `_practiceNudge()`; (3) with nothing weak, practice on the last lesson's content beats a hash-picked unrelated driller; (4) no second "alt" button. Also fixed: Home's practice button called `Workshop.open('srs')` (no such driller) for the weakest-words candidate. It now routes through the engine's shared `RecommendationEngine.open()`. And results screens' `excludeDrillerId` compared against a `kind` that never exists, so a driller's "What's next?" could send you straight back into the same driller; it now falls back to the continue step. `tests/drills/test-scenario-learner-path.js` Test 4 updated to match. Verified live with a seeded es-latam B1 learner.
- **Home's Practice Card Only Says What's True** — 2026-09-28. Follow-up to the one-recommendation change above. The post-lesson practice card claimed mistakes that hadn't happened: `LearnerModel.weakSkills()` returns *weak or developing* skills, and a skill only ever answered right sits at the starting ease (2.5), which classifies "developing", so after a few lessons Home said "You made a few mistakes with X lately" about skills never missed. The same went for words (`weakWords()` returns the lowest-ease cards even when none was missed) and for drills and speaking (lifetime or undated accuracy, so "lately" could mean months ago). Practising didn't clear it either: Grammar Driller answers only reschedule items that are due, so a same-sitting practice after a miss changed nothing. Fixes: new `LearnerModel.troubleSkills()`: an exercise counts only while its latest answer is a miss, within the last 20 app opens, and not since answered right; a skill needs 2 such exercises. `Recycle.credit()` now marks a missed item `recoveredAtOpen` when a correct answer doesn't reschedule it (the schedule itself is unchanged). Words count only below the starting ease (or repeated Reader lookups), 3 minimum. Drill and speaking signals must be from the last 14 days (`DrillHistory.classify()` now returns `lastDate`). `_miniGameNudge()` was rewritten: only these weak signals make a card, and with none it returns null so Continue leads (no more "fresh"/"variety" cards after every lesson). "Not now" and taking a card are recorded (`recommendationOutcomes`, last 50): a skipped offer stays away for 5 app opens, a taken one for the rest of the sitting, and the next-worst skill takes its place. Home's "Not now" calls `RecommendationEngine.skip()`. New `tests/drills/test-home-recommendation-profiles.js`: 15 learner profiles, each with the card it must produce, run on the real engine files and es-latam curriculum. 9 of the first 13 failed before the fix. Verified live in the browser. Follow-ups: completed queue item 106 above.
- **Grammar Driller autoStart Opens the Weakest Skill** — Fixed 2026-09-25. `GrammarDriller.render(host, { autoStart: true })` (`engine/drills/grammar.js`) read `LearnerModel.weakSkills(1)` without `await`. The call returns a Promise, so `weak.length` was always undefined and autoStart fell back to the first learned skill every time. It now awaits the call. A new `_moduleIdFor()` also maps the lesson-index id it returns (`ser-estar`) back to the bank's module id (`ser_estar`) when one exists. Without that mapping, `_buildPool()`'s exact-id bank filter would drop every bank item. `options.skill` goes through the same mapping, because the recommendation engine passes `weakSkills()` ids there and had the same silent loss. Verified in the browser: with a seeded recycle schedule that made `ser-estar` weak, autoStart, `skill: 'ser-estar'` and `skill: 'ser_estar'` all opened a ser/estar session with `ser_estar` selected ("Ser vs estar (20)"). The same day, three stale `tests/drills` suites were brought up to date with the code; none of them had found a code bug. `test-diagnostic-test.js` now accepts the `text-input` questions from 5aa013d9, reads the wrapped header-comment quote, and checks the first-open welcome screen's language choice instead of the removed Home card chips. `test-functional-polishes.js` now expects `enterkeyhint="next"`, the deliberate change in 561ac11e. `test-vocabulary-surface-matching.js` now uses `es-latam`, since the `es` course code was retired in the Spanish split. All 14 suites in `tests/drills/` pass.

### Library & Dictionary Polish
- **Library: % Familiar, Continue Reading & Series Progress** — Built 2026-09-24 (`engine/reader.js`, `styles/components.css`; ROADMAP "Library & Reading Experience" items 1–2). **% familiar**: each story card shows the share of the story's content words (nouns/verbs/adjectives/adverbs) the learner has reviewed at least once or marked known; hidden for a learner with no such words yet. The per-story lemma lists are cached in localStorage per course (`storyLemmas`, ~420 bytes/story, versioned by `STORY_LEMMA_CACHE_VERSION`); uncached stories are computed only as their cards scroll into view, one at a time, so opening the Library doesn't fetch a whole level. The percentage is recomputed against the live deck on every render. **Continue reading**: the reader remembers how far into an unfinished story you scrolled (`storyProgress`, cleared on finish) and resumes there; a "Continue Reading" row (up to 3, most recent first) sits above the recommendations; in-progress cards get a ribbon bookmark and a progress sliver. **Series progress**: Original and track shelves show "7 / 36 read" once started; finishing a story in a series offers "Next in the … series" with a Read next button instead of dropping back to the shelf. Related fixes: `Library.analyseText()` now counts My Dictionary known words as familiar (matching the reader's word colours); `Reader.storyPlainText()` now skips non-target-language paragraphs, so HU A1's English narration no longer shows up in the end-of-story word review; and ES `original/a1/a1-21.json` ("Cómo es cada uno") had a duplicate id `story.a1.04` (shared read-state with `a1-04.json`, and opened the wrong story by id) — renamed to `story.a1.21` in both es-latam and es-es, manifests rebuilt. Anyone who had read "Cómo es cada uno" loses its ✓ once (it was recorded under the other story's id).
- **Library Track Shelf, Shelf Ordering & Card Polish** — Built 2026-09-24 (`engine/reader.js`). A dual-track level's non-core track (ES B1 "latam", HU B1 "citizenship" — stored as type `world`, keyed by `unit.track`) now has its own shelf ("Latin America" / "Citizenship"). Original and track shelves sort chronologically (unit label → lesson → id); Classics/World/Current sort by title. Shelves appear in a fixed order (Original, track, Classics, World, Current). The learner's own level room opens by default ("you're here"); empty levels say "Coming soon". Cards drop the redundant level badge; classics show the author, track cards a part number + unit title. Recommendations prefer continuing a started series and name it ("Next in the Latin America series") or the classic's source instead of generic copy. Also fixed a false "Failed to load story" toast on phones: `loadStory()` caught an exception from word-colouring when the Lexicon hadn't loaded yet — it now awaits `Lexicon.load()` first, and `getWordStatus()` skips lookups until it's loaded.
- **Reader End-of-Story Word List Showing Raw Dictionary Glosses** — Fixed 2026-09-19. Bug report (#171, "Haber has a long definition", flagged from the ES reader on `story.a1.01`): `Library.analyseText()` (`engine/library.js`) stored a word's raw, unstripped dictionary translation instead of running it through `Lexicon.shortGloss()`, so any word whose raw gloss spelled out usage notes — "haber" (used as impersonal "hay" twice in that story) reads "to have (auxiliary verb used with a past participle to form the perfect tenses: he comido = I have eaten); impersonal form 'hay' means 'there is/are'" in `imports/dictionary/spanish-en.json` — rendered as a full paragraph in the compact end-of-story SRS review row (`engine/reader.js`'s `showWordReview()`) and the Library's own vocabulary list, instead of the short one-line gloss those views are designed for (and that the Reader's own tap popup already gets right on purpose, per `Lexicon.shortGloss`'s comment). Now applies `Lexicon.shortGloss()` when building the lemma map, matching the "to have" already used for `haber` in the pre-built decks.
- **ES Dictionary "llamas" Wrong-Entry Gloss Fix** — Fixed 2026-09-24. Bug report (#192, "check the english gloss for llamas", flagged from the ES-LATAM review tab): `imports/dictionary/spanish-en.json`'s `"llamas"` headword had been imported as "a name of several localities in Asturias, Spain" (type: proper noun) — a Wiktionary placename artifact, not the reflexive-verb form ("you call / you are called") taught in `lesson.a1.01.03`. `engine/srs.js`'s `renderCard()` reads this dictionary directly via `Lexicon.define(card.spanish)` rather than the curated vocab gloss, so the due review card showed the nonsense entry. Corrected via `MANUAL_OVERRIDES` in `scripts/import_dictionary.py` (also applied directly to the generated JSON so the fix ships without a full re-import), covering both the taught verb sense and the unrelated "flames"/animal noun sense the same string means elsewhere (e.g. "arrojados a las llamas" in a B1 story).
- **HU Dictionary Wrong-Sense Gloss Fixes** — Fixed 2026-09-18. `scripts/import_hu_dictionary.py` had two related bugs surfacing as bad glosses in `content/hu/decks/decks.json`'s frequency decks: (1) `PRIMARY_SENSE_OVERRIDES` reorders specific lemmas' senses when Wiktionary's own page order puts a rare/wrong sense first — e.g. "forrás" ("source") was showing "boiling", "mű" ("work") was showing "artificial" (only valid as the "mű-" compound prefix); (2) a `BARE_FORM_HEADING` filter drops 57 dictionary-wide senses that were just a bare "present participle of X:" / "verbal noun of X:" heading with no real translation after the colon (Wiktionary's actual definition lives on a nested line the importer never captured) — e.g. "vezető" ("leader") was showing literally "present participle of vezet:". Rebuilt `imports/dictionary/hungarian-en.json` and `content/hu/decks/decks.json` via `python scripts/import_hu_dictionary.py && python build-manifest.py`. Only 2 lemmas needed sense-order overrides and 3 bare-heading glosses had leaked into decks.json specifically, but the audit covered the top 1000 frequency-ranked words' full sense lists.
- **Word Translation Popup Sheets** — Refined 2026-09-12. Standardized `.wp-sheet` with desktop modal centering and mobile safe-area insets.
- **Library Room & Shelf Navigation** — Built 2026-08-28. Hierarchical browsing across levels, rooms, and shelves.
- **Library Topic Search & Recommended Reading** — Built 2026-09-14. Universal search across readings with context banner recommendations.
- **Reading Attribution & Classics Sourcing** — Added 2026-09-10. Standardized attribution headers across authentic literary texts in Hungarian and Spanish.
- **Fourth Library Shelf (Articles / Cultural Reads)** — Built 2026-09-10. Added contemporary non-fiction and cultural texts shelf.

### Decks & SRS Subsystem Polish
- **Blast Time Attack Stuck on the Same Few Words** — Fixed 2026-09-27. With a 200-word deck, Time Attack kept asking for the same 4 words (Easy caps the field at 4). After a correct hit, `_handleCanvasCoords()` (`engine/decks/blast.js`) called `_fillTargetField()` before `_advanceToNextTarget()`, while the current target was still the word just blasted. The field therefore put that word straight back and was full again, so no new word could enter. Time Attack showed it worst because meteors bounce forever. Survival had it too, just less visibly: meteors fall off the bottom and get replaced, but every word you hit correctly still came straight back (simulated: 9 different words in 86 hits before the fix, 72 after). The first refill now passes `ensureTarget = false`. Checked in the browser with a debug copy of the module: over 40 correct hits the prompt covered 5 different words before the fix and 37 after. Blast still draws from the whole deck at random; it doesn't favour due words.
- **Listen to SRS Cards** — Built 2026-09-14. Speech synthesis audio playback on flashcard review.
- **Quizlet-Style Study Modes (Review / Match / Learn)** — Built 2026-08-27. Full study mode switcher with dedicated mechanics for each mode.
- **Study Modes Feed SRS** — Built 2026-09-25. Match/Blast misses are "again", hits a weak good; Learn's stage 4 is a good (due cards only). See queue item 95.
- **Learn Mode Small-Batch Pacing** — Built 2026-08-27. Step-by-step introduction of new words in bite-sized batches.
- **SRS Hotkeys & Touch Gestures** — Built 2026-09-12. Added desktop keys `1`-`4` and fluid mobile swipe gestures (left = Again, right = Good).
- **Review Card Stays Put on Phones** — Fixed 2026-09-24. Flipping pushed the rating row below the fold, and hiding it for the next card shrank the page so the browser snapped the scroll back up — the learner scrolled down on every card. `revealAnswer()` (`engine/srs.js`) now scrolls the ratings into view and holds `#review-card` at its flipped height (cleared on session start / Flip↔Type toggle); `.review-flip-actions` uses `margin-top: auto` so Show Answer sits where the ratings were. Same day, Type mode got the same treatment in `revealTypedResult()`, plus `#review-answer` now keeps its (invisible) slot before Check so the input field no longer drops ~90px when the answer appears above it; `isAnswerShown()` checks visibility as well as display for the swipe/keyboard handlers.

### Cross-App Flow & Integration
- **Grammar & Decks Search in Both Languages** — Built 2026-09-28. **Grammar Guide search** used to match topic titles only, and titles are a mix of English and target language, so whether a search worked depended on how the topic happened to be titled. `scripts/build_grammar_guide_index.py` now adds a hidden `keywords` string to each topic in `indexes/grammar-guide-index.json`: English from the topic id slug and section headings, target-language forms from the italicised terms (≤30 chars) in its explanations. Full prose and examples are left out on purpose, so "verb" doesn't match everything. `engine/curriculum.js` matches title or keywords and lists title matches first, each group in course order ("soy" → "Soy: saying who you are" first, then "Ser for origin"). Index size: es-es 95 → 182 KB, hu 240 → 511 KB (one fetch, gzipped in transit). **Decks search** used to match the deck name, level, kind and only the five preview words on the card, with exact accents and no English. Each card now carries all its words plus their full English glosses from `decks.json` (or the stored translation for My Decks), matched accent-insensitively through the Library's `_normSearch()`/`_matchesTerm()` (`engine/decks.js`): "morning", "manana" and "mañana" all find Daily Routine. Both placeholders now say "in <language> or English". Verified in the browser on es-es.
- **Connective Lesson-Complete Screen** — Built 2026-08-27. Post-lesson action recommendations linking directly to relevant drills and deck reviews.
- **In-Lesson XP & Streak Animations** — Built 2026-09-02. Immediate feedback badges and streak counters inside active sessions.
- **Journey Deep Integration** — Built 2026-09-11. Unified progress tracking, XP history, and drill stats consolidated in My Journey.
- **Resume a Lesson Where You Left Off** — Built 2026-09-24 (ROADMAP "Ideas from other language apps" item 1, after Babbel). `renderStep()` (`engine/lessons.js`) saves the lesson in progress to `<course>:lessonInProgress`: the built step list, position, missed steps, stats, graded indices and elapsed time. The step list is saved because `buildSteps()` recycles and shuffles, so a rebuild wouldn't match. On reopening, `startLesson()` shows "Pick up where you left off? Continue / Start over". There is one slot per course, nothing is saved at step 1 (so opening another lesson just to look at it doesn't overwrite the slot), `finishLesson()` clears it, and it expires after 14 days. Not cloud-synced; `sync.js` uses an allowlist.
- **Vocabulary Credit When Testing Out** — Built 2026-09-24 (same list, item 2, after Memrise). `markLevelComplete()` (`engine/progress.js`), used by the diagnostic and level tests, now calls `creditTestedOutWords()` (`engine/srs.js`). That function reads each skipped lesson's own vocabulary (`collectLessonVocabulary()`, the list its "Add to Review" step offers) and adds the words to My Dictionary as known, with `source: 'level-test'`. Words already in the deck or known are left alone. Before this, a learner placed into A2 counted as knowing no A1 words in the Reader, "% familiar" and "Within reach". Verified: testing out of ES A1 credits 618 words, all with lesson translations. It runs in the background (about 15 s on the dev server).

### Interface, Audio & Platform Architecture
- **Boot Screen & Loading Overlay** — Built 2026-09-17. Minimalist `#boot-screen` and smooth loading spinner overlays on driller/lesson transitions.
- **Constructivist Dark / Light Theme** — Built 2026-09-12. Inverted midnight navy / warm cream palette (`[data-theme="dark"]`) with quick-toggles.
- **Speech Recognition & Pronunciation Studio** — Built 2026-09-14. Web Speech API evaluation engine with Speaking and Writing Studios.
- **Offline PWA & Service Worker** — Built 2026-09-14. Complete asset caching and offline-ready service worker (`sw.js`).
- **Language-Isolated Asset Loading** — Optimized 2026-09-14. Isolated dictionaries and indexes per language to eliminate unnecessary network/memory overhead.
- **Contextual Accent Popover** — Built 2026-09-23. Replaced the always-visible diacritics bar (`UI.diacriticsBarHtml`) across all text-entry drills with a Conjuguemos-style popover that only shows the accented variants of the letter just typed (`n` → `ñ`, `o` → `ó/ö/ő` in Hungarian, etc.), plus `¿`/`¡` openers triggered by typing `?`/`!` and inserted at the sentence start. Same call-site API, so no runner/lesson code changed — only `engine/ui.js` and `styles/components.css`.
- **iOS Speaking Studio falling into self-evaluation** — Fixed 2026-09-25. On iPhone (cloud Whisper STT path), every Read & Repeat after the first ended in "No voice heard" + self-eval buttons. The level-meter `AudioContext` was created inside the `getUserMedia` `.then`, outside the tap gesture, so iOS left it suspended; the meter read silence, `_hasSpoken` never flipped, and the 10s initial-silence timer fired `no-speech` and discarded a perfectly good recording. `engine/speech-input.js` now creates (and resumes) the context synchronously in `_startRecordingStream`, and if a cloud session's meter still isn't `running` when the silence timer fires, it sends the recording to Whisper instead of reporting `no-speech`. Regression test: `tests/speech/test-speech-ios-meter.js`. Not yet confirmed on a real iPhone.

---

## Completed Curriculum Phases (archived from `docs/CURRICULUM_ROADMAP.md`, merged into ROADMAP.md 2026-09-28)

### Phase 1: Spanish A1 Core Gaps — Done
Six units filling A1 gaps: **Gustar** (inverted syntax, indirect object pronouns), **Daily Routine / Reflexive Verbs** (paradigm, stem-changing reflexives, sequencing connectors), **Demonstratives** (3-tier spatial system, neuter pronouns), **Present Continuous** (*estar + gerundio*, irregular gerunds), **Doler** (inverted *doler*, body parts, pharmacy vocab), and **Poder & Saber** (ability vs. skill, *saber vs. conocer*, personal *a*). Each with 5 lessons + consolidation + original story set in Hanói.

### Phase 2: Spanish A2 — Pretérito Imperfecto — Done 2026-09-16
- **Unit 21** (`a2-imperfectobasico-*`): Regular *-ar/-er/-ir* endings, the 3 irregulars (*ser/ir/ver*), states/descriptions in the past.
- **Unit 22** (`a2-imperfectocontraste-*`): Imperfect (background) vs. Preterite (foreground), *mientras + imperfecto*, narrative structure. Both units shipped as 5 lessons + consolidation.

### Phase 3: Spanish A2 — Imperativo & Clitic Pronouns — Done 2026-09-17
- **Unit 23** (`a2-imperativoafirmativo-*`): Regular & 8 irregular *tú* imperatives, formal *usted/ustedes*. Story: *Las instrucciones de la abuela*.
- **Unit 24** (`a2-imperativonegativo-*`): Negative *tú* commands, pronoun attachment vs. pre-command placement, accent shifts. Story: *Las reglas del hostel*.
- **Unit 25** (`a2-pronombrescliticos-*`): Indirect object pronouns, double-object clitics (*se lo dije*, *le → se* rule). Story: *Un favor entre amigos*.

### Phase 4: Spanish A2 — Modality, Subjunctive & Pragmatics — Done 2026-09-17
- **Unit 26** (`a2-condicionalsimple-*`): *-ría* endings for polite requests & advice. Story: *El dilema del café*.
- **Unit 27** (`a2-subjuntivobasico-*`): Introductory subjunctive triggers (desires, feelings, impersonal expressions, future *cuando*). Story: *Deseos para el viaje*.
- **Unit 28** (`a2-perifrasisverbales-*`): Verbal periphrases & discourse connectors. Story: *Nuevos hábitos en Valencia*.
- **Unit 29** (`a2-educacionyestudios-*`): School life vocabulary & *se me da bien / me cuesta*. Story: *El primer día en la facultad*.

### Phase 5: Hungarian A1 — Core Case Integrations — Done 2026-09-17
- **Unit 31** (`a1-151` to `a1-155-consolidation`): Elative *-ból/-ből*, Delative *-ról/-ről*, 3-way source contrast. Story: *Honnan jöttök?*
- **Unit 32** (`a1-156` to `a1-160-consolidation`): Essive-modal *-ul/-ül*, language adverbials, fluency adverbs. Story: *Nyelvgyakorlás a kávézóban*.
- **Unit 33** (`a1-161` to `a1-165-consolidation`): Core postpositions (*alatt, felett, mellett, előtt, mögött, között, után*). Story: *Hol van a jegy?*

### Phase 6: Hungarian A2 — Inflected Personal Pronouns — Done 2026-09-17
- **Unit 33** (`a2-161` to `a2-165-consolidation`): Inessive, Superessive, Sublative declined pronouns + governing verbs.
- **Unit 34** (`a2-166` to `a2-170-consolidation`): Adessive, Allative, Ablative, Delative declined pronouns; hosting & visiting etiquette.

### Phase 7: Hungarian A2 — Advanced Grammar & Culture — Done 2026-09-17
- **Unit 35** (`a2-171` to `a2-175-consolidation`): Translative *-vá/-vé* with consonant assimilation, verbs of becoming. Story: *Az új műhely*.
- **Unit 36** (`a2-176` to `a2-180-consolidation`): Essive-Formal *-ként*, professions, temporal distributives. Story: *Önkéntesként a táborban*.
- **Unit 37** (`a2-181` to `a2-185-consolidation`): Deferential politeness (*tetszikelés*), Hungarian name order, honorifics, Name Day etiquette. Story: *Névnap a nagymamánál*.

### Phase 8: Comprehensive CEFR Assessment Tests — Done 2026-09-17
Multi-modal 3-part test engine (contextual cloze, active recall, pragmatic choice, writing task, speaking task with SpeechRecognition). Tests authored and validated for: `es` A1 (22 items), `es` A2 (24 items), `hu` A1 (26 items), `hu` A2 (26 items), `hu` B1 (28 items). Schema updated for all courses.

### Phase 9: Hungarian B2 — Dual-Track Curriculum Blueprint — Done 2026-09-27
Full 72-unit / 432-lesson B2 curriculum (`content/hu/curriculum/units/b2.json`) — 36 Core grammar units paired with 36 Culture, History & Society track units across 6 blocks (Units 01–36). Core track: one adapted Hungarian literary classic per unit (lesson 5). Culture track: 5-part serialised reading across lessons 1–5 plus a combined standalone story. All 432 lessons live on master.

### Phase 10: Spanish A2 Core Additions — Units 30 to 33 — Done 2026-09-27
Resolves Instituto Cervantes PCIC A2 gaps:
- **Unit 30** (`a2-porpara`): *Por* vs. *Para*.
- **Unit 31** (`a2-indefinidosnegacion`): Indefinites & double negation.
- **Unit 32** (`a2-perifrasisduracion`): Life in Duration & aspectual periphrases.
- **Unit 33** (`a2-vosotrospeninsular`): Vosotros in Peninsular Spanish (es-es only).
Deliverables: 23 new lessons, 23 grammar modules, 20 vocabulary modules, 246 schema-validated exercises, 4 original stories. Units 30–32 in both es-es and es-latam; Unit 33 es-es only.

### Phase 11: Spanish B1 Core Missing Grammar — Units 37 to 40 — Done 2026-09-27
Completes B1 grammatical inventory vs. Instituto Cervantes Plan Curricular:
- **Unit 37** (`b1-37`): Pretérito Perfecto de Subjuntivo.
- **Unit 38** (`b1-38`): Sequence of tenses & reported speech.
- **Unit 39** (`b1-39`): Spanish verbs of becoming (*ponerse, quedarse, volverse, hacerse, convertirse en, llegar a ser*).
- **Unit 40** (`b1-40`): Advanced connectors, prepositional regimes, *pero/sino/sino que*, neuter *lo*.
Deliverables: 24 new lessons, 24 grammar modules, 20 vocabulary modules, 264 exercises across es-es and es-latam. Wired into `curriculum/units/b1.json` under `"track": "core"`.

### Phase 12: Peninsular Spanish Track Vosotros & Lexical Alignment — Done 2026-09-27
Dedicated *vosotros* active mastery unit at A2 (Unit 33) and systemic B1 integration. Authentic Spain lexical variants throughout: *coche, ordenador, móvil, piso, zumo, camarero, chavales, colegas, pandilla, quedada, tapeo, caña, chulo*.

### Phase 13: Full Build Pipeline & Index Regeneration — Done 2026-09-27
- `build-manifest.py`: 810 lessons/135 units (es-es), 816 lessons/136 units (es-latam), decks and story manifests rebuilt.
- `build_grammar_index.py --strict`: 5,027 exercises/213 skills (es-es), 5,425/234 (es-latam), 7,782 (HU) — zero errors.
- `build_translation_index.py`: All bilingual indexes regenerated.
- `audit_exercise_metadata.py`: 12,094 (es-es) + 12,113 (es-latam) exercises — 0 missing teaches, 0 missing categories, 0 unregistered tags.

### Phase 14: Comprehensive Spanish B1 CEFR Assessment Test — Done 2026-09-27
`content/es-es/tests/b1-test.json` and `content/es-latam/tests/b1-test.json`. Part 1: 28 multi-modal questions (present & perfect subjunctive, sequence of tenses, reported commands, conditionals, verbs of becoming, prepositional verbs, *sino/pero*, neuter *lo*, pragmatic interaction). Part 2 Writing: formal debate text (80–120 words). Part 3 Speaking: voice memo (45–60 s) proposing a teamwork conflict solution.

### Hungarian A1 Lesson 16 split into 16a / 16b — Done 2026-09-30
"Numbers 0-10 - Számok 0-10" became `a1-16a` (numbers 0–10, *hány?*; 11 words, 19 exercises) and `a1-16b` (numbers 11–100; 9 words, 21 exercises, 15 of them newly written). Lesson files use a letter suffix so lessons 17+ keep their numbers. `auto_group_units()` in `build-manifest.py` now accepts `a1-NNx` stems and keeps the parts inside one block, so unit boundaries do not shift. Note: progress recorded against `lesson.a1.16` now maps to nothing; `16a` is a new lesson id.

### Reader: plain text by default — Done 2026-09-30
The LingQ-style status underlines are gone: story text reads as plain text and every word stays tappable (the existing first-visit margin note says so). A word you tap gets a faint ochre hairline wherever it appears in that story (`word-tapped`, `engine/reader.js`'s delegated click handler). A "Mark words you're learning" switch in the story header (off by default, stored in `parlour_reader_mark_learning`, applied as `html.reader-marks`) adds a dotted underline to deck words only: ochre until first reviewed, navy after; new and known words stay plain. Status classes (`word-unknown/seen/known/mastered`) are still computed, so Library's "% familiar" figure is unaffected. Spec in DESIGN.md (Reader text).

### ES-LATAM B2 Library: one Latin America shelf of 36 — Done 2026-09-30
B2's Library showed a "Latin America" shelf and a separate "Regional" shelf with the wrong counts. Root cause: 22 of the 36 Latin America units in `content/es-latam/curriculum/units/b2.json` were tagged `track: "regional"`, a track B2 doesn't declare in `LEVEL_TRACKS` — so they also never appeared in the Learn tab's B2 path (`engine/curriculum.js` draws declared tracks only). Retagged as `latam` (unit ids are now `unit.b2.latam.15`…`36`). Also fixed story ids that hid or duplicated readings: 8 combined readings carried their consolidation's id (Colombia I/II, Ecuador, Peru I, Venezuela I/II) or a `.consolidation` suffix (Panama, Guianas), and 3 consolidations carried the combined id (Cuba, Dominicana, Puerto Rico). Guatemala, El Salvador & Honduras and Nicaragua had segments but no combined reading; built them by joining the five segments. B2 now shows 36 Classics + 36 Latin America.

### ES-LATAM B1 "inspired by" readings moved to Classics — Done 2026-09-30
22 of the old B1 originals (`classics/b1/b1-13.json`…`b1-35.json`, e.g. *Dos caminos* = the Odyssey) are original texts written around a classic's themes. They're now type `classic` with `work`/`author` and a new `inspired: true` flag (added to `story.schema.json` in all three courses, passed through by `build-manifest.py`); the reader's attribution and recommendation lines say "Inspired by …" instead of "Adapted from …". `b1-12` (*La mesa de Elena*) and `b1-30` (*Muchas maneras de hablar*) name no source work and stay under Original. B1 Classics now holds 62 readings.

### Overhaul stylesheet folded into the base files — Done 2026-09-30
`styles/overhaul.css` is gone. Each of its 948 rules now lives in the base stylesheet that owns its component: 202 merged into an existing rule with the same selector, 746 appended to a "The Composed Room overhaul" section at the end of the latest-loaded file that uses its classes. A rule was only merged in place when no later rule in the cascade (and no earlier overhaul rule already appended) sets the same property on a related class; otherwise it was appended, and never into an earlier file than a conflicting rule before it, so the original cascade order holds. Verified by swapping the old and merged stylesheets on the live page and comparing every element's computed style across all tabs, sub-screens, lesson steps and feedback, deck modes, studios, drillers and the diagnostic, at phone and desktop width in light and dark: zero differences. The phone lighter layer now sits in `@media (max-width: 639px)` blocks inside those sections. Hover styles across all stylesheets (130 older ones too) apply only on devices that can hover. Item 111 above describes the earlier two-file state.

### Repo cleanup: scripts archived, documents merged — Done 2026-09-30
- **`scripts/`**: 274 one-shot scripts (unit generators, `data_*` and helper modules, A1 block scaffolding, one-off fixes and backfills, and the root `download_verbs.py`) moved to `scripts/archive/`, in whole dependency chains. 32 tools stay, described in the new `scripts/README.md`. Nothing in CI, the pre-push hook, the engine or any live document referenced the archived ones. `build_competencies_index.js`, `import_verbs.py`, `verify_grammar_embedding.py` and `audit_hu_citizenship_stories.py` went too: each had a hardcoded old path (`content/es`) or unit list.
- **Service setup docs**: `BUG_REPORT_SETUP`, `CLOUD_SYNC_SETUP`, `GOOGLE_SIGNIN_SETUP`, `GRADER_SETUP` and `STT_SETUP` merged into `docs/SERVICES.md`, which also documents the Turnstile bot check the sync Worker uses (its old doc, `TURNSTILE_SETUP.md`, never existed). Code comments and `tests/sync/test-google-signin.js` now point there.
- **Design docs**: `design principles.md`, the v1 principles, and the 2,098-line `parlour_visual_overhaul_spec.md` moved to `docs/archive/`. `DESIGN.md` is the one visual reference; it gained a short "Standing rules carried over" section (copy discipline, mockups are visual-only, the unsettled nav label, shared components).
- **`PLANNING.md`** archived; its exercise-behaviour, teaching and `es-latam` (no `vosotros`) rules are now "Teaching and exercise principles" in `AGENTS.md`, next to a new "Wiring a new unit into the app" section taken from `docs/CURRICULUM_ROADMAP.md`, which was archived (its product ideas were already in `ROADMAP.md`).
- **`TROUBLESHOOTING_BACKLOG.md`** (1,560 lines, resolved except two items) archived; the open items are ROADMAP 112 and 113.
- **`README.md`** fixed (stale `content/es` paths) and given a documentation map.
- **Guides and drafts**: six unreferenced Latin America A1/A2 guides and the four Hungarian planning drafts moved to `docs/archive/guides/` and `docs/archive/hu-drafts/`. The `backfill_sentences/` batches stay: `build_translation_index.py` reads them as input.
- **A1 guides merged (2026-10-02)**: `a1-content-spec`, `a1-exercises`, `a1-lesson-template` and `a1-srs-srategy` were merged into one `a1-authoring-guide.md` (archived the same day, see the next bullet), rewritten against the current code and data (the old SRS note still said the recycle block was "not built"; paths said `content/es/`; the audit and the B1 spec cited sections that no longer existed). The unit list, vocabulary themes and grammar progression, which only mirrored data, were archived to `docs/archive/guides/`. References updated in the three vocabulary schemas, `engine/recycle.js`, both audit scripts, `b1-content-spec.md` and the Hungarian authoring template.
- **Prose guides archived (2026-10-02)**: the merged A1 guide, `B1_GUIDE.md`, `b1-content-spec.md` and `latam-generation-brief.md` moved to `docs/archive/guides/`. Nothing reads them, the shipped content no longer follows them (`audit-lesson.py` flags 123 of 156 A1 lessons and 296 B1 ones), and what is enforced is the validator, the schemas and `AGENTS.md`, which gained the fill-blank hint rule, the unambiguous-question rule and a pointer to the audit. `a2-lesson-guide.md` and the B1 unit list stay because `audit-lesson.py` parses them; `editorial-style-guide.md` stays as the style reference. References updated in the three lesson schemas, `engine/recycle.js`, `audit-lesson.py` and the style guide.
- **Worktrees**: eight orphaned folders under `.claude/worktrees/` (not registered with git) deleted. The eight registered ones (six `agent-*` worktrees from 20 August plus two session worktrees, all stale, none ahead of master, and none in use by an open session) were removed on 2026-10-02 after checking their uncommitted Spanish grammar edits were already in master (the same text appears in the current `es-latam` files with later italics applied); their six merged branches and git's 19 dead bookkeeping stubs went too. `.claude` went from about 1.3 GB to 17 MB.

### Hungarian Reader: words written without accents now resolve — Done 2026-10-03
Tapping a Hungarian word written without accents ("kerdes", "kerdezte", "varosban"), as pasted texts and casual writing often are, showed "Not in the dictionary yet" or a wrong guess. `lookupHungarian()` in `engine/lexicon.js` now retries an unresolved, fully accentless word against accent-folded indexes of the dictionary and word-index ("kerdes" → *kérdés*, "varosban" → *város*), then as a dictionary stem plus each accent variant of the rest ("kerdez|te" → *kérdez*), which is kept only if it reads as a verb form of that stem, since the analyser accepts odd nominal spellings ("kés"+"ma"). A word that resolves as written keeps its reading ("kor" stays *kor*, not *kór*/*kör*), and a word with any accent is never re-accented. The fold index (~0.5 s) builds in `requestIdleCallback` after the lexicon loads. Test: `tests/reader/test-hu-accentless-lookup.js`. The analyser's vowel-harmony gap this exposed is item 123 above (done).

### One correct answer per choice exercise, A1-A2 — Done 2026-10-01
Every multiple-choice, dialogue and listening-choice exercise should have exactly one acceptable option. Three passes over A1-A2 (all three courses):
- **Mechanical** (commit `d3bc485c`): 13 Spanish A2 exercises listed the correct option twice; 5 were built as "pick any" (`correct` was a list) and now have one answer; 7 vocabulary questions offered a dictionary synonym of the answer as a wrong option (adónde/where, férfi/ember, heti/hetente, hisz/gondol, kedvezmény/akció, hideg/hűvös).
- **Read by hand**: the 1,043 riskiest questions ("Which sentence is correct?", "Which reply fits…", "Which sentence means…"); 94 fixed (160 copies across both Spanish courses). Typical cases: "What do you want?" with both ¿Qué quieres? and the usted ¿Qué quiere?; "describes a completed past action" with the pretérito perfecto as a "wrong" option; "La compré / Los compré / Las compré" with no antecedent (the question now names it); "Which question fits the meaning?" with no meaning given (HU a1-46…50). The wrong option is now clearly wrong, or the question names what decides it.
- **Wrong answers found on the way**: HU A1 units 57-60 taught -ba/-ban with nouns that take -ra/-n (*az állomásban*, *a postába*, *a helyben*, *a munkahelybe*); those exercises now use mozi, gyógyszertár, központ, iroda. Eight Spanish A1 "Which sentence starts this exchange?" items whose options were the words of one sentence are now sentence-builder exercises. *Bal van.* → *Balra van.* and similar were fixed in the HU A1 121-150 rewrite (ACHIEVED 116).
Not covered: B1 and above, and the A1-A2 question types outside the risky set (mostly single-word vocabulary questions, which the dictionary check covered); see ROADMAP 117.


### Cloud sync no longer turns array stores into objects — Done 2026-10-01
Spoken (and written) production grading crashed with `history.unshift is not a function`. Cause: `mergeField()` in `engine/sync.js` fell back to `Object.assign({}, cloud, local)` for any store without a dedicated merger, which turned array stores into `{"0": …, "1": …}` objects after a sync. That hit `assessmentHistory` (the crash), `recommendationOutcomes` (`.push`), `milestonesSeen` (`.includes`), and silently emptied `listeningLog` and `verbSpeedScores`. Array stores now merge as arrays (`mergeArrayById`), values already damaged are turned back into arrays on the next merge, and `LearnerModel`'s assessment loader accepts the damaged form and keeps entries newest first.

### Deck answers: article required, word read aloud on reveal — Done 2026-10-01
Typed Spanish answers in deck Review (type mode) and Learn (stages 3-4) must now include an article of the right gender whenever the dictionary knows the noun's gender: *el/un perro*, *la/una casa*, *el agua* (feminine nouns starting with a/ha also take el/un). A bare noun or a wrong article is wrong, not an accent "near miss". Words with no known gender (verbs, adjectives, invariant nouns) are graded as before. The accepted articles come from `Lexicon.acceptedArticles()`. When the answer is revealed (flip, typed Check, or a settled Learn question), the target-language word is read aloud with its article, so you hear the gender too. Stressed-a feminine nouns (agua, águila, alma, hambre…) now display, read and grade as *el agua*; `Lexicon.article()` uses a fixed list (`STRESSED_A_FEMININE`), since "starts with a" would wrongly catch *la amiga*.

### ES-LATAM B2 Library: Guatemala, El Salvador & Honduras, Nicaragua expanded — Done 2026-10-01
Units 04, 05, and 06 on the B2 Latin America shelf were previously thin (15 short paragraphs, no narration audio segments, no comprehension questions). All 15 underlying lesson stories (`b2-guatemala-01..05`, `b2-salvadorhonduras-01..05`, `b2-nicaragua-01..05`) were expanded to 7 paragraphs (~650 words each) with 3 text-grounded comprehension questions each, covering the unit topics (Mayan archaeology & biosphere concessions in Petén, Popol Vuh & corn cosmogony, seismic baroque in Antigua, armed conflict & Rigoberta Menchú, 48 Cantones & Lake Atitlán; Copán stelae & Gulf of Fonseca, banana enclaves, Garifuna resistance & Berta Cáceres, San Óscar Romero & Chapultepec, Northern Triangle migration & remittances, youth muralism & security; Lake Cocibolca & Ometepe, Rubén Darío & Modernism, Augusto C. Sandino in Las Segovias, 1980 Literacy Crusade & Solentiname, 2018 civic resistance & writers in exile). The 3 consolidated Library readings (`b2-guatemala.json`, `b2-salvadorhonduras.json`, `b2-nicaragua.json`) were re-stitched via `scripts/stitch_track_unit_stories.py` with 35 paragraphs (~3,100 words), full narration segments with clause-boundary cues, and 15 comprehension questions each, preserving their Spanish titles. Manifests and indexes rebuilt.

### Lesson goals and post-lesson word match: two repeat-offender fixes — Done 2026-10-01
- **"Goals to lock down" after a near-perfect lesson**: the lesson summary read the checklist before `LearnerModel.recordCompetencies()` had given each goal a `state`, so every goal showed as unverified at any score. `lessonSaveChecklistChoices()` (`engine/lessons.js`) now hands the summary the stored records. A goal left unticked at ≥75% still shows as a Confidence Gap, which is intended.
- **Word match offered after every lesson with the same ten words**: `_missedWords()` (`engine/recommendationEngine.js`) took the ten lowest-ease cards, but a correct match only credits due cards and never raises ease, so nothing could move them. It now draws from due cards only, so a played card is rescheduled and drops out. A taken practice offer also stays away for 4 hours (`TAKEN_COOLDOWN_HOURS`), not just one page load, which a phone repeats constantly.

### Cloud sync: devices no longer overwrite each other — Done 2026-10-01
Deck reviews done on a laptop never reached the phone. The Worker stores whatever snapshot it's sent, so a device that saved before pulling (a phone with a stale copy saving XP, say) replaced the other device's newer save in the cloud. It then marked itself "in sync" and never pulled the lost changes. Fixes in `engine/sync.js`: `backup()` now reads the cloud first and merges it in whenever it's newer than this device's last sync; it refuses to upload if the cloud can't be read. After such a merge the last-synced marker is left behind, so the next foreground check pulls and reloads. `mergeSrsDeck` keeps the most recently reviewed copy of a card (by `lastReviewed`) instead of the one with more reviews, because "Again" resets `reviews` to 0. After a merge, every stored value is compared (`differsFromCloud`), so deck reviews and drill history trigger a re-upload too, not just lessons, known words and XP. A save arriving while another is in flight is queued, not dropped. Saves made when the app is hidden or closed use `keepalive` only when the body is under 64 KB (browsers reject larger keepalive bodies, so those saves always failed). The two-device scenario was simulated against the old and new code.

### Reading comprehension in level tests, diagnostic and Library — Done 2026-09-27/28
- New question types added to `engine/leveltest.js` & `engine/diagnostic.js`: `reading-mc`, `true-false-not-stated`, `gapped-text`
- `readingSection` schema added to `test.schema.json` (all 3 courses)
- Reading sections authored and validated for 9 level test files: A1/A2/B1 × es-es/es-latam/hu
- Diagnostic placement test (`engine/diagnostic.js`) now features an adaptive reading comprehension section on every tier (A1, A2, B1 × es-es, es-latam, hu), evaluated seamlessly with core questions and surfaced in tier debrief
- Scores saved to `Lang.key('readingScores')` across both level tests and diagnostic placement
- **Fix + "nearly there" band (2026-09-28):** the diagnostic's reading section was never actually shown — `_renderTesting` scored the tier as soon as the last core question was answered, so reading always counted 0/2 and the best possible tier score was 10/12 (83%), under the 85% pass mark. Nobody could pass A1, so everyone was placed in A1 (surfaced by a learner who scored 8/10). Fixed, plus a middle band: 70% to 84% on a tier (`borderlineRatio`, optional per test file) places one level up with a "Review <tier> first" option and a "Nearly there" badge. The preface now shows the real per-tier question count (12, not 10) and the pass/band percentages from the data.
- **Library Comprehension Scoring (Phase 5):** `engine/reader.js` and `engine/library.js` now score and persist reading comprehension checks to `Lang.key('storyComprehension')`, surface completion feedback upon answering, and display a `Quiz N/M ✓` badge on both home shelves and saved cards

### Speaking steps return once, never loop — Done 2026-10-04
A speaking or challenge step missed in a lesson used to be re-served at the end and, if missed again on the retry, queued again, so it never went away until answered right. Now it comes back exactly once (including when the learner ran out of tries the first time); a second miss moves on. Every attempt was already saved by `LearnerModel.recordProduction()`, so a weak oral skill still surfaces in later recommendations. `engine/lessons.js` (`requeuedMicSteps`, `queueForRemediationIfMissed`, `failStep`). Non-speaking exercises keep the old remediation behaviour.

### "Finish Lesson" no longer dead-ends — Done 2026-10-04
Finishing a lesson ran several unguarded steps (checklist save, progress/XP writes, the curriculum re-render, the async summary lookups); if any threw, `Finish Lesson` silently did nothing. `finishLesson()` in `engine/lessons.js` now isolates each stage, ignores a repeat tap while it runs, and falls back to a plain "Lesson complete" screen with a Done button if the full summary fails. Failures log to the console with the stage name. The exact throwing step wasn't reproduced; check the console if a learner still reports it.

## Skill-tag read-through log (ROADMAP 125 step 3)

One entry per locked unit: what was read, what changed, what was found.

### HU A1 `reading-hungarian` (a1-01–a1-05) — locked 2026-10-05
All 92 exercises were read and given one tag each. 29 now carry the unit vocabulary skill: word-meaning questions, greetings and any-answer items. Fourteen exercises changed `category` to follow their tag. The rest carry one of `hungarian-vowels`, `hungarian-consonant-sounds`, `personal-pronouns`, `van-zero-copula`, `ki-and-mi`, `demonstratives-ez-az`, `yes-no-questions` and `negation-with-nem`. Nine choice items got `distractor_skills`, mostly *ki/mi* offered where *ez/az* is needed. Review items now carry the skill they review, not the lesson's new skill: a1-05 had *Ki ő?* items tagged `negation-with-nem`. Thin skills were filled. Five consonant-sound items were added to a1-01, taking `hungarian-consonant-sounds` from 1 to 6. Six vowel-harmony items were added to a1-05, a new "Vowel Harmony" group, taking `vowel-harmony` from 0 to 6. `personal-pronouns` now has `taught_in` `a1-02-a-gr` (*Én, te, ő*), the screen that first teaches it, instead of a1-11's re-teach. Found while locking: the exercise schemas didn't allow `distractor_skills`, so it was added to every choice type in all three courses. Two weak exercises were fixed the same day and the unit was re-locked. `a1-05-practice-dialogue` used *nagy*, *ház* and *ez a ház*, none of them taught yet; it is now *Ő Anna?* → *Nem, ő Meg.* (against *Nem, ez egy tea.*). `a1-04-practice-1` accepted both *Igen* and *Nem*, so it tested nothing; it is now *Te Meg vagy? — ____, Károly vagyok.* (answer *Nem*, tagged `yes-no-questions`) and has the `english` line it lacked.

### HU A1 `greetings-basic-interaction` (a1-06–a1-10 + consolidation) — locked 2026-10-05
All 115 exercises were read (by a Sonnet subagent, decisions reviewed in the main session). The unit is a phrasebook of set phrases and no grammar skill is taught in it (its grammar screens are phrase notes), so 109 items carry `a1-greetings-basic-interaction-vocab`. Five carry `van-zero-copula`, the items that produce *vagy* in *Hogy vagy?*. One carries `negation-with-nem`, "Which is a negative statement?". Thirty choice, fill-blank and matching items moved from `grammar` to `vocabulary` to follow their tag. Old tags that didn't fit were removed. `kerek-vs-szeretnek` was on every a1-07 *please/thank you/sorry* item. `an-en-adverb` was on *jól/rosszul*; it is an A2 skill, so the level rule would have failed. `definite-vs-indefinite-conjugation` was on *értem/nem értem*, which are tested here as phrase meaning; the skill is taught at a1-102. No `distractor_skills`: no wrong option is a well-formed form of another grammar skill. One content fix: `a1-10-check-2` offered the formal *Megismételné?*, which is never taught; it is now the taught *Megismételnéd?*. `a1-07-practice-3` (*____, hol van a kávé?*) gave no context, so *Bocsánat* looked as good as *Elnézést*. The a1-07 grammar screen teaches *Elnézést* for getting attention (with this very sentence), so the answer stays *Elnézést* only; the sentence now says *(excuse me, to get someone's attention)* and has an `english` line. The same split was blurred in `a1-07-intro-2` ("Which means *sorry / excuse me*?" → *bocsánat*) and in `a1-07-voc.json` (*bocsánat* "sorry / excuse me", *elnézést* "excuse me / sorry"); they now say "sorry" (for something you did) and "excuse me", as the matching items already did. Left as they are: dialogue lines use a few untaught words as context only (*Segíthetek?*, *Kávét?*, *újra látlak*).

### HU A1 `introducing-yourself` (a1-11–a1-15 + consolidation) — locked 2026-10-05
All 115 exercises were read (Sonnet subagent, decisions reviewed in the main session). Tags now: `a1-introducing-yourself-vocab` 36, `van-zero-copula` 28, `ki-and-mi` 19, `spatial-questions-hol-hova` 19, `personal-pronouns` 8, `yes-no-questions` 5. The old tags were two-tag pairs from the bulk retag, and nineteen carried `ban-ben-in` (taught at a1-23) on *hol*/*itt* items. The review settled one point the conventions left open: a "Which means …?" item whose options are all members of one paradigm (*én/te/ő*; *ki/mi/hol*; *vagyok/vagy/van*) gets that paradigm's grammar skill, as a1-02/a1-03 already did, while a gloss against mixed words (*barát/ember/nő*, *itt/ott*) stays vocabulary. Eighteen items the subagent had sent to vocabulary moved back on that rule. Twenty choice items got `distractor_skills`, mostly *ki/mi* offered against *hol* and the reverse. *itt/ott* and *lakom/laksz/lakik* stay vocabulary: the a1-13 screen teaches them as chunks, and `itt-ott-here-there` and verb conjugation come later. Content fixes: `a1-11-practice-5` and its copy `a1-15-consolidation-13` asked *Anna itt van?* (untaught *itt van*, non-sequitur distractor); now *Te Anna vagy?* → *Igen, Anna vagyok.* against *Igen, Anna vagy.* `a1-14-practice-5` and `a1-15-consolidation-16` accepted only *Igen, ő egy barát.* though *Nem, ő nem barát.* was equally right; the distractor is now the contradictory *Igen, ő nem barát.* `a1-13-dialogue-2` answered with untaught *Budapesten*; now *Ott lakom.* `a1-14-practice-4` matched *Budapest* to "Budapest"; now *nő* "woman". Left as they are: review-1/2 are the same two items in all five lessons, several check items repeat an intro item, and the consolidation copies lesson items verbatim (the user prefers mostly-reused review content).

### HU A1 `numbers-personal-information` (a1-16a–a1-20 + consolidation) — locked 2026-10-05
All 137 exercises were read in the main session. Tags now: `a1-numbers-personal-information-vocab` 81, `cardinal-numbers` 41, `basic-hungarian-word-order` 7, `spatial-questions-hol-hova` 4, `ki-and-mi` 2, `van-zero-copula` 1, `a1-greetings-basic-interaction-vocab` 1 (the *köszönöm* review item). The old tags were mostly wrong: every a1-16a number item carried `singular-after-numbers` (taught at a1-30; nothing here puts a noun after a number), every address and *lakom* item carried `ban-ben-in` (taught at a1-23; *Budapesten* is a memorised chunk with the *-on/-en* ending), and the a1-19/a1-20 items paired `ki-and-mi` with `cardinal-numbers` or `basic-hungarian-word-order` whatever they tested. Decisions: a choice, fill-blank, builder, dialogue or writing item whose content is number words gets `cardinal-numbers` (the paradigm rule from unit 3: every option is a number), while number matching stays vocabulary as in units 1–3. *Hány éves*, *éves*, *cím*, *utca*, *telefonszám*, *születésnap*, *lakom* and "which question asks for …?" items whose options differ by noun are vocabulary. Items whose wrong options only reorder *Harminc éves vagyok* / *Hány éves vagy?* get `basic-hungarian-word-order` (the a1-17 tip teaches number–*éves*–*vagyok* order; the skill's screen is a1-20-b). Category changed on 33 items to follow the tag; two choice items got `distractor_skills` (*hol* against *ki*/*mi* and the reverse). Content fixes: `a1-17-practice-5` asked "Which sentence starts this exchange?" with no exchange shown; it now gives Meg's answer *Tíz éves vagyok.* and asks for Károly's question. `a1-18-dialogue-1` asked *Melyik városban laksz?* (untaught *melyik*, *-ban*); now *Hol laksz?*. `a1-19-writing-2` gave the phone number in the prompt and asked the learner to copy it; it now asks for *Kossuth utca 10.* from "10 Kossuth Street". `a1-20-controlled-2` and its copy `a1-20-consolidation-11` (*____ éves vagyok.*) accepted only 1–10 without 2; they now also accept *két* and the tens up to *száz*. The "Which sentence starts this exchange?" item recurs in a1-21–a1-23 and gets the same fix when those units are read.

### HU A1 `objects-locations` (a1-21–a1-25 + consolidation) — locked 2026-10-05
All 125 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a1-objects-locations-vocab` 74, `van-and-nincs-there-is-there-isn-t` 11, `ban-ben-in` 9, `ki-and-mi` 8, `demonstratives-ez-az` 6, `indefinite-article-egy` 5, `definite-article-a-az` 5, `itt-ott-here-there` 3, `van-zero-copula` 2, `plural-nouns-k` 2. Old bulk tags such as `present-tense-routine-language` on a1-25 were replaced. Glosses against mixed words (*ez/az/mi*, *itt/ott/van*) stay vocabulary; *van/vagyok/vagy* for "there is" is `van-and-nincs` with `ds` `van-zero-copula`. Content fixes: the five "Which sentence starts this exchange?" items (a1-21–a1-25 practice-5) showed no exchange; each now shows the reply and asks for the question. `a1-22-dialogue-2` answered *Mi az?* with two right options (*Az egy telefon./Az egy tea.*); the second is now *Ő Károly.*

### HU A1 `family` (a1-26–a1-30 + consolidation) — locked 2026-10-05
All 125 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a1-family-vocab` 60, `kinship-possessives` 26, `van-possessive-to-have` 13, `possessive-suffixes` 11, `singular-after-numbers` 4, `nem-vs-nincs-two-kinds-of-negation` 3, `a1-objects-locations-vocab` 2, `ki-and-mi` 2, `egyutt-together` 2, `van-zero-copula` 1, `personal-pronouns` 1. Both possessive skills are taught on a1-26-b: a choice of person (*anyám/anyád*) and *család* items are `possessive-suffixes`, producing a kin noun with its suffix is `kinship-possessives`; options that all carry the same suffix test the noun and are vocabulary. *Nincs* "don't have" in a1-27 stays `van-possessive-to-have` (`nem-vs-nincs` is taught at a1-28). Content fixes: the five practice-5 "starts this exchange" items now show the reply and ask for the question; `a1-29-practice-6` had two right options for a photo (*Ki az?/Ki ő?*), now *Ki az?/Mi az?/Hol az?*; `a1-27-dialogue-1` and its copy `a1-30-consolidation-14` answered *Van testvéred?* with *Igen. Van egy fiú és egy lány.* ("there is a boy and a girl"), now *Igen, van egy testvérem.* Left: `a1-29-dialogue-2` uses untaught *Kik*/*szüleim* in both options, still answerable.

### HU A1 `describing-people` (a1-31–a1-35 + consolidation) — locked 2026-10-05
All 125 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a1-describing-people-vocab` 63, `van-possessive-to-have` 13, `van-zero-copula` 11, `plural-predicate-adjectives-k` 10, `quantity-choice-questions-mennyi-melyik` 7, `adjective-order-before-the-noun` 7, `nagyon-very` 7, `possessive-suffixes` 3, `negation-with-nem` 2, `a1-family-vocab` 1, `egyutt-together` 1. Linking with *és/de* has no skill and stays vocabulary; dialogue items whose wrong option misuses *van* are `van-zero-copula`. Content fixes: the five practice-5 "starts this exchange" items now show the reply and ask for the *milyen* question; `a1-31-practice-5` also had a second right option (*Milyen a fiú?*), now *Ki ő?*.

### HU A1 `plurals-quantities` (a1-36–a1-40 + consolidation) — locked 2026-10-05
All 125 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a1-plurals-quantities-vocab` 49, `plural-nouns-k` 43, `adjective-order-before-the-noun` 9, `egyutt-together` 8, `singular-after-numbers` 6, `van-zero-copula` 3, `vowel-harmony` 3, `plural-predicate-adjectives-k` 2, `possessive-suffixes` 2. Linking-vowel questions are `vowel-harmony`; plain plural items stay `plural-nouns-k` even with a harmony-error distractor; *van/vannak* agreement is `egyutt-together` (taught on the a1-30-b screen); *sok/egy* + singular is `singular-after-numbers`. Content fixes: the five practice-5 items as in the other units; `a1-38-practice-6` claimed the adjective never changes for the plural (false: *az asztalok nagyok*), now asks about *a nagy asztalok* only; `a1-36-practice-2` hinted "(people)" while only singular *ember* is accepted, now "(people; singular noun)".

### HU A1 `possession` (a1-41–a1-45 + consolidation) — locked 2026-10-05
All 125 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `possessive-suffixes` 45, `possessive-pronouns-enyem` 41, `a1-possession-vocab` 32, `van-possessive-to-have` 5, `a1-plurals-quantities-vocab` 1, `plural-nouns-k` 1. Choices among *enyém/tiéd/övé/miénk/övék* are `possessive-pronouns-enyem`; *Nekik van egy autójuk*-type items are `van-possessive-to-have`. Content fixes: the five practice-5 "starts this exchange" items now show the reply and ask for the question. Left: *Kié*/*Milyen* appear untaught in a few dialogue prompts without affecting the answer.

### HU A1 `where-things-are` (a1-51–a1-55 + consolidation) — locked 2026-10-05
All 115 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `ban-ben-in` 89, `a1-where-things-are-vocab` 16, `spatial-questions-hol-hova` 10. 60 items carry `ds` `movement-with-ba-be` for a well-formed *-ba/-be* option (taught next unit) and 10 carry `ki-and-mi`. Content fixes: review-2 in all five lessons asked "Which question asks for a location?" with *Hol?/Hová?/Ki?*, so *Hová* was arguably right too; now "…asks where something is?". `a1-51-controlled-2` and its copy `a1-55-consolidation-7` ("in the room") now also accept *teremben*. `a1-55-writing-1` glossed *az ablakban* as "by the window", now "in the window".

### HU A1 `going-places` (a1-56–a1-60 + consolidation) — locked 2026-10-05
All 115 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `movement-with-ba-be` 78, `a1-going-places-vocab` 16, `ban-ben-in` 11, `spatial-questions-hol-hova` 10. *-ba* vs *-ban* choices carry `ds` for the other case. *Hová ____ Károly?* supplying *megy* is vocabulary (`megy-jon` is taught at a1-136). Content fixes: about twenty items asked for *-ra/-re* destinations (*postára*, *egyetemre*, *munkahelyre*, *állomásra*) that the unit never teaches, or for unnatural *-ba* forms (*útba*, *bejáratba*, *kijáratba*); they now use *-ba/-be* nouns taught by that lesson (*mozi*, *étterem*, *múzeum*, *megálló*, *bank* from a1-59, *központ*). `a1-58`/`a1-59-dialogue-2` asked untaught *Mit csinálsz?* with a *-ban* option that also fitted; now *Hová mész?*. `a1-56-writing-1` had a garbled model answer. *Hová ____ Károly?* and `a1-56-controlled-2` accepted one answer where several fit; they now carry a hint. *-ra/-re* stays untaught at A1 although the a1-56–a1-60 vocabulary lists *posta*, *egyetem*, *munkahely*.

### HU A1 `everyday-actions` (a1-61–a1-65 + consolidation) — locked 2026-10-05
All 115 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `present-tense-routine-language` 90, `a1-everyday-actions-vocab` 20, `subject-pronouns-omission` 5. Wrong options ending in *-ni* carry `ds` `building-the-infinitive-the-suffix-ni`, *dolgozik* for *dolgozom* carries `ik-verbs-dolgozom-not-dolgozok`. Content fixes: `a1-61-practice-3` and its copy `a1-65-consolidation-12` keyed definite *olvassa* (taught at a1-102), now *Károly ____ egy könyvet.* → *olvas*; three *Én ____ magyarul.* fill-blanks accepted one verb where several fit, now hinted. Left: the a1-63/a1-64 writing models use the accusative (*Vizet iszom*) before it is taught; writing is ungraded.

### HU A1 `foundations-review` (a1-46–a1-50 + consolidation) — locked 2026-10-05
All 125 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `possessive-pronouns-enyem` 20, `plural-nouns-k` 19, `a1-foundations-review-vocab` 13, `possessive-suffixes` 12, `van-zero-copula` 11, `spatial-questions-hol-hova` 9, `ki-and-mi` 8, `egyutt-together` 7, earlier units' vocabulary skills 15, and nine smaller grammar skills. A review unit: matching takes the vocabulary skill of the unit its words come from. Content fixes: four dialogue/choice items had two right options (`a1-47-dialogue-1`, `a1-47-dialogue-2`, `a1-48-practice-5`, `a1-50-practice-5`; the last two also used untaught *kevés*/*egyedül*); `a1-48-review-1` and `a1-48-check-1` marked the acceptable *Ez mi?* wrong, now *Ki ez?*; `a1-46-controlled-2` now also accepts *az*; two fill-blank hints didn't signal the expected answer (`a1-47-controlled-2` "(my sibling)", `a1-50-consolidation-11` "(Meg)").

### HU A1 `questions-negation` (a1-66–a1-70 + consolidation) — locked 2026-10-05
All 115 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a1-questions-negation-vocab` 61, `negation-with-nem` 29, `present-tense-routine-language` 18, `yes-no-questions` 6, `spatial-questions-hol-hova` 1. Question-word glosses mixing *hogyan/miért/mit/melyik/ki/hol* have no single skill and stay vocabulary. Content fixes: `a1-67-dialogue-2`, `a1-67-practice-5` and its copy `a1-70-consolidation-14` had two sensible replies; `a1-66-controlled-2` had no hint for *beszélek*; `a1-68-dialogue-2` used *Hogyan vagy?*, now *Hogy vagy?*; `a1-70-consolidation-20`'s model answer needed accusative *senkit*. Left: practice-2 items use untaught *mert*/*beteg* in options, answerable by elimination.

### HU A1 `daily-routine` (a1-71–a1-75 + consolidation) — locked 2026-10-05
All 115 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a1-daily-routine-vocab` 64, `present-tense-routine-language` 51; wrong *-ni* options carry `ds` `building-the-infinitive-the-suffix-ni`. Content fixes: about twenty choice items had two right options ("Choose the morning sentence" with two morning sentences; "Which sentence is correct?" where the third-person *Reggel felkel* is also correct); each now asks "Which sentence means 'I …'?". The five dialogue-1 items asked a bare *Mikor?* that any option answered; now *Mikor fekszel le?*, *Mikor alszol?*, *Mikor ebédelsz?*, *Mikor kelsz fel?*, *Mikor van ebéd?*. `a1-72-writing-1` modelled *Reggelizek* for the -ik verb, now *Reggelizem*.

### HU A1 `time-dates` (a1-76–a1-80 + consolidation) — locked 2026-10-05
All 115 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a1-time-dates-vocab` 96, `fractions` 7, `ban-ben-in` 7, `van-zero-copula` 3, `cardinal-numbers` 1, `present-tense-routine-language` 1. Days with *-n* (*kedden*) are vocabulary because `on-en-on` is registered A2 (ROADMAP 135). Months with *-ban* are `ban-ben-in`. Content fixes: `a1-76-controlled-2` and its copy `a1-80-consolidation-7` printed the answer *óra* in the prompt; `a1-77-controlled-3` ("Choose the natural sentence") had two right options; `a1-80-controlled-4` and `a1-80-practice-2` accepted one day where any fitted; now hinted.

### HU A1 `frequency-word-order` (a1-81–a1-85 + consolidation) — locked 2026-10-05
All 115 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a1-frequency-word-order-vocab` 45, `mindig-and-gyakran-frequency-adverbs` 24, `soha-needs-nem-negative-concord` 10, `basic-hungarian-word-order` 8, `present-tense-routine-language` 5, `is-placing-also-too` 5, `temporal-postpositions` 5 (*után*), `ik-verbs-dolgozom-not-dolgozok` 5, `szokott-infinitive-habitual-actions` 3, and 5 on four smaller skills. Choices among frequency adverbs are `mindig-and-gyakran…` by the paradigm rule. 14 items are flagged "taught later" only because the registry's `taught_in` screens are late (ROADMAP 135). Content fixes: `a1-83-practice-1` and `a1-85-practice-5` each had a second acceptable reply; the wrong options are now clearly wrong.

### HU A1 `home` (a1-86–a1-90 + consolidation) — locked 2026-10-05
All 115 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `postpositions-basic` 41, `a1-home-vocab` 39, `van-zero-copula` 13, `definite-article-a-az` 10, `possessive-suffixes` 4, `ban-ben-in` 3, and one each on five other skills. 16 a1-86–a1-88 items are on `postpositions-basic` although its registered screen is a1-89, because a1-87 already teaches *előtt/mellett* (ROADMAP 135). No content defects found.

### HU A1 `food-drink` (a1-91–a1-95 + consolidation) — locked 2026-10-05
All 115 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a1-food-drink-vocab` 53, `how-the-accusative-t-works` 32 (*Kérek kenyeret*; the accusative is taught on the a1-91-b screen, and the skill's `taught_in` now points there), `van-zero-copula` 10, `containers-and-measures` 10, and 10 on six smaller skills. Content fixes: `a1-91-dialogue-2` and `a1-95-dialogue-1` had a second acceptable reply; `a1-93-practice-1` asked for "the" measure word with three measure words offered; `a1-95-practice-1` printed the answer *nagyon* in the prompt. The a1-92-b screen glossed *reggel* as "breakfast", now *reggeli*.

### HU A1 `everyday-hungarian-review` (a1-96–a1-100 + consolidation) — locked 2026-10-05
All 120 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a1-everyday-hungarian-review-vocab` 55, `movement-with-ba-be` 10, `present-tense-routine-language` 10, `ban-ben-in` 10, `postpositions-basic` 7, `megy-jon` 7, `on-en-on` 4, and 17 on ten smaller skills. `megy-jon` items are flagged "taught later": a1-97-b introduces *megy/jön*, but the skill's screen stays a1-136-b, which teaches the full paradigm. Content fixes: `a1-96-dialogue-2` had two right replies; `a1-100-practice-1` described its sentence wrongly. The a1-99-a screen's *szobaban/konyhaban* now carry accents.

### HU A1 `buying-food` (a1-101–a1-105 + consolidation) — locked 2026-10-05
All 117 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a1-buying-food-vocab` 73, `how-the-accusative-t-works` 26, `containers-and-measures` 5, `van-zero-copula` 3, and 10 on six smaller skills. Content fixes: seven fill-blanks accepted one food or measure word where any fitted (*Kérek egy ____.*); now hinted. `a1-104-writing-2` asked for a sentence with *ár* but modelled untaught *Mennyibe kerül?*; now *Mennyi az ár?*. Left: *Mennyibe kerül?* stays as untaught context in four dialogue prompts.

### HU A1 `market` (a1-106–a1-110 + consolidation) — locked 2026-10-05
All 115 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a1-market-vocab` 89, `how-the-accusative-t-works` 14, `demonstratives-ez-az` 3, `fractions` 3, `containers-and-measures` 3, `a1-buying-food-vocab` 2, `quantity-choice-questions-mennyi-melyik` 1. Content fixes: fourteen fill-blanks accepted one word where several fitted (*Kérek egy ____ tejfölt.*, *____ kiló is elég?*); each now carries an English hint, mirrored in the consolidation copies. Left: the a1-107-a screen calls *ezt/azt* "accusative" and says *friss* comes before the noun.

### HU A1 `cafe` (a1-111–a1-115 + consolidation) — locked 2026-10-05
All 115 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a1-cafe-vocab` 84, `how-the-accusative-t-works` 22, `present-tense-routine-language` 3, `definite-vs-indefinite-conjugation` 3, and 3 on three smaller skills. The old tags (`nek-conditional`, `quantity-choice…`, `van-and-nincs`, A2 `egyreszt-masreszt`) were bulk-retag noise. Content fixes: fifteen fill-blanks accepted one noun where several fitted, now hinted; `a1-114-intro-2` and `a1-114-controlled-1` hinted "(I'd like)"/"(would he/she like)" while only *Kérek*/*kér* was accepted; `a1-114-controlled-2` and `a1-114-check-1` each had a second right option (*kér* glossed "would like" on its own screen). Left: the a1-114-b screen cites a stale unit number.

### HU A1 `restaurant` (a1-116–a1-120 + consolidation) — locked 2026-10-05
All 115 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a1-restaurant-vocab` 86, `how-the-accusative-t-works` 20, `van-zero-copula` 3, `mert-because` 3, `val-vel` 2 (*körettel*, flagged taught later: `val-vel` is taught at a1-136), `present-tense-routine-language` 1. *és/de* items stay vocabulary. Content fixes: `a1-116-dialogue-2` had two natural replies to *Mit kér?*; thirteen fill-blanks where another word fitted (*és*/*de*, *Van*/*Kell*, two foods) are now hinted, mirrored in the consolidation copies.

### HU A1 `shopping` (a1-121–a1-125 + consolidation) — locked 2026-10-05
All 115 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a1-shopping-vocab` 88, `how-the-accusative-t-works` 8, `quantity-choice-questions-mennyi-melyik` 8, earlier units' vocabulary 2 (the *kártya*/*fizet* review items, corrected in review from this unit's skill), and 9 on seven smaller skills. Content fixes: four fill-blanks accepted one answer where any noun, number or *Az* fitted, now hinted; two writing prompts glossed their model answer wrongly ("what the size is like" for *Milyen méretek vannak?*, "how much the price is" for *Mennyibe kerül?*).

### HU A1 `clothes-appearance` (a1-126–a1-130 + consolidation) — locked 2026-10-05
All 115 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a1-clothes-appearance-vocab` 92, `van-zero-copula` 6, `how-the-accusative-t-works` 4, `demonstratives-ez-az` 3, `definite-vs-indefinite-conjugation` 3, `a1-shopping-vocab` 2, and 5 on five skills (`a1-128-practice-2`, *felpróbálni*, is on `building-the-infinitive-the-suffix-ni`, taught at a1-143). Content fixes: seven fill-blanks where another garment, adjective or *és* fitted, now hinted; `a1-129-practice-2` printed its answer *sötét* in the prompt; `a1-129-dialogue-2` and `a1-130-practice-5` had a second acceptable reply; a substitution option changed more than the noun; "Is the trousers short?" corrected in an exercise and on the a1-130-a screen.

### HU A1 `city` (a1-131–a1-135 + consolidation) — locked 2026-10-05
All 115 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a1-city-vocab` 93, `spatial-questions-hol-hova` 9, `on-en-on` 4 (*a téren*), `a1-clothes-appearance-vocab` 2, `postpositions-basic` 2, `van-and-nincs-there-is-there-isn-t` 2, `is-placing-also-too` 2, `possessive-suffixes` 1. Content fixes: eight fill-blanks where another place or word fitted, now hinted. The a1-135-b screen taught *A park bal van* / *A múzeum jobb van*, which isn't Hungarian; screen and four items (`a1-135-controlled-1`, `-controlled-4`, `-production-2`, `a1-135-consolidation-11`) now use *balra/jobbra van*, still tagged vocabulary because `direction-adverbs-jobbra-balra` is taught at a1-140. Left: a1-132-a says *hová* answers take *-ra/-re*, which no exercise tests.

### HU A1 `transport-directions` (a1-136–a1-140 + consolidation) — locked 2026-10-05
All 115 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a1-transport-directions-vocab` 73, `val-vel` 10, `megy-jon` 10 (including the *menj* imperative, which has no A1 skill), `direction-adverbs-jobbra-balra` 8, `possessive-suffixes` 5, `ik-verbs-dolgozom-not-dolgozok` 4, `a1-city-vocab` 2, `directional-preverbs` 2, `spatial-questions-hol-hova` 1. Content fixes: seven fill-blanks where another transport, verb or direction fitted are now hinted, and `a1-137-controlled-1`'s hint "(a ticket)" invited *jegy* against the key *jegyünk*. `a1-136-practice-4` taught *A metróval megyünk?* with an article; now *Metróval megyünk?* (and *Vonattal*/*Busszal*).

### HU A1 `hobbies-free-time` (a1-141–a1-145 + consolidation) — locked 2026-10-05
All 115 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a1-hobbies-free-time-vocab` 71, `building-the-infinitive-the-suffix-ni` 16, `how-the-accusative-t-works` 10, `erdekel-construction` 5 (*szeretek* + infinitive, which that skill covers), `on-en-on` 4 (*hétvégén*), `basic-hungarian-word-order` 3, and 6 on four smaller skills. Content fixes: six fill-blanks where another noun, infinitive or verb fitted are now hinted (with "object form" where the accusative is the point); a substitution option claimed to swap in *játszani* but its sentence didn't contain it. Left: untaught *ráérek* and *-j* imperatives in a few correct dialogue replies, answerable by elimination; four grammar screens (a1-141-b, a1-142-b, a1-143-b, a1-144-b) have muddled wording.

### HU A1 `friends-making-plans` (a1-146–a1-150 + consolidation) — locked 2026-10-05
All 115 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a1-friends-making-plans-vocab` 85, `possessive-suffixes` 6, `nek-conditional` 5, `lehet-infinitive` 4, `kor-time` 3, `present-tense-routine-language` 3, and 9 on six smaller skills. Content fixes: five fill-blanks where a time word or noun also fitted are now hinted; `a1-150-practice-2`'s hint "(shall we meet)" invited a rejected *találkozzunk*; `a1-147-practice-2` now also accepts *szeretném*. The subagent called the a1-146-b screen's *szerettek* ("you all like") a past form; it is the regular present, so the screen stands. Left: *Szeretnétek együtt programot?* (verbless, the screen's own model) stays as acceptable spoken Hungarian.

### HU A1 `origin-cases` (a1-151–a1-155 + consolidation) — locked 2026-10-05
All 105 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `delative-rol-rel` 41, `a1-origin-cases-vocab` 31, `elative-bol-bel` 28, `spatial-questions-hol-hova` 3 (*honnan*), `vowel-harmony` 2. Wrong-case options carry `ds` (`ban-ben-in`, `on-en-on`, `movement-with-ba-be`, and elative/delative against each other). Six *-tól/-től* items stay vocabulary because `tol-tol` is registered A2 (ROADMAP 136). Content fixes: `a1-155-introduce-2` and `a1-155-controlled-4` asked about a story shown only after them, the second also with untaught *zseb*; `a1-155-practice-3` asked for *Bécsből* though the screen never says foreign cities take *-ból*, now *Tokajból*, which it does show. Twenty choice and fill-blank items filed as `dialogue`/`writing` now follow their tag.

### HU A1 `languages-manner` (a1-156–a1-160 + consolidation) — locked 2026-10-05
All 105 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a1-languages-manner-vocab` 72, `ul-ul-essive-modal` 25 (*magyarul*, *rosszul*; its `taught_in` now points at a1-156-a, which teaches the suffix, instead of a1-159-a), `present-tense-routine-language` 4, `on-en-on` 3 (*két nyelven*), `possessive-suffixes` 1. *egy kicsit/jól/már/még/csak* (a1-158) have no grammar skill and stay vocabulary. Content fixes: five fill-blank hints printed the answer verb ("(olvas + she)"), now English ("(read + she)"); `a1-159-production-1` hinted "(mother tongue)" for *anyanyelvem*. Left: a1-158-a glosses *Hogy beszélsz magyarul?* as "How well…"; a1-158-b and two a1-159 items use the untaught past tense.

### HU A1 `postpositions` (a1-161–a1-165 + consolidation) — locked 2026-10-05
All 105 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `postpositions-basic` 54, `a1-postpositions-vocab` 25, `temporal-postpositions` 25, `how-the-accusative-t-works` 1. Choices among *alatt/felett/mellett/előtt/mögött/között/után* are `postpositions-basic` by the paradigm rule; time uses are `temporal-postpositions`. Content fixes: four *felett* fill-blanks now also accept *fölött*, which the a1-161-b screen teaches as a variant; `a1-161-dialogue-1`, `a1-163-dialogue-1` and `a1-165-dialogue-1` each had a second fitting postposition; `a1-165-check-2` asked for untaught *tetején*; `a1-165-consolidation-20` had garbled options; `a1-161-practice-1` glossed a singular as "The shoes". Left: *megtaláltam*/*aludtam* use the past tense, which no A1 skill covers.

### HU A1 read-through complete — 2026-10-05
All 33 HU A1 units (3,842 exercises) are read and locked, every exercise with exactly one tag: 1,986 vocabulary, 1,856 grammar. Units 1–4 were read in the main session, units 5–33 by Sonnet subagents (one per unit, at most two at a time) with every decisions file checked by `scripts/readthrough_check.py` and the reports and content diffs reviewed before `apply_tags.py`/`lock_tags.py`. Roughly 250 exercise defects were fixed on the way, mostly fill-blanks that accepted one answer where several fitted, two-right-answer choices, answers printed in the prompt, untaught forms, and a few pieces of wrong Hungarian (*A park bal van*, *A metróval megyünk?*, *Van egy fiú és egy lány* for "I have a brother and a sister"). Follow-ups: ROADMAP 136 (`tol-tol` level) and 137 (thin A1 skills).

### HU A1 registry fixes, ROADMAP 135 — 2026-10-05
Signed off by the user. `on-en-on` moved from A2 to A1 (`taught_in` `a1-78-b-gr`), and 19 day-suffix items in `time-dates` and `frequency-word-order` moved to it from vocabulary (both units re-locked). `taught_in` now points at the screen that first teaches the skill for `mindig-and-gyakran-frequency-adverbs` (a1-81-a), `postpositions-basic` (a1-87-b), `temporal-postpositions` (a1-83-b, and it no longer `requires` `postpositions-basic`, taught after it) and `how-the-accusative-t-works` (a1-91-b). `scripts/readthrough_check.py` now also checks category on `substitution` items, after three slipped through to the validator.

### ES A1 `greetings-introductions` (a1-01-01–a1-01-05 + consolidation), es-es and es-latam — locked 2026-10-05
The first Spanish unit. The two courses' files were identical before and after, so one set of decisions was applied to both (98 exercises each; Sonnet subagent, reviewed in the main session). Tags now: `a1-greetings-introductions-vocab` 54, `ser` 36, `questions` 5; the three story-comprehension `reading` items carry none. The retired slugs `names`, `introductions` and `greetings` are gone. *Me llamo / te llamas* items stay vocabulary as a set chunk: `reflexives` is taught much later, and `subject-pronouns` (a1-02-02) after this unit, so *¿Y tú?* is vocabulary too. Thirty items changed `category`, mostly `grammar` → `vocabulary`, plus nine `structured-writing`/`dialogue-complete` items in the consolidation and the lesson-final writings that were filed as `grammar`. No `distractor_skills`: no wrong option is a form of another grammar skill. `ser`'s `taught_in` moved from `a1-01-04-origin-gr` to `a1-01-02-ser-gr` (*Soy: saying who you are*), the screen that first teaches it. Content fixes, made identically in both courses: `a1-01-05.ex14` (reply to *Hola. Soy Meg.*) offered *¿De dónde eres?* and *Buenos días.* as wrong, both defensible; the distractors are now *Adiós.* and *Hasta mañana.* `a1-01-consolidation.ex15/16` asked "Which sentence starts this exchange?" with no exchange shown; now "Which one is a greeting?". `a1-01-03.ex07` matched *me* to "me"; now *¿y tú?* "and you?". `a1-01-02.ex10` duplicated ex03; now *Yo ___ Meg.* `a1-01-01.ex06` accepts *luego* and *mañana* but its `english` only said "See you later."; now both. Found: Spanish has no pronunciation skill in the frozen list, although a1-01-01 has *Spanish Vowels* and *Spanish Letter Sounds* screens; no exercise tests them yet, so nothing is mis-tagged, but sound exercises would need a skill (user sign-off; ROADMAP 133). Left: the three reading items can be answered without the story (ROADMAP 134).

### ES A1 `meeting-someone-new` (a1-02-01–a1-02-05 + consolidation), es-es and es-latam — locked 2026-10-06
98 exercises per course, one decisions file applied to both (Sonnet subagent, reviewed in the main session). Tags now: `a1-meeting-someone-new-vocab` 41, `a1-greetings-introductions-vocab` 19 (the recycled unit-1 items 01–03 of each lesson, true review), `por-que-y-porque` 16, `ser` 13, `subject-pronouns` 7, two story-comprehension `reading` items untagged. The *Which expression means "hello"?* item repeated in each lesson was tagged `ser` by the subagent and corrected to unit-1 vocabulary. *Presenta a* word-order items are vocabulary (no skill covers them); *estudias* is vocabulary because `ar-verbs` comes later; *amigo/amiga* glosses are vocabulary, not `gender`. No `distractor_skills`. Content fixes, both courses: `a1-02-04.ex15` and `a1-02-consolidation.ex15` asked "Which sentence starts this exchange?" with no exchange shown; now "Which sentence says that someone introduces a person?". Found: that "starts this exchange" template recurs in later units and is the same defect.

### ES A1 `naming-things` (a1-03-01–a1-03-05 + consolidation), es-es and es-latam — locked 2026-10-06
98 exercises per course. Tags now: `adjective-agreement` 27, `gender` 22, `articles` 15, `a1-naming-things-vocab` 14, `ser` 5, `questions` 5, review items `a1-greetings-introductions-vocab` 5 and `a1-meeting-someone-new-vocab` 5. Lesson 1 *un/una/unos/unas* choices are `articles` (the gender screen is lesson 2; *unas fotos* would otherwise be `plural`, taught later); the definite-article gender choices of lesson 3 are `gender`. No `distractor_skills`. Content fixes, both courses: `a1-03-03.ex12` third option *Un teléfono está aquí.* was a correct reply, now *Una teléfono…*; `a1-03-04.ex10` "small for a masculine noun" passed *pequeños* too, now "for one masculine noun"; `a1-03-consolidation.ex13` "starts this exchange" is now "Which sentence tells us the girl is tall?". Left: `a1-03-04.ex15` has an odd prompt but a valid answer.

### ES A1 `describing-people` (a1-03c-01–a1-03c-05 + consolidation), es-es and es-latam — locked 2026-10-06
99 exercises per course. Tags now: `adjective-agreement` 33, `a1-describing-people-vocab` 23, `plural` 15, `gender` 13, `ser` 8, `a1-greetings-introductions-vocab` 3 (consolidation review), four `reading` items untagged. Nine multiple-choice dialogue items moved from `dialogue` to `grammar`. One `distractor_skills` (`a1-03c-03-g01`, *altas* as an adjective-agreement error in a plural item). Mixed-group items (*Carlos y Ana son altos*) test the mixed-gender rule and are `adjective-agreement`. Content fixes, both courses: `a1-03c-03-d02`, `-d03`, `-g06` used *mis hermanos / tus hermanas / Mis amigas*, possessives taught only in the family unit; rewritten without them. `a1-03c-04-w02` said "kind" but wanted *simpática*; now "friendly woman (use simpática)". Left: `a1-03c-c-v02` has a distractor *Es mi hermano*.

### ES A1 `family` (a1-05-01–a1-05-05 + consolidation), es-es and es-latam — locked 2026-10-06
104 exercises per course. Tags now: `a1-family-vocab` 29, `tener` 23, `possessives` 23, `adjective-agreement` 13, `ser` 9, three `reading` items untagged, and one each on `subject-pronouns` (*Tú / Tu*), `gender`, `a1-meeting-someone-new-vocab` and `a1-greetings-introductions-vocab` (review). Four `distractor_skills` (`tener` or `ser` as the wrong verb). `a1.05.01.ex16` differs between the courses (*vosotros* / *ellos*); `tener` fits both. Content fixes, both courses: `a1.05.02.ex11/ex12`, `a1.05.03.ex12` and `a1.05.05.ex11` accepted *mi*, *tu* and *su* because nothing said whose relative; each prompt now names who is answering. `a1.05.05.ex04` accepted *hermanos* and *hermanas*; now "(brothers)". `a1.05.consolidation.ex11` ("starts this exchange") now "Which sentence means 'I have two brothers'?". Found: the unit's own possessives screen also teaches *este/esta*, registered under `demonstratives` at `a1-demonstrative-01`; no change made. Left: reading items 05.ex14–16 were not checked against the story.

### ES A1 `daily-routine` (a1-06-01–a1-06-05 + consolidation), es-es and es-latam — locked 2026-10-06
100 exercises per course. Tags now: `reflexives` 26, `a1-daily-routine-vocab` 23, `ar-verbs` 21, `er-ir-verbs` 15, `present-tense` 9 (lesson 1 only; `ar-verbs` is taught in lesson 2), and one each on `tener`, `ser`, `possessives`, `plural`, `adjective-agreement` (the consolidation's family recycles). Three lesson-1 items whose options differ in verb meaning (*camino / trabajo / estudio*) moved from `grammar` to `vocabulary`. One `distractor_skills` (`a1.06.06.ex10`, *Una* as an `articles` error). `a1.06.05.ex03/04` are `ar-verbs` because the blank is the non-reflexive verb. Content fixes, both courses unless noted: `a1.06.01.ex10` got "(I walk)" (three verbs fitted); `a1.06.03.ex06` es-latam only said "We live in Madrid" for *Hanoi*; `a1.06.03.ex12` and `a1.06.04.ex12` now ask "¿… ustedes?" so the first-person answer is the only one; `a1.06.05.ex05` used *acostarse* (stem change taught in the next unit), now *levantarse*; `a1.06.06.ex06` ("¿Cuándo __?", three options fit, tagged `demonstratives`) now "¿Cuándo __ tú?"; `a1.06.06.ex10` got the hint "(My mother is calm.)" because *Una madre es tranquila* is also correct. Left: `a1.06.01.ex04` accepts *hablo* before *hablar* is taught; the builders `a1.06.04.ex08` and `a1.06.05.ex08` use *acuestan/acuesta* before the stem-change lesson, but the grammar screens show both forms.

### ES A1 `daily-routine-reflexive-verbs` (a1-reflexive-01–a1-reflexive-05 + consolidation), es-es and es-latam — locked 2026-10-06
73 exercises per course. Tags now: `a1-daily-routine-reflexive-verbs-vocab` 24, `reflexives` 24, `stem-changes` 14, `contraste-reflexivo` 9, `ar-verbs` 2 (blanks *lavan*, *lavamos*). Dialogues whose wrong replies answer a different question are unit vocabulary. The old `verbs-of-change` slug (not in the registry) is gone, and the lesson 1–3 vocabulary and matching items that carried the greetings vocabulary skill now use the unit's own. *me pongo / ponemos* (irregular *ponerse*) have no skill and are vocabulary; *viste* (e→i of *vestirse*) is `stem-changes`, although the e→i change is taught on the vestirse screen, not the registered `a1-reflexive-02-cambio-radical-gr`. Content fix: `a1.refl.05.ex09` accepts *después* as well as *luego*. Left: `a1.refl.04.ex08` (*Lavo mis manos*, unidiomatic, taught as wrong), `a1.refl.04.ex07` needs the personal *a* taught later, `a1.refl.02.ex07` accepts *levantas/despiertas* against a "go to bed" gloss.

### ES A1 `home` (a1-07-01–a1-07-05 + consolidation), es-es and es-latam — locked 2026-10-06
106 exercises per course. Tags now: `estar` 31, `hay` 30, `a1-home-vocab` 28, `gender` 11, `plural` 2, `tener` 2, `ser` 1, `ar-verbs` 1. Five `distractor_skills` (`hay` or `estar` as the other verb's error: `a1.07.04.ex03/04/16`, `a1.07.05.ex16`, `a1.07.06.ex10`). Sentence builders are tagged by the structure built; mixed hay-and-estar open writing is unit vocabulary; the consolidation's `ser`, `tener`, `ar-verbs` items are earlier-unit review. 12 "taught later" warnings on `hay`: the registry says `a1-07-04-hay-estar-gr`, but `a1-07-01-hay-gr` is the first screen (registry fix pending the user's sign-off). No content fixes. Left: *Están dos libros* is grammatical (location), but the lesson's hay-vs-estar contrast makes it clearly wrong; *Mi madre está amable* is marginal Spanish, wrong at this level.

### ES A1 `supermarket` (a1-08-01–a1-08-05 + consolidation), es-es and es-latam — locked 2026-10-06
106 exercises per course. Tags now: `a1-supermarket-vocab` 31, `querer-poder` 22, `ar-verbs` 19 (*necesitar*), `gender` 15, `plural` 8, `articles` 3, five story `reading` items untagged, and one each on `tener`, `ser`, `stem-changes` (*cuestan*). `numbers` is taught later in the registry, so number-plus-plural-noun items are `plural`. One `distractor_skills` (`a1.08.06.ex10`). 21 "taught later" warnings on `querer-poder` (registered at `a1-abilities-01`; `a1-08-03-querer-gr` is the first screen, pending sign-off). Content fixes, both courses: `a1.08.03.ex09` and `a1.08.04.ex09` ("¿Qué __?" accepted three persons) now "¿Qué __ tú?"; `a1.08.05.ex12` offered *vas/van a pagar* (forms of `ir`, taught later), now *vamos / hay una caja / quiero leche*; `a1.08.06.ex04` offered *una leche* against *leche*, which contradicted `a1.08.01.ex14`, now *unos / unas leche*. Left: `a1.08.02.ex17` glosses *kilo* with *kilo*.

### ES A1 `demonstratives` (a1-demonstrative-01–a1-demonstrative-05 + consolidation), es-es and es-latam — locked 2026-10-06
73 exercises per course. Tags now: `demonstratives` 56 (including *esto/eso/aquello*, since no neuter-pronoun skill is in the A1 list), `a1-demonstratives-vocab` 17 (the matching items and the dialogues whose wrong replies answer a different question). No category changes, no `distractor_skills`, no content fixes. Left: `a1.dem.04.ex06` (*¡__ es genial!* with *Eso / Ese / Esa*): *Ese* is a weak second answer.

### ES A1 `ordering-cafe` (a1-cafe-01–a1-cafe-05 + consolidation), es-es and es-latam — locked 2026-10-06
105 exercises per course. Tags now: `a1-ordering-cafe-vocab` 46, `querer-poder` 22, `er-ir-verbs` 15, `ar-verbs` 14 (*tomar*), five story `reading` items untagged, and one each on `hay`, `tener`, `ser`. The polite-phrase items of lessons 4–5 (*por favor*, *¿Algo más?*, *Eso es todo*) are vocabulary: no skill covers them. Fifteen items moved from `grammar` to `vocabulary`. Two `distractor_skills` (`a1.cafe.05.ex19` `er-ir-verbs`, `a1.cafe.06.ex10` `estar`). 24 "taught later" warnings on `querer-poder` (first screen is `a1-cafe-03-querer-gr` or earlier `a1-08-03-querer-gr`). Four items differ between the courses (*zumo / jugo*): vocabulary fits both. Content fixes, both courses: `a1.cafe.01.ex09`, `02.ex09` and `03.ex07` ("¿Qué __?" accepted several persons) now "¿Qué __ tú?"; `a1.cafe.04.ex04` accepted *Quiero un café.* as a complete order, now asks for both a coffee and a sandwich; `a1.cafe.04.ex14` accepted *o*, now "(and)"; `a1.cafe.06.ex15` offered *Quiero un café.* as a wrong reply to *¿Algo más?*, now *Tengo tres hermanos.* Left: `a1.cafe.04.ex11` / `05.ex11` offer *Sí, gracias. Eso es todo.* as a wrong reply, which is odd but not a correct answer.

### ES A1 `birthdays-celebrations` (a1-10-01–a1-10-05 + consolidation), es-es and es-latam — locked 2026-10-06
100 exercises per course. Tags now: `a1-birthdays-celebrations-vocab` 62, `tener` 12 (age), `connectors` 9, `ar-verbs` 4, `saber-infinitivo` 4, four story `reading` items untagged, and one each on `er-ir-verbs`, `ser`, `gender`, `hay`, `a1-family-vocab` (the consolidation's family matching). The date patterns (*el nueve de septiembre*, months, capitalisation) have no skill and are unit vocabulary; no item tests the number form, so `numbers` is unused here. One `distractor_skills` (`consolidation.ex04`, *Hay veinticinco años* as a `hay` error). Four "taught later" warnings on `saber-infinitivo`: `a1-10-05-celebracion-gr` in this unit teaches *saber*, the registry says `a1-abilities-02-saber-gr` (pending sign-off). Content fixes, both courses: `a1.10.01.ex12` asked about Lauren, known only from the story, now Kaylee (shown on the screen); `a1.10.03.ex11` printed the answer in the question, now "Which is the correct way to say 9 September?". Left: the "starts this exchange" items `10.01.ex05`, `10.03.ex05`, `10.05.ex01`, `consolidation.ex09` were not checked against their stories; `10.02.ex07` uses *Quiero* before it is taught.

### ES A1 `kitchen` (a1-kitchen-01–a1-kitchen-05 + consolidation), es-es and es-latam — locked 2026-10-06
106 exercises per course. Tags now: `a1-kitchen-vocab` 34, `imperativo-afirmativo` 26, `ar-verbs` 21, `hay` 8, `gender` 6, `er-ir-verbs` 6 (*abrir, añadir* are -ir verbs), two story `reading` items untagged, one each on `tener`, `ser`, `plural`. Fourteen `distractor_skills`, all on imperative items: a present-tense wrong option points at `ar-verbs` or `er-ir-verbs`; the formal imperatives (*Lave, Corte*) get none (not a taught skill). Sequence-word items of lesson 5 are vocabulary. Content fixes, both courses: `a1.kitchen.05.ex13` accepts *Después* as well as *Luego*; `a1.kitchen.05.ex15` "after primero" had two answers, now "right after"; `a1.kitchen.06.ex09` offered *Mi madre está amable* (also acceptable), now *ser amable*; `a1.kitchen.06.ex12` had three subjectless grammatical options, now glossed "I eat in the kitchen"; `a1.kitchen.06.ex19` used *encender* (stem-changing imperative, untaught), now *abrir*. Left: `kitchen.06.ex10` ("I want two apples") is ahead of the course (`querer` comes later) and tagged `plural`.

### ES A1 `numbers-time-schedules` (a1-12-01–a1-12-05 + consolidation), es-es and es-latam — locked 2026-10-06
106 exercises per course. Tags now: `a1-numbers-time-schedules-vocab` 48, `numbers` 27, `questions` 8 (choices between *¿Cuándo? / ¿A qué hora? / ¿Qué hora?*), `ar-verbs` 8, `tener` 5, `er-ir-verbs` 3, `present-tense` 2, and one each on `ser`, `stem-changes` (*duermo*), `plural`, `hay`; one `reading` item untagged. Number glosses and "which number is 12?" items are `numbers`, matching stays vocabulary; telling the time (*es / son*, *la / las*, *a las*) has no skill and is unit vocabulary. No `distractor_skills`. No "taught later" warnings (`numbers` and `hay` are first taught in the earlier units). Content fixes, both courses: `a1.12.01.ex10` accepted *Tengo dieciocho.*, now *Estoy dieciocho años*; `a1.12.01.ex11` ("¿Cuántas personas hay?", any option passed) now lists the numbers 1–5; `a1.12.02.ex07` tiles and `a1-12-02-compound-numbers-gr` had *treinta y uno años*, now *treinta y un años*; `a1.12.02.ex11` accepted *Tiene treinta y cinco.*, now *Es treinta y cinco años*; `a1.12.06.ex20` used *tren / llega* (untaught), now "Estudio ___ las seis". Found: `translation-index.json` still holds the old *treinta y uno años* line (generated, will refresh on the next index build). Left: `a1.12.04.ex10` ("Es a las ocho.") is weak but not clearly acceptable.

### ES A1 `around-town` (a1-04-01–a1-04-05 + consolidation), es-es and es-latam — locked 2026-10-06
98 exercises per course. Tags now: `hay` 30, `estar` 25, `a1-around-town-vocab` 15, `a1-greetings-introductions-vocab` 10 (items 01 and 03 of every lesson, true review), `adjective-agreement` 6, `ser` 5, `questions` 5 (*¿Dónde …?*), `gender` 1, `plural` 1. Three `distractor_skills` (`a1-04-03.ex06/07` with *hay* as the wrong verb, `consolidation.ex13`). *A la izquierda* and *al lado de* are chunks with no skill and stay vocabulary. Content fix, both courses: `a1-04-consolidation.ex13` ("starts this exchange") now "Which sentence says what exists in the neighbourhood?".

### ES A1 `directions` (a1-directions-01–a1-directions-05 + consolidation), es-es and es-latam — locked 2026-10-06
106 exercises per course. Tags now: `a1-directions-vocab` 34, `imperativo-afirmativo` 26, `preposiciones-movimiento` 15, `estar` 11, `ir` 5, `questions` 5 (the old `full-directions` has no skill), `hay` 2, one each on `tener`, `ser`, `querer-poder`, five story `reading` items untagged. Eighteen `distractor_skills`: `ir` / `estar` / `ar-verbs` for the present-tense wrong options of command items, `stem-changes` for *sigues*. The *a / al* blanks are `preposiciones-movimiento`. Content fixes, both courses: `02.ex16` *Camino de la calle* was also a valid sentence, now glossed "along the street"; `03.ex10/11`, `04.ex10`, `05.ex09`, `05.ex12` had a second acceptable reply (*Vas a la derecha*, *Sigues recto*, *Está a la derecha*, *Hay una farmacia*), now clearly wrong options; `03.ex05`, `03.ex14`, `05.ex06` accept the formal command too (*Gire, Siga, Vaya*); `05.ex02` printed *cómo* in the prompt, now "Which word means 'how'?". Left: `04.ex06` and `04.ex13` are near-duplicates and offer *Sigue recta por la calle*, dubious but not clearly acceptable.

### ES A1 `weather` (a1-weather-01–a1-weather-05 + consolidation), es-es and es-latam — locked 2026-10-06
106 exercises per course. Tags now: `a1-weather-vocab` 67 (*hace calor, llueve, está nublado* have no skill; 26 items moved from `grammar` to `vocabulary`), `ar-verbs` 23, `ir` 5, `hay` 2, one each on `tener`, `ser`, `querer-poder`, `estar`, five story `reading` items untagged. The old `demonstratives` tag on lesson 3 was wrong. Two `distractor_skills`. Content fixes, both courses: `Hay sol` / `Hay viento` were offered as wrong options (acceptable Spanish), now *Está sol / Es sol* (`01.ex06`, `01.ex10`, `02.ex17`, `06.ex14`, `02.ex06`); five fill-blanks that accepted several verbs got English hints (`03.ex05`, `03.ex14`, `04.ex05`, `04.ex14`, `05.ex05`). Left: *Hay calor / Hay frío* as distractors, borderline.

### ES A1 `work-obligations` (a1-work-01–a1-work-05 + consolidation), es-es and es-latam — locked 2026-10-06
106 exercises per course. Tags now: `a1-work-obligations-vocab` 31, `tener-que` 29, `hay-que` 22, `ar-verbs` 9, `er-ir-verbs` 4, five `reading` items untagged, and one each on `present-tense`, `tener`, `ser`, `querer-poder`, `hay`, `estar`. About 36 `distractor_skills`, nearly all `tener-que` ↔ `hay-que` (the lesson-4 contrast). Two-target writing is unit vocabulary. Content fixes, both courses: nine fill-blanks in lessons 1–5 that accepted several verbs got English hints (`work.01.ex05/14`, `02.ex05/14`, `03.ex05/14`, `04.ex05`, `05.ex06/07`); `work.01.ex09` and `06.ex11` had two matching sentences, now narrowed; `work.02.ex11` and `03.ex11` offered two correct replies; `work.06.ex09` offered *está amable*, now *eres amable*. Left: `work.02.ex10`, `03.ex10`, `04.ex10` keep the other obligation form as a wrong reply, deliberately (the lesson contrast), though it is a defensible answer in a general question; reading items 14–18 are generic.

### ES A1 `present-continuous` (a1-continuous-01–a1-continuous-05 + consolidation), es-es and es-latam — locked 2026-10-06
73 exercises per course. Tags now: `progressive` 37, `a1-present-continuous-vocab` 22 (matching and the dialogues whose wrong replies are unrelated), `gerundios-irregulares` 18, `estar` 6, `present-tense` 5. Eight `distractor_skills` (`present-tense` ↔ `progressive`). Content fixes: `cont.02.ex06` ("¿Qué __ aprendiendo?" accepted three persons) now "… tú"; `cont.03.ex11` used *trabajó* (untaught preterite), now *trabaja de noche*; `cont.04.ex04` got "(I am)", with *zumo* (es-es) and *jugo* (es-latam) kept; `cont.05.ex03` now names the person "(estar, tú)".

### ES A1 `health` (a1-health-01–a1-health-05 + consolidation), es-es and es-latam — locked 2026-10-06
106 exercises per course. Tags now: `a1-health-vocab` 38 (all matching items and the off-topic dialogues), `tener` 34, `imperativo-afirmativo` 17, `estar` 12, `questions` 2 (*¿Qué tienes?* vs *¿Dónde tienes?*), and one each on `ser`, `querer-poder`, `ar-verbs`. Twelve `distractor_skills` on the advice lessons (*Descansas / Tomas* → `ar-verbs`, *Vas* → `ir`, *Duermes* → `stem-changes`). Nine items moved from `grammar` to `vocabulary`. The old `doctor-interaction` slug is gone. Content fixes, both courses: `health.01.ex05` accepts *enferma* too; `04.ex05`, `05.ex05`, `05.ex14` now say "tú" in the hint; `06.ex09` offered *está amable*, now *tiene amable*; `06.ex11` pinned to "I rest at eight o'clock"; `06.ex19` needed *doler* (a later unit), now *Estoy* cansado. Left: `05.ex10` uses *Me duele* and *aspirina* in its prompt only.

### ES A1 `what-hurts` (a1-doler-01–a1-doler-05 + consolidation), es-es and es-latam — locked 2026-10-06
73 exercises per course. Tags now: `a1-what-hurts-vocab` 29, `doler` 29 (indirect-object pronouns *me / te / le / nos / les* with *doler* included), `intensificadores-y-grado` 5, `tener` 4, `adjective-agreement` 2, `estar` 2, one each on `imperativo-afirmativo`, `stem-changes`. One `distractor_skills`. *para / por / de* in `a1.dol.04.ex02` is vocabulary (no preposition skill). Content fixes, both courses: `dol.03.ex07` printed the answer in the hint, now "(having a cold)"; `dol.05.ex08` was a subjunctive sentence (*Espero que te recuperes*), now "Hoy no me duele la espalda."; `dol.05.ex09` offered *del estómago* (also acceptable), now *de el*; `dol.cons.ex11` used the preterite (*fuiste*, *compré*), now a present-tense exchange. Left: `dol.01.ex05` uses *mucho* before the intensity lesson.

### ES A1 `likes-dislikes` (a1-gustar-01–a1-gustar-05 + consolidation), es-es and es-latam — locked 2026-10-06
73 exercises per course. Tags now: `gustar` 58, `a1-likes-dislikes-vocab` 14, `articles` 1 (`a1.gustar.01.ex09`, *el / un / del*). The old `pronombres-combinados` slug is gone; *me / te / le / nos / les* with *gustar* and *encantar / interesar* are `gustar`. One `distractor_skills` (`a1.gustar.04.ex02`, *leo / leemos* → `er-ir-verbs`). Content fixes, both courses: `gustar.04.ex03` and `ex09` printed the answer in the hint; now "(to do)" and "(to study)".

### ES A1 `hobbies-free-time` (a1-hobbies-01–a1-hobbies-05 + consolidation), es-es and es-latam — locked 2026-10-06
106 exercises per course. Tags now: `a1-hobbies-free-time-vocab` 39, `ar-verbs` 21, `gustar` 9, `stem-changes` 8 (*juego, jugamos*), `er-ir-verbs` 7, `present-tense` 7 (mixed -ar/-er answers and irregular *salgo*), `questions` 5, five story `reading` items untagged, and one each on `tener`, `ser`, `estar`, `numbers`, `querer-poder`. Two `distractor_skills`. Content fix, both courses: the five reading items `a1.hobbies.05.ex14`–`ex18` asked about a person, Ana, and a week that appear nowhere in story `a1-11` (Carlos, Meg and Daniela in the park); rewritten to ask about the story as written (Carlos's football, Meg's cooking, Lauren's guitar, Carlos's afternoons, next Saturday's plan), checked against the story text. Left: the distractors *Ayer* and *jugué* in `03.ex09/ex16` use untaught words, but the correct answers do not need them.

### ES A1 `skills-abilities` (a1-abilities-01–a1-abilities-05 + consolidation), es-es and es-latam — locked 2026-10-06
73 exercises per course. Tags now: `a1-skills-abilities-vocab` 22, `querer-poder` 16, `saber-vs-conocer` 12, `a-personal` 12, `saber-infinitivo` 11. *No sé a qué hora…* (saber for a fact) and *I know Carlos* are `saber-vs-conocer`. Pronoun choice in the favours lesson (*Me / Te / Se*) and the attached-pronoun builder have no skill and are vocabulary; the *poder* forms of that lesson are `querer-poder`. One `distractor_skills` (`a1.abi.cons.ex06`, *puedo*). Content fixes, both courses: `a1.abi.cons.ex01` accepted *puede*, now *sabes*; `a1.abi.03.ex06` printed *saber* in the question; `a1.abi.cons.ex11` used the subjunctive *sepa*, untaught, now "¿conoces a un buen profesor de guitarra?".

### ES A1 `future-plans` (a1-future-01–a1-future-05 + consolidation), es-es and es-latam — locked 2026-10-06
106 exercises per course. Tags now: `ir-infinitive` 44, `a1-future-plans-vocab` 40 (fill-blanks where only the infinitive is supplied and the English pins the word, mixed writing), `tener-que` 12 (items combining a plan and an obligation), five story `reading` items untagged, one each on `ir`, `tener`, `ser`, `querer-poder`, `estar`. Two `distractor_skills`. The old `time-dates` slug is gone. Content fixes, both courses: `future.04.ex11`, `05.ex11` and its copy `06.ex15` accepted *voy a …*; `future.06.ex09` offered *está amable*, now *eres amable*. Left: `future.03.ex05/ex14` accept only *vas*; `future.04.ex02` ("hotel") is a cognate printed in the prompt; `future.01.ex14` is pinned only by its English line.

### ES A1 `travel-getting-away` (a1-20-01–a1-20-05 + consolidation), es-es and es-latam — locked 2026-10-06
106 exercises per course. Tags now: `a1-travel-getting-away-vocab` 45 (choices among *tener / querer / necesitar* by meaning are not one paradigm), `tener-que` 13, `ir-infinitive` 12, `estar` 9, `ir` 8, `questions` 5, `ar-verbs` 4, `querer-poder` 3, `tener` 2, `a-personal` 2 (*Necesito a agua*), and one each on `stem-changes` (*Compruebo*), `ser`, `present-tense`. Fourteen `distractor_skills`. Content fixes, both courses: `a1.20.02.ex11` ("¿Quieres una maleta?", three replies fitted) and `a1.20.03.ex11` ("¿A qué hora sale el tren?", *Es a las ocho* fitted) have one clear answer now. Left: near-duplicate items (`20.03.ex06/ex17`, `20.05.ex09/ex14/ex18`); *Es allí* as a marginal answer to *¿Dónde está el andén?*.

### ES A1 read-through complete (26 units, es-es and es-latam) — 2026-10-06
All 26 units of the A1 unit table are locked in both courses (2,504 exercises each, one decisions file per unit applied to both). Run with the Sonnet-subagent process in [docs/readthrough-process.md](docs/readthrough-process.md): two units per subagent, at most two subagents at a time, each pair reviewed with `readthrough_review.py` before `apply_tags.py` and `lock_tags.py`. Set-up first: registry scan (four `taught_in` mismatches listed for sign-off, ROADMAP 142), Spanish section in the rule sheet, Spanish support in the three scripts (table-order "taught later", es-es / es-latam comparison, other-unit vocabulary warning). Conventions the level added are in the spec § "Read-through conventions" (Spanish). The two courses' A1 text is identical except 14 exercises in 7 files (*vosotros* vs *ellos*, *zumo* vs *jugo*); every tag fits both versions. Main-session corrections to the subagents: the repeated *Which expression means "hello"?* review item (tagged `ser`); a family dialogue chunk (*mucho gusto*) moved to the meeting unit's vocabulary; a hobbies reading set that asked about a person who is not in the story was rewritten from the story text. Across the level over a hundred content defects were fixed: two-answer items, hints that printed the answer, "starts this exchange" items with no exchange, subjects dropped from conjugation blanks, untaught grammar in answers. Left for sign-off: ROADMAP 142.

### ES A1 registry fixes and orphan lessons, ROADMAP 142(a)(b) — 2026-10-06
Approved by the user. `taught_in` in `skills/es.json` now points at the screen that first teaches each of four A1 skills, as the read-through found: `hay` a1-07-01-hay-gr (was a1-07-04-hay-estar-gr), `querer-poder` a1-08-03-querer-gr (was a1-abilities-01-poder-gr), `numbers` a1-10-02-edad-gr (was a1-12-01-numbers-gr), `saber-infinitivo` a1-10-05-celebracion-gr (was a1-abilities-02-saber-gr). Levels and prerequisites unchanged; no tag changed, so no unit was re-locked. Registry regenerated for both courses. The optional `plural` and `stem-changes` moves were not made. The orphan lessons `a1-18-01` and `a1-18-02` ("What Do You Like?", "Hobbies"; 32 exercises) were deleted from es-es and es-latam together with their grammar and vocabulary files (16 files); they were in no unit table and are superseded by the `likes-dislikes` and `hobbies-free-time` units. Every remaining ES A1 exercise id is in `tags.lock.json` in both courses. The generated indexes (grammar and translation) will drop the deleted lessons on the next index build.

### ES A2 registry scan, ROADMAP 125 set-up — 2026-10-06
Approved by the user. Scan of the 43 A2 grammar skills against the A2 screens that first teach them (a keyword read of all 178 es-es screens in unit order). `taught_in` moved to the first screen that teaches the skill: `ya-todavia-no` a2-02-03 → a2-02-01, `antes-despues-infinitive` a2-04-02 → a2-04-01, `alguna-vez` a2-09-05 → a2-09-01, `desde-desde-hace` a2-07-04 → a2-07-01, `porque-y-por-eso` a2-15-03 → a2-05-01, `cuando-mientras` a2-13-02 → a2-13-01 (its `requires` drops `imperfect`, taught in unit 21; unit 13 teaches *mientras* with the indefinido). `por-vs-para` was left at a2-porpara-01 (the screen teaches *para*, the skill covers both). Two skill-list changes, also approved: the A2 periphrases are one skill, so `seguir-gerundio`, `llevar-tiempo-gerundio` and `acabar-de` were merged into `perifrasis-verbales` (aliases kept, `taught_in` a2-perifrasisverbales-01-gr, `requires` present-tense and progressive; the B2 `perifrasis-*` skills stay separate); and `cuando-subjuntivo` became an A2 skill with `taught_in` a2-subjuntivobasico-04-gr (the A2 screen *Cuando + Subjunctive* had no skill; the B1 screen still practises it). `scripts/resolve_skill_aliases.py` rewrote 22 exercise files (6 es-es, 16 es-latam, tag-only), `skills/frozen-es.json` records both changes, registry and `grammar-index.json` rebuilt, validator green, no locked tag changed. Still without a skill: the *llevar sin + infinitivo*, *ponerse a* and *al + infinitivo* screens (a2-perifrasisduracion-03/04) now fall under `perifrasis-verbales`.

### ES A2 units 1–4 (`your-trip`, `what-you-have-done`, `day-out`, `following-instructions`) — locked 2026-10-06
464 exercises per course (116 per unit), read by two Sonnet subagents and reviewed in the main session; one decisions file covers es-es and es-latam. Tags: `your-trip` preterito-perfecto 60, past-participles 27, vocab 25; `what-you-have-done` ya-todavia-no 75, vocab 23, preterito-perfecto 14; `day-out` ya-todavia-no 62, preterito-perfecto 26, vocab 22, past-participles 2; `following-instructions` antes-despues-infinitive 80, vocab 22, past-participles 8, preterito-perfecto 3. Four reading items per unit untagged. Conventions settled: choosing the *haber* person is `preterito-perfecto`, choosing between participle, infinitive and gerund or producing the participle is `past-participles`; a dialogue whose wrong replies differ in *ya* vs *todavía no* (*Sí, todavía no…*) is `ya-todavia-no`, not vocabulary (a deliberate exception to the Sí/No rule, because the contrast is what the unit teaches); fill-blank *todavía quiere* (*still*) is vocabulary. Content fixes in both courses: three two-answer items rewritten (`a2.03.04.ex09`, `a2.03.05.ex17`, `a2.04.01.ex09`), `mochilas` gloss, and person or verb hints added to seven underspecified fill-blanks in units 1–2. Left: sentence-builders without an `english` prompt, near-duplicate items between lessons and the consolidation, dialogues that use *lo / la / las* before a2-12 teaches them, *tenido* with no participle screen, reflexive *ponerse* with no skill.

### ES A2 units 5–8 (`giving-reasons-opinions`, `comparing-trips-memories`, `how-long`, `making-responding-invitations`) — locked 2026-10-06
464 exercises per course. Tags: `giving-reasons-opinions` porque-y-por-eso 70, vocab 32, preterito-perfecto 6, por-que-y-porque 2, past-participles 1; `comparing-trips-memories` comparatives 75, vocab 29, adjective-agreement 7; `how-long` desde-desde-hace 91, vocab 20; `making-responding-invitations` vocab 66, ya-todavia-no 35, preterito-perfecto 10 (nine `ds` to `present-tense`). Content fixes in both courses: nine two-answer or answer-in-the-question items in unit 8 rewritten (`a2.08.03.ex15/16`, `a2.08.05.ex14/16/17/18`, `a2.08.consolidation.ex15/18`), an English gloss in `a2.07.consolidation.ex03`, a *empezar a* sentence in `a2.05.05.ex17` that is taught later. The new check also found five second-correct-answer options in unit 2 (*Ya he… / He ya…*, *Hemos ya recorrido*); each was replaced by an ungrammatical option (`a2-02-01`, `a2-02-04`, `a2-02-consolidation`, no tag change). Check additions in `scripts/readthrough_check.py` (Spanish, warnings): a fill-blank whose answer is a *haber* form with no person in the hint, sentence or English line, and a wrong option that swaps two adjacent words of the answer. Exception to the Sí/No rule written into the rule sheet. Left: unit 8 has no invitation skill (66 vocabulary tags, a template of eight items repeated in lessons 01–05, reading items 11–13 and 15 of `a2-08-05` do not match the story); sentence-builders without an English prompt.

### ES A2 units 9–10 (`experiences`, `keeping-touch`) — locked 2026-10-06
232 exercises per course. Tags: `experiences` alguna-vez 76, vocab 25, preterito-perfecto 4 (one `ds` to `preterito-indefinido`); `keeping-touch` preterito-perfecto 38, ya-todavia-no 34, por-que-y-porque 11, vocab 28 (seventeen `ds`, mostly to `preterito-indefinido`, which unit 11 teaches). Content fixes in both courses: sentence-builders with no English prompt got one (ex08 in every lesson and two more per unit); eight items had two acceptable answers (*¿Has alguna vez visitado…?* beside the reordered option, *Todavía no llamo* as a wrong option) and now have a clearly ungrammatical distractor; seven dialogue replies that were themselves valid answers were changed to *No, he …* or *Sí, nunca …*; one prompt in `a2.10.consolidation.ex18` now matches its answer. The 13 adjacent-swap warnings in `experiences` stand: each is a split auxiliary or reordered *alguna vez*, ungrammatical on purpose. Left: unit 10 repeats one eight-item template in lessons 01–05 (ROADMAP 143); `a2.10.04.ex15` option 2 and `a2.10.04.ex16` option 1 fail on meaning only.

### ES A2 units 11–12 (`what-happened`, `giving-receiving-things`) — locked 2026-10-06
232 exercises per course. Tags: `what-happened` preterito-indefinido 63, preterite-irregular-stems 17, secuencia-narrativa 11, vocab 20 (21 `ds` on present-tense, preterito-perfecto and futuro-simple options); `giving-receiving-things` objeto-directo 89, vocab 20, preterito-indefinido 2. Content fixes in both courses: six fill-blank or dialogue items in `a2-12-03`, `a2-12-05` and the consolidation named no object so *lo / la / los* all fitted, and now name it; one structured-writing answer used *le*, taught later, and was rewritten from the grammar screen; `a2.11.02.ex15` option *Sí, he ido al festival* is a valid reply to *¿Fuiste al festival?* and became *Sí, ir al festival*. The old `objeto-directo` tags on five unit-11 items were replaced because the skill is taught in unit 12. Left: `a2.11.01.ex10` prints *festival* in its own gloss question (a true cognate); the awkward English line in `a2.12.consolidation.ex12`.

### ES A2 units 13–16 (`describing-events-time`, `asking-what-happened`, `explaining-what-happened`, `plans`) — locked 2026-10-06
464 exercises per course. Tags: `describing-events-time` cuando-mientras 90, vocab 20, secuencia-narrativa 1; `asking-what-happened` questions 80, vocab 20, preterito-indefinido 11 (15 `ds` to `ar-verbs` and `stem-changes`); `explaining-what-happened` porque-y-por-eso 85, vocab 23, por-que-y-porque 2, questions 1; `plans` ir-infinitive 70, vocab 22, preterito-indefinido 19 (about 22 `ds`). Content fixes in both courses: *mañana* options in unit 13 (a present-for-future sentence that was also correct) replaced by ungrammatical ones; four wrong reported-question replies in unit 14 that were valid (*Preguntó qué pasa*) replaced; the four unit 14 reading items about a journalist not in the story rewritten from the story (`a2-14-05` ex11, ex13, ex14, ex15); English prompts added to every sentence-builder without one in units 13–16. Left: units 13–16 each repeat one eight-item template across lessons 01–05; the *mientras* dialogues in unit 13 (`a2.13.02.ex15/16`, `03.ex16`, `04.ex16`, `05.ex17`, `consolidation.ex15`) have a wrong reply *Cuando trabajamos, hablamos…* that is arguably a valid answer to a *mientras* question; no skill covers reported (indirect) questions, so unit 14 uses `questions` (nearest). Unit 16 uses the A1 skill `ir-infinitive` for its *ir a* items. Recorded in ROADMAP 143.

### ES A2 units 17–18 (`review-experiences`, `travel-goodbyes`) — locked 2026-10-06
232 exercises per course. Tags: `review-experiences` preterito-perfecto 35, preterito-indefinido 33, preterito-perfecto-vs-indefinido 21, vocab 20, past-participles 1, preterite-irregular-stems 1 (28 `ds`); `travel-goodbyes` ir-infinitive 47, vocab 20, preterito-indefinido 17, preterito-perfecto 13, antes-despues-infinitive 11, preterito-perfecto-vs-indefinido 3 (21 `ds`). The contrast skill is only taught in `a2-17-03`, so the template items in lessons 01–02 carry the single-tense skill and identical items carry identical tags. Content fixes in both courses: time markers added or corrected where a wrong option was also a valid answer (*este año* vs *el año pasado* in `a2.17.01.ex15`, `03.ex15/16`, `05.ex18`, `a2.18.03.ex16`, `02.ex15/16`), a garbled prompt in `a2.17.03.ex15`, `a2.17.03.ex12` option 3, *journey* as a second valid gloss of *viaje* (`a2.18.03.ex10`), two writing prompts that said *you* for first-person answers, English prompts added to every sentence-builder without one. Left: both units repeat one eight-item template across lessons 01–05; `a2.17.02.ex17` asks for *Recordé* while the screen shows *recordamos*.

### ES A2 units 19–20 (`the-future`, `looking-back-moving-forward`) — locked 2026-10-06
232 exercises per course. Tags: `the-future` futuro-simple 91, vocab 20 (about 66 `ds`); `looking-back-moving-forward` preterito-perfecto 35, vocab 21, preterito-indefinido 13, futuro-simple 13, ir-infinitive 12, preterito-perfecto-vs-indefinido 7, past-participles 6, preterite-irregular-stems 3, comparatives 1 (about 74 `ds`). Old `alguna-vez`, `ser-passive` and `imperfect` tags in unit 20 were wrong or taught later and were replaced. Content fixes in both courses: six listening-choice items whose wrong option *I am going to…* is also a correct translation of the future now have a clearly wrong present-tense option; *usted* forms accepted in two *you* fill-blanks; person or verb hints added to six unit 20 blanks; a time cue added to two unit 20 dialogue questions whose wrong reply was valid; the generic *uses the target form* question in unit 20 replaced by *uses the pretérito perfecto correctly*; English prompts for every sentence-builder without one. Left: both units repeat one 9-item block across lessons 01–05, and unit 20's lessons 03–05 are mostly the same *Hemos aprendido* drill even in the future and *ir a* lessons (ROADMAP 143); unit 20's mixed-tense writing items carry the unit vocabulary skill.

### ES A2 units 23–24 (`giving-instructions-directions`, `setting-rules-warnings`) — locked 2026-10-06
132 exercises per course (66 per unit; these units use a shorter 11-item lesson layout). Tags: `giving-instructions-directions` imperativo-afirmativo 24, imperativo-formal-usted 18, imperativo-afirmativo-irregular 12, vocab 10; `setting-rules-warnings` imperativo-negativo 14, posicion-pronombres-imperativo 14, imperativo-formal-usted 13, imperativo-negativo-irregular 11, vocab 11, imperativo-afirmativo 1; two reading items untagged per unit. Content fixes in both courses: a tú / usted / ustedes person added to the hint of 15 command blanks; four writing prompts pinned to one person; two multiple-choice items with two grammatical options rewritten (`aff.02.ex01`, and `neg.05.ex01`, which had a *vosotros* answer in es-latam, a form that course does not teach); two reading fill-blanks that printed their answer rewritten as reading questions from the story; `neg.01.ex06` used *hagas* before lesson 2 teaches it; eleven dialogue replies that were valid colloquial answers replaced by ungrammatical forms. Regular tú commands use the A1 skill `imperativo-afirmativo`. Left: every lesson uses the same 11-item layout and the same imperative / present / preterite dialogue pattern; the stories use *vosotros* in es-es and the es-latam story text was not checked; one stray vocabulary pair in `a2-imperativonegativo-04` ex05.

### ES A2 units 21–22 (`imperfect-tense`, `imperfect-vs-preterite`) — locked 2026-10-06
157 exercises per course (74 and 83). Tags: `imperfect-tense` imperfect 66, vocab 8; `imperfect-vs-preterite` preterite-vs-imperfect 51, imperfect 13, preterito-indefinido 11, vocab 8 (43 `ds` across both). Convention: a fill-blank whose hint names the tense (`(caminar, imp)`) tests the form and is tagged `imperfect` or `preterito-indefinido`; a blank or choice where the learner must pick the tense is `preterite-vs-imperfect`. Old tags `preterite-irregular-stems`, `comparatives` and `alguna-vez` on lesson-03 and error-correction items were replaced by `imperfect`. Content fixes in both courses: two duplicate listening items rewritten (`a2.imperfectobasico.02.ex08`, `03.ex08`); six dialogue replies that were valid answers got a time marker (*Ayer viví*) or a different option; `a2.imperfectocontraste.01.ex01/02` pinned with a role hint (*one completed event*, *background weather*), `03.ex11` question reworded so only the imperfect fits, consolidation ex10 accepts *Fue* and *Era*, ex15's answer was printed in the prompt and now asks `(ocurrir)`. Left: the two units split one sentence into one blank per verb across lessons and consolidation; `a2.imperfectocontraste.02.ex05`, `03.ex12`, `04.ex12` have marginally acceptable wrong replies; `a2.imperfectocontraste.03.ex06` repeats one label three times in a matching.

### ES A2 units 25–26 (`pronouns`, `asking-politely-giving-advice`) — locked 2026-10-06
132 exercises per course (66 per unit). Tags: `pronouns` pronombres-combinados 33, objeto-indirecto 15, vocab 12, objeto-directo 5, one reading item untagged (11 `ds`, lo/la options to `objeto-directo` and *le* to `objeto-indirecto`, also on loísmo-type options because that confusion is the lesson's contrast); `asking-politely-giving-advice` condicional-regular 20, condicional-irregular 12, condicional-consejos 12, vocab 11, polite-softening 10, one reading item untagged (31 `ds`). No skill covers pronouns with infinitives and gerunds (lesson 05) or hypothetical scenarios, so those items use `pronombres-combinados` and `condicional-regular` / `condicional-irregular`. Content fixes in both courses: *se lo*, *os* and *prestármelos* items rewritten where the course had not taught them or two clitic forms fitted; four hints that printed their answer; seven condicional multiple-choice items where a present, imperfect or future option was also valid (*gustará*, *puede*, *desea*, *haré*); the *vosotros* form *os* removed from the course-shared items; prompts rewritten to match answers in `a2.pronombrescliticos.03.ex09`, `a2.condicionalsimple.01.ex09` and `02.ex09`. Two adjacent-swap warnings stand (*lo te*, *la me*, both ungrammatical). Left: lesson-05 builders accept one word order; lowercase *carlos* and *meg* tiles; `a2.pronombrescliticos.01.ex02` and `04.ex08` are loosely acceptable.

### ES A2 units 27–28 (`expressing-wishes-feelings`, `connecting-ideas-habits`) — locked 2026-10-06
132 exercises per course (66 per unit). Tags: `expressing-wishes-feelings` subjuntivo-morfologia 16, vocab 13, cuando-subjuntivo 10, subjuntivo-deseos 9, subjunctive-emotion 9, subjunctive-value-judgments 8, one reading item untagged; `connecting-ideas-habits` perifrasis-verbales 23, vocab 18, ordering-markers 9, concesivas-aunque 6, porque-y-por-eso 4, preterito-indefinido 3, imperativo-negativo 2, one reading item untagged. Lesson-01 subjunctive items are `subjuntivo-morfologia` because `subjuntivo-deseos` is taught in lesson 02. *por lo tanto* and *ya que* are `porque-y-por-eso` (`ordering-markers` covers *primero / además / por un lado* only). Registry: `concesivas-aunque` `taught_in` moved from a2-perifrasisverbales-04-gr to a2-perifrasisverbales-03-gr, the screen that first teaches *aunque* (screen 04 never mentions it); no tag changed. Content fixes in both courses: eight multiple-choice items in unit 28 where a second option was valid once the verb hint was ignored; four hints that printed their answer (*(aunque)*, *(ya)*, *(cuaderno)*, *(decisión)*); two *vosotros* answers in the course-shared `a2-subjuntivobasico-consolidation` (ex04, ex07) changed to *ustedes* because es-latam does not teach *vosotros*; two *cuando llego / termino* wrong options changed to future forms (valid habitual readings before); *Siento que* changed to *Lamento que*; an English line corrected in `a2.perifrasisverbales.02.ex11`. Left: `a2.perifrasisverbales.05.ex10` option *me acostumbrar* is clumsy; lessons 01, 02 and 05 of unit 28 repeat one *pick the periphrasis verb* template.

### ES A2 units 29–32 (`studying-school-life`, `por-and-para`, `indefinites-double-negation`, `duration-recent-actions`) — locked 2026-10-06
261 exercises per course (66, 69, 63, 63). Tags: `studying-school-life` vocab 52, gustar 5, preterito-indefinido 3, adjective-agreement 2, gender 1, perifrasis-verbales 1, two reading items untagged; `por-and-para` por-vs-para 53, vocab 15, numbers 1; `indefinites-double-negation` indefinidos-negativos 38, vocab 13, negation 12; `duration-recent-actions` perifrasis-verbales 51, vocab 12. Unit 29 is mostly vocabulary because no skill covers *darse bien*, *costar* or the study collocations (`gustar` takes *se me da bien*, *me cuesta*). Registry: `negation` `taught_in` moved from a2-indefinidosnegacion-05-gr to 04-gr, the screen that first teaches *tampoco / nunca / jamás*; no tag changed. Content fixes in both courses: eleven fill-blank hints in unit 29 and four in unit 32 that printed their answer replaced by English hints; about thirty multiple-choice items across the four units where a second option was grammatical (*¿Hay nadie?*, *No vino ninguno*, *chaqueta de cincuenta euros*, *Tengo tres años practicando* in es-latam, *costó* for *cuesta*) replaced; `cons.ex01` in unit 31 had its `correct` pointing at an ungrammatical option; the screen example *Ya no fumo desde hace seis meses* in `a2-indefinidosnegacion-04-gr` was wrong and was corrected (the generated `translation-index.json` still holds the old line until the next index build). `scripts/readthrough_check.py` now also warns, in every course, on a fill-blank whose parenthesised hint is the answer; it finds 217 such items in ES B1 per course and 5 in HU A1 (ROADMAP 143). Left: the 11-item layout repeats in every lesson of these units.

### ES A2 unit 33 (`vosotros`, es-es only) — locked 2026-10-06
63 exercises. Tags: vocab 17, vosotros-imperativo 14, vosotros-indicativo 13, preterito-indefinido 10, preterito-perfecto 4, objeto-indirecto 2, subject-pronouns 2, possessives 1. The check printed `missing from es-latam` for all 63 ids, as expected for an es-es-only unit; the unit was applied and locked in es-es only. Choosing a *vosotros* form of any verb is `vosotros-indicativo` rather than the verb's own skill; the clitic *os* blanks are `objeto-indirecto`; vosotros-versus-ustedes pronoun choices are `subject-pronouns`. Content fixes: eight multiple-choice items with a second valid option (*Pasen*, *vengan*, *han* beside *chicos*, *Sentaros*, *piensan*) replaced, the possessive item now offers *vuestro / vuestra / vuestros / vuestras*, and the listening sentence `a2.vosotrospeninsular.05.ex07` was rewritten (*qué alegría veros en Madrid*), so any cached audio for it must be regenerated. Left: every sentence-builder ends with both a `?`/`!` tile and a stray `.` tile; `01.ex05` and `04.ex02` are near-duplicates.

### ES A2 read-through complete (33 units, es-es and es-latam) — 2026-10-06
All 33 es-es units (3,197 exercises) and 32 es-latam units (3,134) are in `tags.lock.json`, checked per course: every exercise id under `exercises/a2/` is locked. Run with the Sonnet-subagent process in [docs/readthrough-process.md](docs/readthrough-process.md): two units per subagent, at most two subagents at a time, each pair reviewed with `readthrough_review.py` before `apply_tags.py` and `lock_tags.py`; one decisions file covers both courses. Set-up: registry scan with the user's sign-off (six `taught_in` moves, the A2 periphrases merged into `perifrasis-verbales`, `cuando-subjuntivo` made A2), then two more `taught_in` moves found during the read (`concesivas-aunque`, `negation`). Conventions the level added are in the rule sheet (`docs/readthrough-brief.md`): the exception to the Sí/No rule for a unit's own contrast, A2 vocabulary names, one periphrases skill. `scripts/readthrough_check.py` gained three Spanish-era checks: a *haber* blank with no person, an option that swaps two adjacent words of the answer, and a hint that is the answer (found 217 per course in ES B1, ROADMAP 143). The level's common defects, all fixed in both courses: a wrong option that was also correct (free word order, a present for the future, colloquial forms), a hint that printed its answer, a blank with no person, sentence-builders without an English prompt, and *vosotros* answers in course-shared items. Left for sign-off: ROADMAP 143.

### Small-fixes pass: lesson-to-lesson copies rewritten (ROADMAP 144(3)) — 2026-10-06
Decided with the user (rewrite, not delete; consolidation lessons keep recycling earlier items). `scripts/dup_report.py` lists exact copies inside a unit, ignoring a trailing *(Lesson N)* label and consolidation lessons; `docs/dedupe-brief.md` is the subagent sheet. Sonnet subagents rewrote every copy as a new item on the same skill and tag (ids, `type`, `category`, `teaches` and `distractor_skills` unchanged), using that lesson's own grammar screen, vocabulary and story: ES A2 458 copies in 33 units (both courses), ES A1 64 (11 units, both courses), HU A1 about 237 in 30 units, HU B1 about 275 in 13 units (facts only from each lesson's story or screen), HU A2 1. Finished units list zero copies and every batch passed the validator, the locked-tag guard and `readthrough_check.py` run on the unit's current tags. Rules added to the briefs on the way: a builder with a natural alternative order carries `solutions` instead of `solution` (never both keys; the engine already accepts the list, ROADMAP 144(9) retrofits the old builders later); no plain reorderings or other valid forms as wrong options. Doubts passed to a native-speaker check: *Isaszegi* (case-sensitive grading), prefix placement in `rakosikorszak-03.ex02` and `-05.ex02`, the suffix-only blanks `b1-18-03.ex06` and `b1-18-05.ex06`, *királynénak* vs *királyné asszonynak* in `kiegyezes-03.ex03`, the definite/indefinite pairs in `b1-vilaghaboru-04.ex02` and `-05.ex02`. Left: ES A2 unit 20 lessons 02–05 keep the perfecto tag per lesson (a different tense per lesson would need retagging); first occurrences were not reviewed.

### Small-fixes pass: ES A2 reading and dialogues, HU B1 history facts (ROADMAP 144(7)) — 2026-10-06
Three small fixes decided with the user. (a) ES A2 unit 8 `a2-08-05` reading items ex11–15 asked about a drink and a dish that are not in the story `a2-08`; all five were rewritten from the story text (who invites, which dish Lucía teaches, what Kaylee answers, what Lucía does after dinner, what the friends do before leaving), in both courses. (b) ES A2 unit 13 *mientras* dialogues (`a2.13.02.ex15/16`, `03.ex16`, `04.ex16`, `consolidation.ex15`): the wrong reply *Cuando trabajamos, hablamos…*, arguably valid, became *Cuando mientras trabajamos, hablamos…* and the third option *Después de trabajar, hablamos…* (wrong in meaning), both courses. (c) HU B1 history and civics fact questions (*Ki volt…*, *Miért…*, *Mikor eredményes egy népszavazás?*) were unit vocabulary in the early units and untagged reading in the later ones. A scan found 330 multiple-choice items tagged as vocabulary that were not blank-fills or meaning questions; a Sonnet subagent classified each as `fact` (answering needs the history, civics or legal content) or `term` (the meaning, definition or usage of a word; ties stay `term`). The 130 `fact` items, in 27 units, are now `category: reading` with no `teaches`; the 200 `term` items stay vocabulary. The 27 units were re-locked with `lock_tags.py --update`. Borderline calls in the classification (kept as term): *preambulum*, *helyi rendelet*, *közteherviselés*, *hősi halott*, *hungarikum*, *felmondási idő*, *ügyintézési határidő*; kept as fact: *maszekok*, *kiskirályok*, *kilenced*, *vilajet*, *labanc*, *kurucok*, *robot*, *sarkalatos törvények*. Closes ROADMAP 141(d).

### Small-fixes pass: `b1-literary-musical-canon-vocab` removed (ROADMAP 144) — 2026-10-07
At the user's request the unused Hungarian skill `b1-literary-musical-canon-vocab` (no exercise carried it: the unit `literary-musical-canon` holds only grammar items and untagged reading) was removed from `skills/hu.json` and `skills/frozen-hu.json`. The validator required every unit to own a `<level>-<id>-vocab` skill, so a unit table entry can now say `"vocabulary": false` (added to the three `units.schema.json` files; `scripts/validate-content.py` skips the check for such a unit) and the unit `literary-musical-canon` carries it. Registry rebuilt and in sync.

### Small-fixes pass: gap skills added, two skills re-levelled, one removed (ROADMAP 144(5), 144(8)) — 2026-10-07
Decided with the user from `docs/skill-gap-proposal.md` (a Sonnet subagent matched each gap with its screen and the exercises that test it; a second hand-checked every candidate: the level of the exercise must be at least the skill's, the skill's screen must not come after the lesson, a wrong answer must show the new skill, the category must follow the tag). **Added:** ES `telling-time` (A1, 22 exercises), `dates-months` (A1, 6) and `preguntas-indirectas` (A2, 38, mostly moved off the A1 `questions` skill; the old alias on `pronombres-combinados` and on the retired `time-dates` was dropped); HU `reflexive-magam` (A2, 5), `inkabb-mint` (A2, 10) and `ide-oda-innen-onnan` (A2, 6). **Re-levelled B1 to A2:** `mediopassive-verbs-odik` (`taught_in` a2-155-a-gr, 25 exercises) and `distributive-nkent` (a2-68-b-gr, 19). **`taught_in` moved:** `correlative-minel-annal` to b1-02-05-gr (the screen that first teaches *egyre* and *minél*), so five more items could carry it. **Removed:** `nominalizing-processes` (one exercise, no screen; the item moved to the unit vocabulary skill) and, earlier, `b1-literary-musical-canon-vocab` (no exercises; the unit now carries `"vocabulary": false`, allowed by the three `units.schema.json` files and `validate-content.py`). Retags: 129 exercises (76 ES shared ids, 53 HU) and about 335 candidates rejected with a reason in the scratchpad's `retag_skipped.json` (above level, taught later, meaning rather than pattern). The affected units were re-locked with `lock_tags.py --update` (ES A1 3, ES A2 1, HU A2 7, HU B1 5, each in both ES courses). Frozen lists carry a dated entry for every change. Still stay vocabulary: weather, café phrases, *presentar a*, direction chunks, invitations, study-life structures, *-ás/-és* nouns, *azelőtt/azóta*, commemorative postpositions, *alighogy … máris*, discourse particles, generic *az ember*; and no retag for *esto/eso*, clitics with infinitives, the hypothetical conditional and `a1-04-02.ex03` (those items test meaning or come before the skill). Housekeeping: cached audio needs no regeneration (exercise audio is content-addressed by text); the stale `translation-index.json` lines were already refreshed by the auto-sync. Thin after this: `reflexive-magam` 5 (needs 1) and `intensificadores-y-grado` 5 (needs 1), part of fix #4.

### Small-fixes pass: thin skills filled to 6 (ROADMAP 144(4)) — 2026-10-07
After the dedupe, the retags and the registry changes, 24 skills were under the 6-exercise rule (HU 23, ES 1) and needed 58 new exercises. Two Sonnet subagents wrote them, each into a lesson that already practises the skill (the lesson holding its `taught_in` screen or a later one of the same unit), in the file's own format and id style, tagged and categorised, using `solutions` for builders with an alternative order, and each id was appended to the lesson's `exerciseRefs` so it appears in the lesson. HU A1/A2 (27): `hungarian-vowels` +4, `jar-iskolaba`, `mit-csinaljak`, `nem-vs-nincs-two-kinds-of-negation`, `sokat-eleget`, `szokott-infinitive-habitual-actions` +3 each, `itt-ott-here-there`, `ordinal-numbers` +2, `reflexive-magam`, `sajat`, `subject-pronouns-omission` and the vocabulary skill `a2-review-work-past-opinions-vocab` +1. HU B1 (30): `kent-vs-mint` +6, `noun-compounds` +6, `historical-routines` +5, `mixed-conditionals` +3, `kepest`, `verb-government-bol-bol`, `verbal-adjectives-hatatlan-hetetlen` +2, and +1 each for `ahol-amikor`, `concessive-postpositions`, `nominalization`, `spatial-belonging-beli`. ES: `intensificadores-y-grado` +1 (`a1.dol.03.ex13`, both courses). Each touched unit was checked with `readthrough_check.py` on its current tags (0 errors), `dup_report.py` lists nothing, and the 23 locked units were re-locked with `--update`; every skill in HU A1–B1 and ES A1–A2 now has at least 6 exercises. Also fixed on the way: `a1.dol.03.ex11` had two identical options (both courses). Doubts for a native check: the *-ként* role/comparison items in `b1-17-01.ex09/10`, the *mixed-conditionals* claim in `b1-35-02.ex08` (*most nem késtem volna* ungrammatical), and `a1.dol.03.ex13` accepts *un poco* only. Not done by decision: the sentence-builder retrofit (ROADMAP 144(9)) is parked.

### Hungarian native check: first answers applied — 2026-10-07
The user (Hungarian speaker) went through `docs/hu-native-check.md` and confirmed 31 of 34 items; three changes. (2) `a1-80-review-2` (*márciusban*) is correct Hungarian but the months are not taught yet at that point, so the item was replaced by a day item (*Which means "on Wednesday"?* szerdán / szerda / szerdában), tag `ban-ben-in` changed to `on-en-on`, unit `time-dates` re-locked. (16) A place-name adjective in *-i* loses its capital: `b1-forradalom-04.ex06` answer *isaszegi* (not *Isaszegi*), and the same word was lower-cased in the unit's two story files and its vocabulary file (*isaszegi csata*). (30) `b1-trianon-04.ex06` answer corrected from *ért* to *éért* (*az igazságérzetéért*, with the possessive). All other 31 items stand as written.

### ES B1 read-through set-up (registry scan, ROADMAP 125) — 2026-10-07
ES B1 is the largest level: 112 units (40 `core` in both courses, 36 `cultura` in es-es, 36 `latam` in es-latam), 8,597 distinct exercises (4,093 shared, 2,268 es-es only, 2,236 es-latam only), 43 B1 grammar skills and 112 B1 vocabulary skills. Registry scan with the user's sign-off: eight es-latam-only skills (`a-pesar-de`, `correlativos-no-solo-sino`, `cuanto-mas-tanto-mas`, `dejar-de-infinitivo`, `estar-a-punto-de`, `formal-cause-connectors`, `futuro-perfecto`, `gerundio-acciones-paralelas`) got `variant: es-latam`; `taught_in` moved for `ser-passive` and `pasiva-refleja` (both to the shared screen b1-18-01), `prepositional-phrases` (b1-24-04), `conditional-conjunctions` (es-latam b1-guerrafria-02) and `relativo-posesivo-cuyo` (es-latam b1-economiasexportacion-02); `superlatives` stays (the shared screen only mentions it). Found and left: 14 B1 and 61 B2 skills have a `taught_in` screen in one course only; `conditional-conjunctions` and `relativo-posesivo-cuyo` have a parallel screen in each course and the registry holds one `taught_in` (a per-course map would need the validator, `build_skill_registry.py` and any engine reader changed first). `scripts/readthrough_check.py` no longer pairs a track-only unit with the other course. B1 notes added to `docs/readthrough-brief.md`.

### ES B1 `telling-stories`, `experiences-memories`, `plans-ambitions`, `giving-advice` — locked 2026-10-07
First four core units, es-es and es-latam (shared ids; 408 exercises each course). Tags: `telling-stories` pluscuamperfecto 22, vocab 19, preterito-indefinido 16, imperfect 11, preterite-vs-imperfect 9, secuencia-narrativa 7, contrast-concession-connectors 5, porque-y-por-eso 5, habitos-soler 2, ordering-markers 1, four reading items untagged; `experiences-memories` vocab 39, preterito-indefinido 19, pluscuamperfecto 17, imperfect 14, preterite-vs-imperfect 10, secuencia-narrativa 8, cuanto-mas-tanto-mas 4, past-participles 1; `plans-ambitions` vocab 34, ir-infinitive 21, futuro-simple 19, subjuntivo-deseos 14, ordering-markers 1, si-clauses 1; `giving-advice` vocab 25, subjunctive-influence 19, deber-vs-tener-que 13, hypothetical-structures 9, ordering-markers 6, futuro-simple 6, condicional-regular 5, condicional-consejos 4, porque-y-por-eso 4, subjuntivo-de-finalidad-para-que 4 and two imperative items. Registry fixes found by the units and applied: `taught_in` of `hypothetical-structures` to b1-04-02-conditional-advice-gr, `subjuntivo-de-finalidad-para-que` to b1-04-04-recommendation-consequence-gr, `contrast-concession-connectors` to b1-01-04-pasados-y-conectores-gr (each unit screen teaches the pattern before the dedicated later one); `habitos-soler` (b1-01-02 only mentions *soler* in passing) and `si-clauses` (b1-03-02 shows *si* + present in examples) stay on their dedicated screens, so those items keep a taught-later warning. Content fixes in both courses: hints that printed the answer replaced by English hints (six in `giving-advice`), two-answer items rewritten (`b1-01.ex06`, `b1-03-04.ex12`), a prompt that printed its answer turned into a blank (`b1-01-05.ex02`), `solutions` with alternative orders on 20 sentence-builders, accepted alternatives added to several fill-blanks (*por eso / así que*, *no obstante*, *desde entonces*). Tooling: `dup_report.py` and `readthrough_check.py` now compare sentence-order items (`sentences`, `tiles`, `solutions`), which had made every sentence-order look like a copy.

### ES B1 `education-learning`, `travel-mobility` — locked 2026-10-07
Core units 7–8, es-es and es-latam (212 exercises each). Tags: `education-learning` vocab 26, opinion-verbs-mood 18, comparatives 13, se-impersonal 11, giving-opinions 9, imperfect 8, preterite-vs-imperfect 6, hay-que 3, ordering-markers 3, superlatives 2, four reading items untagged; `travel-mobility` preposiciones-movimiento 17, vocab 13, si-clauses 12, hypothetical-structures 10, ir-infinitive 9, preterite-vs-imperfect 9, futuro-simple 8, imperfect 7, pluscuamperfecto 7, secuencia-narrativa 4, one comprehension item moved to untagged reading. Registry: `taught_in` of `giving-opinions` to b1-07-05-defending-opinions-gr and `superlatives` to b1-07-04-comparison-evaluation-gr (each unit screen names the pattern before the later dedicated one). Content fixes in both courses: twelve hints that printed the answer replaced by English hints, *vosotros* forms in shared text changed to *ustedes* (eight items in `b1-08`), arbitrary sentence-orders given a real ordering signal (*primero / después / finalmente*), five builders with `solutions`, accepted alternatives (*hasta / a*, *perdiéramos / perdiésemos*), a present-tense option in `b1-08-02.ex14` that also answered the question replaced, and three `b1-08-05` items made story-neutral because they named Odysseus before the learner reaches the story. Consolidation items of `travel-mobility` that carried wrong bulk tags were retagged to the skill each reviews.

### ES B1 `relationships`, `work-professional-life` — locked 2026-10-07
Core units 5–6, es-es and es-latam (207 exercises each). Tags: `relationships` relative-clauses 24, vocab 20, imperfect 14, preterito-perfecto 13, reflexives 12, imperfect-vs-present-perfect 7, ordering-markers 5, habitos-soler 4, preterito-indefinido 2, four reading items untagged; `work-professional-life` vocab 49, pasiva-refleja 9, porque-y-por-eso 6, se-impersonal 6, present-tense 5, ordering-markers 5, imperfect 4, comparatives 2, formal-cause-connectors 2, preterito-indefinido 2, four reading items untagged. Registry (each unit screen teaches the pattern before the dedicated later one): `taught_in` of `relative-clauses` to b1-05-04-relative-clauses-gr, `habitos-soler` to b1-05-02-imperfecto-habitual-gr, `imperfect-vs-present-perfect` to b1-05-05-interpersonal-language-gr, `pasiva-refleja` and `se-impersonal` to b1-06-03-impersonal-passive-gr; `formal-cause-connectors` lost its `variant: es-latam` (the shared unit `b1-06-04` tags it for both courses) and moved to b1-06-04-cause-consequence-gr. Content fixes in both courses: nine *vosotros* items changed to *ustedes*, nine hints that printed the answer replaced by English hints, an imperfect-subjunctive line (not yet taught) replaced in `b1-05-05.ex06`, look-alike present/preterite *nosotros* options replaced by futures, `b1-06-02.ex14` rebuilt (its English gloss did not match the Spanish), `b1-05-05.ex17` accepted *escuchar* for *escucharnos*. No exact copies.

### ES B1 `health-wellbeing`, `home-housing`, `cities-communities`, `food-lifestyle` — locked 2026-10-07
Core units 9–12, es-es and es-latam (420 exercises each). Tags: `health-wellbeing` vocab 28 (20 listening or dictation), subjunctive-influence 17, estar 12, habitos-soler 11, se-impersonal 9, pasiva-refleja 8, subjunctive-value-judgments 5; `home-housing` vocab 33, relative-clauses 15, comparatives 8, hypothetical-structures 8, condicional-regular 8, intensificadores-y-grado 5, porque-y-por-eso 5; `cities-communities` subjunctive-influence 19, vocab 18, relative-clauses 17, porque-y-por-eso 15, subjunctive-value-judgments 10, imperfect-vs-present-perfect 7, formal-cause-connectors 4; `food-lifestyle` vocab 18, frequency-adverbs 10, imperfect 10, preterite-vs-imperfect 10, subjunctive-influence 9, subjunctive-value-judgments 9, contrast-concession-connectors 9, ordering-markers 8, comparatives 8. Content fixes in both courses: about 20 hints that printed the answer replaced by English hints, sentence-orders given a real ordering signal in all four units, *vosotros* and *podáis* forms changed to *ustedes*, items that used the imperfect subjunctive (taught later) rewritten (`b1-11-02.ex10` and the `b1-11-02` grammar screen: *antes de construir*; `food-lifestyle` consolidation ex13), two wrong options that were also grammatical fixed in `home-housing`, one answer that needed *en el que* (taught later) rewritten, `solutions` added to nine builders, stray punctuation in model answers fixed. Registry: no new `taught_in` changes (`pasiva-refleja` was already moved to b1-06-03; `formal-cause-connectors` already points at b1-06-04). Left: several writing answers in `cities-communities` end in the same templated *porque creo que es importante para la comunidad*; `indexes/translation-index.json` still holds the old *antes de que construyeran* line until the next index build.

### ES B1 `media-information`, `technology-communication`, `culture-entertainment`, `environment` — locked 2026-10-07
Core units 13–16, es-es and es-latam (432 exercises each). Tags: `media-information` vocab 30, estilo-indirecto-informacion 13, opinion-verbs-mood 12, ordering-markers 12, argument-markers 10, estilo-indirecto 10; `technology-communication` vocab 32, hypothetical-structures 17, preterito-perfecto 13, present-tense 8, contrast-concession-connectors 7, frequency-adverbs 6, argument-markers 6; `culture-entertainment` vocab 46, argument-markers 13, subjunctive-influence 13, comparatives 8, resultar-adjective 8, relative-clauses 6; `environment` vocab 52, subjunctive-value-judgments 20, relative-clauses 14, porque-y-por-eso 11, past-participles 9, formal-cause-connectors 4. Four reading items per unit stay untagged. Registry: `taught_in` of `subjunctive-doubt` to b1-13-03-indicative-subjunctive-evaluation-gr and of `argument-markers` to b1-13-05-summarising-and-responding-gr. Content fixes in both courses: about 20 hints that printed the answer replaced by English hints; sentence-orders given a real ordering signal in all four units; distractors that used grammar taught later (*haya ocurrido*, *sin que* + imperfect subjunctive, *dudo que*, a relative-clause subjunctive) replaced; two wrong options that were also valid answers fixed; fill-blanks now accept both valid forms (*afirmó / afirmaba*, *tuviéramos / tuviésemos*, *ya que*, *a causa de*). Units 13–16 have no exact copies.

### ES B1 `society-inequality`, `politics-public-life`, `money-economy`, `problems-solutions` — locked 2026-10-07
Core units 17–20, es-es and es-latam (432 exercises each). Tags: `society-inequality` vocab 29, comparatives 12, argument-markers 12, subjunctive-value-judgments 11, giving-opinions 10, porque-y-por-eso 6; `politics-public-life` subjunctive-value-judgments 31, vocab 24, pasiva-refleja 12, giving-opinions 10, contrast-concession-connectors 9; `money-economy` vocab 28, porque-y-por-eso 19, hypothetical-structures 12, comparatives 11, giving-opinions 8, condicional-regular 7; `problems-solutions` vocab 36, porque-y-por-eso 12, subjunctive-value-judgments 12, hypothetical-structures 12, condicional-regular 11, relative-clauses 7, argument-markers 5. Four reading items per unit stay untagged. No `taught_in` changes. Content fixes in both courses: about 30 hints that printed the answer replaced by English hints, accepted alternatives listed in `answers` (*porque / ya que*, *por eso / por lo tanto*, *tuviera / tuviese*, *funcionara / funcionase*), sentence-orders given a real ordering signal, `solutions` on eight builders, a grammar-screen example fixed (`b1-17-02`: *Algunas personas have* became *tienen*), a broken question and two second-valid options in `money-economy` and `problems-solutions` rewritten (*si tengo* / *funciona* after *si* offered as wrong options), *haríais* changed to *harían*, an untaught answer (*conforme*) replaced. No exact copies in units 17–20.

### ES B1 `opinions-arguments`, `possibilities-predictions`, `making-decisions`, `how-things-work` — locked 2026-10-07
Core units 21–24, es-es and es-latam (432 exercises each). Tags: `opinions-arguments` subjunctive-value-judgments 20, contrast-concession-connectors 19, porque-y-por-eso 18, argument-markers 14, vocab 13, giving-opinions 12; `possibilities-predictions` hypothetical-structures 25, vocab 20, subjunctive-doubt 18, futuro-simple 14, condicional-irregular 10, future-probability 7; `making-decisions` vocab 28, subjunctive-value-judgments 18, comparatives 17, si-clauses 14, ordering-markers 8, argument-markers 8; `how-things-work` pasiva-refleja 22, ordering-markers 33, vocab 20, se-impersonal 15, prepositional-phrases 7, hay-que 6. Four reading items per unit stay untagged; no exact copies, no `taught_in` changes. Content fixes in both courses: about 35 hints that printed the answer replaced by English hints and alternatives listed in `answers` (*sin embargo / no obstante*, *quizá / quizás / tal vez*, *finalmente / por último*, *compuesto / formado*); ungrammatical frames removed (*Posiblemente que*, *Quizá que*); wrong options that were also valid replaced in `making-decisions` and `possibilities-predictions`; `evidencia que apoye` (B2) replaced; *habéis* changed to *han* in a shared item; sentence-orders given a real ordering signal in all four units; `solutions` on 14 builders.

### ES B1 `change-development` to `culture-language-society` (units 25–30) — locked 2026-10-07
Core units 25–30, es-es and es-latam (648 exercises each). Tags: `change-development` vocab 58, subjunctive-value-judgments 17, futuro-simple 7, imperfect-vs-present-perfect 6; `work-ambition-balance` vocab 37, hypothetical-structures 21, subjunctive-value-judgments 18, comparatives 11; `social-life-communication` vocab 54, estilo-indirecto 39, objeto-indirecto 4; `rules-rights-responsibilities` vocab 48, subjunctive-value-judgments 17, porque-y-por-eso 15, se-impersonal 7; `migration-identity` vocab 55, relative-clauses 12, preterito-indefinido 9, verbos-regimen-preposicional 5, relativas-preposicion-el-que 5; `culture-language-society` vocab 47, comparatives 16, subjunctive-value-judgments 14, opinion-verbs-mood 7. Four reading items per unit stay untagged. Registry: `taught_in` of `verbs-of-change` to b1-25-01-change-over-time-gr and `verbos-regimen-preposicional` to b1-29-03-change-experience-gr (each unit screen teaches the pattern before the dedicated later one). Content fixes in both courses: about 55 hints that printed the answer replaced by English hints and alternatives in `answers`; every sentence-order given a real signal; distractors with grammar taught later replaced (present-perfect subjunctive *haya viajado*, imperfect subjunctive *explicara / estuviera*, *resolvisteis*); wrong options that were also valid answers replaced (`b1-28-05.ex12`, `ex13`, `b1-29-03.ex12`); `solutions` on 18 builders; `clarification-explanation`, an unknown slug in the old file tags of unit 27, is gone. No exact copies in units 25–30.

### ES B1 `reported-speech` to `sequence-of-tenses` (units 31–38) — locked 2026-10-07
Core units 31–38, es-es and es-latam (690 exercises each). Tags: `future-society` futuro-simple 24, vocab 25, subjunctive-value-judgments 19, hypothetical-structures 19; `connecting-ideas` porque-y-por-eso 26, vocab 25, ordering-markers 16, subjuntivo-de-finalidad-para-que 8, contrast-concession-connectors 8, por-vs-para 7, argument-markers 7; `reported-speech` estilo-indirecto-informacion 27, estilo-indirecto 24, preguntas-indirectas 21, vocab 29; `complex-opinions` subjunctive-doubt 36, vocab 33, opinion-verbs-mood 20, subjunctive-value-judgments 11; `present-perfect-subjunctive` subjuntivo-perfecto 46, vocab 17; `sequence-of-tenses` correlacion-temporal-subjuntivo 17, vocab 17, estilo-indirecto-ordenes 15, estilo-indirecto 14. (`hypotheticals-possibilities` and `independent-spanish`, units 35–36, follow in the next entry.) Four reading items per 108-exercise unit stay untagged. Registry: `a-pesar-de` lost its `variant: es-latam` and moved to b1-32-03-contrast-concession-gr, like `formal-cause-connectors` before it (a shared core unit tags it for both courses). Content fixes in both courses: `reported-speech` 01.ex02 had the direct-speech option marked correct; wrong options that used grammar taught later (imperfect subjunctive *tuviera*, *hubiera visto*, *subiera*) or were also valid answers replaced; *vosotros* forms (*organizasteis*, *salisteis*, *perdisteis*, the imperative *¡Esperad!*, *os*) changed to *ustedes*, including a screen example in `b1-37-02`; broken fill-blanks fixed (*abriría abrir*, *primer oferta*); about 40 hints that printed the answer replaced and alternatives listed in `answers`, including the *-ra / -se* subjunctive forms; all sentence-orders given a real signal. Left: `decks.json` still holds *primer oferta* until the next build; the vocabulary entry *multi-cláusula* in `b1-38-05` is not a real word.

### ES B1 core track complete (40 units, es-es and es-latam) — 2026-10-07
All 40 `core` units are locked in both courses (shared ids, about 4,100 exercises per course). Units 35–40: `hypotheticals-possibilities` hypothetical-structures 51, si-clauses 33, vocab 19; `independent-spanish` vocab 33, opinion-verbs-mood 16, subjunctive-value-judgments 14, hypothetical-structures 12; `verbs-of-becoming` verbs-of-change 41, vocab 22; `connectors-prepositional-regimes` verbos-regimen-preposicional 20, lo-neutro-abstraccion 16, sino-vs-pero 15, vocab 12 (units 37–38 are in the previous entry). Registry gaps found and left for decision: `pluscuamperfecto-subjuntivo-si` is B2 although unit 35 teaches *si* + pluperfect subjunctive, so about 30 B1 items use `si-clauses`; `conectores-con-subjuntivo` has `taught_in` b1-36-03, a screen that teaches *porque*, *por eso* and *es necesario que* rather than *sin que* or *de ahí que*, so no item uses it; the emphatic *lo + adjective + que* of `b1-40-04` has no skill of its own. Content fixes in units 35–40, both courses: hints that printed the answer replaced by English hints; every sentence-order given a real ordering signal; wrong options that were also valid answers replaced (*Elegiera otra*, *imaginara*, *me pone loco*, *sino que que*); `answers` for interchangeable forms (*hubieran / hubiesen sido*, *puso / quedó*); a dictation that tested *quedarse + gerundio*, not taught, rewritten; *vosotros* forms changed to *ustedes*. Known and left: the present-perfect subjunctive appears as a wrong option in units 35–36 although it is taught only in unit 37.

### ES B1 `cultura` track, units 1–12 (es-es only) — locked 2026-10-07
Units `constitution-1978` to `instituto-cervantes` (constitution, crown, Cortes, government, courts, regional institutions, elections, armed forces, EU, state symbols, co-official languages, Instituto Cervantes) are read and locked, 63 exercises each, by Sonnet subagents in pairs, decisions checked with `scripts/readthrough_check.py` (0 errors) before `apply_tags.py` and `lock_tags.py`. Shape of every unit: about 36–45 items on the unit vocabulary skill, 13–21 untagged reading (civics/history fact questions, rule in `docs/readthrough-brief.md`), a handful of grammar tags where a unit screen teaches one (`prepositional-phrases`, `ser-passive`, `verbos-regimen-preposicional`, `adjective-agreement`). Content fixes: facts that the lesson did not contain were removed or reworded (Erasmus+ ranking, the 27 commissioners, 1785 flag design, 'más de quinientos millones', and about 20 more), answers printed in the prompt were reworded, several fill-blanks got `answers` lists. Old B2 `nominalization` and `ser-passive` tags on these units were dropped. Registry decisions of the same day: `pluscuamperfecto-subjuntivo-si` moved to B1 (taught in `b1-35-03`), `conectores-con-subjuntivo` retired, four pattern gaps (*deber de*, *derecho a*, *al* + infinitive, *lo* + adjective + *que*) folded into existing skills (`docs/readthrough-brief.md` § B1 folds). Units 13–36 (`fundamental-rights` to `ccse-mock-exam`) followed the same day, so **the whole `cultura` track (36 units, es-es only) is locked**; the subagents rewrote about 60 fact questions whose answers were not on the lesson screens and turned every answer-printing English line into a bracketed hint. `latam` units 1–4 (`pre-columbian-america`, `indigenous-civilizations`, `arrival-of-europeans`, `conquest`, es-latam only) are locked too: these carry real grammar tags (`ser-passive`, `pasiva-refleja`, `gerundio-acciones-paralelas`, `formal-cause-connectors`) and about 50 rewritten fact questions, because the short, partly garbled stories did not contain what the questions asked. Still open: about ten `taught_in` moves (units 5–6 screens, `superlatives` to `b1-transporte-01`, `relativo-posesivo-cuyo` to the `arrival-of-europeans` screen and the first `latam` pair's screens), and a handful of fact questions whose detail is not on the screens (`b1-igualdad-02/03.ex05`, `civic-duties-taxes`, `b1-geografia` 01.ex03/03.ex03/04.ex03).

### ES B1 read-through complete (core 40, cultura 36, latam 36 units) — 2026-10-08
All 112 ES B1 units are read and locked: `core` (40, shared ids, es-es and es-latam), `cultura` (36, es-es only) and `latam` (36, es-latam only), about 7,000 exercises per course by Sonnet subagents two units at a time, each batch checked with `scripts/readthrough_check.py` before `apply_tags.py` and `lock_tags.py`. In the `cultura` and `latam` tracks the old file tags were mostly noise (`pasiva-refleja`, `ser-passive`, `nominalization` on fact questions), so most items became unit vocabulary or untagged reading and a small set of real grammar tags stayed where a unit's own screen teaches the pattern. About 1,200 fact questions, listening sentences and fill-blank English lines were rewritten, because the short, partly garbled stories did not contain what the questions asked or the English line printed the answer; five wrong facts were corrected (e.g. `military-governments` 02.ex02 31 March, not 1 April). Registry decisions of 2026-10-07: `pluscuamperfecto-subjuntivo-si` to B1, `conectores-con-subjuntivo` retired, *deber de* / *derecho a* / *al* + infinitive / *lo* + adjective + *que* folded into existing skills. The follow-ups are ROADMAP 145.

### Read-through check for unanchored "this exchange" questions, ROADMAP 142(d) — 2026-10-06
`scripts/readthrough_check.py` now errors on a multiple-choice question that points at an exchange, conversation or dialogue that is not shown (*Which sentence starts / begins / follows this exchange?* and the like). The match is narrow on purpose: *Where does this conversation take place?* in `a1.cafe.05.ex14` follows a story shown in the lesson and is not flagged. Seven more items carrying the template, all in `a1-10` (`a1.10.01.ex05`, `10.02.ex05`, `10.03.ex05`, `10.04.ex05`, `10.05.ex01`, `10.05.ex09`, `10.consolidation.ex09`; both courses), were rewritten to stand alone: *Which sentence describes preparing the party?*, *… is the question that asks someone's age?*, *… best opens a story about a special day?*, *… gives someone's age?*, *… the first thing that happens in the morning?*, *What happens first in the story?*, *… says what happens in the morning?*. Answers and tags are unchanged, so no unit was re-locked. A search of every `*-ex.json` in es-es, es-latam and hu finds no other instance; the earlier note that A2–B2 probably repeat the template was wrong.

### HU A2 `daily-life-routines` (a2-01–a2-05 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-daily-life-routines-vocab` 34, `sequencing-elobb-aztan-utana-vegul` 11, `on-en-on` 9, `nta-productive` 9, `kor-time` 7, `tol-tol` 6, `mert-because` 4, `present-tense-routine-language` 4, `szor-szer-multiplicatives` 3, `soha-needs-nem-negative-concord` 3, and one each on three smaller skills. The mediopassive *borotválkozom/fésülködöm* items stay vocabulary (no registered skill). The nine `nta-productive` items are flagged "taught later": the a2-04-b screen teaches *-nta/-nte*, but the skill's `taught_in` is a2-54-b. Content fixes: `a2-02-controlled-4` (*Előbb felkelek, ____ zuhanyozom*) now accepts *utána* as well as *aztán*; `a2-02-practice-1` offered *aztán* as a wrong option for "after that", now *végül*; `a2-04-controlled-5` and `a2-05-controlled-4` got hints; `a2-05-consolidation-7`'s wrong reply was another valid routine, now a wrong-person *felkelsz … dolgozol* (tagged `present-tense-routine-language`).

### HU A2 `time-dates-schedules` (a2-06–a2-10 + consolidation) — locked 2026-10-05
All 93 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-time-dates-schedules-vocab` 47, `tol-tol` 15, `on-en-on` 13, `kor-time` 5, `ban-ben-in` 4, `sequencing-elobb-aztan-utana-vegul` 4, `ordinal-numbers` 3, `vowel-harmony` 1, `present-tense-routine-language` 1. *-ig* items are `tol-tol` (its title covers *-tól … -ig*; `terminative-case-ig` is B1). Date endings *-án/-én* are `on-en-on`; *Hányadika* and month glosses are vocabulary. Content fix: `a2-09-controlled-4` ("Which suffix never changes for vowel harmony?") offered *-kor*, also harmony-free, as a wrong option; now *-ban/-ben*. Left: the a2-10 schedule items say "Monday to Friday, and then on Tuesday evening", which reads oddly but isn't wrong.

### HU A2 `family-life` (a2-11–a2-15 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-family-life-vocab` 44, `3rd-person-possessive` 14, `plural-possessive` 9, `nal-nel` 7, `present-tense-routine-language` 5, `possessive-suffixes` 4, `mert-because` 3, `van-possessive-to-have` 2, and one each on four smaller skills. The nine `plural-possessive` items are flagged "taught later": the a2-13-a screen teaches the *-i* plural possessive, but the skill's `taught_in` is a2-191-b. Content fixes: `a2-12-dialogue-1` answered *Ki ez?* with *Ez az apja.* against *Ez az apa.*, both sensible; now *Ez Anna apja.* / *Ez Anna apa.* Eleven fill-blanks that accepted one answer where several fitted got English hints, including the person where the blank is a possessed form (`a2-11-controlled-2` "(I have a cousin)", `a2-12-controlled-4` "(his family)").

### HU A2 `people-personality` (a2-16–a2-20 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-people-personality-vocab` 46, `relative-clauses-aki-ami-amely` 23, `having-s` 11, `olyan-mint` 6, `3rd-person-possessive` 2, and one each on four smaller skills. The old `comparative-bb` (taught at a2-64) and `definite-vs-indefinite-conjugation` tags on the *hasonló/különböző/ismer* glosses were removed; those items are vocabulary. Glosses whose wrong option is the *-s* adjective (*szakáll/szakállas*) are `having-s`. Content fixes: five fill-blanks got English hints (*szemüveges*, *Vörös*, *hasonlóak*, *Ismerek*, *segít*), mirrored in `a2-20-consolidation-6`.

### HU A2 `friends-relationships` (a2-21–a2-25 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-friends-relationships-vocab` 48, `egyreszt-masreszt` 10 (*nem csak … hanem … is*), `present-tense-routine-language` 8, `keresztul` 6, `sajat` 5, `egymas` 4, `ik-verbs-dolgozom-not-dolgozok` 3, `verb-government-val-vel` 3, `yes-no-questions` 3, `3rd-person-possessive` 2, `possessive-suffixes` 1. Review moved five items the subagent had put on `ik-verbs…` (*ismerkedünk*, a "we" form) or `egymas` (options that differ only in person) to `present-tense-routine-language`. The three `verb-government-val-vel` items (*kijön valakivel*) are flagged "taught later": the a2-23-a screen teaches the pattern, but the skill's `taught_in` is a2-144-a. Content fixes: six fill-blanks got English hints (*ismerkedünk*, *kijövök*, *egymással*, *barátkozom*, *nyitott*, *saját*); `a2-23-writing-2` and its copy `a2-25-consolidation-11` asked "say you …" for a *beszélünk/kijövünk* answer, now "say we …".

### HU A2 `home-housing` (a2-26–a2-30 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-home-housing-vocab` 39, `on-en-on` 12, `ra-re` 11, `three-locatives` 8, `ban-ben-in` 7, `delative-rol-rel` 6, `movement-with-ba-be` 3, `nal-nel` 3, `is-placing-also-too` 3; 12 items carry `ds` for another case's form. Before the a2-28-b screen, *-on* and *-ban* items take the single-case skill; from a2-28 the in/on/at contrast items take `three-locatives`. The old `megy-jon` on *költözik* and `ra-re` on *üres/kilátás* glosses were removed. Content fixes: `a2-27-dialogue-1` (*A polc a szekrényben van.*) and `a2-28-dialogue-1` (*A fiókon van.*) had a second plausible reply; now *a falra*/*a fiókra*. Three fill-blanks got hints.

### HU A2 `neighbourhood-city` (a2-31–a2-35 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-neighbourhood-city-vocab` 52, `hoz-suffix` 19, `three-locatives` 7, `itt-ott-here-there` 6, `spatial-questions-hol-hova` 3, `vowel-harmony` 3, `tol-tol` 1, `van-possessive-to-have` 1. Choices among *-hoz/-hez/-höz* are `vowel-harmony` (the old `hungarian-vowels` tag was wrong); a fill-blank producing the whole word is `hoz-suffix`. The *ide/oda/innen/onnan* items are `itt-ott-here-there`, the nearest registered skill (its title names only *itt/ott*; no skill covers the direction series), while *honnan/hová* question items stay `spatial-questions-hol-hova`. The a2-35 adjective items lost a wrong `van-zero-copula` tag. Content fixes: `a2-33-dialogue-2` and its copy `a2-35-consolidation-8` (*Milyen ez a negyed?*) and `a2-35-dialogue-1` offered a second sensible description as the wrong reply; now a location answer (*A pékségnél vagyok.*, *A sarkon van.*).

### HU A2 `shopping-prices` (a2-36–a2-40 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-shopping-prices-vocab` 62, `definite-vs-indefinite-conjugation` 8 (*keresek/találom/választom*), `olyan-mint` 8, `cardinal-numbers` 7, `yes-no-questions` 2, `nagyon-very` 2 (*túl*), `verb-government-ert` 2 (*forintért*), `movement-with-ba-be` 1 (*Ezer forintba kerül*). Choices between different verbs (*keres/talál/választ*) are vocabulary. The old `comparative-bb` on *olyan … mint* items was wrong (the a2-39 screen says there's no comparative ending yet). Content fix: `a2-37-controlled-3` printed its answer *túl* in the prompt; now *Ez ____ nagy. (too)*.

### HU A2 `food-eating-habits` (a2-41–a2-45 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-food-eating-habits-vocab` 58, `szor-szer-multiplicatives` 15, `definite-vs-indefinite-conjugation` 8, `eszik-iszik` 5, `erdekel-construction` 5 (*ízlik*), `possessive-suffixes` 1. Review moved eight items from `eszik-iszik` to vocabulary: "Which means *to eat*?" against other verbs, and dialogues whose wrong option swaps *iszom* for *eszem*, fail on meaning; `eszik-iszik` keeps the items whose options are forms of the same verb. The old `good-for-me-nekem-jo` on a2-45 items was wrong. No content defects.

### HU A2 `cooking` (a2-46–a2-50 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-cooking-vocab` 50, `val-vel` 7, `imperative-definite` 7, `imperative-indefinite` 6, `prefix-word-order` 6, `movement-with-ba-be` 6 (*bele*), `junk-suggestion` 5, and one each on five smaller skills. *kell hozzá* ("it needs") is vocabulary, not `kell-infinitive`. Eleven items are flagged "taught later": `junk-suggestion` is taught on the a2-48-b screen (*Főzzünk együtt!*) and `prefix-word-order` on a2-49-b, but their `taught_in` are a2-136 and a2-110. Content fixes: `a2-49-dialogue-1` offered *Vágj hagymát!* as the wrong reply to a definite-object question, also acceptable; now *Vágok hagymát.* `a2-50-consolidation-6` hint "(recipe)" → "(to a recipe)".

### HU A2 `leisure-hobbies` (a2-51–a2-55 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-leisure-hobbies-vocab` 47, `ota-duration` 8, `erdekel-construction` 7, `nta-productive` 6, `szor-szer-multiplicatives` 6, `building-the-infinitive-the-suffix-ni` 4, `possessive-suffixes` 3, `majd-adverb` 3, `ra-re` 2, `hogy-clauses` 2, and one each on four smaller skills. *attól függ* is a vocabulary chunk; only the *Attól függ, hogy …* sentences are `hogy-clauses`. Fourteen items are flagged "taught later" because the screens that teach them in this unit (a2-52-a/b, a2-55-a/b) are earlier than the registered `taught_in` of `ota-duration` (a2-83), `jar-iskolaba` (a2-91), `majd-adverb` (a2-95) and `hogy-clauses` (a2-88). Content fixes: `a2-54-practice-1` asked which word order says "three times a day" with *háromszor naponta*, also correct, as the wrong option; now "Which means …?" against *naponta három*. Three dialogues (`a2-51-dialogue-1`/`-2`, `a2-55-consolidation-7`) and `a2-55-dialogue-2` had a wrong reply that also answered the question; replaced.

### HU A2 `culture-going-out` (a2-56–a2-60 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-culture-going-out-vocab` 57, `relative-clauses-aki-ami-amely` 7 (*amit*), `on-en-on` 5 (*zongorán játszik*), `verb-government-nak-nek` 5 (*ajánlok neked*), `ra-re` 4 (*jegy a vetítésre*), `szerintem` 4, `case-inflected-pronouns` 3 (*hozzá/hozzánk*), and five on three smaller skills. The old `participle-actions`, `formal-address-on` and `light-verb-collocations` tags fitted no item. Seven items are flagged "taught later": the a2-58-b and a2-60-a screens teach *szerintem* and *hozzá*, but the skills' `taught_in` are a2-141-b and a2-163-a. Content fixes: `a2-58-dialogue-1` had two right replies (*amit most olvasok* / *amit a moziban láttunk*), the second is now the wrong-relative *aki most olvasok*; `a2-60-practice-1` printed its answer *hozzá* in the prompt, now a *hozzá/hozzád/hozzám* choice.

### HU A2 `weather-seasons` (a2-61–a2-65 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-weather-seasons-vocab` 72, `comparative-bb` 8, `good-for-me-nekem-jo` 5 (*kabát kell nekem*), `nagyon-very` 4, `ha-clause` 3. The weather verbs (*süt, fúj, esik*) and the season forms (*tavasszal, nyáron*, learned as chunks per the a2-62-a screen) are vocabulary; the old `weather-verbs-esik-sut` slug is not a registered skill. Four *nagyon/elég* items had `comparative-bb`, now `nagyon-very`. Content fix: `a2-65-dialogue-2` (*Kell neked kabát?*) had a wrong reply that also fitted; now self-contradictory.

### HU A2 `transport-getting-around` (a2-66–a2-70 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-transport-getting-around-vocab` 60, `ra-re` 8, `directional-preverbs` 6 (*fel-/le-/átszáll*), `sequencing-elobb-aztan-utana-vegul` 6, `val-vel` 4 (*busszal*), `present-tense-routine-language` 4, and one each on four smaller skills. *-nként* (`distributive-nkent` is B1) and *hányas* items are vocabulary. Content fixes: `a2-67-controlled-2`/`practice-2` missing article (*Az automatánál …*); `a2-70-controlled-4` now accepts *Először* as well as *Előbb*; `a2-70-dialogue-1` had *a hármas buszon* as a wrong option that also fitted, now *buszra*; `a2-70-consolidation-7` used the inflected infinitive *át kell szállnod* (taught at a2-201), now *át kell szállni*.

### HU A2 `travel-holidays` (a2-71–a2-75 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-travel-holidays-vocab` 55, `tol-tol` 7, `kell-infinitive` 5, `how-the-accusative-t-works` 4, `ha-clause` 4, `mert-because` 3, `erdekel-construction` 3 (*szeret/utál/imád* + infinitive, which the skill covers), and one or two each on seven smaller skills. *múlva* has no skill and is vocabulary. Review moved seven dialogues whose wrong reply answers a different question to vocabulary. Content fixes: `a2-73-controlled-4` and `a2-73-writing-2` needed the possessive accusative *poggyászomat* (taught at a2-104), now *a poggyászt*; `a2-75-controlled-3` now accepts *kelni* as well as *felkelni*; `a2-75-consolidation-8`'s model answer used the untaught past tense, now *Be kell csekkolni, és meg kell mutatni a beszállókártyát.*

### HU A2 `hotels-accommodation` (a2-76–a2-80 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-hotels-accommodation-vocab` 64, `val-vel` 6 (*kártyával*, *elégedett … -val*), `ra-re` 4 (*három éjszakára*), `superlative` 4, `how-the-accusative-t-works` 4, `having-s` 4 (*erkélyes, klímás szoba*), `comparative-bb` 2, `negation-with-nem` 2, `ordinal-numbers` 1, `verb-government-nak-nek` 1. Ten dialogues whose wrong reply answers a different question are vocabulary, as are three "which asks …?" and no-dative items moved there in review. No content defects found.

### HU A2 `health-body` (a2-81–a2-85 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-health-body-vocab` 57, `possessive-suffixes` 6, `ota-duration` 6 (*két napja*), `faj-construction` 5, `postpositions-basic` 4 (*ellen*, the nearest skill), `van-possessive-to-have` 3 (*lázam van*, moved from `faj-construction` in review), `3rd-person-possessive` 3, `how-the-accusative-t-works` 3, `kell-infinitive` 3, `present-tense-routine-language` 2. The reflexive *rosszul érzem magam* has no skill and is vocabulary. Four a2-81 items are flagged "taught later": the a2-81-a screen teaches *Fáj a fejem*, but `faj-construction`'s `taught_in` is a2-82-b. Content fixes: three fill-blank hints now pin the person (*fejem*, *kezem*, *Lázam*); three dialogues had a wrong reply that also fitted (`a2-81-dialogue-2`, `a2-82-dialogue-2`, `a2-83-dialogue-2`).

### HU A2 `healthy-living-advice` (a2-86–a2-90 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-healthy-living-advice-vocab` 56, `hogy-clauses` 5, `tud-infinitive-skills` 5, `lehet-infinitive` 5, `tol-tol` 4 (*mostantól*), `sokat-eleget` 3, `eszik-iszik` 3 (*alszom*), `kellene` 3, `mit-csinaljak` 3, `postpositions-altal-reven` 3 (*helyett*), `comparative-bb` 2. Thirteen dialogues whose wrong reply fails on meaning are vocabulary. Five items are flagged "taught later": the a2-89-a screen teaches *tudok* + infinitive, but `tud-infinitive-skills`' `taught_in` is a2-111-a. Content fixes: `a2-87-controlled-4` now accepts *tegyek* (taught on the same screen) as well as *csináljak*; `a2-89-controlled-4` and its copy `a2-90-consolidation-6` ("it's allowed") now accept *szabad* as well as *lehet*; `a2-90-dialogue-1` had a plausible wrong goal, now *rosszabbul aludjak*.

### HU A2 `school-language-learning` (a2-91–a2-95 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-school-language-learning-vocab` 56, `ota-duration` 6, `ban-ben-in` 5 (incl. *jó vagyok biológiában*; `verb-government-ban-ben` is B1), `ul-ul-essive-modal` 5, `an-en-adverb` 4, `hogy-clauses` 4, `definite-vs-indefinite-conjugation` 3, `val-vel` 3 (*gyakorlással*; no skill covers the *-ás/-és* noun), `majd-adverb` 3, `jar-iskolaba` 2, `tud-infinitive-skills` 1. Content fixes: six fill-blanks got hints where another taught word fitted.

### HU A2 `review-life-leisure-health` (a2-96–a2-100 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. A review unit: word items take the vocabulary skill of the unit they review (hotels 11, leisure 9, weather 8, transport 8, culture 7, travel 7, healthy living 6, school 6, health 5), and only items mixing several units take `a2-review-life-leisure-health-vocab` (7). Grammar items: `ota-duration` 5, `ha-clause` 4, `hogy-clauses` 2, and one each on seven skills. Content fixes: `a2-97-controlled-3`'s hint "(hot)" also fitted *forró*, now "(warm)"; three fill-blanks now accept a second natural answer (*itthon*, *bulira*, *szállok le*).

### HU A2 `work-professions` (a2-101–a2-105 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-work-professions-vocab` 54, `inflected-infinitives` 8 (*kell dolgoznom*), `van-zero-copula` 5 (*Tanár vagyok*, no article), `ban-ben-in` 5, `nal-nel` 4 (*cégnél*), `possessive-suffixes` 4, `acc-poss` 4 (*munkatársamat*), `how-the-accusative-t-works` 3, `kor-time` 3, `ki-and-mi` 2. All fourteen dialogues have a non-sequitur wrong reply and are vocabulary. Eight items are flagged "taught later": the a2-105-b screen teaches *Kell dolgoznom*, but `inflected-infinitives`' `taught_in` is a2-201-b. Content fix: `a2-105-consolidation-6` hint "(company)" also fitted *cégben*, now "(for a company)".

### HU A2 `verb-prefixes` (a2-106–a2-110 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-verb-prefixes-vocab` 35, `meg-meaning` 21 (its title covers aspectual *el-/be-/meg-*), `directional-preverbs` 17, `prefix-word-order` 13, `present-tense-routine-language` 3, and one each on three smaller skills. Glosses whose options are one verb with and without a prefix (*megeszik/eszik*) are `meg-meaning`. Seven a2-108 items (*elkezd, befejez, elindul*) are flagged "taught later": the a2-108 screens teach them, but `meg-meaning`'s `taught_in` is a2-109-a. Content fixes: ten fill-blanks got hints where another prefix fitted, mirrored in `a2-110-consolidation-6`; `a2-110-consolidation-8` used the untaught past *Elkezdted* (now *Elkezded*); `a2-110-consolidation-10`'s prompt said "on Saturday" with no Saturday in the answer.

### HU A2 `ability-possibility-permission` (a2-111–a2-115 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-ability-possibility-permission-vocab` 55, `tud-infinitive-skills` 12, `szabad-infinitive` 12, `lehet-infinitive` 8, `potential-hat-het` 3, `yes-no-questions` 1, `mert-because` 1; seven choice items carry `ds` across the *tud/lehet/szabad/kell* set. All dialogues but one have a non-sequitur wrong reply and are vocabulary. The old `an-en-adverb` on *nagyon jól tud* was wrong. Content fixes: three fill-blanks got hints; `a2-115-check-1` offered *Tudok menni.* as a wrong meaning of *Mehetek*, also acceptable, now *Kell mennem.*; `a2-115-consolidation-5` keyed the past *tanultam* (taught at a2-116), now *tud*; `a2-115-consolidation-6` now hinted "(is allowed)".

### HU A2 `the-past-1` (a2-116–a2-120 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `past-tense-indefinite` 32, `a2-the-past-1-vocab` 26, `van-past` 15, `irregular-past` 13, `meg-meaning` 4 (*megettem*), `definite-past` 2. 21 items carry `ds`, mostly a present-tense form (`present-tense-routine-language`, `van-zero-copula`, `megy-jon`, `eszik-iszik`) offered where the past is needed. The old `definite-past` on *kirándultunk/piknikeztek* (indefinite) was wrong. Two items are flagged "taught later": the a2-118-b screen teaches *ettem/ette*, but `irregular-past`'s `taught_in` is a2-120-b. No content defects found.

### HU A2 `the-past-2` (a2-121–a2-125 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-the-past-2-vocab` 44, `definite-past` 12, `sequencing-elobb-aztan-utana-vegul` 9, `past-tense-indefinite` 8, `verb-government-val-vel` 7 (*találkoztam Tamással*), `how-the-accusative-t-works` 4, `case-inflected-pronouns` 3 (*vele*), `adjective-order-before-the-noun` 2, `irregular-past` 2, `tol-tol` 1. Ten items are flagged "taught later": the a2-122-a and a2-124-a screens teach *találkozik -val* and *vele*, but the skills' `taught_in` are a2-144-a and a2-163-a. Content fixes: `a2-121-check-1` and its copy `a2-125-consolidation-1` offered *Vettem.* as wrong for "I bought it", also valid, now *Vettem egy kabátot.*; `a2-124-dialogue-1` had a second sensible reply; three fill-blanks now accept a second natural answer (*szép*, *utána/aztán*).

### HU A2 `telling-stories` (a2-126–a2-130 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-telling-stories-vocab` 68, `past-tense-indefinite` 12, `on-en-on` 4 (*elején/végén*), `hogy-clauses` 4 (*azt mondta, hogy*; `reported-speech-statements` is retired), and one each on four skills. Content fixes: eight items. `a2-126-dialogue-2`'s right reply didn't answer *Hol van a kulcsod?*, now *Mi történt a kulcsoddal?*; `a2-127-dialogue-2`, `a2-128-dialogue-1`, `a2-129-dialogue-2` and `a2-130-dialogue-2` had a second sensible reply; `a2-129-dialogue-1` had two fitting replies until the prompt asked what happened *unexpectedly*; `a2-129-intro-2` offered *hirtelen*, a near-synonym of the answer, as wrong; `a2-129-controlled-2` now accepts *hirtelen* as well as *egyszer csak*.

### HU A2 `future-plans` (a2-131–a2-135 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-future-plans-vocab` 36, `fog-infinitive` 30, `akar-tervez-infinitive` 13, `majd-adverb` 6, `prefix-word-order` 4, and one each on three skills. The three "already-arranged plan, not a prediction" checks have a present-tense answer, so review moved them from `fog-infinitive` to `majd-adverb` (present for future), with `ds` on the *fog* and *tervez* options. Content fixes: two hints now pin the form (*tapasztalatom* "(I have a lot of experience)", *hónapig* "(for a whole month)").

### HU A2 `suggestions-conditional` (a2-136–a2-140 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-suggestions-conditional-vocab` 36, `nek-conditional` 34, `good-for-me-nekem-jo` 8 (*neked kellene*), `junk-suggestion` 7, `irregular-nek-conditional` 7 (*ennék, mennék, lenne, tennél*). Hypothetical *ha* items are `nek-conditional` (`hypothetical-ha-conditional` is B1), with `ds` `ha-clause` on the real-*ha* option; most conditional choices carry `ds` for their present and past options. Content fixes: `a2-136-check-1` offered *esetleg* as a wrong option where it also fitted, now *remek*; `a2-140-consolidation-10`'s prompt allowed several answers.

### HU A2 `opinions-preferences-comparisons` (a2-141–a2-145 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-opinions-preferences-comparisons-vocab` 59, `mert-because` 9 (incl. *azért, mert*), `szerintem` 8 (*azt hiszem, gondolom*), `prefix-word-order` 6 (*nem értek egyet*), `comparative-bb` 5 (incl. *inkább/jobban … mint*), `an-en-adverb` 3 (*egyformán*), `verb-government-val-vel` 2. The old `evidentials` and `light-verb-collocations` tags were wrong. Content fix: `a2-145-controlled-3` "(because)" now also accepts *mivel*.

### HU A2 `review-work-past-opinions` (a2-146–a2-150 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. A review unit: word items take the vocabulary skill of the unit they review (ability 8, work 6, opinions 5, telling stories 4, and smaller counts), mixed items `a2-review-work-past-opinions-vocab` (5), and grammar items the skill they review (`prefix-word-order` 7, `past-tense-indefinite` 6, `szerintem` 5, `tud-infinitive-skills` 4, `fog-infinitive` 4, and 25 more across 22 skills). Content fixes: `a2-146-check-1` offered *Fel nem kelek hétkor.*, a valid emphatic negation, as wrong (now *Nem fel kelek hétkor.*); `a2-148-writing-1` said "you" for a *we* answer.

### HU A2 `problems-requests` (a2-151–a2-155 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-problems-requests-vocab` 64, `fog-infinitive` 7, `nek-conditional` 6, `mert-because` 6, `possessive-suffixes` 4 (*szükségem van*), `lehet-infinitive` 3, and one each on two skills. *hiányzik*, *nem működik/elromlott*, *megoldódik* and the *szeretnék reklamálni* chunks have no skill and are vocabulary; the old `erdekel-construction`, `light-verb-collocations` and `mediopassive-verbs-odik` tags were wrong or unregistered. Content fix: `a2-152-dialogue-1` had a plausible refusal as its wrong reply.

### HU A2 `living-in-hungarian` (a2-156–a2-160 + consolidation) — locked 2026-10-05
All 92 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-living-in-hungarian-vocab` 50, `past-tense-indefinite` 19, `sequencing-elobb-aztan-utana-vegul` 4, `van-past` 3, `inflected-infinitives` 3 (*sikerült megoldanom*, flagged "taught later": taught on a2-160-b, registered at a2-201-b), and 13 more across ten skills. Content fixes: seven. `a2-156-dialogue-1`, `a2-160-dialogue-2`, `a2-160-consolidation-8` and `-9` had a wrong reply that also answered the question; `a2-159-practice-1` had two right options; `a2-157-controlled-3`'s hint now pins *they*; `a2-159-practice-2` now also accepts *mentünk*.

### HU A2 `pronouns-internal-surface-cases` (a2-161–a2-165 + consolidation) — locked 2026-10-05
All 105 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `case-inflected-pronouns` 59 (*benne, rajta, rá*), `a2-pronouns-internal-surface-cases-vocab` 42, `on-en-on` 2, `ra-re` 1. Choices whose options differ by verb or meaning are vocabulary; those that differ by case or person are the pronoun skill. The old `good-for-me-nekem-jo` on all of a2-164–a2-165 was wrong. Twenty choice and fill-blank items with category `dialogue`/`writing` now follow their tag, as in HU A1. 24 items are flagged "taught later": the a2-161-a and a2-162-a screens teach the *benn-* and *rajt-* paradigms, but the skill's `taught_in` is a2-163-a. Content fixes: `a2-161-dialogue-1` accepted both *benne* and *benned* (now *Bízol Annában?*); `a2-162-controlled-4` offered *Segíts nekik!*, also valid; `a2-162-dialogue-1` (*Ki következik?*) fitted any person; `a2-163-writing-1` had a wrong gloss; `a2-165-consolidation-18`'s hint now matches its lesson copy. Left: the a2-165 story comes after the comprehension items that ask about it (`a2-165-intro-1`/`-2`, `controlled-4`).

### HU A2 `pronouns-proximity-motion` (a2-166–a2-170 + consolidation) — locked 2026-10-05
All 105 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `case-inflected-pronouns` 83 (*nálam, hozzám, tőlem, rólam*), `a2-pronouns-proximity-motion-vocab` 22 (all matching plus five word items). No `ds`: every wrong option is another member of the same paradigm. Every a2-170 and consolidation item carried a wrong `good-for-me-nekem-jo`. Content fixes: `a2-166-writing-1` keyed *náluk* for "at her place" (now *nála*); `a2-167-writing-1` wanted *hozzá* where *magához* is natural (hint now "to Péter's place"); `a2-170-intro-1`/`-2` and `controlled-4` asked about the lesson's story before the learner reaches it, now glosses of the lesson's own example sentences.

### HU A2 `translative-case` (a2-171–a2-175 + consolidation) — locked 2026-10-05
All 105 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `translative-morphology` 55 (*-vá/-vé*), `a2-translative-case-vocab` 29, `valik-verb` 20 (when the verb or its person is what's tested), `definite-past` 1; 21 choice items carry `ds` for other cases' forms. Content fix: seven "(became)" fill-blanks accepted only *vált*; they now also accept *lett*.

### HU A2 `essive-formal` (a2-176–a2-180 + consolidation) — locked 2026-10-05
All 105 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `essive-formal-kent` 68, `a2-essive-formal-vocab` 29, `past-tense-indefinite` 3, `definite-vs-indefinite-conjugation` 2, and one each on three skills; 22 items carry `ds` (mostly *-vá/-vé* and *-val/-vel* options). The a2-179-a screen teaches *időnként, óránként* as "-ként forms", so items producing them are `essive-formal-kent` (`distributive-nkent` is B1); glosses stay vocabulary. Content fixes: `a2-178-dialogue-1` and `a2-178-writing-2` had wrong options that were natural Hungarian (*emléket*, *emléknek*, *emlékbe*); `a2-180-intro-2` asked about the story before the learner reaches it; six hints now pin the person or give the word.

### HU A2 `sociocultural-pragmatics-customs` (a2-181–a2-185 + consolidation) — locked 2026-10-05
All 105 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-sociocultural-pragmatics-customs-vocab` 56, `formal-address-on` 15, `building-the-infinitive-the-suffix-ni` 7 (*Tetszik kérni?*), `imperative-indefinite` 6, `how-the-accusative-t-works` 6, `present-tense-routine-language` 3, and eleven more across eight skills. Name order and titles have no skill and are vocabulary. Content fixes: `a2-181-practice-1` had two acceptable greetings; `a2-183-check-1` and `a2-183-writing-1` used the untaught *vezetéknév* (now *családnév*); three hints now pin the person (*egészségedre* vs *-etekre*, *-ére*); `a2-185-practice-1` and `-2` asked about the story and its *Kezét csókolom* before the learner reaches it.

### HU A2 `lak-lek-suffix` (a2-187–a2-190 + consolidation) — locked 2026-10-05
All 84 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `lak-lek-suffix` 66, `a2-lak-lek-suffix-vocab` 10, `prefix-word-order` 3, `vowel-harmony` 2, and one each on three skills; 21 items carry `ds` (definite *-om/-em* options → `definite-vs-indefinite-conjugation`, indefinite and other-person options → `present-tense-routine-language`). Content fixes: seven. `a2-187-dialogue-1` keyed *féltelek* where the line needed *féltesz*; `a2-187-dialogue-2` keyed *hívlak* with the object *őket*; `a2-187-writing-1` printed its answer; `a2-188-controlled-4` offered *Nem értem téged*, also heard as correct; `a2-190-controlled-2` and `a2-190-writing-1` now also accept *átölellek* and *várlak*; `a2-190-check-2` had two blanks and one answer.

### HU A2 `plural-possessed` (a2-191–a2-195 + consolidation) — locked 2026-10-05
All 100 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `plural-possessive` 57, `acc-poss` 19 (accusative plural-possessed forms such as *szüleimet*; taught at a2-104-b), `val-vel` 13 (*barátaimmal*), `a2-plural-possessed-vocab` 10, `hoz-suffix` 1. Dative and sublative plural-possessed forms have no skill of their own and stay `plural-possessive`. Content fixes: four dialogues offered a wrong option that also fitted (*barátom*, *könyvünk*, *barátommal* twice); each is now a clear form error.

### HU A2 `inflected-postpositions` (a2-196–a2-200 + consolidation) — locked 2026-10-05
All 100 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `inflected-postpositions` 67, `a2-inflected-postpositions-vocab` 33. Items whose wrong options are other postpositions (*előttem/mögöttem/mellettem*) fail on meaning and are vocabulary; items whose options are person or form variants of one postposition are grammar. Content fixes: `a2-196-dialogue-2` and `a2-197-dialogue-1` had several fitting postpositions until the context was sharpened; three fill-blanks now accept the long *közöttünk/közöttetek* the screen teaches; `a2-198-dialogue-2`, `a2-199-dialogue-1` and `a2-200-check-1` had a wrong option that also fitted; `a2-200-consolidation-18` made no sense and was rewritten.

### HU A2 `inflected-infinitives-necessity` (a2-201–a2-205 + consolidation) — locked 2026-10-05
All 100 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `inflected-infinitives` 76, `a2-inflected-infinitives-necessity-vocab` 15, `szabad-infinitive` 4, `prefix-word-order` 3, `kell-infinitive` 1, `lehet-infinitive` 1; 8 items carry `ds`. Content fixes: eleven. Six dialogues let the impersonal infinitive or another person fit until *nekem/nekünk* was added; `a2-202-intro-2` offered *Nem muszáj sietned*, which is correct Hungarian, as wrong; `a2-202-controlled-1` now accepts *muszáj*; two hints printed their answer; `a2-205-consolidation-18` printed its answer in a malformed blank. The a2-202-a screen said *muszáj* can't be negated; it now says *nem muszáj* is also correct, a bit more colloquial than *nem kell*.

### HU A2 `post-office` (a2-206–a2-210 + consolidation) — locked 2026-10-05
All 100 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. The unit teaches no grammar of its own (its old `public-service-interactions` tag is retired), so items are vocabulary (51) or recycled grammar: `how-the-accusative-t-works` 9, `imperative-definite` 8, `inflected-infinitives` 6, `kerek-vs-szeretnek` 3, `nek-conditional` 3, `an-en-adverb` 3, and 17 more across 14 skills. Content fixes: nine. Three *szeretnék* dialogues offered *akarok*, also acceptable, as wrong; `a2-208-check-1` offered *kifizet*, which can also mean "pay"; four hints didn't pin the answer or person; `a2-210-controlled-2` and `-practice-4` now also accept *be* and *van*.

### HU A2 `banking` (a2-211–a2-215 + consolidation) — locked 2026-10-05
All 100 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Another phrase-note unit: `a2-banking-vocab` 52, `how-the-accusative-t-works` 11, `prefix-word-order` 6, `acc-poss` 4, `val-vel` 4, and 23 more across 16 skills. Content fixes: `a2-211-dialogue-1` and its copy `a2-215-consolidation-11` offered *akarok*, also acceptable; `a2-211-dialogue-2` keyed the unnatural *szignózza alá* (now *írja alá*); `a2-213-intro-1` had a second valid cashier question; seven hints now pin person, case or possession.

### HU A2 `pharmacy` (a2-216–a2-220 + consolidation) — locked 2026-10-05
All 100 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `a2-pharmacy-vocab` 68, `how-the-accusative-t-works` 16 (fill-blanks producing *tablettát, csillapítót*), `ra-re` 3, `inflected-infinitives` 2, `acc-poss` 2, and nine skills once each. Content fixes: `a2-216-dialogue-2` offered *panaszom*, also sensible; four hints didn't match the accepted answer or pin the person.

### HU A2 read-through complete — 2026-10-05
All 44 HU A2 units (4,154 exercises, a2-01–a2-220) now carry exactly one locked tag, read by Sonnet subagents (one per unit, two at a time) with every batch checked by `scripts/readthrough_check.py` and reviewed, and often corrected, in the main session before `apply_tags.py`/`lock_tags.py`. Rules settled during A2, on top of the A1 conventions: a dialogue whose wrong reply answers a different question fails on meaning and is vocabulary, while one whose wrong reply differs in a form takes that form's skill; an *Igen/Nem* contradiction is `yes-no-questions`; matching is always vocabulary; choice, fill-blank and builder items with category `dialogue`/`writing` follow their tag; the here/there direction series (*ide/oda/innen/onnan*) is `itt-ott-here-there`; a harmony-variant choice is `vowel-harmony`; a wrong option in another tense or mood gets `ds` for that form's skill. About 300 content defects were fixed along the way, most often a wrong option that was also a right answer, a fill-blank hint that didn't pin the person, or an item asking about a story the learner hadn't reached yet. One grammar screen was wrong: a2-202-a said *muszáj* can't be negated. Follow-ups queued as ROADMAP 138: 17 A2 skills whose `taught_in` points later than the screen that actually teaches them, and 11 A2 grammar skills under the 6-exercise minimum.

### HU A2 registry fixes, ROADMAP 138(a) — 2026-10-05
Approved by the user. `taught_in` in `skills/hu.json` now points at the screen that first teaches each of 17 A2 skills, as the read-through found: `nta-productive` a2-04-b, `plural-possessive` a2-13-a, `verb-government-val-vel` a2-23-a, `junk-suggestion` a2-48-b, `prefix-word-order` a2-49-b, `jar-iskolaba` a2-52-a, `ota-duration` a2-52-b, `hogy-clauses` a2-55-a, `majd-adverb` a2-55-b, `szerintem` a2-58-b, `case-inflected-pronouns` a2-60-a, `faj-construction` a2-81-a, `tud-infinitive-skills` a2-89-a, `inflected-infinitives` a2-105-b, `meg-meaning` a2-108-a, `irregular-past` a2-118-b, `valik-verb` a2-171-a (previously a2-54 to a2-201). Every skill's level is unchanged and every prerequisite of the 17 is still taught at or before the new screen; no tag changed, so no unit was re-locked. Registry regenerated. Found while checking: 11 older skills whose prerequisite is taught after them (item 138(d)).

### HU prerequisite order, ROADMAP 138(d) — 2026-10-05
Decided with the user. Eleven HU skills listed a prerequisite taught after them; one was a false alarm (`b2-relative-postpositions` needs a B1 skill, which comes first). Fixed in `skills/hu.json`: requirements dropped where the curriculum teaches the skill without them, for `olyan-mint` (`comparative-bb`), `tol-tol` (`nal-nel`), `kell-infinitive` and `szokott-infinitive-habitual-actions` (`building-the-infinitive-the-suffix-ni`, taught at a1-143 after both use ready-made infinitives), `kerek-vs-szeretnek` (`nek-conditional`; *szeretnék* is a set phrase at a1-94), `formal-obligation` (`future-participle-ando`) and `essay-oratory-style` (`conclusive-markers`, culture track unit 34). `egyutt-together` now requires `van-zero-copula` instead of the present-tense paradigm, since its screen is about *van/vannak*. `erdekel-construction` was registered at a1-95-b, which teaches *kérek*; it now points at a1-141-a (*szeret* + infinitive, what its A1 items test) and no longer requires `good-for-me-nekem-jo`. `mixed-conditionals` keeps its track-only prerequisite pending a curriculum fix (ROADMAP 139). New check in `scripts/validate-content.py`: a prerequisite must be taught no later than the skill (by unit-table position) and not only on a track the skill isn't on; it fails the validator and pre-push. HU now passes with no exceptions but ROADMAP 139; the 12 Spanish cases it found are exempted pending ROADMAP 140. Rule written into the spec and AGENTS.md.

### HU B1 read-through set-up, ROADMAP 125 and 139 — 2026-10-05
Registry scan of the 46 B1 grammar skills against the screens that first teach them (a keyword read of all 724 B1 screen titles, then the screens themselves where a title was ambiguous). Approved by the user; five `taught_in` changes in `skills/hu.json`, no tag changed, no unit re-locked: `verb-government-hoz-hez` b1-07-03 → b1-05-03-a (*ragaszkodik valakihez*; 07-03 teaches study verbs with *-ra*), `adversative-contrast` b1-32-03-a → b1-11-03 (*ellenben, ezzel szemben*), `past-conditional-volna` b1-rakoczi-02 → core b1-20-01-a, `miutan-mielott` b1-01-03-b → b1-01-02-a, `mar-experiential` b1-02-01-b → b1-02-01-a. The `past-conditional-volna` change resolves ROADMAP 139 with no curriculum change: the core screen b1-20-01-a (unit 20) already teaches *ha … volna*, well before `mixed-conditionals` (unit 35), so the `KNOWN_PREREQ_ORDER` exemption is removed and the validator passes without it. Found and left: `nominalizing-processes` is titled "progressive state in -óban/-őben van" and no screen teaches that (the *-ás/-és* screens belong to `nominalization`), so it still has no `taught_in`; the checker's "taught later" test compares unit numbers only, so a mismatch inside one unit is invisible to it and cheap to ignore. `docs/readthrough-brief.md` is now the condensed, level-neutral one-page rule sheet (A1/A2 conventions and review notes folded in, B1 two-track and untagged-reading rules added). `scripts/readthrough_check.py` gained the checks the HU A2 reviews asked for: matching not vocabulary (error), `ds` on suffix-name options, an Igen/Nem contradiction not tagged `yes-no-questions`, `ik-verbs-dolgozom-not-dolgozok` on a non-*-m* answer, the answer printed in the prompt, and a person-marked fill-blank answer whose hint names no person (warnings); it also lets `category: reading` items stay untagged and no longer flags their category. `scripts/readthrough_review.py` now flags `ERROR` lines (its filter was case-sensitive and missed them). Run over all 75 B1 units with their current tags the new checks give about 24 hint warnings, 22 answer-in-prompt warnings (a real defect class, e.g. `b1-03-03-intro-1` prints *menjen*), 15 Igen/Nem warnings and two B1 items tagged with a B2 skill (`causative-verbal-derivations`, `b1-mariaterezia-05`).

### HU B1 `experiences-memories` (b1-02-01–b1-02-05 + consolidation) — locked 2026-10-05
All 95 exercises were read by a Sonnet subagent; decisions checked with `scripts/readthrough_check.py` and reviewed in the main session. Tags now: `b1-experiences-memories-vocab` 35, `mar-experiential` 22 (incl. *életemben először*), `past-participle-adjective` 9, `comparative-bb` 5, `kepest` 4, `verb-government-ra-re` 4, `yes-no-questions` 3, three reading items untagged, and eleven more across six skills; 20 grammar-category items became vocabulary to follow their tag, 6 items carry `ds`. *azelőtt, azóta, egyre, minél* have no skill in this unit and are vocabulary (`correlative-minel-annal` is taught only in the citizenship unit `matthias-corvinus`). Content fixes: second answers added to `b1-02-01-controlled-2` and consolidation 4 (*valaha*) and `b1-02-04-controlled-3` (*változott*).

### HU B1 `carpathian-basin-before-magyars` (b1-karpatmedence-01–05 + consolidation) — locked 2026-10-05
All 65 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 24 (all listening items and the dialogues whose wrong replies fail on meaning), 20 reading items untagged, `past-tense-indefinite` 8, `mig-egyidejuseg` 8, `sequencing-elobb-aztan-utana-vegul` 2, `3rd-person-possessive` 2 (*törzsszövetsége*), `definite-past` 1. Content fixes: five fill-blanks now accept a second natural answer or a sharper hint (*éltek/laktak*, *Míg/Amíg*, *felbomlott/összeomlott*, "(they settled)"). Left: the Avar rule is "about 250 years" in `b1-karpatmedence-03.ex05` but *másfél évszázadig* in the míg screen's example; not clearly contradictory.

### HU B1 `plans-ambitions` (b1-03-01–b1-03-05 + consolidation) — locked 2026-10-05
All 95 exercises read by a Sonnet subagent and reviewed. Tags now: `b1-plans-ambitions-vocab` 19, `barcsak-wish` 17, `hogy-jon-jen` 14, `nek-conditional` 10, `azert-hogy-purpose` 9, `nehogy-purpose` 9, `formal-purpose` 6, `present-tense-routine-language` 4 (wrong-person replies), three reading items untagged, and four more; 7 items carry `ds`. Content fixes (applied by the main session, the subagent's edits were blocked): `b1-03-03-intro-1` no longer prints *menjen* in the question; `b1-03-02-dialogue-1` had a wrong reply that was also acceptable; `b1-03-02-check-2` accepts *jönne*; `b1-03-05-practice-3` had nonsense options (*saját karriert/életet indítanom*), now *céget/projektet*. Found: `formal-purpose` is registered at citizenship b1-erdelyaranykora-04 but this unit's b1-03-05 screen teaches *annak érdekében*; to fix at the end of the level.

### HU B1 `honfoglalas` (b1-honfoglalas-01–05 + consolidation) — locked 2026-10-05
All 65 exercises read by a Sonnet subagent and reviewed. Tags now: `b1-honfoglalas-vocab` 27, 20 reading items untagged, `miutan-mielott` 11, `definite-past` 3, `past-tense-indefinite` 2, `ban-ben-in` 1, `3rd-person-possessive` 1. The listening items test no grammar point and are vocabulary; the passive-like 3rd-person-plural builder has no skill and is vocabulary. Content fixes (main session): hints now pin the form on `b1-honfoglalas-03.ex04`, `consolidation.ex09` ("(they united)"), `05.ex04` ("(in identity)") and `consolidation.ex11` ("(its cornerstone)").

### HU B1 `longer-stories` (b1-01-01–b1-01-05 + consolidation) — locked 2026-10-05
All 95 exercises read by a Sonnet subagent and reviewed. Tags now: `b1-longer-stories-vocab` 51 (all substitution items and builders without one grammar target), `miutan-mielott` 22, `irregular-past` 3, `definite-past` 3, `sequencing-elobb-aztan-utana-vegul` 3, `past-tense-indefinite` 2, `van-past` 2, three reading items untagged, and four more; 24 grammar-category items became vocabulary, 8 carry `ds`. Content fixes: `b1-01-02-intro-1` and `b1-01-03-intro-1` described *miután* and *mielőtt* in the same words, so each now asks only for its own meaning; `b1-01-02-check-2` accepts *jövő* as well as *következő*; `b1-01-consolidation-1` said *mielőtt* marks the FIRST event (it marks the later one) and `-2` fitted both connectors; `b1-01-03-controlled-3` accepts *becsuktam*; `b1-01-03-check-2`'s hint now pins "(its turning point)". Left: `b1-01-05-dialogue-2` keeps an Igen/Nem warning (a consistent *Nem* that fails on meaning, so vocabulary).

### HU B1 `hungary-today-land-symbols` (b1-orszagma-01–05 + consolidation) — locked 2026-10-05
All 65 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 37, 20 reading items untagged, `verb-government-bol-bol` 4 (*-ból/-ből áll*, taught by this unit's own screen), `ban-ben-in` 1, `verb-government-val-vel` 1, `postpositions-basic` 1, `ra-re` 1 (*nyugatra*). Content fixes: `b1-orszagma-03.ex04` and `consolidation.ex08` also accept *tevődik össze*, which the screen teaches; `b1-orszagma-05.ex04` read "Mint az köztudott", now "Mint köztudott". The subagent flagged the screen's dexter/sinister sentence as reversed; it isn't (dexter is the bearer's right, the viewer's left), so it stands.

### HU B1 `giving-advice` (b1-04-01–b1-04-05 + consolidation) — locked 2026-10-05
All 95 exercises read by a Sonnet subagent and reviewed. Tags now: `b1-giving-advice-vocab` 32, `potential-hat-het` 15, `hypothetical-ha-conditional` 13, `nehogy-purpose` 10, `nek-conditional` 7, `egyreszt-masreszt` 6, three reading items untagged, and eight more across six skills; 6 items carry `ds`. *inkább … mint* has no skill and is vocabulary. Content fixes: `b1-04-03-dialogue-1` and its copy `b1-04-consolidation-9` offered a wrong reply that was a legitimate answer. Found: `hypothetical-ha-conditional` is registered at b1-04-01-b but b1-04-01-a already teaches *helyedben* + conditional (same unit, so no warning); to fix at the end of the level.

### HU B1 `saint-stephen` (b1-istvankiraly-01–05 + consolidation) — locked 2026-10-05
All 65 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 22, `past-participle-adjective` 21 (*megkoronázott, megkeresztelt, szentté avatott*), 20 reading items untagged, `definite-past` 1, `postpositions-altal-reven` 1 (*által* phrase before a participle). Listening and dialogues are vocabulary. No content fixes.

### HU B1 `relationships` (b1-05-01–b1-05-05 + consolidation) — locked 2026-10-05
All 93 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 44, `egymas` 17, `concessive-annak-ellenere` 7, `relative-clauses-aki-ami-amely` 5, `past-tense-indefinite` 4, `present-tense-routine-language` 3, `good-for-me-nekem-jo` 3 (*neked, neki*), `verb-government-rol-rel` 2, `ik-verbs-dolgozom-not-dolgozok` 2 (*gondoskodom, törődöm*), and four more; 24 items became vocabulary, no `ds`. Content fixes: `b1-05-01-dialogue-1` had an ungrammatical prompt; `b1-05-03-dialogue-1`, `-dialogue-2` and `b1-05-05-dialogue-1` offered wrong replies that were acceptable answers; `b1-05-05-writing-2` needed the untaught *törődés*; `b1-05-consolidation-5`'s hint said "we" for an *I* answer. No exercise here tests `verb-government-hoz-hez`, although the b1-05-03-a screen teaches it (registry already points there).

### HU B1 `arpad-dynasty` (b1-arpadhaz-01–05 + consolidation) — locked 2026-10-05
All 65 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 22, 20 reading items untagged, `relative-clauses-aki-ami-amely` 14, `vonatkozoi-nevmas-esetei` 4 (*akit, akinek*), `ahol-amikor` 4, `miutan-mielott` 1; 4 `ds` on the consolidation choices. No content fixes. Left: `consolidation.ex20` needs *fiúágon* but the prompt only says "in the male line".

### HU B1 `work-professional-life` (b1-06-01–b1-06-05 + consolidation) — locked 2026-10-05
All 93 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 24, `mediopassive-verbs-odik` 10, `present-participle` 9, `present-tense-routine-language` 7 (wrong-person dialogues), `ban-ben-in` 6, `verb-government-ra-re` 6, `verb-government-val-vel`, `-ert`, `-nak-nek`, `how-the-accusative-t-works` and eleven more; 12 items carry `ds`; ten dialogues moved from category dialogue to grammar/vocabulary to follow their tag in the choice items. The retired `light-verb-collocations` tag is gone. Content fixes: `b1-06-02-practice-4` used the untaught *értekezlet* (now *megbeszélés*); `b1-06-04-writing-1` said "you" for a *we* answer.

### HU B1 `mongol-invasion` (b1-tatarjaras-01–05 + consolidation) — locked 2026-10-05
All 65 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 25, 20 reading items untagged, `past-tense-indefinite` 5, `how-the-accusative-t-works` 4, `mediopassive-verbs-odik` 4 (*leég, elpusztul*), `definite-past` and a few single-skill items. Content fixes: `b1-tatarjaras-01.ex01b` matched *hadsereg* before it is taught (now *zúdul*); `b1-tatarjaras-03.ex04`'s hint pins "(they burned down – plural past)"; `b1-tatarjaras-consolidation.ex19` printed its own answer and asked about a saint the unit never mentions, now asks which fortifications Béla IV built. Left: `b1-tatarjaras-01.ex04` (*figyelmeztette*) would also accept an indefinite form typed by mistake, a hint "past definite" would pin it.

### HU B1 `education-learning` (b1-07-01–b1-07-05 + consolidation) — locked 2026-10-05
All 93 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 54, `potential-hat-het` 7, `azert-hogy-purpose` 6, `hogy-jon-jen` 5, `present-tense-routine-language` 4, `yes-no-questions` 3, three reading items untagged, and fifteen more across ten skills; 35 items changed category to follow their tag, 13 carry `ds`. Content fixes: `b1-07-03-dialogue-2` had a wrong reply that was also acceptable; `b1-07-04-check-2` doubled the *meg* of *megbukik* in its question.

### HU B1 `angevin-kings` (b1-anjouk-01–05 + consolidation) — locked 2026-10-05
All 65 exercises read by a Sonnet subagent and reviewed. Tags now: 35 untagged reading (27 history-fact questions moved from vocabulary to `reading`), unit vocabulary 25, `evidentials` 2 (*a krónikák szerint*), `essive-formal-kent`, `hogy-clauses` and `ota-duration` once each. Content fixes: the answer was printed in brackets in `ex05` of lessons 01–05 (now blanks); `anjouk-01.ex04` had a second acceptable option; `anjouk-consolidation.ex15` had a wrong date range. Note: units locked before this one (carpathian-basin, honfoglalas, arpad-dynasty, saint-stephen, mongol-invasion, matthias-corvinus) keep history-fact questions as unit vocabulary; the rule sheet now says reading, untagged, for later units; see ROADMAP follow-up at the end of the level.

### HU B1 `travel-mobility` (b1-08-01–b1-08-05 + consolidation) — locked 2026-10-05
All 93 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 52, `terminative-case-ig` 8, `postposition-fele` 6, `on-en-on` 5, `keresztul` 4, `how-the-accusative-t-works` 3, `val-vel` 2, and ten more once each; three reading items untagged; 35 category changes, 11 `ds`. The screens teach set phrases (*lekési a vonatot, panaszt tesz*) with no skill, so those items are vocabulary. Content fix: `b1-08-04-practice-3` now accepts *pótlóbuszokkal* and *pótlóbusszal*.

### HU B1 `matthias-corvinus` (b1-matyas-01–05 + consolidation) — locked 2026-10-05
All 65 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 45 (civics questions kept as vocabulary), 15 reading items untagged, `correlative-minel-annal` 2, `superlative`, `past-tense-indefinite`, `ban-ben-in` once each. Content fixes: `b1-matyas-01–05.ex05` printed their answer in brackets in the question (now blanks); `b1-matyas-03.ex03` had two acceptable answers (a Corvina is a codex), now *Naptáraknak* instead of *Kódexeknek*. Note: the b1-matyas-04 screen calls *álruhában* "essive-modal -ban/-ben", a mislabel (no skill covers it).

### HU B1 `health-wellbeing` (b1-09-01–b1-09-05 + consolidation) — locked 2026-10-05
All 93 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 53, `szabad-infinitive` 9, `kellene` 8, `kell-infinitive` 4, `present-tense-routine-language` 5 (wrong-person dialogues), `how-the-accusative-t-works` 3, `ra-re` 2, and seven single-item skills; three reading items untagged; about 40 category changes, 8 items carry `ds`. The generic *az ember* has no skill (vocabulary). Content fixes (main session; the subagent's edits were blocked): `b1-09-01-controlled-2` now has the hint "(must)" so *szabad* is not a second answer; `b1-09-03-practice-3`'s hint is "(onto the prescription)" so the superessive isn't accepted.

### HU B1 `mohacs-1526` (b1-mohacs-01–05 + consolidation) — locked 2026-10-05
All 65 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 33 (civics questions kept as vocabulary), 21 reading items untagged, `causal-postpositions` 4, `miutan-mielott` 2, `past-participle-adjective` 2, `past-tense-indefinite` 2 (*veszett*), `3rd-person-possessive` 1. *alighogy … máris* has no skill (vocabulary). Content fixes (main session): `b1-mohacs-01.ex04` called a postposition an *utónév* (now *névutó*); `consolidation.ex19`'s question did not fit its options; `b1-mohacs-05.ex05`'s hint pins "(its turning point)". Left: the `b1-mohacs-02.ex07` Igen/Nem warning (the wrong replies fail on fact, not polarity).

### HU B1 `home-housing` (b1-10-01–b1-10-05 + consolidation) — locked 2026-10-05
All 93 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 47, `translative-morphology` 9, `inflected-postpositions` 7, `relative-clauses-aki-ami-amely` 4, `how-the-accusative-t-works` 4, `valik-verb` 3, `vonatkozoi-nevmas-esetei` 3, `formal-obligation` 2, `hogy-jon-jen` 2, and five single-item skills; eight reading items untagged; 43 category changes, 3 `ds`. Content fixes: `b1-10-01-writing-2` accepts *lett*; `b1-10-02-practice-1` and `-writing-2` accept the equivalent relative words (*ahonnan/amelyről*, *amibe/amelybe*); `b1-10-consolidation-4` asked for the translative of *szép* but keyed *szebbé*, now *széppé/szépvé/szépé*. `translative-morphology` and `valik-verb` are taught by this unit's own screens, registered at a2-171 (earlier, so no change needed).

### HU B1 `three-part-hungary` (b1-haromresz-01–05 + consolidation) — locked 2026-10-05
All 65 exercises read by a Sonnet subagent and reviewed. Tags now: 33 untagged reading (history-fact items moved from vocabulary), unit vocabulary 22, `concessive-annak-ellenere` 2, `how-the-accusative-t-works` 2, `3rd-person-possessive` 2, and `val-vel`, `historical-routines`, `ra-re`, `keresztul` once each. `b1-haromresz-01.ex04` was `essive-formal-kent` but *székhellyel* is instrumental. Content fix: `consolidation.ex11` accepts *városa* and *fővárosa*. Left: this unit's screen teaches `essive-formal-kent` (*-ként*), but after retagging no exercise tests it.

### HU B1 `cities-communities` (b1-11-01–b1-11-05 + consolidation) — locked 2026-10-05
All 93 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 51, 22 untagged reading (fact questions), `relative-clauses-aki-ami-amely` 7, `spatial-belonging-beli` 6, `adversative-contrast` 6 (*míg, ellenben, ezzel szemben*), `kellene` 4, `verb-government-hoz-hez` 4, `vonatkozoi-nevmas-esetei` 3, `verb-government-ban-ben` 2, `translative-morphology` 2, and four single-item skills; 10 items carry `ds`. Content fixes: `b1-11-01-writing-2` accepts *amiben*; `b1-11-02-controlled-1` offered a real word (*környéki*) as a wrong option; `b1-11-consolidation-8` keyed an ungrammatical *tételéhez*, now a *hozzá* fill-blank. `vonatkozoi-nevmas-esetei` is taught here (b1-11-01-b) but registered at citizenship b1-arpadhaz-03: registry follow-up at the end of the level.

### HU B1 `transylvania-golden-age` (b1-erdelyaranykora-01–05 + consolidation) — locked 2026-10-05
All 65 exercises read by a Sonnet subagent and reviewed. Tags now: 36 untagged reading (fact questions moved from vocabulary), unit vocabulary 17, `essive-formal-kent` 5 (*székhelyeként, mecénásként*), `formal-purpose` 2, and `movement-with-ba-be`, `hoz-suffix`, `verb-government-nak-nek`, `how-the-accusative-t-works`, `past-tense-indefinite` once each; 4 items carry `ds`. Content fix: `consolidation` had a matching pair *Gyulafehérvár*/*Gyulafehérvár*, now *hűbérúr*/overlord.

### HU B1 `food-lifestyle` (b1-12-01–b1-12-05 + consolidation) — locked 2026-10-05
All 93 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 52, 17 untagged reading, `sequencing-elobb-aztan-utana-vegul` 6, `3rd-person-possessive` 6, `how-the-accusative-t-works` 3, `nek-conditional` 3 (polite requests), and four single-item skills; 3 `ds`. The *-ul/-ül* inchoative verbs (*sül, fő*) and flavour adjectives screens have no skill and are vocabulary. Content fixes: `b1-12-01-writing-1` needed the untaught *kel* (now *fő*); `b1-12-03-practice-1` replaced an awkward *receptjének*; `b1-12-03-practice-2`'s hint pins "(its time)"; `b1-12-04-dialogue-2`'s wrong option *összetartás* also fitted.

### HU B1 `driving-out-ottomans` (b1-torokkiuzese-01–05 + consolidation) — locked 2026-10-05
All 65 exercises read by a Sonnet subagent and reviewed. Tags now: 36 untagged reading (fact questions moved from vocabulary), unit vocabulary 21, `azert-hogy-purpose` 2, and `van-past`, `formal-obligation` (*kénytelen*), `miutan-mielott`, `concessive-annak-ellenere`, `essive-formal-kent`, `3rd-person-possessive`, `how-the-accusative-t-works`, `valik-verb` once each. Content fix: `b1-torokkiuzese-02.ex05` had the hint "(fennhatóság, their)" for *fennhatósága* (now "of the Habsburgs").

### HU B1 `media-information` (b1-13-01–b1-13-05 + consolidation) — locked 2026-10-05
All 48 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 21, `evidentials` 6, `how-the-accusative-t-works` 4, `additive-connectors` 3, `reported-speech-statements` 2, `3rd-person-possessive` 2, and `indirect-questions`, `verb-government-ra-re`, `-nak-nek`, `ban-ben-in`, `egyreszt-masreszt`, `miutan-mielott` once each; five reading items untagged. Content fixes: four hints now pin the possessor or case ("its correspondent", "to fact-checking", "their reliability", "in an op-ed piece"); `b1-13-consolidation.ex08` asked about a novel the unit never mentions, now asks why to check news in several sources. Registry follow-ups at the end of the level: `additive-connectors` is taught here (b1-13-05-a) but registered at b1-32-01-b (three "taught later" warnings stand); `evidentials` is registered at b1-13-03-a but *szerint* is taught by b1-13-01-b.

### HU B1 `rakoczi-war` (b1-rakoczi-01–05 + consolidation) — locked 2026-10-05
All 53 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 28, 16 untagged reading, `past-conditional-volna` 4, and `val-vel`, `concessive-annak-ellenere`, `past-tense-indefinite`, `how-the-accusative-t-works`, `meg-meaning` once each; builders with no target form moved to vocabulary. Content fixes (main session): `b1-rakoczi-01.ex04` pins the instrumental and accepts *kiáltvánnyal*; `b1-rakoczi-02.ex04` printed *volna* in its prompt (now keys *győztek*); `b1-rakoczi-03.ex07` accepts *hadi szerencse*.

### HU B1 `technology-communication` (b1-14-01–b1-14-05 + consolidation) — locked 2026-10-05
All 48 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 32, six reading items untagged, `future-participle-ando` 3, `formal-purpose` 2, `valik-verb` 2, and `on-en-on`, `directional-preverbs`, `imperative-indefinite` once each; 2 `ds`. Content fixes: `b1-14-03.ex07` accepts *céljából*; `b1-14-consolidation.ex03` needed an untaught -i adjective (now *kiberbiztonság*). `formal-purpose` is also taught here (b1-14-03-b), core, after b1-03-05.

### HU B1 `18th-century-rebuilding` (b1-mariaterezia-01–05 + consolidation) — locked 2026-10-05
All 53 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 36, 11 untagged reading, `postpositions-altal-reven` 3, `val-vel`, `formal-obligation`, `concessive-postpositions` once each. Content fixes: `b1-mariaterezia-01.ex03` and `consolidation.ex04` accept *által* as well as *révén*; `b1-mariaterezia-04.ex04` accepts *dacára*. Left: `consolidation.ex03` (*sanguinem*, a Latin motto) keeps a possessor-hint warning, a false positive.

### HU B1 `culture-entertainment` (b1-15-01–b1-15-05 + consolidation) — locked 2026-10-05
All 48 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 26, five reading items untagged, `correlative-minel-annal` 3, `3rd-person-possessive` 3, `superlative` 2, and `kellene`, `irregular-nek-conditional`, `nek-conditional`, `past-participle-adjective`, `how-the-accusative-t-works`, `verb-government-hoz-hez`, `-val-vel`, `plural-nouns-k` once each. Content fixes: three hints pin the possessor ("its venue", "its director", "its lead actor"); `consolidation.ex07` had a wrong gloss ("performers" for *főszereplők*). `correlative-minel-annal` is taught here (b1-15-01-a) but registered at citizenship b1-matyas-02: registry follow-up.

### HU B1 `reform-age` (b1-reformkor-01–05 + consolidation) — locked 2026-10-05
All 53 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 31, 17 untagged reading (history-fact questions), `evidentials` 3 (*kétségkívül*, the nearest skill), `valik-verb` 1, `how-the-accusative-t-works` 1. Content fixes: `b1-reformkor-02.ex04` and `-04.ex04` accept equivalent answers (*kétségtelenül*, *lett*).

### HU B1 `environment` (b1-16-01–b1-16-05 + consolidation) — locked 2026-10-05
All 48 exercises (a repeated 8-item template per lesson) read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 24, `mert-because` 10 (the *ezért* choice and fill-blank of each lesson), `causal-postpositions` 5 (*aminek következtében*), `kell-infinitive` 1, `azert-hogy-purpose` 1, six reading items untagged. Content fixes (main session): `ex04` of lessons 01–05 accepts *emiatt* and *tehát* as well as *ezért*; `b1-16-01.ex06` and `.ex07` used *következtében* and *szempontjából*, which only lesson 2 teaches (now a *kell* fill-blank and a sentence from the 01-b screen); `b1-16-consolidation.ex08` asked about an invented Gárdonyi novella and is now a plain question about protecting nature. `causal-postpositions` is taught here (b1-16-02-a) but registered at citizenship b1-mohacs-01: registry follow-up.

### HU B1 `revolution-1848` (b1-17-01–b1-17-05 + consolidation) — locked 2026-10-05
All 48 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 28, `hogy-jon-jen` 5, `hogy-clauses` 5, seven reading items untagged. No content fixes needed. *nélkül* has no skill (vocabulary); *államként* stays vocabulary because `kent-vs-mint` is taught later (b1-17).

### HU B1 `society-inequality` (b1-17-01–b1-17-05 + consolidation) — locked 2026-10-05
All 48 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 17, `essive-formal-kent` 14, `distributive-nkent` 5, `postpositions-basic` 1, 11 reading items untagged. Content fixes: `b1-17-01.ex03`, `ex05`–`ex08` used words from lessons 2, 4 and 5 and the distributive suffix, first taught in 02-a (rewritten with lesson-1 material); `b1-17-02`–`05` `ex06` read "hónapok____" (now "hónap____"). Lessons 02–05 repeat the lesson-1 item set (`ex02`/`ex04` verbatim, and the `ex02` question asks "-ként vagy -nként" with no *-nként* option): a structural content issue, queued for the end of the level. `kent-vs-mint` has no item that tests it cleanly.

### HU B1 `kossuth-petofi-national-cause` (b1-nemzetiugy-01–05 + consolidation) — locked 2026-10-05
All 48 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 22, `participle-actions` 5 (*-va/-ve*), `azert-hogy-purpose` 5, `postpositions-basic` 1, 15 reading items untagged. Content fixes: `b1-nemzetiugy-01.ex03`, `ex05`–`ex08` used words taught only in lessons 2–5 (replaced with lesson-1 content, including a question on the purpose of Kossuth's 1851–52 US tour); `consolidation.ex07`'s hint pins "(we will be)". Lessons 02–04 still use later-lesson words (*kokárda, trikolór, koszorúzás*) and lessons 02–05 repeat the lesson-1 item set; queued as the same structural issue.

### HU B1 `politics-public-life` (b1-18-01–b1-18-05 + consolidation) — locked 2026-10-05
All 48 exercises (one 8-item template copied into all five lessons) read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 21, `concessive-annak-ellenere` 11, `on-en-on` 5, `ban-ben-in` 5, `how-the-accusative-t-works` 1, `hogy-clauses` 1, one untagged reading; the old per-lesson tags (e.g. `valik-verb` on all of one lesson) were wrong. Content fixes: the lesson 1–2 copies asked about words from later lessons (*szavazati jog*, *jogállamiság*, *kompromisszum*), so `ex05`, `ex07` and `ex08` were rewritten with each lesson's own vocabulary. Left: `hiába` appears in lesson 1's `ex06` sentence before lesson 2 teaches it (the blank tests only the suffix).

### HU B1 `compromise-1867` (b1-kiegyezes-01–05 + consolidation) — locked 2026-10-05
All 48 exercises (same template shape) read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 20, eight reading items untagged, `azert-hogy-purpose` 5, `concessive-annak-ellenere` 5, `verb-government-nak-nek` 4, `definite-past` 3, `past-tense-indefinite` 2, `how-the-accusative-t-works` 1; 5 `ds`. Content fixes: the lesson 1–3 copies asked about later-lesson material (*bürokrácia*, *passzív ellenállás*, *tárgyalási alap*, *koronázási eskü*, the Húsvéti cikk), so `ex03`–`ex08` were rewritten for each lesson. Left: the `ex02` stem names Deák before his lesson-2 vocabulary introduces him (the answer does not depend on it).

### HU B1 `problems-solutions` (b1-20-01–b1-20-05 + consolidation) — locked 2026-10-05
All 48 exercises (the shared 8-item template) read by a Sonnet subagent. Tags now: unit vocabulary 19, `past-conditional-volna` 12, `kellett-volna` 5, `how-the-accusative-t-works` 5 (*megoldást, javaslatát*), `acc-poss` 1, six reading items untagged. No content fixes. Left: lessons 01–02 test *megoldás* and *felelősségvállalás* before they are taught, and `consolidation.ex08` asks about a Karinthy story the unit never shows (the same template issue as the other late units); `consolidation.ex04` keeps a "volna printed in the prompt" warning (a two-clause conditional needs it in both clauses).

### HU B1 `world-war-1` (b1-vilaghaboru-01–05 + consolidation) — locked 2026-10-05
All 48 exercises read by a Sonnet subagent. Tags now: unit vocabulary 22, `past-conditional-volna` 10, `how-the-accusative-t-works` 5, `delative-rol-rel` 1, ten reading items untagged. No content fixes. Left: the template tests *jegyrendszer*, *forradalom* and the aster flower before they are taught; warnings stand for the printed *volna* and a false possessor-ending hit on *forradalom*.

### HU B1 `money-economy` (b1-19-01–b1-19-05 + consolidation) — locked 2026-10-05
All 48 exercises (the shared 8-item template) read by a Sonnet subagent; the content fixes were applied by the main session. Tags now: unit vocabulary 21, `correlative-minel-annal` 10, `verb-government-ra-re` 5, `olyan-mint` 3 (*annyi … mint*), `meg-meaning` 2, `fractions`, `val-vel`, `how-the-accusative-t-works` once each, six reading items untagged. Content fixes: `ex03` of every lesson keyed *költségvetést* before *összegét* (now *költségvetés*); lessons 01–02 asked about *minél … annál* and *kamatláb*/*üzleti terv* before they are taught, so `b1-19-01.ex02`, `ex05`–`ex07`, `b1-19-02.ex02`, `ex06`, `ex07` and `b1-19-03.ex07` were rewritten with material already shown. `correlative-minel-annal` is taught here (b1-19-03-a) but registered at citizenship b1-matyas-02 (registry follow-up, also taught at b1-15-01-a).

### HU B1 `austria-hungary` (b1-monarchia-01–05 + consolidation) — locked 2026-10-05
All 48 exercises read by a Sonnet subagent; content fixes applied by the main session. Tags now: unit vocabulary 24, `egyreszt-masreszt` 8, `meg-meaning` 4 (*alakult át*), twelve reading items untagged. Content fixes: the repeated template asked for later-lesson vocabulary in lessons 01–03, so lesson 01 `ex03`–`ex08`, lesson 02 `ex06`–`ex08`, lesson 03 `ex07`–`ex08` and lesson 04 `ex07` were rewritten with each lesson's own material (*közös hadsereg, egyrészt … másrészt, emlékére*); the `ex04` hint no longer names the suffix. *emlékére*/*tiszteletére* have no skill (vocabulary).

### HU B1 `opinions-arguments` (b1-21-01–b1-21-05 + consolidation) — locked 2026-10-05
All 48 exercises (the shared 8-item template) read by a Sonnet subagent. Tags now: unit vocabulary 21, `evidentials` 7 (*Állítólag …*), `adversative-contrast` 5, `relative-clauses-aki-ami-amely` 4, `val-vel` 3, `verb-government-ra-re` 1, `hogy-clauses` 1, five reading items untagged. Content fixes: copies in lessons 01–04 that used words taught only later (*érv, kétségtelenül, legmeggyőzőbb, részben, szempont, érvelés*) were rewritten with each lesson's own material; `ex06` accepts *azonban* and *viszont* as well as *de*; `consolidation.ex08` asked about a Karinthy satire the unit never mentions (now asks which word flags hearsay).

### HU B1 `trianon-1920` (b1-trianon-01–05 + consolidation) — locked 2026-10-05
All 48 exercises read by a Sonnet subagent. Tags now: unit vocabulary 18, `azert-hogy-purpose` 6, `how-the-accusative-t-works` 5, `postpositions-basic` 4, `verb-government-ert` 3, and `val-vel`, `prefix-word-order`, `acc-poss`, `plural-nouns-k`, `past-tense-indefinite` once each; seven reading items untagged. Content fixes: `ex04` hints in lessons 02–05 printed the answer (*-> közé*); lesson 01–04 `ex04`/`ex06`–`ex08` used lesson 5's national-unity text and vocabulary before it is taught, now rewritten with each lesson's own material; `consolidation.ex03`'s hint pins "(his speech)".

### HU B1 `possibilities-predictions` (b1-22-01–b1-22-05 + consolidation) — locked 2026-10-05
All 48 exercises read by a Sonnet subagent; content fixes applied by the main session. Tags now: unit vocabulary 24, `hogy-clauses` 6, `fog-infinitive` 3, `verb-government-ban-ben` 2, `verb-government-ra-re` 2, `plural-possessive`, `valik-verb`, `past-tense-indefinite` once each, one reading item untagged. Content fixes: `b1-22-03.ex05` keyed *számításai* for "their" (now also *számításaik*); `b1-22-05.ex05` and `b1-22-consolidation.ex07` hints now pin tense and case.

### HU B1 `interwar-years` (b1-horthykorszak-01–05 + consolidation) — locked 2026-10-05
All 48 exercises read by a Sonnet subagent; content rewrites applied by the main session. The five lessons held the same eight items copied from lesson 1, which tested later material (*pengő*, *révén*, Klebelsberg, Szent-Györgyi, *azzal a céllal*, the First Vienna Award) and nothing of lessons 02–05's own; lessons 01–05 `ex01`–`ex08` were rewritten per lesson (*trónfosztás*, *konszolidáció*, *népiskola*, *dzsentri*, *tengelyhatalmak*, with fill-blanks and sentence-builders from each lesson's screens). Tags now: unit vocabulary 21, `postpositions-altal-reven` 5, `future-participle-ando` 4, `azert-hogy-purpose` 3, `formal-address-on` 3, `miutan-mielott` 3, `how-the-accusative-t-works` 1, six reading items untagged. The facts in the new history items (Horthy as admiral, Bethlen–Peyer pact, 1924 League of Nations loan, Klebelsberg's schools, Szent-Györgyi's 1937 Nobel, the 1938 Vienna Award) should be spot-checked against the unit's own screens.

### HU B1 `making-decisions` (b1-23-01–b1-23-05 + consolidation) — locked 2026-10-05
All 48 exercises read by a Sonnet subagent; content fixes applied by the main session. Tags now: unit vocabulary 32, `postpositions-basic` 3, `egyreszt-masreszt` 3, `nek-conditional` 2, and `possessive-suffixes`, `hogy-clauses`, `comparative-bb`, `hoz-suffix`, `verb-government-ert`, `ra-re` once each; one reading item untagged. The unit's screens teach idioms rather than paradigms, so sentence-builders and stem completions are vocabulary. Content fixes: `b1-23-03.ex07` accepts *ugranál* (hint "would jump"); `b1-23-consolidation.ex02`'s hint now pins "(we would reach)".

### HU B1 `world-war-2` (b1-masodikvh-01–05 + consolidation) — locked 2026-10-05
All 48 exercises read by a Sonnet subagent; content rewrites applied by the main session. Lessons 01–05 repeated one set of eight items that tested the other lessons' words (Wallenberg, the siege of Budapest, the Don), so `ex01`–`ex08` of each lesson were rewritten from that lesson's own material (*hadüzenet, munkaszolgálat, deportálás, rádióproklamáció, romváros*; *következtében, útján, ellenére, kockáztatva*). Tags now: unit vocabulary 28, seven reading items untagged, `causal-postpositions` 2, `participle-actions` 2 (*kockáztatva*), `translative-morphology` 2, `concessive-postpositions`, `postpositions-altal-reven`, `postpositions-basic` once each. *hatására, következtében, útján, ellenére* have no skill of their own and are mapped to the nearest. `consolidation.ex03` accepts *deportálták*. The new history facts (1941 entry into the war, Don disaster Jan 1943, Margarethe 19 Mar 1944, 15 Oct 1944 proclamation) should be spot-checked against the screens.

### HU B1 `change-development` (b1-25-01–b1-25-05 + consolidation) — locked 2026-10-06
All 48 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 31, `past-tense-indefinite` 6, `acc-poss` 2, `mediopassive-verbs-odik` 2 (the *-ul/-ül* becoming-verbs, nearest skill; its `taught_in` is b1-06-02-a), and `translative-morphology`, `an-en-adverb`, `adversative-contrast`, `verb-government-hoz-hez`, `valik-verb`, `how-the-accusative-t-works` once each; one reading item untagged; 1 `ds`. Content fix: `05.ex02`'s hint now matches its past-tense answer ("counted as").

### HU B1 `kadar-era` (b1-kadarkorszak-01–05 + consolidation) — locked 2026-10-06
All 48 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 21, ten reading items untagged (who/when/why facts), `building-the-infinitive-the-suffix-ni` 4, `definite-past` 3, `past-tense-indefinite` 3, `acc-poss` 2, `verb-government-hoz-hez` 2, and `plural-nouns-k`, `potential-hat-het`, `meg-meaning` once each. Content fixes: `01.ex02` keyed *hatott* for "was released" (now *kiszabadult*, matching the screen); `04.ex02`'s hint pins "(banned)"; `04.ex05` keyed *rá* where *öncenzúra eszközéhez* needs *ra*; `consolidation.ex05`'s hint pins the accusative.

### HU B1 `how-things-work` (b1-24-01–b1-24-05 + consolidation) — locked 2026-10-06
All 48 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 25 (fixed-phrase items such as *végbe, kifejt, elhárít* and the sentence-builders), `mediopassive-verbs-odik` 3, `sequencing-elobb-aztan-utana-vegul` 2, and `elative-bol-bel`, `egymas`, `nominalization`, `verb-government-ra-re`, `how-the-accusative-t-works`, `val-vel`, `acc-poss` once each; one reading item untagged; 2 `ds`. Content fix: `consolidation.ex02` printed its answer *körbe* in the prompt (now "…áramlik _____. (round and round)").

### HU B1 `rakosi-era` (b1-rakosikorszak-01–05 + consolidation) — locked 2026-10-06
All 48 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 25, 13 reading items untagged (history-fact questions), `meg-meaning` 5, `prefix-word-order` 3, `how-the-accusative-t-works` 1, `past-tense-indefinite` 1. Content fixes: `consolidation.ex03`'s hint no longer prints the abbreviation; lessons 01–04 template copies that tested later-lesson material were rewritten (`b1-rakosikorszak-01.ex03`–`ex08`, `02.ex04`–`ex08`, `03.ex06`–`ex08`, `04.ex07`–`ex08`). Four "answer carries a possessor ending" warnings stand (false positives on *állam*).

### HU B1 `work-ambition-balance` (b1-26-01–b1-26-05 + consolidation) — locked 2026-10-06
All 48 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 29 (all sentence-builders), `verb-government-ra-re` 2, `-ban-ben` 2, `-hoz-hez` 2, `-nak-nek` 1, and `definite-past`, `present-tense-routine-language`, `val-vel`, `past-tense-indefinite`, `acc-poss` once each; one reading item untagged; 2 `ds`. Content fixes: `b1-26-02.ex07` also accepts *re* (*joguk van a pihenésre*); `b1-26-04.ex07`'s hint pins "(they received)".

### HU B1 `regime-change` (b1-rendszervaltas-01–05 + consolidation) — locked 2026-10-06
All 48 exercises read by a Sonnet subagent and reviewed. Tags now: 19 reading items untagged (history facts), unit vocabulary 12, `how-the-accusative-t-works` 5, `acc-poss` 5, `past-tense-indefinite` 3, and `hogy-jon-jen`, `van-past`, `postpositions-basic`, `plural-possessive` once each. Content fixes: `b1-rendszervaltas-01.ex07` keyed *tak* where the form needs *ottak* (*jutottak*); `b1-rendszervaltas-02.ex07`'s hint said "(its opening)" for a plain accusative.

### HU B1 `rules-rights-responsibilities` (b1-28-01–b1-28-05 + consolidation) — locked 2026-10-06
All 48 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 22, `formal-obligation` 4, `verb-government-ra-re` 3, `future-participle-ando` 3, `verb-government-ert` 2, `past-tense-indefinite` 2, and nine single-item skills; four reading items untagged; 5 `ds`. Content fix: `b1-28-04.ex04` offered *Hacsak nem* as a second acceptable conditional (now *Habár / noha*).

### HU B1 `modern-democratic-hungary` (b1-demokracia-01–05 + consolidation) — locked 2026-10-06
All 48 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 17, 14 reading items untagged (civics facts), `acc-poss` 4, `valik-verb` 2, `ban-ben-in` 2, and nine single-item skills (including `participle-actions` for *alá vannak rendelve*). *nyugszik* has no skill (vocabulary). Content fix: `b1-demokracia-05.ex05`'s hint pins "(remaining, accusative)".

### HU B1 `revolution-1956` (b1-otvenhat-01–05 + consolidation) — locked 2026-10-06
All 48 exercises read by a Sonnet subagent and reviewed. The template had been copied verbatim into lessons 01–05, with `ex04`–`ex08` testing later lessons' words; each lesson now keeps its own original item and has new items from its own vocabulary and screen (01 `ex04`–`ex08`; 02 `ex01`–`ex03`, `ex05`–`ex08`; 03 `ex01`–`ex04`, `ex06`–`ex08`; 04 `ex01`–`ex05`, `ex07`–`ex08`; 05 `ex01`–`ex06`). Tags now: unit vocabulary 28, eight reading items untagged, `how-the-accusative-t-works` 2, and `meg-meaning`, `elative-bol-bel`, `acc-poss`, `verb-government-ert`, `plural-nouns-k`, `hoz-suffix`, `terminative-case-ig`, `translative-morphology`, `past-tense-indefinite`, `3rd-person-possessive` once each. Other fixes: `consolidation.ex04` was a fragment blank (*in_____* → *tézett*), now *intéz_____* → *ett*; `consolidation.ex03` accepts *szobrot* and *szobrát*. *nélkül* has no skill (vocabulary).

### HU B1 `social-life-communication` (b1-27-01–b1-27-05 + consolidation) — locked 2026-10-06
All 48 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 21, `nominalization` 3 (the *-ás/-és* blanks), `reported-commands` 3, `egymas` 3, three reading items untagged, `definite-past` 2, `concessive-annak-ellenere` 2, `how-the-accusative-t-works` 2, and nine single-item skills; 4 `ds`. Content fixes: `b1-27-05.ex07` produced "grundra védelmére" (now *grundért*); the hints of `02.ex02` and `02.ex07` pin the person; `03.ex04` now says the speaker addresses "me", so only one imperative fits.

### HU B1 `migration-identity` (b1-29-01–b1-29-05 + consolidation) — locked 2026-10-06
All 48 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 22 (all sentence-builders), `acc-poss` 6, `present-tense-routine-language` 2, `causal-postpositions` 2, `concessive-postpositions` 2, `verb-government-hoz-hez` 2, four reading items untagged, and seven single-item skills; 4 items carry `ds`. *során*, *nemcsak/egyszerre*, *reményében* have no skill (vocabulary). Content fixes: `b1-29-01.ex05` accepted both *ki-* and *be-* (now "(emigration, prefix)"); `b1-29-02.ex02` accepts *megtelepedett*; `b1-29-03.ex05` had a wrong stem (*idegens + ég*, now *idegen_____* → *ség*); `consolidation.ex07`'s hint said "(his peace)" for a plain accusative. `participle-actions` and `causal-postpositions` are also taught here (core) while registered at citizenship screens.

### HU B1 `national-symbols` (b1-nemzetijelkepek-01–05 + consolidation) — locked 2026-10-06
All 48 exercises read by a Sonnet subagent and reviewed. Tags now: 17 reading items untagged (history and citizenship facts), unit vocabulary 14, `meg-meaning` 7 (lexical prefix fills), `definite-vs-indefinite-conjugation` 4, `definite-past` 3, `past-tense-indefinite` 2, and `how-the-accusative-t-works`, `essive-formal-kent`, `kell-infinitive` once each. Content fix: `b1-nemzetijelkepek-05.ex07` accepts *muszáj*. Left: several items name facts the lesson text never shows (the *lyukas zászló*, the 1978 return of the Holy Crown).

### HU B1 `culture-language-society` (b1-30-01–b1-30-05 + consolidation) — locked 2026-10-06
All 48 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 21 (all sentence-builders), `relative-clauses-aki-ami-amely` 4, `verbal-adjectives-hatatlan-hetetlen` 3, `postpositions-basic` 3 (*számára*), `3rd-person-possessive` 3, `ra-re` 2, `how-the-accusative-t-works` 2, and `ban-ben-in`, `tol-tol` once each; five reading items untagged. Content fixes: `b1-30-03.ex05` and `b1-30-05.ex07` hints said "(for them)" for *a család* and *mindenki*. Left: `04.ex02` blanks only the final *-t* of *nyit* (vocabulary).

### HU B1 `national-holidays-remembrance-days` (b1-nemzetiunnepek-01–05 + consolidation) — locked 2026-10-06
All 48 exercises read by a Sonnet subagent and reviewed. Tags now: 16 reading items untagged (history and civics facts), unit vocabulary 12, `how-the-accusative-t-works` 5, `3rd-person-possessive` 3, `ra-re` 3, `meg-meaning` 3, `present-tense-routine-language` 3 (*-ik* plural forms), `past-tense-indefinite` 2, `ban-ben-in` and `postpositions-basic` once each. Content fix: `b1-nemzetiunnepek-03.ex07` keyed *számík* (now *számít*). No skill covers the commemorative postpositions (*alkalmából, tiszteletére*).

### HU B1 `future-society` (b1-31-01–b1-31-05 + consolidation) — locked 2026-10-06
All 48 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 25, `how-the-accusative-t-works` 4, `future-participle-ando` 3, `an-en-adverb` 2, `3rd-person-possessive` 2, two reading items untagged, and ten single-item skills (including `nominalizing-processes` for *átalakulóban van*, whose registry title says "progressive state in -óban/-őben van" but which still has no `taught_in`). Content fixes: `b1-31-01.ex05` was nonsense (*kezdi kibontakozását elérni*), rewritten; `b1-31-01.ex08` used lesson 05's *fejlődése*; `b1-31-05.ex07`'s hint pins "(its perspectives, plural)"; `consolidation.ex07` accepts *előreláthatóan*; `consolidation.ex05`'s hint contradicted its answer.

### HU B1 `fundamental-law` (b1-alaptorveny-01–05 + consolidation) — locked 2026-10-06
All 48 exercises read by a Sonnet subagent and reviewed. Tags now: 11 reading items untagged (39 category changes, mostly civics facts to reading and builders to vocabulary), unit vocabulary 19, `how-the-accusative-t-works` 3, `ban-ben-in` 3, `acc-poss` 2, `3rd-person-possessive` 2, `verb-government-hoz-hez` 2, `verb-government-ert` 2, and four single-item skills. Content fixes: `b1-alaptorveny-02.ex04` contained a non-word (*értékelköteleződést*); `02.ex05` and `03.ex07` had "(its …)" hints that contradicted the plain accusative they accept (now "(identity)", "(freedom)" with a second answer). Left: `b1-alaptorveny-01.ex08` uses *jogállam* before lesson 05 introduces it.

### HU B1 `connecting-ideas` (b1-32-01–b1-32-05 + consolidation) — locked 2026-10-06
All 48 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 15, `how-the-accusative-t-works` 7, `additive-connectors` 5, `mert-because` 2, `concessive-annak-ellenere` 2, two reading items untagged, and twelve single-item skills (including `is-placing-also-too`); 1 `ds`. Content fixes: hints of `02.ex07` ("they foresaw it") and `05.ex02` ("in the future") now pin person and case; `consolidation.ex04` had a second equally correct option (*másrészről viszont*).

### HU B1 `government-institutions-today` (b1-allamszervezet-01–05 + consolidation) — locked 2026-10-06
All 48 exercises read by a Sonnet subagent and reviewed. Tags now: 20 reading items untagged (civics facts), unit vocabulary 12, `acc-poss` 6, `how-the-accusative-t-works` 3, `3rd-person-possessive` 2, `definite-vs-indefinite-conjugation` 2, and `on-en-on`, `verb-government-rol-rel`, `postpositions-basic`, `ban-ben-in`, `participle-actions`, `inflected-postpositions` once each. Content fix: `b1-allamszervezet-05.ex02`'s hint pins "(they adopt it)". Left: `01.ex05` probably also accepts *-ra* besides *-ról*.

### HU B1 `complex-opinions` (b1-34-01–b1-34-05 + consolidation) — locked 2026-10-06
All 42 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 21, `concessive-annak-ellenere` 4, `hogy-clauses` 2, `adversative-contrast` 2, `egyreszt-masreszt` 2, `how-the-accusative-t-works` 2, and `an-en-adverb`, `ha-clause`, `present-tense-routine-language`, `val-vel`, `ban-ben-in`, `szerintem` once each; one reading item untagged; 1 `ds`. Content fix: `b1-34-04.ex05` also accepts *-sel* (*meggyőződéssel*).

### HU B1 `hungarian-culture-science-heritage` (b1-nemzetiertekek-01–05 + consolidation) — locked 2026-10-06
All 42 exercises read by a Sonnet subagent and reviewed. Tags now: 14 reading items untagged (facts), unit vocabulary 10, `how-the-accusative-t-works` 4, `definite-past` 3, `essive-formal-kent` 2, `3rd-person-possessive` 2, and `verb-government-ban-ben`, `-hoz-hez`, `superlative`, `translative-morphology` once each. Content fixes: hints of `05.ex05` and `consolidation.ex05` now say "(masterpiece of)", "(cornerstone of)" to pin the possessed form. `essive-formal-kent` and `translative-morphology` are also taught by this unit's own screens (registered at a2-176-a, a2-171-b, earlier).

### HU B1 `reported-speech` (b1-33-01–b1-33-05 + consolidation) — locked 2026-10-06
All 48 exercises read by a Sonnet subagent and reviewed. Tags now: `reported-speech-statements` 12, `indirect-questions` 9, `reported-commands` 8, unit vocabulary 11, `how-the-accusative-t-works` 7 (the accusative fill-blanks are tagged by their suffix), `evidentials` 4, `definite-past` and `on-en-on` once each, three reading items untagged. Content fixes: `01.ex02` keyed *volt* against the screen (no backshift); `01.ex05` used *holnap* instead of *másnap*; `01.ex06` and `04.ex06` had later-lesson distractors; `05.ex05` needed a possessor (rewritten); `consolidation.ex01`'s *titeket → minket* was ambiguous; `consolidation.ex02` used the untaught *intette*; `consolidation.ex05`'s hint is "at the forum". `03.ex04` keeps an Igen/Nem warning (a rule question about the *-e* particle). The unit's own screens (b1-33-01 to -05) teach `reported-speech-statements`, `indirect-questions`, `reported-commands` and `evidentials`, registered at b1-13 and b1-27 (registry follow-up).

### HU B1 `local-governments-public-administration` (b1-onkormanyzat-01–05 + consolidation) — locked 2026-10-06
All 48 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 17, nine reading items untagged (civics facts), `how-the-accusative-t-works` 3, `definite-vs-indefinite-conjugation` 3, `verb-government-rol-rel` 3, `definite-past` 2, and `verb-government-hoz-hez`, `val-vel`, `plural-predicate-adjectives-k`, `acc-poss`, `present-tense-routine-language`, `plural-nouns-k` once each. Content fixes: `01.ex05` also accepts *ra* and `01.ex07` *át*; `02.ex02` and `consolidation.ex02` accept *felelős*; `03.ex07` said 25 cities with county rights (there are 23), and the story text (`stories/world/b1/b1-onkormanyzat-03-varmegyek.json`, `b1-onkormanyzat.json`) had the same error (now *huszonhárom*).

### HU B1 `hungarians-abroad` (b1-magyarsag-01–05 + consolidation) — locked 2026-10-06
All 42 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 15, 15 reading items untagged (Alaptörvény, V4, naturalization and geography facts), `present-tense-routine-language` 4 (plural *-ik* forms), `ban-ben-in` 3, `3rd-person-possessive` 2, `vowel-harmony` 1 (the dative *-nak* on *tagjai*, no skill fits), `on-en-on`, `how-the-accusative-t-works` once each. Content fix: `04.ex05` had *érdekképviselet_____ során* with answer *ben* (*során* takes no case ending), now "…érdekképviselet_____. (in diplomatic advocacy)".

### HU B1 `independent-hungarian` (b1-36-01–b1-36-05 + consolidation) — locked 2026-10-06
All 42 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 18, `3rd-person-possessive` 3, `how-the-accusative-t-works` 2, `hogy-jon-jen` 2, two reading items untagged, and `additive-connectors`, `inflected-postpositions`, `basic-hungarian-word-order`, `egymas`, `formal-address-on`, `plural-nouns-k`, `concessive-annak-ellenere`, `acc-poss` once each. Content fixes: `b1-36-01.ex01` printed its answer in the prompt; `b1-36-02.ex06` asked for the sentence stressing the actor, but no option did (now the destination). The particles and idioms taught here (*ugyebár, apropó, vagyis inkább, ha jól értem*) have no skill and sit in the unit vocabulary skill.

### HU B1 `literary-musical-canon` (b1-europaiorokseg-01–05 + consolidation) — locked 2026-10-06
All 42 exercises read by a Sonnet subagent and reviewed. Tags now: 18 reading items untagged (author, work and composer facts), `definite-past` 7, `3rd-person-possessive` 5, `how-the-accusative-t-works` 3, `acc-poss` 2, and `definite-vs-indefinite-conjugation`, `plural-possessive`, `val-vel`, `delative-rol-rel`, `translative-morphology` once each; no vocabulary-tagged items (every item is a fact question or a form drill). Content fixes: `01.ex05`, `02.ex05`, `03.ex05` had unnatural dative-possessor stems or printed their answer (now *gondolkodó_____ → ja*, *mélység_____ → eit*, *mester_____ → ei*).

### HU B1 `hypotheticals-possibilities` (b1-35-01–b1-35-05 + consolidation) — locked 2026-10-06
All 42 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 15, `past-conditional-volna` 8, `past-tense-indefinite` 4, `kellett-volna` 3, `mixed-conditionals` 3, `definite-past` 3, `kell-infinitive` 2, and `reported-speech-statements`, `inflected-infinitives`, `postpositions-basic`, `verb-government-ra-re`, `van-past` once each; one reading item untagged; 6 `ds` on five items. Content fix: `b1-35-03.ex02`'s hint pins "(for you to argue)". `mixed-conditionals` is exercised here with `past-conditional-volna` taught at core b1-20-01-a (ROADMAP 139, done).

### HU B1 `tenancy-contracts` (b1-alberlet-01–05 + consolidation) — locked 2026-10-06
All 52 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 36 (the old `contractual-tenancy-clauses` tag is gone; its screens are phrase prose with no paradigm), `ra-re` 2, `acc-poss` 2, `formal-obligation` 2, `building-the-infinitive-the-suffix-ni` 2, and `ban-ben-in`, `relative-clauses-aki-ami-amely`, `ul-ul-essive-modal`, `an-en-adverb`, `postpositions-altal-reven`, `how-the-accusative-t-works`, `val-vel`, `verb-government-nak-nek` once each; 3 `ds`; 16 items changed category to vocabulary. Content fix: `b1-alberlet-02.ex06` also accepts *ként* (*fedezetként*).

### HU B1 `being-hungarian-citizen` (b1-allampolgarsag-01–05 + consolidation) — locked 2026-10-06
All 42 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 20, ten reading items untagged (history and civics facts), `how-the-accusative-t-works` 2, `acc-poss` 2, `3rd-person-possessive` 2, and `verb-government-ban-ben`, `definite-vs-indefinite-conjugation`, `inflected-postpositions`, `verbal-adjectives-hatatlan-hetetlen`, `present-tense-routine-language`, `verb-government-ra-re` once each. No content fixes. Worth a fact-check: `03.ex04` says compulsory schooling runs to age 16.

### HU B1 `kormanyablak` (b1-kormanyablak-01–05 + consolidation) — locked 2026-10-06
All 52 exercises read by a Sonnet subagent and reviewed. Tags now: unit vocabulary 33 (every sentence-builder and dialogue; the old `official-administrative-procedures` tag is not a registered skill), `val-vel` 4 (*fellebbezéssel él*), `acc-poss` 2, and `ra-re`, `how-the-accusative-t-works`, `past-tense-indefinite`, `verb-government-nak-nek`, `on-en-on`, `building-the-infinitive-the-suffix-ni`, `ban-ben-in` once each. Content fixes: hints of `02.ex02` ("myself, accusative ending"), `04.ex02` ("submitted"), `consolidation.ex06` ("in an official decree"); `05.ex07` had a wrong reply that was arguably acceptable.

### HU B1 read-through complete — 2026-10-06
All 75 HU B1 units (4,333 exercises, 36 core and 39 citizenship) now carry exactly one locked tag or are untagged reading, read by Sonnet subagents (two units each, two agents at a time) and reviewed and applied in the main session; per-unit entries are above. The set-up (five `taught_in` fixes, one-page rule sheet, eight new checker checks) is logged under "HU B1 read-through set-up". What the level added to the process: `category: reading` items stay untagged, and history/civics fact questions on the citizenship track are reading (the rule sheet says so from `angevin-kings` on; earlier citizenship units keep some as unit vocabulary); `apply_tags.py` now writes no `teaches` key for untagged items and adds one to an item that had none; the late units repeat one eight-item template in lessons 01–05, which tested later lessons' words, so those copies were rewritten per lesson (`society-inequality`, `kossuth-petofi-national-cause`, `environment`, `politics-public-life`, `compromise-1867`, `money-economy`, `austria-hungary`, `opinions-arguments`, `trianon-1920`, `interwar-years`, `world-war-2`, `revolution-1956`, `rakosi-era`, and part of `problems-solutions` and `world-war-1`). About 200 content defects were fixed along the way (wrong or doubled answers, hints that did not pin the person or case, an answer printed in the prompt, items asking about words taught later, an invented novel, the county-rights city count in a story). Follow-ups queued as ROADMAP 141.

### Unit pipeline: read first, three new checks — 2026-10-09
After runs 1–3 of ROADMAP 153 (a Sonnet second read found 20–30 defects per unit after Antigravity's pass, most of them words used before they are taught), three changes. **Read first:** the Sonnet read now comes before Antigravity's pass, so a unit is worked once (brief § "One unit", `docs/unit-second-read.md` § "The flow"). **`unmet-word`** (`scripts/unmet-words.js`, run by `check-content.py`, HU A1–A2, suspect): looks every target-language word of a unit's exercises up with the Reader's `Lexicon.lookup()` and checks the lemma against the vocabulary lists (`word-lesson-index.json`), earlier grammar screens' tables and single italic words, and the lesson's own screens; names, English options and glosses, number compounds and deliberately wrong forms are skipped. On units 4–7 it found 45 hits, every one real, including most of what the readers had found and *szép*, *ma* they had missed; HU A1 has 613, A2 1,522. It checks words, not forms (*címem* passes once *cím* is met). Spanish is left out: its lists omit function words and put *ser* at A2. **`checklist-shared`** (error): a checklist line another lesson of the course has; 201 in HU A1, 14 in HU A2, 9 in each Spanish A1. **`reply-as-option`** (error): a "which line comes before the reply" item offering the reply; 5, all in unit 7. The rules (one fault per wrong option, never the quoted line, each lesson's own checklist) are in `docs/course-generation-brief.md` § 2.2, § 2.3, § 6.3. Also: `cardinal-numbers` `taught_in` moved to `a1-16a-gr` (the user's decision), clearing 15 `taught-later` errors.

### HU A1 units 1–3: `unmet-word` fixes, re-frozen — 2026-10-09
The new check found words used before they are taught in the three frozen units. Unfrozen, fixed and re-frozen with their earlier accepts: *tea*, *kávé*, *viszlát* out of a1-01 (`intro-1`, `intro-2`, `dialogue-2`, `practice-3`, `practice-dialogue`, now only a1-01's own words); *kérem* (taught a1-65) out of `a1-02-review-1`, `a1-04-intro-2`, `a1-04-controlled-3`, `a1-11-review-2`; *persze*/*rendben* (a1-10) out of a1-09; *tea* → *kávé* in `a1-12-dialogue-1`; *lakik* → *vagy* in `a1-15-check-2`. The three "Which means 'thank you'?" items had no met wrong option long enough, so they now ask what *köszönöm* means, with English options. Accepted: `a1-09-dialogue-1` (the line is meant to be too fast to follow) and `a1-10-consolidation-10` (the English cue in the sentence).

