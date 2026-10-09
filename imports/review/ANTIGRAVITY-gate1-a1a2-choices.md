# Task: release gate 1, A1–A2 choice give-aways in hu, es-es and es-latam (ROADMAP 152)

Gate 1 ships A1 and A2 in all three courses with nothing a learner can pick
without understanding it. This task fixes the choice exercises
(`multiple-choice`, `dialogue-complete`, `listening-choice`) that
`scripts/check-content.py` still flags at A1–A2:

- **length-giveaway**: the correct option is over **1.3×** the longest
  wrong one (and 4+ characters longer). The 2× cases were fixed in ROADMAP
  130; these are the milder ones it left, and the user set 1.3× for all
  content on 2026-10-09.
- **tell-absolute**: only wrong options carry an absolute (*mindig, soha,
  senki, semmi, teljesen, kizárólag; siempre, nunca, nadie, ninguno,
  totalmente, completamente*), so the learner picks the moderate option
  without understanding.
- **tell-time-word**: only wrong options carry a time word (*tegnap,
  holnap, tavaly, jövőre; ayer, anoche, anteayer, pasado mañana*).

Many tell hits are not real tells: a vocabulary item whose wrong options
are simply other words (*Which word means "which"? melyik / senki /
valami*), or a tense item where the time word *is* the grammar
(*Compramos los billetes ayer* as the wrong option to "which uses the
pretérito perfecto?" is wrong because *ayer* takes the indefinido). Those
are `keep`, with the reason. Fix only the ones where the word lets a
learner rule the option out without knowing the point being tested.

Repository: this one (Parlour). Commit straight to `master` and push after
every commit.

## Read first

1. [ANTIGRAVITY-length-giveaway-hu.md](ANTIGRAVITY-length-giveaway-hu.md):
   its method, **rules 1–13 and every review note at the bottom** apply in
   full to the Hungarian worksheet. Its scope section and its checker
   commands do not; this brief replaces them.
2. [ANTIGRAVITY-length-giveaway-es.md](ANTIGRAVITY-length-giveaway-es.md):
   the same for the Spanish worksheet, with its review notes.
3. [docs/course-generation-brief.md](../../docs/course-generation-brief.md)
   § 6.3 (option rules).

The standard the reviews settled on, in one line: **each wrong option is a
different real fact, form or reply, in the same tone and about the same
length as the correct one; never an absolute, never a stock "bad news"
line, never absurd.**

## The worksheets

| Worksheet | Blocks | Entries |
|---|---|---|
| `imports/review/gate1-hu-worksheet.txt` | 6 (A1 1–3, A2 3–6) | 471 |
| `imports/review/gate1-es-worksheet.txt` | 4 (A1 1–2, A2 2–4) | 279 |

Built by `python scripts/make_worksheet.py` from the checker. One entry per
exercise; `files:` lists every copy (lesson and consolidation, **es-es and
es-latam**), and every copy gets the identical change. `checks:` says which
finding put it there. The format and the decisions (`shorten`, `match`,
`keep`, `log`) are at the top of each worksheet; `keep` is only for the two
tell checks, never for length.

Left out on purpose: the 14 HU `a1-121…150` dialogue items a native speaker
reviewed (listed in the HU brief).

## Scope

- Edit only the option text of the exercises in your block, in the files
  listed, plus the worksheet and `imports/review/hu-review-questions.txt` /
  `es-review-questions.txt`.
- Don't touch `question`, `prompt`, `correct`, the order of options,
  `teaches`, `distractor_skills`, `category`, `stage`, `skills/`, or any
  `tags.lock.json`. Exception: fix a number or wording mismatch your change
  creates in the question, and say so in `why:`.
- **es-latam never gets a vosotros form**, and es-es and es-latam copies stay
  identical. If a fix needs a form that differs between Spain and Latin
  America, `log` it.
- Stage only the files you changed (`git add <path> …`). Run
  `git pull --rebase origin master` before each block and before each push.
  If it reports changes that aren't yours, stop and report.

## Order and stops

Do the **HU worksheet first, then ES**. One block per chat:

1. Re-read this brief and the review notes in the two older briefs, and any
   review notes added at the bottom of this file.
2. Fill in `decision:` and `why:` for every entry of the block **before**
   editing any file. For each unit read its lesson file (and, for reading
   questions, its story) so you know what the learner has met.
3. Read every new option next to **its own question** (HU rule 13).
4. Apply exactly what the worksheet says, in every listed file.
5. Run the checks, commit, push, **stop and report**. The reviewer tells you
   when to start the next block.

## Checks before each commit

    python scripts/check-content.py <course> <level> --summary
    python scripts/check-content.py --changed
    python scripts/validate-content.py --changed

For each level in your block: no id of the block may still be flagged for
`length-giveaway`, `tell-absolute` or `tell-time-word`, except `keep` and
`log` entries. `--changed` must report no new errors and no new suspects
(fix a new suspect, or say in the report why it stays). The validator must
pass.

Commit per block, e.g.

    fix(hu/a1): choice give-aways, gate 1 block 1 (ROADMAP 152)

with the shorten / match / keep / log counts in the body.

## The report at each stop

- the block's counts (shorten / match / keep / log), counted from the
  worksheet;
- every id where the **correct option** changed;
- every `keep`, with its reason;
- every logged question, with its `why`.

Do not edit ROADMAP.md or ACHIEVED.md. The reviewer does.

---

## Review notes

(The reviewer adds notes here after each stop. Read them before starting
the next block.)
