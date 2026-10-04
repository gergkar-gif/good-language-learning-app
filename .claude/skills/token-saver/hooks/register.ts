import type { Register } from 'claude-code'

const MAX_BYTES = 60_000 // ~15k tokens; ROADMAP.md, dictionaries, indexes and decks all exceed it
const BINARY = /\.(png|jpe?g|gif|webp|svg|pdf|ipynb)$/i

export const register: Register = on => {
  on('tool.call', { tool: 'Read' }, async ($, e, next) => {
    if (e.offset !== undefined || e.limit !== undefined || BINARY.test(e.file_path)) return next(e)

    const stat = await $.fs.stat(e.file_path).catch(() => undefined)
    if (!stat || stat.kind !== 'file' || stat.size <= MAX_BYTES) return next(e)

    return {
      deny: `token-saver: ${e.file_path} is ${Math.round(stat.size / 1000)} KB. Grep for what you need, or Read it with offset/limit around the relevant part. If the whole file really is needed, Read it with an explicit limit.`,
    }
  })

  on('turn.complete', async ($, e, next) => {
    const { context } = await $.session.usage()
    if (context.tokens !== undefined)
      $.ui.status(`ctx ${Math.round(context.tokens / 1000)}k / ${Math.round(context.window / 1000)}k (${Math.round(context.percent ?? 0)}%)`)
    return next(e)
  })
}
