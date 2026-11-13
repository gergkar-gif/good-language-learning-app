"""People named in challenges, against the course's character bible (ES B2, 2026-11-13).

Two batches of B2 challenges made Ana, Carlos's sister in the B1 stories, a work
colleague, and others brought in people the stories never have ("Pablo"). This
finds both, for check-content.py (suspects) and on its own:

    python scripts/challenge_people.py <course> [level]

- character-role: a family member of the bible (Ana, Andreas, Kaylee, Lauren) in
  the same sentence as a role the bible does not give them (colleague, classmate,
  boss, neighbour, client, teacher, friend).
- character-extra: a common first name that is not in the bible. A name inside a
  story the learner continues ("continue a short story: Luis is waiting…") is
  allowed: say so with --accept when freezing.
Spanish courses read content/es-latam/characters/characters.md (es-es tells the same
story). Other courses have no bible yet: nothing is checked.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROLES = r"colleague|co-?worker|classmate|boss|manager|neighbou?r|client|customer|teacher|friend|compañer[oa]|jef[ea]|vecin[oa]|amig[oa]|profesor[a]?"
COMMON = set("""Pablo Luis Marta Tomás Mariana Juan Pedro Sofía Laura José María Elena Javier Miguel Carmen Lucas
Diego Andrés Alejandro Gabriela Valentina Camila Isabel Fernanda Ricardo Jorge Antonio Manuel Rosa Paula Sara
Clara Julia Raúl Sergio Daniel David Carla Lucía Daniela Ana Andreas Kaylee Lauren Peter John Mary Anna""".split())
BIBLE_FILE = {"es-es": "content/es-latam/characters/characters.md", "es-latam": "content/es-latam/characters/characters.md"}


def bible(course):
    p = BIBLE_FILE.get(course)
    if not p or not (ROOT / p).is_file():
        return None
    t = (ROOT / p).read_text(encoding="utf-8")
    names = re.findall(r"^## (\S+)", t, re.M)
    family = {n for n in names if n not in ("Carlos", "Meg")}
    # people the stories name without a section of their own (rulebook § 6c)
    extra = {"Daniela", "Lucía"}
    return set(names) | extra, family


def unit_story_text(course, stem):
    """Text of every story on the lessons of the unit that has `stem`: a name the
    learner meets there (doña Rosa, Luis de Vargas) is a story character, not an extra."""
    for lvl_file in sorted((ROOT / f"content/{course}/curriculum/units").glob("*.json")):
        for u in json.loads(lvl_file.read_text(encoding="utf-8")):
            if stem in u.get("stems", []):
                out = []
                for s in u["stems"]:
                    lp = ROOT / f"content/{course}/lessons/{lvl_file.stem}/{s}.json"
                    if not lp.is_file():
                        continue
                    for sec in json.loads(lp.read_text(encoding="utf-8")).get("sections", []):
                        if sec.get("type") == "story" and sec.get("ref"):
                            sp = ROOT / f"content/{course}/{sec['ref']}"
                            if sp.is_file():
                                out.append(sp.read_text(encoding="utf-8"))
                return " ".join(out)
    return ""


def findings(course, entries):
    """entries: {stem: challenge dict} -> [(check, id, msg)]"""
    b = bible(course)
    if not b:
        return []
    known, family = b
    out = []
    for stem, c in entries.items():
        if not isinstance(c, dict):
            continue
        cid = f"{stem}:challenge"
        text = " ".join(str(c.get(k, "")) for k in ("scenario", "prompt", "target", "english"))
        text += " " + " ".join(map(str, c.get("cues") or []))
        for n in family:
            # the role must be the name's own: "your colleague Ana", "Ana, a classmate"
            near = rf"\b(?:{ROLES})\s+{n}\b|\b{n},?\s+(?:your|my|a|his|her|tu|mi|una?)\s+(?:{ROLES})\b"
            m = re.search(near, text, re.I)
            if m:
                out.append(("character-role", cid, f"{n} is family in the stories, here: {m.group(0)}"))
        # a first name followed by a surname is a real person (an author): not a character
        names = {m.group(1) for m in re.finditer(r"\b([A-ZÁÉÍÓÚ][a-záéíóúñ]+)\b(?!\s+(?:de\s+|del\s+)?[A-ZÁÉÍÓÚ])", text)}
        story = unit_story_text(course, stem) if any(w in COMMON and w not in known for w in names) else ""
        for n in sorted(w for w in names if w in COMMON and w not in known and not re.search(rf"\b{w}\b", story)):
            out.append(("character-extra", cid, f"{n} is not a course character"))
    return list(dict.fromkeys(out))


def main():
    course = sys.argv[1]
    level = sys.argv[2].lower() if len(sys.argv) > 2 else None
    ch = json.loads((ROOT / f"content/{course}/curriculum/challenges.json").read_text(encoding="utf-8"))
    entries = {k: v for k, v in (ch.get("challenges", ch)).items() if not level or k.startswith(level + "-")}
    f = findings(course, entries)
    for x in f:
        print(*x, sep="  ")
    print(f"{len(f)} finding(s)", file=sys.stderr)


if __name__ == "__main__":
    main()
