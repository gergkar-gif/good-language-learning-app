#!/usr/bin/env python3
"""fix_a2_goals_checklist.py

Resolves the systemic '2 goals vs 1 checklist item' issue across A2 lessons:
1. Trims Goal 2 in the 100 numbered teaching lessons, leaving Goal 1 (1:1 with Checklist 1).
2. Cleans up double-period ('..') typos in checklist items.
3. Aligns the 20 numbered consolidation lessons to 1:1.
4. Aligns the 3 named units (imperativonegativo-04, perifrasisverbales-01, pronombrescliticos-05) to 2:2.
5. Fixes the 16 non-'I can' checklist items across named units to start with 'I can'.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ES_A2 = ROOT / "content" / "es" / "lessons" / "a2"

# Specific overrides for named units and non-"I can" checklist items
NAMED_FIXES = {
    "a2-imperativonegativo-04.json": {
        "goal": [
            "Place pronouns correctly with affirmative commands (enclitic) and negative commands (preceding).",
            "Apply written accent marks when attaching pronouns increases syllable count."
        ],
        "checklist": [
            "I can place pronouns after affirmative commands (hazlo) and before negative commands (no lo hagas).",
            "I can place accent marks when attaching pronouns makes words longer (dímelo, cómetelo)."
        ]
    },
    "a2-perifrasisverbales-01.json": {
        "goal": [
            "Express when an action begins (empezar a), ends (dejar de), or repeats (volver a) using periphrases.",
            "Describe habit changes with confidence using verbal periphrases."
        ],
        "checklist": [
            "I can explain when an action begins (empezó a llover), ends (dejó de fumar), or repeats (volví a llamar).",
            "I can describe habit changes with confidence."
        ]
    },
    "a2-pronombrescliticos-05.json": {
        "goal": [
            "Attach pronouns to infinitives and gerunds, recognizing valid placements.",
            "Place written accents correctly when adding two pronouns to an infinitive or gerund."
        ],
        "checklist": [
            "I can attach pronouns to the end of infinitives and gerunds.",
            "I can place written accents correctly when adding two pronouns to an infinitive or gerund."
        ]
    },
    "a2-condicionalsimple-01.json": {
        "checklist_replaces": {
            "I know that every conditional form carries an accent mark on the 'í'.": "I can identify and write accent marks on every conditional form."
        }
    },
    "a2-educacionyestudios-03.json": {
        "checklist_replaces": {
            "I know the difference between 'aprobar' and 'suspender / reprobar'.": "I can distinguish between 'aprobar' and 'suspender / reprobar'."
        }
    },
    "a2-imperativonegativo-01.json": {
        "checklist_replaces": {
            "I know that negative commands use opposite vowel endings (-es for -ar, -as for -er/-ir).": "I can apply opposite vowel endings (-es for -ar, -as for -er/-ir) to form negative commands."
        }
    },
    "a2-imperativonegativo-03.json": {
        "checklist_replaces": {
            "I understand formal negative rules in public places.": "I can understand and follow formal negative rules in public places."
        }
    },
    "a2-imperativonegativo-consolidation.json": {
        "checklist_replaces": {
            "I understand the difference in pronoun placement between affirmative and negative commands.": "I can apply correct pronoun placement with affirmative and negative commands."
        }
    },
    "a2-perifrasisverbales-03.json": {
        "checklist_replaces": {
            "My writing flows logically with cohesive connectors.": "I can write logically and cohesively using connectors."
        }
    },
    "a2-pronombrescliticos-02.json": {
        "checklist_replaces": {
            "I know the test question for each: '¿Qué?' (direct) vs. '¿A quién?' (indirect).": "I can use the test questions '¿Qué?' (direct) and '¿A quién?' (indirect) to choose pronouns."
        }
    },
    "a2-pronombrescliticos-03.json": {
        "checklist_replaces": {
            "I know that the person comes before the thing (Indirect + Direct: me lo, te la, nos los).": "I can order object pronouns with the person before the thing (me lo, te la, nos los)."
        }
    },
    "a2-pronombrescliticos-04.json": {
        "checklist_replaces": {
            "I know that 'le lo' and 'les la' never exist in Spanish; they become 'se lo' and 'se la'.": "I can change 'le lo' and 'les la' to 'se lo' and 'se la'."
        }
    },
    "a2-pronombrescliticos-consolidation.json": {
        "checklist_replaces": {
            "I have mastered Spanish clitic pronouns across statements, questions, and commands.": "I can use Spanish clitic pronouns accurately across statements, questions, and commands."
        }
    },
    "a2-subjuntivobasico-01.json": {
        "checklist_replaces": {
            "I know that the indicative deals with facts, while the subjunctive deals with wishes and subjectivity.": "I can distinguish between facts (indicative) and wishes or subjectivity (subjunctive)."
        }
    },
    "a2-subjuntivobasico-02.json": {
        "checklist_replaces": {
            "I know when to use the infinitive (one subject) vs. the subjunctive (two subjects).": "I can choose between the infinitive (one subject) and the subjunctive (two subjects)."
        }
    },
    "a2-subjuntivobasico-04.json": {
        "checklist_replaces": {
            "I know that 'cuando' takes the subjunctive when pointing to future events.": "I can use the subjunctive with 'cuando' when referring to future events."
        }
    },
    "a2-subjuntivobasico-consolidation.json": {
        "checklist_replaces": {
            "I understand the core purpose and triggers of the Spanish subjunctive mood.": "I can understand and apply the core triggers of the Spanish subjunctive mood."
        }
    }
}


def clean_check_text(text):
    text = text.strip().rstrip(".") + "."
    if not text.startswith("I can"):
        text = "I can " + text[0].lower() + text[1:]
    return text


def process_file(fpath):
    text = fpath.read_text(encoding="utf-8")
    data = json.loads(text)
    fname = fpath.name
    changed = False

    # Check if this file has a full override in NAMED_FIXES
    if fname in NAMED_FIXES and "goal" in NAMED_FIXES[fname]:
        override = NAMED_FIXES[fname]
        for s in data.get("sections", []):
            if s.get("type") == "goal":
                s["items"] = override["goal"]
                changed = True
            elif s.get("type") == "checklist":
                s["items"] = override["checklist"]
                changed = True
    else:
        # Check if it has checklist replacements
        if fname in NAMED_FIXES and "checklist_replaces" in NAMED_FIXES[fname]:
            replaces = NAMED_FIXES[fname]["checklist_replaces"]
            for s in data.get("sections", []):
                if s.get("type") == "checklist":
                    new_items = []
                    for item in s.get("items", []):
                        if item in replaces:
                            new_items.append(replaces[item])
                            changed = True
                        else:
                            new_items.append(item)
                    s["items"] = new_items

        # Numbered files processing
        is_numbered = fname.startswith("a2-0") or fname.startswith("a2-1") or fname.startswith("a2-2")
        if is_numbered:
            goal_sec = None
            check_sec = None
            for s in data.get("sections", []):
                if s.get("type") == "goal":
                    goal_sec = s
                elif s.get("type") == "checklist":
                    check_sec = s

            if goal_sec and check_sec:
                old_goals = goal_sec.get("items", [])
                old_checks = check_sec.get("items", [])

                if "consolidation" in fname:
                    # Consolidation: 1 synthesized checklist item -> 1 matching goal item
                    if old_checks:
                        c_text = clean_check_text(old_checks[0])
                        # Derive imperative goal from 'I can ...'
                        if c_text.startswith("I can "):
                            g_text = c_text[6].upper() + c_text[7:]
                        else:
                            g_text = c_text
                        goal_sec["items"] = [g_text]
                        check_sec["items"] = [c_text]
                        changed = True
                else:
                    # Teaching lesson: keep Goal 1, trim Goal 2
                    if old_goals:
                        g_text = old_goals[0].strip().rstrip(".") + "."
                        goal_sec["items"] = [g_text]
                        if old_checks:
                            c_text = clean_check_text(old_checks[0])
                        else:
                            c_text = "I can " + g_text[0].lower() + g_text[1:]
                        check_sec["items"] = [c_text]
                        changed = True

    if changed:
        fpath.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return True
    return False


def main():
    files = sorted(ES_A2.glob("*.json"))
    modified_count = 0
    for f in files:
        if process_file(f):
            modified_count += 1
    print(f"Processed {len(files)} files. Modified: {modified_count} files.")


if __name__ == "__main__":
    main()
