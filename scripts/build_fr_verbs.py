#!/usr/bin/env python3
"""
Build French verb library and reverse verb index from Lexique 383.

Outputs:
  imports/verbs/fr/<lemma>.json     (Conjugation tables for top verbs)
  imports/verbs/fr/verb-list-fr.js  (ALL_FRENCH_VERBS list)
  content/fr/indexes/verb-index.json (Reverse conjugation index for tap-to-lemma)
"""
import csv
import json
import os
from collections import defaultdict
from pathlib import Path

LEXIQUE_PATH = Path("imports/dictionary/Lexique383.tsv")
VERBS_OUT_DIR = Path("imports/verbs/fr")
VERB_LIST_FILE = VERBS_OUT_DIR / "verb-list-fr.js"
VERB_INDEX_FILE = Path("content/fr/indexes/verb-index.json")

# Verbs that take être as auxiliary in compound tenses
ETRE_VERBS = {
    "devenir", "revenir", "monter", "rester", "sortir", "venir", "aller",
    "naître", "naitre", "descendre", "entrer", "rentrer", "tomber", "retourner",
    "arriver", "mourir", "partir"
}

ETRE_AUX_PRES = {
    "je": "suis", "tu": "es", "il": "est", "nous": "sommes", "vous": "êtes", "ils": "sont"
}
AVOIR_AUX_PRES = {
    "je": "ai", "tu": "as", "il": "a", "nous": "avons", "vous": "avez", "ils": "ont"
}

ETRE_AUX_IMP = {
    "je": "étais", "tu": "étais", "il": "était", "nous": "étions", "vous": "étiez", "ils": "étaient"
}
AVOIR_AUX_IMP = {
    "je": "avais", "tu": "avais", "il": "avait", "nous": "avions", "vous": "aviez", "ils": "avaient"
}

PERSON_MAP = {
    "1s": "je",
    "2s": "tu",
    "3s": "il",
    "1p": "nous",
    "2p": "vous",
    "3p": "ils"
}

TENSE_MAP = {
    "ind:pre": ("indicatif", "present"),
    "ind:imp": ("indicatif", "imparfait"),
    "ind:fut": ("indicatif", "futur_simple"),
    "cnd:pre": ("indicatif", "conditionnel_present"),
    "sub:pre": ("subjonctif", "present"),
    "ind:pas": ("indicatif", "passe_simple")
}

def main():
    if not LEXIQUE_PATH.exists():
        print(f"Error: {LEXIQUE_PATH} does not exist. Run import_fr_lexique.py first.")
        return

    VERBS_OUT_DIR.mkdir(parents=True, exist_ok=True)
    VERB_INDEX_FILE.parent.mkdir(parents=True, exist_ok=True)

    print("Extracting French verbs from Lexique 383...")
    verb_data = defaultdict(lambda: {
        "forms": defaultdict(dict),
        "participePasse": None,
        "participePresent": None,
        "freq": 0.0
    })
    verb_index = defaultdict(list)

    with open(LEXIQUE_PATH, "r", encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            cgram = (row.get("cgram") or "").strip()
            if cgram not in ("VER", "AUX"):
                continue

            ortho = (row.get("ortho") or "").strip().lower()
            lemme = (row.get("lemme") or "").strip().lower()
            infover = (row.get("infover") or "").strip()
            freq_films = float(row.get("freqfilms2") or row.get("freqfilms") or 0.0)
            freq_livres = float(row.get("freqlivres") or 0.0)

            if not lemme or not ortho:
                continue

            verb_data[lemme]["freq"] = max(verb_data[lemme]["freq"], freq_films + freq_livres)

            # Parse infover tags (e.g. ind:pre:1s;ind:pre:3s; or par:pas;)
            tags = [t.strip() for t in infover.split(";") if t.strip()]
            for tag in tags:
                parts = tag.split(":")
                if len(parts) == 3:
                    mood_tense = f"{parts[0]}:{parts[1]}"
                    pers_num = parts[2]
                    person = PERSON_MAP.get(pers_num)
                    tense_info = TENSE_MAP.get(mood_tense)

                    if tense_info and person:
                        mood, tense = tense_info
                        if person not in verb_data[lemme]["forms"][f"{mood}.{tense}"]:
                            verb_data[lemme]["forms"][f"{mood}.{tense}"][person] = ortho

                        # Record in reverse verb_index
                        mood_name = "indicative" if mood == "indicatif" else "subjunctive"
                        p_num = int(pers_num[0])
                        num_str = "singular" if pers_num[1] == "s" else "plural"
                        verb_index_entry = {
                            "lemma": lemme,
                            "mood": mood_name,
                            "tense": tense,
                            "person": p_num,
                            "number": num_str
                        }
                        if verb_index_entry not in verb_index[ortho]:
                            verb_index[ortho].append(verb_index_entry)

                elif len(parts) == 2:
                    if tag == "par:pas":
                        if not verb_data[lemme]["participePasse"]:
                            verb_data[lemme]["participePasse"] = ortho
                        verb_index[ortho].append({
                            "lemma": lemme,
                            "mood": "participle",
                            "form": "participle"
                        })
                    elif tag == "par:pre":
                        if not verb_data[lemme]["participePresent"]:
                            verb_data[lemme]["participePresent"] = ortho
                        verb_index[ortho].append({
                            "lemma": lemme,
                            "mood": "gerund",
                            "form": "gerund"
                        })

    print(f"Total verb lemmas found: {len(verb_data):,}")
    print(f"Total inflected verb surface forms: {len(verb_index):,}")

    # Rank verbs by frequency
    sorted_verbs = sorted(verb_data.items(), key=lambda x: -x[1]["freq"])
    top_verbs = [v[0] for v in sorted_verbs if v[0] and len(v[1]["forms"]) > 0][:400]

    # Ensure key essential verbs are included
    ESSENTIALS = [
        "être", "avoir", "aller", "faire", "pouvoir", "vouloir", "devoir", "savoir",
        "venir", "voir", "prendre", "parler", "aimer", "finir", "mettre", "dire",
        "attendre", "partir", "sortir", "croire", "boire", "écrire", "lire", "dormir",
        "vivre", "connaître", "comprendre", "donner", "trouver", "demander", "passer",
        "rester", "porter", "entendre", "regarder", "suivre", "rendre", "arriver",
        "montrer", "tomber", "choisir", "répondre", "penser", "ouvrir", "fermer"
    ]
    for ess in ESSENTIALS:
        if ess in verb_data and ess not in top_verbs:
            top_verbs.append(ess)

    print(f"Writing {len(top_verbs)} verb files into {VERBS_OUT_DIR}...")
    for lemma in top_verbs:
        vinfo = verb_data[lemma]
        pp = vinfo["participePasse"] or (lemma[:-2] + "é" if lemma.endswith("er") else lemma[:-1])
        pp_p = pp + "s"
        is_etre = lemma in ETRE_VERBS
        aux_pres = ETRE_AUX_PRES if is_etre else AVOIR_AUX_PRES
        aux_imp = ETRE_AUX_IMP if is_etre else AVOIR_AUX_IMP

        indicatif = {}
        for mood_tense, persons in vinfo["forms"].items():
            if mood_tense.startswith("indicatif."):
                tense_name = mood_tense.split(".")[1]
                indicatif[tense_name] = persons

        subjonctif = {}
        for mood_tense, persons in vinfo["forms"].items():
            if mood_tense.startswith("subjonctif."):
                tense_name = mood_tense.split(".")[1]
                subjonctif[tense_name] = persons

        # Synthesize compound tenses: passé composé & plus-que-parfait
        pc = {}
        pqp = {}
        for pers in ["je", "tu", "il", "nous", "vous", "ils"]:
            part = pp_p if (is_etre and pers in ("nous", "vous", "ils")) else pp
            pc[pers] = f"{aux_pres[pers]} {part}"
            pqp[pers] = f"{aux_imp[pers]} {part}"

        indicatif["passe_compose"] = pc
        indicatif["plus_que_parfait"] = pqp

        verb_obj = {
            "regular": lemma.endswith("er") and lemma not in ("aller", "envoyer"),
            "infinitivo": lemma,
            "infinitive": lemma,
            "participePresent": vinfo["participePresent"] or (lemma[:-2] + "ant" if lemma.endswith("er") else ""),
            "participePasado": pp,
            "participePasse": pp,
            "auxiliaire": "être" if is_etre else "avoir",
            "english": {
                "infinitivo": f"to {lemma}"
            },
            "indicatif": indicatif,
            "subjonctif": subjonctif
        }

        # Safe filename
        safe_name = lemma.replace("ê", "e").replace("é", "e").replace("è", "e").replace("î", "i").replace("ï", "i").replace("ô", "o").replace("û", "u").replace("ç", "c")
        with open(VERBS_OUT_DIR / f"{safe_name}.json", "w", encoding="utf-8") as vf:
            json.dump(verb_obj, vf, ensure_ascii=False, indent=2)
        if safe_name != lemma:
            with open(VERBS_OUT_DIR / f"{lemma}.json", "w", encoding="utf-8") as vf:
                json.dump(verb_obj, vf, ensure_ascii=False, indent=2)

    # Write verb-list-fr.js
    safe_top_verbs = sorted(list(set(
        lemma.replace("ê", "e").replace("é", "e").replace("è", "e").replace("î", "i").replace("ï", "i").replace("ô", "o").replace("û", "u").replace("ç", "c")
        for lemma in top_verbs
    )))
    with open(VERB_LIST_FILE, "w", encoding="utf-8") as f:
        f.write("const ALL_FRENCH_VERBS = " + json.dumps(safe_top_verbs, ensure_ascii=False) + ";\n")
    print(f"Wrote {len(safe_top_verbs)} verbs to {VERB_LIST_FILE}")

    # Write verb-index.json
    print(f"Writing {len(verb_index):,} forms to {VERB_INDEX_FILE}...")
    with open(VERB_INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(verb_index, f, ensure_ascii=False, indent=2)

    print("French verbs processing complete.")

if __name__ == "__main__":
    main()
