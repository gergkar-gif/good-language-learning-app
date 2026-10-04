import type { Register } from 'claude-code'

const INSTRUCTION = `next-options: when your reply finishes a task (you changed, built, fixed, reviewed or researched something — not a clarifying question, not a mid-task check-in, not a one-line factual answer), end it with exactly this block, after any summary:

**What next?**
1. **Polish** — <one concrete step that makes something that already exists correct and complete: a bug, gap, inconsistency, unverified edge case or rough content you saw during this task>
2. **Next step** — <the natural next feature or capability that builds directly on what just shipped>
3. **Long shot** — <a bigger plan or large content effort worth doing eventually>

Rules: always that order (perfecting existing work comes first, then logical next steps, then big/long-shot work). One line each, specific to this project and this task — name the file, unit, feature or ROADMAP.md queue item, never generic advice. If ROADMAP.md's "Current priority queue" already lists a fitting item, point to it by number rather than inventing a new one. Don't start any of them; the user picks.`

export const register: Register = on => {
  on('prompt.submit', ($, e, next) => {
    // Only the user's own prompts (terminal, phone, desktop app via the SDK) — not notifications or peers.
    if (!['composer', 'bridge', 'sdk', 'unclassified'].includes(e.origin.kind)) return next(e)
    return next({ ...e, context: [...(e.context ?? []), INSTRUCTION] })
  })
}
