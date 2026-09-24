import json
import sys
from pathlib import Path

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

units_file = Path("content/hu/curriculum/units/b1.json")
with open(units_file, "r", encoding="utf-8") as f:
    units = json.load(f)

citizenship_units = [u for u in units if u.get("track") == "citizenship"]

print(f"Total citizenship units: {len(citizenship_units)}")
for i, unit in enumerate(citizenship_units, 1):
    title = unit.get("title", "")
    stems = unit.get("stems", [])
    print(f"Unit {i:02d}: {title} (stems: {len(stems)})")
    for s in stems:
        lesson_file = Path(f"content/hu/lessons/b1/{s}.json")
        print(f"   - {s}: exists={lesson_file.exists()}")
