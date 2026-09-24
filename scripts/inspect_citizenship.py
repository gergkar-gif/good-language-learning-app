import json
from pathlib import Path

units_path = Path("content/hu/curriculum/units/b1.json")
with open(units_path, "r", encoding="utf-8") as f:
    units = json.load(f)

citizenship_units = [u for u in units if u.get("track") == "citizenship"]
print(f"Total citizenship units: {len(citizenship_units)}")
for i, u in enumerate(citizenship_units, 1):
    stem_base = u["stems"][0].rsplit("-", 1)[0]
    print(f"{i:2d}. {u['title']:<55} | base: {stem_base}")
