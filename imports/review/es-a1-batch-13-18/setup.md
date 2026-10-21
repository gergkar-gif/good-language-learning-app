# es A1 batch: es-a1-batch-13-18

Started 2026-10-21T03:20:18Z from origin/master 7c0af07f. Two Sonnet readers, three units each; es-es read once, fixes mirrored to es-latam.

- Reader A: Unit 13 birthdays-celebrations (a1-10-01 a1-10-02 a1-10-03 a1-10-04 a1-10-05 a1-10-consolidation; stories ['a1-10']); Unit 14 kitchen (a1-kitchen-01 a1-kitchen-02 a1-kitchen-03 a1-kitchen-04 a1-kitchen-05 a1-kitchen-consolidation; stories ['a1-09']); Unit 15 around-town (a1-04-01 a1-04-02 a1-04-03 a1-04-04 a1-04-05 a1-04-consolidation; stories ['a1-04'])
- Reader B: Unit 16 directions (a1-directions-01 a1-directions-02 a1-directions-03 a1-directions-04 a1-directions-05 a1-directions-consolidation; stories ['a1-13']); Unit 17 weather (a1-weather-01 a1-weather-02 a1-weather-03 a1-weather-04 a1-weather-05 a1-weather-consolidation; stories ['a1-14']); Unit 18 work-obligations (a1-work-01 a1-work-02 a1-work-03 a1-work-04 a1-work-05 a1-work-consolidation; stories ['a1-15'])

## Baseline check-content, errors / suspects

| Unit | es-es | es-latam |
|---|---|---|
| 13 birthdays-celebrations | 3 / 39 | 3 / 39 |
| 14 kitchen | 2 / 4 | 2 / 4 |
| 15 around-town | 6 / 10 | 6 / 10 |
| 16 directions | 3 / 5 | 3 / 5 |
| 17 weather | 1 / 13 | 1 / 14 |
| 18 work-obligations | 2 / 12 | 2 / 12 |

## Files differing es-es vs es-latam

- birthdays-celebrations: a1-10-01-ex.json, a1-10-05-ex.json, a1-10-01-fiesta-gr.json, a1-10-05-celebracion-gr.json
- kitchen: a1-kitchen-02-hacer-gr.json
- around-town: none
- directions: none
- weather: none
- work-obligations: none
- Readers launched 03:22:15Z (Sonnet, background); prompts in prompt-a.txt / prompt-b.txt.
