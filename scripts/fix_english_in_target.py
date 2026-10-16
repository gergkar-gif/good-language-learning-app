"""Write a fix list for check-content's `english-in-target` (user, 2026-10-16).

Spanish A1–A2 exercises put English inside target-language lines, which the
TTS reads in the Spanish voice and which the Hungarian course never does:

- an instruction before a colon on a fill-blank ("Complete the greeting:
  Buenos ___."): removed; `english` already pins the answer;
- a scene line before " / " on a fill-blank ("Two colleagues are talking
  about … / Marta: …"): removed from `sentence`; `english` keeps it;
- a bracketed stage direction in a dialogue line ("¿Quién es ella? (Meg
  answers about her own sister.)"): moved to the exercise's `hint`, which
  lessons show after the question (fill-blank, dialogue-complete).

It refuses rather than guesses: an item it can't fix by these rules (the
sentence would be a bare blank, an item without `english`, a `hint`
already set where a direction would go, English in another shape) goes to
<out>.byhand.json with the reason. Nothing is written to content.

    python scripts/fix_english_in_target.py <course> <level> <out.json>
    python scripts/apply_replacements.py <out.json>
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("check_content", ROOT / "scripts/check-content.py")
cc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cc)


def main():
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    course, level, out = sys.argv[1], sys.argv[2], Path(sys.argv[3])
    fixes, byhand = [], []
    for f in sorted((ROOT / f"content/{course}/exercises/{level}").glob("*-ex.json")):
        rel = f.relative_to(ROOT).as_posix()
        for e in json.loads(f.read_text(encoding="utf-8")).get("exercises", []):
            sets, why = {}, None
            s = e.get("sentence")
            if isinstance(s, str):
                segs = re.split(r"\s+/\s+", s)
                m = re.match(r"^([^:/()]{2,80}):\s+(\S.*)$", s, re.S)
                if m and cc.english_text(m.group(1)):
                    rest = m.group(2)
                    if not re.sub(r"[_\W]", "", rest):
                        why = "the sentence would be a bare blank"
                    else:
                        sets["sentence"] = rest
                elif len(segs) > 1 and cc.english_text(segs[0]) and not any(cc.english_text(x) for x in segs[1:]):
                    sets["sentence"] = " / ".join(segs[1:])
                elif any(cc.english_text(b) for b in re.findall(r"\(([^)]*)\)", s)):
                    why = "a bracketed direction inside a sentence"
                if sets and not e.get("english"):
                    why, sets = "no `english` to carry the meaning", {}
            prompt = e.get("prompt")
            if isinstance(prompt, list):
                new_prompt, dirs = [], []
                for line in prompt:
                    text = line.get("text") if isinstance(line, dict) else None
                    if isinstance(text, str):
                        found = [b for b in re.findall(r"\(([^)]*)\)", text) if cc.english_text(b)]
                        for b in found:
                            text = text.replace(f"({b})", "")
                        dirs += found
                        line = {**line, "text": re.sub(r"\s{2,}", " ", text).strip()}
                    new_prompt.append(line)
                if dirs:
                    if e.get("hint"):
                        why = "a direction to move but `hint` is already set"
                    elif len(dirs) > 1:
                        why = "more than one direction"
                    else:
                        sets["prompt"] = new_prompt
                        sets["hint"] = dirs[0].strip().rstrip(".")
            if why:
                byhand.append({"file": rel, "id": e.get("id"), "why": why})
            elif sets:
                fixes.append({"file": rel, "id": e["id"], "set": sets, "why": "english-in-target"})
    out.write_text(json.dumps(fixes, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    bh = out.with_suffix(".byhand.json")
    bh.write_text(json.dumps(byhand, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(fixes)} fixes in {out}, {len(byhand)} by hand in {bh}")
    for x in byhand:
        print(f"  by hand: {x['id']}  ({x['why']})")


if __name__ == "__main__":
    main()
