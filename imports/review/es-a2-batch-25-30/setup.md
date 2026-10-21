# es A2 batch: es-a2-batch-25-30

Started 2026-10-21T22:34:56Z from origin/master f3d75341. 2 Sonnet reader(s); es-es read once, fixes mirrored to es-latam.

- Reader A: Unit 25 pronouns (a2-pronombrescliticos-01 a2-pronombrescliticos-02 a2-pronombrescliticos-03 a2-pronombrescliticos-04 a2-pronombrescliticos-05 a2-pronombrescliticos-consolidation; stories ['a2-pronombrescliticos']); Unit 26 asking-politely-giving-advice (a2-condicionalsimple-01 a2-condicionalsimple-02 a2-condicionalsimple-03 a2-condicionalsimple-04 a2-condicionalsimple-05 a2-condicionalsimple-consolidation; stories ['a2-condicionalsimple']); Unit 27 expressing-wishes-feelings (a2-subjuntivobasico-01 a2-subjuntivobasico-02 a2-subjuntivobasico-03 a2-subjuntivobasico-04 a2-subjuntivobasico-05 a2-subjuntivobasico-consolidation; stories ['a2-subjuntivobasico'])
- Reader B: Unit 28 connecting-ideas-habits (a2-perifrasisverbales-01 a2-perifrasisverbales-02 a2-perifrasisverbales-03 a2-perifrasisverbales-04 a2-perifrasisverbales-05 a2-perifrasisverbales-consolidation; stories ['a2-perifrasisverbales']); Unit 29 studying-school-life (a2-educacionyestudios-01 a2-educacionyestudios-02 a2-educacionyestudios-03 a2-educacionyestudios-04 a2-educacionyestudios-05 a2-educacionyestudios-consolidation; stories ['a2-educacionyestudios']); Unit 30 por-and-para (a2-porpara-01 a2-porpara-02 a2-porpara-03 a2-porpara-04 a2-porpara-05 a2-porpara-consolidation; stories [])

## Baseline check-content, errors / suspects

| Unit | es-es | es-latam |
|---|---|---|
| 25 pronouns | 3 / 26 | 3 / 26 |
| 26 asking-politely-giving-advice | 6 / 37 | 6 / 39 |
| 27 expressing-wishes-feelings | 0 / 35 | 0 / 35 |
| 28 connecting-ideas-habits | 4 / 44 | 4 / 44 |
| 29 studying-school-life | 5 / 50 | 5 / 49 |
| 30 por-and-para | 1 / 32 | 1 / 37 |

## Files differing es-es vs es-latam

- pronouns: a2-pronombrescliticos-01-ex.json, a2-pronombrescliticos-03-ex.json, a2-pronombrescliticos-04-gr.json, a2-pronombrescliticos-04-ex.json, a2-pronombrescliticos.json, a2-pronombrescliticos-consolidation-ex.json
- asking-politely-giving-advice: a2-condicionalsimple-01-gr.json, a2-condicionalsimple-03-gr.json, a2-condicionalsimple-03-voc.json, a2-condicionalsimple-03-ex.json, a2-condicionalsimple-04-gr.json, a2-condicionalsimple-05-ex.json, a2-condicionalsimple.json, a2-condicionalsimple-consolidation-ex.json
- expressing-wishes-feelings: a2-subjuntivobasico-03-gr.json, a2-subjuntivobasico-05-gr.json, a2-subjuntivobasico.json
- connecting-ideas-habits: a2-perifrasisverbales-04-ex.json
- studying-school-life: a2-educacionyestudios-04-ex.json, a2-educacionyestudios.json
- por-and-para: a2-porpara-02-ex.json, a2-porpara-03-gr.json, a2-porpara-04-ex.json, a2-porpara-05-ex.json

## Walk (with `python scripts/dev-server.py 8131` running)

    node scripts/walk_lessons.js <course> a2 --jobs 4 --only a2-pronombrescliticos-01 a2-pronombrescliticos-02 a2-pronombrescliticos-03 a2-pronombrescliticos-04 a2-pronombrescliticos-05 a2-pronombrescliticos-consolidation a2-condicionalsimple-01 a2-condicionalsimple-02 a2-condicionalsimple-03 a2-condicionalsimple-04 a2-condicionalsimple-05 a2-condicionalsimple-consolidation a2-subjuntivobasico-01 a2-subjuntivobasico-02 a2-subjuntivobasico-03 a2-subjuntivobasico-04 a2-subjuntivobasico-05 a2-subjuntivobasico-consolidation a2-perifrasisverbales-01 a2-perifrasisverbales-02 a2-perifrasisverbales-03 a2-perifrasisverbales-04 a2-perifrasisverbales-05 a2-perifrasisverbales-consolidation a2-educacionyestudios-01 a2-educacionyestudios-02 a2-educacionyestudios-03 a2-educacionyestudios-04 a2-educacionyestudios-05 a2-educacionyestudios-consolidation a2-porpara-01 a2-porpara-02 a2-porpara-03 a2-porpara-04 a2-porpara-05 a2-porpara-consolidation
- Readers launched 22:35:48Z.
- Reader A finished 23:04Z: fixes 73 + 73 + 65 = 211; report file allowed
