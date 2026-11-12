# Content schemas (Slovak)

Formal JSON schemas validating all Slovak authoring output.

## Schemas

- `lesson.schema.json` - Single lesson file (`content/sk/lessons/a1/<stem>/lesson.<id>.json`)
- `grammar.schema.json` - Grammar explanation pages
- `exercises.schema.json` - Standalone exercise banks
- `vocabulary.schema.json` - Unit vocabulary definitions
- `story.schema.json` - Graded reader stories
- `test.schema.json` - Placement diagnostic and level tests
- `units.schema.json` - Level curriculum unit tables (`content/sk/curriculum/units/<level>.json`)
- `drill-bank.schema.json` - Drill banks for Workshop

## Validation

Validate content files with:
```bash
python scripts/validate-content.py --changed
```
