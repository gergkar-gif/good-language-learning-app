import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

# Let's inspect Unit 2 story
p = Path("content/hu/stories/world/b1/b1-karpatmedence-01.json")
if not p.exists():
    # look for matching story
    for match in Path("content/hu/stories/world/b1").glob("b1-karpatmedence*.json"):
        print("Found story:", match)
        with open(match, "r", encoding="utf-8") as f:
            data = json.load(f)
            print("Title:", data.get("title"))
            print("Characters:", data.get("characters"))
            print("Pedagogical:", json.dumps(data.get("pedagogical", {}), ensure_ascii=False)[:300])
            break
