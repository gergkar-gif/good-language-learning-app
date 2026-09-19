#!/usr/bin/env python3
"""Convert all fill-in-the-blank exercises in Unit 7 and 8 to schema-compliant fill-blank."""

import glob
import json
import re
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET_DIR = os.path.join(ROOT, "content", "hu", "exercises", "b1")

# English hints for target words to enrich pedagogical value
HINTS = {
    "jelentkezhetnek": "they may apply",
    "fejlessze": "to develop / subjunctive",
    "módszer": "method",
    "bizonyítványát": "his/her certificate",
    "kíváncsiság": "curiosity",
    "tanulhat": "can study",
    "járhassak": "so that I could attend",
    "jegyzetelnek": "they take notes",
    "bukom": "I fail",
    "önképzés": "self-education",
    "összpontosítanunk": "we must concentrate",
    "menetrend": "schedule / timetable",
    "folyóparton": "on the riverbank",
    "késéssel": "with delay",
    "panaszt": "complaint",
    "útitervét": "its itinerary",
    "felől": "from the direction of",
    "hágón": "on the mountain pass",
    "estig": "until evening",
    "pótlóbuszok": "replacement buses",
    "látnivalókkal": "with sights",
    "alagúton": "through the tunnel",
    "szállásfoglalást": "accommodation booking",
    "aranyforintot": "gold florin",
    "közvetítő": "mediator",
    "megerősítette": "confirmed / reinforced",
    "végvárrendszert": "border fortress system",
    "hősiessége": "heroism",
    "holló": "raven",
    "állandó hadsereget": "standing army",
    "humanista": "humanist",
    "füstadót": "chimney tax",
    "virágkora": "golden age"
}

def fix_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    changed = False
    for ex in data.get("exercises", []):
        if ex.get("type") == "fill-in-the-blank":
            sentence = ex.get("sentence", "")
            match = re.search(r"\[(.*?)\]", sentence)
            if match:
                answer = match.group(1)
                hint = HINTS.get(answer, "")
                hint_str = f" ({hint})" if hint else ""
                clean_sentence = re.sub(r"\[.*?\]", "____", sentence) + hint_str
            else:
                answer = ex.get("options", [""])[ex.get("correct", 0)]
                hint = HINTS.get(answer, "")
                hint_str = f" ({hint})" if hint else ""
                clean_sentence = sentence + " ____" + hint_str

            ex["type"] = "fill-blank"
            ex["sentence"] = clean_sentence
            ex["answer"] = answer
            ex.pop("options", None)
            ex.pop("correct", None)
            changed = True

    if changed:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print(f"Fixed {os.path.basename(file_path)}")

def main():
    files = glob.glob(os.path.join(TARGET_DIR, "b1-07-*.json")) + \
            glob.glob(os.path.join(TARGET_DIR, "b1-08-*.json")) + \
            glob.glob(os.path.join(TARGET_DIR, "b1-anjouk-*.json")) + \
            glob.glob(os.path.join(TARGET_DIR, "b1-matyas-*.json"))
    for file_path in files:
        fix_file(file_path)

if __name__ == "__main__":
    main()
