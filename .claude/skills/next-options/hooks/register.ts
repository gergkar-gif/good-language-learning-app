import type { Register } from 'claude-code'

const INSTRUCTION = `next-options: when your reply finishes a task (you changed, built, fixed, reviewed or researched something — not a clarifying question, not a mid-task check-in, not a one-line factual answer), end it with a "**What next?**" block of exactly three numbered options, after any summary.

Fill the three slots strictly by priority, not one per tier:
- First, Polish: making existing functionality or content correct and complete (bugs, gaps, inconsistencies, unverified edge cases, rough content you saw during this task or know of). If there are three real polish items, all three options are polish.
- Only when polish runs out, Next step: the logical next feature or capability building on what exists.
- Only when both run out, Long shot: bigger plans and large content work.

Label each option with its tier, e.g. "1. **Polish** — …". Order them by that priority. One line each, specific to this project — name the file, unit, feature or ROADMAP.md queue item, never generic advice; don't pad a tier with weak items just to reach a lower one or to avoid it. If ROADMAP.md's "Current priority queue" already lists a fitting item, point to it by number rather than inventing a new one. Don't start any of them; the user picks.`

export const register: Register = on => {
  on('prompt.submit', ($, e, next) => {
    // Only the user's own prompts (terminal, phone, desktop app via the SDK) — not notifications or peers.
    if (!['composer', 'bridge', 'sdk', 'unclassified'].includes(e.origin.kind)) return next(e)
    return next({ ...e, context: [...(e.context ?? []), INSTRUCTION] })
  })
}
