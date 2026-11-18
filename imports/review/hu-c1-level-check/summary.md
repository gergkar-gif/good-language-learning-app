# HU C1 level checklist (2026-11-18)

Run per `docs/unit-pipeline-log.md` § "Before calling a level done".

| Check | Result |
|---|---|
| `freeze_unit.py --status hu` | C1 72/72 frozen (36 core, 36 culture) |
| `check-content.py hu c1` | 0 errors, 0 suspects; 307 accepted findings stored with the units (301 `vocab-unused` lessons, 4 consolidation replays, 2 `article-blank` false positives: cataphoric *az*) |
| `validate-content.py --warnings` | no HU warning. Four thin skills were fixed at the checklist: `conclusive-markers`, `framing-markers`, `optative-subjunctive` and `satire-parody` each got two consolidation replays (`thin_skills.py`; Culture Units 15, 19, 21 and core Unit 5 unfrozen, relocked, refrozen) |
| `walk_lessons.js hu c1 --jobs 4` | 430/432 first run; the 2 failures (c1-megfigyeles-04, c1-magyarjovo-03) were click timeouts on a story step right after a Guide note was closed, and both pass alone: 432/432, every challenge on screen and passing the grader; no console errors, no failed requests. The four consolidation lessons edited during the run were walked again, 4/4 |
| `check_unit_refs.py hu c1` | 8 hits, all false positives (the recap names the unit of the skill that teaches the pattern; the italic is another example of it, or *nemcsak* vs A2's *nem csak*) |
| C1 formulas before their screen | none in screens, items or goals; the only earlier uses are two unit intros previewing their unit's forms (c1-07-01, c1-03-01) and *végső soron* in Culture Unit 8's reading (stories are exempt) |
| Reader library | 251 C1 stories in the manifest, every one in a unit |

Also fixed on the way: Culture Unit 15 consolidation matched SZTAKI with "magyar kutatóhálózat" (now *a HUN-REN egyik kutatóintézete*).

Not covered: speaking steps, spoken challenge answers, wrong-answer paths, real audio, the live site, a native speaker's eye. The culture track is still hidden (`HIDDEN_TRACKS`).

Open for the user:
- the 1,573 list words in 301 C1 lessons that no item drills (accepted "until the C1 level checklist", user 2026-11-14): keep them as SRS-only words, or prune them;
- unhiding the culture track.
