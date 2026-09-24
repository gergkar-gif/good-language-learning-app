import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

units_file = Path("content/hu/curriculum/units/b1.json")
with open(units_file, "r", encoding="utf-8") as f:
    units = json.load(f)

citizenship_units = [u for u in units if u.get("track") == "citizenship"]

for i, unit in enumerate(citizenship_units[1:], 2):
    title = unit.get("title", "")
    stems = unit.get("stems", [])
    base = stems[0].rsplit("-", 1)[0]
    print(f"=== Unit {i:02d}: {base} ({title}) ===")
    for s in stems:
        lf = Path(f"content/hu/lessons/b1/{s}.json")
        if lf.exists():
            with open(lf, "r", encoding="utf-8") as lfp:
                ldata = json.load(lfp)
                refs = [sec.get("ref") for sec in ldata.get("sections", []) if "ref" in sec]
                print(f"  Lesson {s}: title='{ldata.get('title')}', refs={refs}")
        else:
            print(f"  Lesson {s}: MISSING")
