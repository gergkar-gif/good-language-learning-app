import os
import glob
import json
import re

def fix_exercise_obj(ex):
    t = ex.get("type")
    
    # Handle fill-in-the-blank -> multiple-choice or fill-blank
    if t == "fill-in-the-blank":
        if "options" in ex and "correct" in ex:
            ex["type"] = "multiple-choice"
            t = "multiple-choice"
            if "question" not in ex and "sentence" in ex:
                ex["question"] = ex.pop("sentence")
            elif "sentence" in ex:
                del ex["sentence"]
        else:
            ex["type"] = "fill-blank"
            t = "fill-blank"

    # Handle multiple-choice
    if ex.get("type") == "multiple-choice":
        if "question" not in ex and "sentence" in ex:
            ex["question"] = ex.pop("sentence")
        for prop in ["sentence", "chips", "target", "prompt", "explanation", "english", "answer", "answers"]:
            if prop in ex:
                del ex[prop]

    # Handle fill-blank
    if ex.get("type") == "fill-blank":
        for prop in ["prompt", "chips", "target", "explanation", "english", "options", "correct", "question"]:
            if prop in ex:
                del ex[prop]
            
        sentence = ex.get("sentence", "")
        answer = ex.get("answer", "")
        
        # Check if sentence has _____
        if "____" not in sentence:
            if answer and answer in sentence:
                sentence = sentence.replace(answer, "_____", 1)
            elif "[" in sentence and "]" in sentence:
                sentence = re.sub(r'\[.*?\]', '_____', sentence)
            else:
                sentence = sentence + " _____"
            ex["sentence"] = sentence

    # Handle sentence-builder
    if ex.get("type") == "sentence-builder":
        if "prompt" in ex:
            del ex["prompt"]
        if "chips" in ex and "tiles" not in ex:
            ex["tiles"] = ex.pop("chips")
        elif "chips" in ex:
            del ex["chips"]
            
        if "target" in ex and "english" not in ex:
            ex["english"] = ex.pop("target")
        elif "target" in ex:
            del ex["target"]
            
        if "sentence" in ex:
            s_text = ex.pop("sentence")
            if "english" not in ex:
                ex["english"] = s_text
                
        if "tiles" in ex and "solution" not in ex:
            ex["solution"] = list(ex["tiles"])
            
        if "english" not in ex:
            ex["english"] = "Build the sentence in the correct order."
            
        for prop in ["explanation", "question", "options", "correct", "answer", "answers"]:
            if prop in ex:
                del ex[prop]

    # Handle matching
    if ex.get("type") == "matching":
        for prop in ["explanation", "sentence", "question", "prompt", "target", "english"]:
            if prop in ex:
                del ex[prop]

    return ex

def fix_all_exercises():
    files = glob.glob("content/hu/exercises/b1/*.json")
    print(f"Checking {len(files)} exercise files...")
    fixed_count = 0
    for fpath in files:
        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        modified = False
        if "exercises" in data:
            new_exs = []
            for ex in data["exercises"]:
                new_ex = fix_exercise_obj(ex)
                new_exs.append(new_ex)
            data["exercises"] = new_exs
            modified = True
            
        if modified:
            with open(fpath, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                f.write("\n")
            fixed_count += 1
            
    print(f"Processed {fixed_count} exercise files.")

if __name__ == '__main__':
    fix_all_exercises()
