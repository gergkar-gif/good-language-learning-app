# Roadmap

Future features and nice-to-haves, captured 2026-08-21 from a user
brain-dump. Not prioritized or sequenced — a parking lot, distinct from
`TROUBLESHOOTING_BACKLOG.md` and `HUNGARIAN_A1_CONTENT_BACKLOG.md`, which
track known bugs in existing content rather than things not yet built.

## Content & curriculum

- [ ] Integrate the same English-Spanish dual-language reading setup with
  originals as exists for Hungarian, up to A1 level.
- [ ] Hungarian: introduce Hungarian cultural material at B1-B2 (for the
  citizenship exam), similar to the LatAm course's dual-track structure.
- [ ] Word Bank: same idea as Grammar Guide, but for vocabulary — a
  per-unit collection of the ~15-20 new words the unit introduces.

## Workshop

- [ ] In the various Workshop drillers, show an English translation and an
  explanation of why that's the right response at the bottom of each
  exercise.
- [ ] Verb drill: leaderboard / top score / top accuracy — maybe extended
  to all Workshop activities, not just verbs.
- [ ] Translation driller: practice by topic.

## Library / dictionary

- [ ] Spanish Library's word-translation popup currently shows the raw
  grammatical parse (e.g. "empezaba: verb · Imperfect, Indicative, 1st
  person singular from empezar, to start, begin, to get started") instead
  of the actual contextual translation (e.g. "started"). Should lead with
  the real translation, and could put the grammar explanation underneath.

## Decks

- [ ] Spanish decks: some verb definitions are overly verbose — needs a
  pass to tighten them.

## Interface & platform

- [ ] Interface increasingly bilingual as level rises, eventually
  Spanish/Hungarian interface by B2.
- [ ] Dark/light mode.
- [ ] Browser extension: add words to your deck from anywhere on the web.
  - [ ] Same idea, one click: import an article/email/any text straight
    into the Reader.
- [ ] Small AI agent for discussion/writing practice.
- [x] End-of-lesson summary screen ("well done, you finished"). **Built 2026-08-27** — see TROUBLESHOOTING_BACKLOG.md's "Lesson-complete summary card" entry for detail.
- [x] Audio: small sound effects for right answer, wrong answer, finishing
  a lesson, etc. **Built 2026-08-27**, then redesigned same day on
  feedback that the first pass sounded too "gamey": `engine/sound.js`
  (new) synthesises two quiet textures with the Web Audio API rather than
  shipping audio files — a soft paper rustle (filtered noise) for wrong
  answers, and a small singing-bowl-like tone (a few detuned sine
  partials over a slow decay) for correct answers, with both combined
  (rustle then a longer bowl) for lesson complete. No bright synth
  "ding," no Duolingo-style cha-ching — a sound here should register once
  and get out of the way, not perform. Wired into the shared
  `solveStep()`/`failStep()` in `engine/lessons.js`, so every exercise type
  gets sound with one hook each instead of five separate places (unlike the
  accent-sensitivity fix earlier this session, there's only one grading
  path in the main lesson flow to wire — Workshop's drillers weren't
  touched, matching the roadmap item's own "lesson" scope). One global mute
  toggle (new speaker icon in the lesson header, `localStorage`-persisted)
  rather than per-course, since a learner who mutes it won't want it back
  the moment they're somewhere else in the app. Verified live via a
  Playwright node-graph inspection (oscillator/bufferSource/filter counts
  and gain envelopes per sound), since literal listening isn't possible in
  this environment; toggling mute actually suppresses/restores node
  creation, not just the visible icon state.
- [ ] Jump ahead: an end-of-level exam that, passed at 90%+, lets a
  learner skip straight to the next level — the assumption being they
  already know that level's content.
