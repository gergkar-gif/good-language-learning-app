# es-es B2 core planted from es-latam (2026-11-14)

User (2026-11-14): "core should remain largely the same (except the regional varieties) then
the culture can distinguish the two". Approved defaults: Unit 34 recast for Spain, *vos* kept
as recognition only, texts unchanged, core only (no es-es B2 culture track yet).

## How

`python scripts/plant_es_es_b2.py` copied the 36 core units (unit table, 216 lessons, screens,
exercises, vocabulary, 36 texts, 216 challenges: 828 files) and put Spanish strings into
Spain's words with `course_variants.convert` (58 files changed: *billete*, *coche*, *móvil*,
*enfadado*, *patatas*, *aparcamiento*, *el salón*). English fields were left alone, except
Spanish forms in italics inside screen text. It lists rather than guesses; `worksheet.md` is
its output. **Do not rerun it with `--force`**: it would overwrite the hand edits below.

## By hand (Spain usage)

- *vosotros*: rows added to the imperfect and pluperfect subjunctive tables (b2-15-01,
  b2-16-01); b2-06-03.ex03 (*vengáis*), b2-16-consolidation.ex02 (*hubierais / hubieseis*),
  b2-09-04 example (*con vosotros*).
- Present perfect for the recent past, which the check found once but a wider search found 9
  more times: b2-03-05 (*ya ha salido* ×4), b2-11-05, b2-13-03.ex02, b2-23-consolidation.ex06
  (4 options), b2-28-02, b2-33-03 (2), challenges b2-19-01, b2-23-05, b2-28-02.
- Unit 34: 34-01 gains a section on Spain (*tú* used more widely; *vosotros* / *ustedes*) and
  one item (ex13); 34-02 rewritten from Spain's side (*coche → carro / auto*, *móvil →
  celular*, *piso → departamento*…), its fill-blank set in Buenos Aires, its sentence builder
  with *coche*; the consolidation matching uses *el móvil*, *el piso*. 34-03 to 34-05 converted
  normally. `voseo-rioplatense-reconocimiento` no longer marked es-latam only (frozen-es.json).
- Vocabulary es-es lacked earlier: *el equipo* (b2-01-01), *el ensayo*, *la revista*
  (b2-05-01), *el sueldo* (b2-11-03).

## Result

| Check | es-es B2 |
|---|---|
| frozen | 36/36 |
| check-content | 0 errors / 0 unaccepted suspects (28 accepts reused from es-latam, 5 new) |
| validate --changed | 830 passed, 0 failed |
| unmet words | names (9), the 5 es-latam kept cases, *sala de reuniones* (standard in Spain) |
| walk with challenges | 216/216 |

Not checked by a speaker of Spain's Spanish: tone of the converted sentences; leftover Latin
American turns that no word list catches (*tomar* for *coger* transport, *acá*, *manejar*:
none found by grep, but the list is not exhaustive).

## From now on

B2 core exists twice. A B2 fix goes into both courses: a fix list through
`mirror_fixes.py <fixes> es-latam es-es <out>` (it converts words; unmatched lines are the
course variants), or the same hand edit in both.
