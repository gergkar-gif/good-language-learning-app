import type { Register } from 'claude-code'

const COMMIT = /\bgit\b[^|;&]*\bcommit\b/
// The command stages files itself (git add ... && git commit, or commit -a/-am)
const STAGES_TOO = /\bgit\s+add\b|\bcommit\b[^|;&]*\s-[a-zA-Z]*a/

const SHELL_ASSET = /^(styles|engine)\/.+\.(css|js)$/
// Files that define how content must be written ...
const RULES = /^content\/[^/]+\/schemas\/(?!README\.md$)|^scripts\/(validate-content|audit-lesson|audit-lesson-hu|audit_exercise_metadata)\.py$/
// ... and the guides that describe it to whoever writes content next.
const GUIDES = /^(AGENTS|CLAUDE)\.md$|^content\/[^/]+\/guides\/|^content\/hu\/HU_Content_Authoring_Template\.md$|^content\/[^/]+\/schemas\/README\.md$/

// What `git add ...` / `commit -a` in the command will stage, from git status.
async function toBeStaged(command: string, git: (...args: string[]) => Promise<string>) {
  const status = (await git('status', '--porcelain', '--untracked-files=all'))
    .split('\n')
    .filter(Boolean)
    .map(l => ({ isTracked: !l.startsWith('??'), path: l.slice(3).replace(/^.* -> /, '').replace(/^"|"$/g, '') }))
  const args = (/\bgit\s+add\s+([^|;&]*)/.exec(command)?.[1] ?? '').match(/"[^"]*"|'[^']*'|\S+/g) ?? []
  const paths = args.map(a => a.replace(/^["']|["']$/g, '').replace(/^\.\//, '').replace(/\/$/, ''))
  const isAll = paths.some(p => ['-A', '--all', '.', '*'].includes(p))
  const isCommitA = /\bcommit\b[^|;&]*\s-[a-zA-Z]*a/.test(command)
  return status
    .filter(
      s =>
        isAll ||
        (isCommitA && s.isTracked) ||
        (paths.includes('-u') && s.isTracked) ||
        paths.some(p => !p.startsWith('-') && (s.path === p || s.path.startsWith(`${p}/`))),
    )
    .map(s => s.path)
}

export const register: Register = on => {
  on('tool.call', { tool: 'Bash' }, async ($, e, next) => {
    if (!COMMIT.test(e.command)) return next(e)

    const git = (...args: string[]) => $.process.run(['git', ...args]).then(r => r.stdout, () => '')
    const root = (await git('rev-parse', '--show-toplevel')).trim()
    const isRepo = root && (await $.fs.stat(`${root}/scripts/validate-content.py`).then(() => true, () => false))
    if (!isRepo) return next(e)

    const staged = (await git('diff', '--cached', '--name-only')).split('\n')
    const pending = STAGES_TOO.test(e.command) ? await toBeStaged(e.command, git) : []
    const files = [...new Set([...staged, ...pending].map(f => f.trim().replace(/^"|"$/g, '')).filter(Boolean))]
    if (files.length === 0) return next(e)

    const problems: string[] = []

    if (files.some(f => SHELL_ASSET.test(f)) && !files.includes('sw.js'))
      problems.push(
        'styles/ or engine/ changed but sw.js did not: bump CACHE_VERSION in sw.js (and the ?v= strings in index.html), or installed users keep the old JS/CSS.',
      )

    if (files.some(f => RULES.test(f)) && !files.some(f => GUIDES.test(f)) && !e.command.includes('[no-guide]'))
      problems.push(
        `Content rules changed (${files.filter(f => RULES.test(f)).join(', ')}) but no guide did. Record the change in AGENTS.md and the matching guide (content/es-latam/guides/editorial-style-guide.md, content/hu/HU_Content_Authoring_Template.md, ...). If it really changes nothing about how content is written, put [no-guide] in the commit message.`,
      )

    if (files.some(f => f.startsWith('content/'))) {
      $.ui.status('commit-gate: validating content…')
      const v = await $.process
        .run(['python', 'scripts/validate-content.py', '--changed'], { cwd: root, timeoutMs: 180_000 })
        .catch(() => undefined)
      $.ui.status(undefined)
      if (v && v.exitCode !== 0)
        problems.push(`validate-content.py --changed fails:\n${(v.stdout + v.stderr).trim().slice(-4000)}`)
    }

    if (problems.length) {
      $.ui.toast('commit-gate: commit blocked')
      return { deny: `commit-gate blocked this commit:\n- ${problems.join('\n- ')}` }
    }

    const ran = await next(e)
    if (ran.deny !== undefined || ran.isError || files.some(f => /^(ROADMAP|ACHIEVED)\.md$/.test(f))) return ran
    return {
      ...ran,
      context: [
        ...(ran.context ?? []),
        'commit-gate: this commit did not touch ROADMAP.md or ACHIEVED.md. If it finished a queue item or is worth a future session knowing about, update them now (CLAUDE.md § "Keep ROADMAP.md current").',
      ],
    }
  })
}
