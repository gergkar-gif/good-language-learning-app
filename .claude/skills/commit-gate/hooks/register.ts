import type { Register } from 'claude-code'

// (?<!-)...(?!-) so a path like commit-gate/ or a word like pre-commit doesn't
// falsely look like the git subcommand "commit".
const COMMIT = /\bgit\b[^|;&]*(?<!-)\bcommit\b(?!-)/
// The command stages files itself (git add ... && git commit, or commit -a/-am)
const STAGES_TOO = /\bgit\s+add\b|(?<!-)\bcommit\b(?!-)[^|;&]*\s-[a-zA-Z]*a/

const SHELL_ASSET = /^(styles|engine)\/.+\.(css|js)$/
// Files that define how content must be written ...
const RULES = /^content\/[^/]+\/schemas\/(?!README\.md$)|^scripts\/(validate-content|audit-lesson|audit-lesson-hu|audit_exercise_metadata)\.py$/
// ... and the guides that describe it to whoever writes content next.
const GUIDES = /^(AGENTS|CLAUDE)\.md$|^content\/[^/]+\/guides\/|^content\/hu\/HU_Content_Authoring_Template\.md$|^content\/[^/]+\/schemas\/README\.md$/

// Git commands that change the index, HEAD or working files. In the main
// checkout these touch Antigravity's uncommitted work too (it stashed,
// rebased and deleted ours on 2026-10-01 and 2026-10-03), so Claude does them
// in its own worktree instead. Read-only commands, fetch and push stay allowed.
const TREE_WRITE =
  /\bgit\b(?:\s+-[Cc]\s+(?:"[^"]*"|'[^']*'|\S+))*\s+(commit|add|stash|reset|rebase|pull|merge|checkout|switch|restore|clean|cherry-pick|revert|am|rm|mv)\b(?!-)/
const CLAUDE_WORKTREE = 'C:/dev/parlour-claude'

// The directory a command's git runs in: a `git -C <dir>`, else the last
// `cd <dir>` before it, else the session's cwd (undefined).
function gitDir(command: string): string | undefined {
  const at = TREE_WRITE.exec(command)?.index ?? command.search(/\bgit\b/)
  const unquote = (s: string) => s.replace(/^["']|["']$/g, '')
  const c = /\bgit\s+-C\s+("[^"]*"|'[^']*'|\S+)/.exec(command.slice(at))
  if (c) return unquote(c[1])
  const cds = [...command.slice(0, Math.max(at, 0)).matchAll(/(?:^|[;&|(]\s*)cd\s+("[^"]*"|'[^']*'|[^\s;&|]+)/g)]
  return cds.length ? unquote(cds[cds.length - 1][1]) : undefined
}

// What `git add ...` / `commit -a` in the command will stage, from git status.
async function toBeStaged(command: string, git: (...args: string[]) => Promise<string>) {
  const status = (await git('status', '--porcelain', '--untracked-files=all'))
    .split('\n')
    .filter(Boolean)
    .map(l => ({ isTracked: !l.startsWith('??'), path: l.slice(3).replace(/^.* -> /, '').replace(/^"|"$/g, '') }))
  const args = (/\bgit\s+add\s+([^|;&\r\n]*)/.exec(command)?.[1] ?? '').match(/"[^"]*"|'[^']*'|\S+/g) ?? []
  const paths = args.map(a => a.replace(/^["']|["']$/g, '').replace(/^\.\//, '').replace(/\/$/, ''))
  const isAll = paths.some(p => ['-A', '--all', '.', '*'].includes(p))
  const isCommitA = /(?<!-)\bcommit\b(?!-)[^|;&\r\n]*\s-[a-zA-Z]*a/.test(command)
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
    if (!TREE_WRITE.test(e.command)) return next(e)

    const dir = gitDir(e.command)
    const git = (...args: string[]) =>
      $.process.run(['git', ...(dir ? ['-C', dir] : []), ...args]).then(r => r.stdout, () => '')

    const [gitDirPath, commonDir] = (await git('rev-parse', '--path-format=absolute', '--git-dir', '--git-common-dir'))
      .trim()
      .split('\n')
    if (gitDirPath && gitDirPath === commonDir && !e.command.includes('[shared-ok]')) {
      const isOurs = await $.fs.stat(`${gitDirPath}/../scripts/validate-content.py`).then(() => true, () => false)
      if (isOurs)
        return {
          deny: `commit-gate: this is the main checkout, which Antigravity shares. Git commands that change files or the index here can sweep up or wipe its uncommitted work. Work in a worktree of your own, one per Claude session: ${CLAUDE_WORKTREE} if this session already uses it, otherwise \`git worktree add --detach C:/dev/parlour-<task> origin/master\` and move your uncommitted files there. Commit there, then \`git pull --rebase origin master\` and \`git push origin HEAD:master\`. Put [shared-ok] in the command only if the user asked for this in the main checkout.`,
        }
    }

    if (!COMMIT.test(e.command)) return next(e)

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
