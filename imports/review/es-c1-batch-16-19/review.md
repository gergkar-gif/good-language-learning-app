# ES C1 core Units 16-19 (Antigravity, first block of the 12-unit run, with self-reads; 2026-11-19)

| Unit | Self-read fixes (Antigravity) | Reader fixes after it (Sonnet) |
|---|---|---|
| 16 `cities-housing` | 33 | 35 |
| 17 `everyday-aspect` (new skill) | 20 | 39 |
| 18 `conversation-markers` (new skill) | 23 | 38 |
| 19 `warnings-conditions` (new skill) | 9 | 54 |

The self-read finds real defects but does not lower what the independent read finds (~32 a unit
before the self-read, ~42 after): the units start with ~60-70 defects each. Unit 19, the fourth
unit of its chat, had the smallest self-read and the most reader fixes, and its report (like
Unit 18's) left out the norm claims (now `c1_report_check.py`).

Reviewer's planning errors found by the readers: `como-condicional-subjuntivo` (Unit 19) is already
taught on B2 Unit 33's screen "Warnings" (items tagged `conditional-conjunctions`); the Unit 17 notes
said no skill teaches the accidental *se*, but B2 Unit 19 does (`desambiguacion-valores-se`). Both
screens now recap the B2 unit; the C1 skill is kept (for the user).

Process slips, fixed: the reviewer froze four units after a failed walk (the command did not stop
on it; freezes are now conditional on the walk); `tier2` on four consolidation challenges (one
failed the grader), set to `tier1`; the es-es plant left «el vaso de jugo» in an English prompt
whose answer it converted to *zumo* (the plant now converts «…» runs; one case in all C1).
New check: `c1-text-length` (texts of Units 18-19 had ~350 words).
