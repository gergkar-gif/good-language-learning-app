import type { Register } from 'claude-code'

const CHECK_INTERVAL_MS = 5 * 60 * 1000
const MAX_BATCHES = 15
const COMMIT_RE = /\bgit\b[^|;&]*\bcommit\b/
const SYNC_BOT_EMAIL = 'actions@users.noreply.github.com'
// content/<lang>/<rest>.json, relative to the repo root (git's own path spelling)
const CONTENT_FILE = /^content\/([^/]+)\/(.+\.json)$/

type WatchedCommit = { sha: string; author: string; date: string; subject: string }
type WatchedBatch = {
  id: string
  checkedAt: string
  commits: WatchedCommit[]
  files: string[]
  validation: 'pass' | 'fail'
  validationDetail?: string
  roadmapAdded: string[]
}

// Runs validate_language() on just the files that actually changed.
const VALIDATE = `
import importlib.util, pathlib, sys
s = importlib.util.spec_from_file_location('v', 'scripts/validate-content.py')
m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
lang = sys.argv[1]
paths = {pathlib.Path(p).resolve() for p in sys.argv[2:]}
ok, bad, fails = m.validate_language(lang, paths)
for f in fails: print(f)
sys.exit(1 if bad else 0)
`

function addedLines(diffText: string): string[] {
  return diffText
    .split('\n')
    .filter(line => line.startsWith('+') && !line.startsWith('+++'))
    .map(line => line.slice(1).trim())
    .filter(Boolean)
    .slice(0, 20)
}

async function repoRoot($: any): Promise<string | undefined> {
  const r = await $.process.run(['git', 'rev-parse', '--show-toplevel']).catch(() => undefined)
  const root = r?.stdout.trim()
  return root || undefined
}

async function recordOwnSha($: any, root: string) {
  const sha = (await $.process.run(['git', 'rev-parse', 'HEAD'], { cwd: root }).catch(() => undefined))?.stdout.trim()
  if (!sha) return
  const existing = ((await $.store.get('own-shas')) as string[] | undefined) ?? []
  if (existing.includes(sha)) return
  await $.store.set('own-shas', [...existing, sha].slice(-300))
}

async function recordOwnPath($: any, path: string) {
  const existing = ((await $.store.get('own-paths')) as string[] | undefined) ?? []
  if (existing.includes(path)) return
  await $.store.set('own-paths', [...existing, path].slice(-500))
}

async function validateFiles($: any, root: string, files: string[]): Promise<{ ok: boolean; detail?: string }> {
  const byLang = new Map<string, string[]>()
  for (const f of files) {
    const m = CONTENT_FILE.exec(f)
    if (!m) continue
    if (!byLang.has(m[1])) byLang.set(m[1], [])
    byLang.get(m[1])!.push(f)
  }
  if (byLang.size === 0) return { ok: true }

  const problems: string[] = []
  for (const [lang, paths] of byLang) {
    const r = await $.process
      .run(['python', '-c', VALIDATE, lang, ...paths], { cwd: root, timeoutMs: 120_000 })
      .catch(() => undefined)
    if (!r) problems.push(`${lang}: validator did not run`)
    else if (r.exitCode !== 0) problems.push((r.stdout + r.stderr).trim())
  }
  return problems.length ? { ok: false, detail: problems.join('\n').slice(0, 4000) } : { ok: true }
}

// New commits on HEAD that weren't made by this plugin's own commit-tracking
// hook, and aren't the content-sync-bot's generated-file regeneration.
async function checkCommits($: any, root: string) {
  const head = (await $.process.run(['git', 'rev-parse', 'HEAD'], { cwd: root }).catch(() => undefined))?.stdout.trim()
  if (!head) return

  const lastSeen = (await $.store.get('last-seen-sha')) as string | undefined
  if (!lastSeen) {
    await $.store.set('last-seen-sha', head) // baseline; don't backfill history
    return
  }
  if (lastSeen === head) return

  const logRes = await $.process
    .run(['git', 'log', '--reverse', `--format=%H%x1f%an%x1f%ae%x1f%aI%x1f%s`, `${lastSeen}..${head}`], { cwd: root })
    .catch(() => undefined)
  await $.store.set('last-seen-sha', head)
  if (!logRes || logRes.exitCode !== 0) return // lastSeen unreachable (force-push/rebase) — resync silently

  const ownShas = new Set(((await $.store.get('own-shas')) as string[] | undefined) ?? [])
  const commits = logRes.stdout
    .split('\n')
    .filter(Boolean)
    .map(line => {
      const [sha, author, email, date, subject] = line.split('\x1f')
      return { sha, author, email, date, subject }
    })
  const externals = commits.filter(c => !ownShas.has(c.sha) && c.email !== SYNC_BOT_EMAIL)
  if (externals.length === 0) return

  const filesRes = await $.process.run(['git', 'diff', '--name-only', lastSeen, head], { cwd: root }).catch(() => undefined)
  const files = (filesRes?.stdout ?? '').split('\n').filter(Boolean)

  const roadmapRes = files.includes('ROADMAP.md')
    ? await $.process.run(['git', 'diff', lastSeen, head, '--', 'ROADMAP.md'], { cwd: root }).catch(() => undefined)
    : undefined
  const roadmapAdded = roadmapRes ? addedLines(roadmapRes.stdout) : []

  const { ok, detail } = await validateFiles($, root, files)

  const batch: WatchedBatch = {
    id: head,
    checkedAt: new Date(await $.clock.now()).toISOString(),
    commits: externals.map(c => ({ sha: c.sha, author: c.author, date: c.date, subject: c.subject })),
    files: files.filter(f => CONTENT_FILE.test(f)),
    validation: ok ? 'pass' : 'fail',
    validationDetail: detail,
    roadmapAdded,
  }

  const stored = ((await $.store.get('batches')) as WatchedBatch[] | undefined) ?? []
  await $.store.set('batches', [batch, ...stored].slice(0, MAX_BATCHES))

  $.ui.toast(
    `antigravity-watch: ${externals.length} commit(s) landed outside Claude — ${ok ? 'validates clean' : 'VALIDATION FAILED'}` +
      (roadmapAdded.length ? `, +${roadmapAdded.length} new ROADMAP line(s)` : '') +
      ' (see /antigravity)',
    { timeoutMs: ok ? 6000 : 15_000 },
  )
}

// Uncommitted changes sitting in the shared working tree that this plugin
// didn't make itself — the live "Antigravity is editing right now" signal.
// Not validated: a file mid-write can be transiently invalid JSON.
async function checkDirty($: any, root: string) {
  const statusRes = await $.process.run(['git', 'status', '--porcelain', '--untracked-files=all'], { cwd: root }).catch(() => undefined)
  if (!statusRes) return

  const ownPaths = new Set(((await $.store.get('own-paths')) as string[] | undefined) ?? [])
  const dirty = statusRes.stdout
    .split('\n')
    .filter(Boolean)
    .map(line => line.slice(3).replace(/^.* -> /, '').replace(/^"|"$/g, ''))
    .filter(path => !ownPaths.has(path))
    .sort()

  const lastDirty = ((await $.store.get('last-dirty-paths')) as string[] | undefined) ?? []
  if (dirty.join('\n') === lastDirty.join('\n')) return

  await $.store.set('last-dirty-paths', dirty)

  if (dirty.length > lastDirty.length)
    $.ui.toast(`antigravity-watch: ${dirty.length} file(s) changing outside Claude right now (see /antigravity)`)
}

async function runChecks($: any) {
  const root = await repoRoot($)
  if (!root) return
  await checkCommits($, root)
  await checkDirty($, root)
}

function formatReport(batches: WatchedBatch[], dirty: string[]): string {
  const lines: string[] = []

  if (dirty.length) {
    lines.push(`In progress now, uncommitted, not Claude's (${dirty.length} file(s)):`)
    lines.push(...dirty.slice(0, 15).map(p => `  ${p}`))
    if (dirty.length > 15) lines.push(`  …and ${dirty.length - 15} more`)
  }

  if (batches.length === 0 && dirty.length === 0) return 'Nothing from outside Claude yet. Checking every 5 minutes.'

  for (const b of batches.slice(0, 10)) {
    lines.push('')
    lines.push(
      `${b.validation === 'fail' ? '✗ FAILED' : '✓ passed'} — ${b.commits.length} commit(s) — ${b.checkedAt.slice(0, 16).replace('T', ' ')}`,
    )
    for (const c of b.commits) lines.push(`  ${c.sha.slice(0, 7)} ${c.author}: ${c.subject}`)
    if (b.validation === 'fail' && b.validationDetail) lines.push('  ' + b.validationDetail.slice(0, 500).replace(/\n/g, '\n  '))
    if (b.roadmapAdded.length) lines.push(`  +${b.roadmapAdded.length} ROADMAP line(s): ${b.roadmapAdded[0]}`)
  }

  return lines.join('\n')
}

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    await $.command.register({
      name: 'antigravity',
      description: "Show content changes Claude didn't make, and their validation status",
    })

    $.clock.every(CHECK_INTERVAL_MS, () => runChecks($))
    void runChecks($)

    return next(e)
  })

  on('command.run', { command: 'antigravity' }, async $ => {
    const batches = ((await $.store.get('batches')) as WatchedBatch[] | undefined) ?? []
    const dirty = ((await $.store.get('last-dirty-paths')) as string[] | undefined) ?? []
    return { text: formatReport(batches, dirty) }
  })

  for (const tool of ['Write', 'Edit'] as const) {
    on('tool.call', { tool }, async ($, e, next) => {
      const ran = await next(e)
      if (ran.deny === undefined && !ran.isError) await recordOwnPath($, e.file_path)
      return ran
    })
  }

  on('tool.call', { tool: 'Bash' }, async ($, e, next) => {
    const ran = await next(e)
    if (ran.deny === undefined && !ran.isError && COMMIT_RE.test(e.command)) {
      const root = await repoRoot($)
      if (root) await recordOwnSha($, root)
    }
    return ran
  })
}
