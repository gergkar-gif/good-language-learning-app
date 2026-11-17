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
import re
import sys
from collections import defaultdict
from pathlib import Path

LEXIQUE_PATH = Path("imports/dictionary/Lexique383.tsv")
FR_DICT_PATH = Path("imports/dictionary/french-en.json")
VERBS_OUT_DIR = Path("imports/verbs/fr")
VERB_LIST_FILE = VERBS_OUT_DIR / "verb-list-fr.js"
VERB_INDEX_FILE = Path("content/fr/indexes/verb-index.json")

FR_VERB_EN_OVERRIDES = {
    "avoir": "to have", "devenir": "to become", "devoir": "must, to have to",
    "sourire": "to smile", "tendre": "to hold out, to stretch", "toucher": "to touch",
    "baiser": "to kiss", "savoir": "to know", "pouvoir": "can, to be able to",
    "vouloir": "to want", "être": "to be", "aller": "to go", "faire": "to do, to make",
    "dîner": "to dine", "déjeuner": "to have lunch", "souvenir": "to remember",
    "falloir": "to be necessary", "pleuvoir": "to rain", "valoir": "to be worth",
    "fallait": "to be necessary"
}

FR_FUTURE_STEMS = {
    "être": "ser", "avoir": "aur", "aller": "ir", "faire": "fer", "pouvoir": "pourr",
    "vouloir": "voudr", "devoir": "devr", "savoir": "saur", "venir": "viendr",
    "devenir": "deviendr", "revenir": "reviendr", "tenir": "tiendr", "voir": "verr",
    "revoir": "reverr", "prévoir": "prévoir", "envoyer": "enverr", "recevoir": "recevr",
    "apercevoir": "apercevr", "décevoir": "décevr", "courir": "courr", "mourir": "mourr",
    "acquérir": "acquerr", "valoir": "vaudr", "falloir": "faudr", "pleuvoir": "pleuvr",
    "asseoir": "assiér", "jeter": "jetter", "appeler": "appeller", "acheter": "achèter",
    "lever": "lèver", "mener": "mèner", "amener": "amèner", "emmener": "emmèner",
    "espérer": "espérer", "préférer": "préférer"
}

FR_IRREG_SUBJ = {
    "être": {"je": "sois", "tu": "sois", "il": "soit", "nous": "soyons", "vous": "soyez", "ils": "soient"},
    "avoir": {"je": "aie", "tu": "aies", "il": "ait", "nous": "ayons", "vous": "ayez", "ils": "aient"},
    "aller": {"je": "aille", "tu": "ailles", "il": "aille", "nous": "allions", "vous": "alliez", "ils": "aillent"},
    "faire": {"je": "fasse", "tu": "fasses", "il": "fasse", "nous": "fassions", "vous": "fassiez", "ils": "fassent"},
    "pouvoir": {"je": "puisse", "tu": "puisses", "il": "puisse", "nous": "puissions", "vous": "puissiez", "ils": "puissent"},
    "savoir": {"je": "sache", "tu": "saches", "il": "sache", "nous": "sachions", "vous": "sachiez", "ils": "sachent"},
    "vouloir": {"je": "veuille", "tu": "veuilles", "il": "veuille", "nous": "voulions", "vous": "vouliez", "ils": "veuillent"},
    "valoir": {"je": "vaille", "tu": "vailles", "il": "vaille", "nous": "valions", "vous": "valiez", "ils": "vaillent"},
    "falloir": {"je": "faille", "tu": "failles", "il": "faille", "nous": "faillions", "vous": "failliez", "ils": "faillent"},
    "pleuvoir": {"je": "pleuve", "tu": "pleuves", "il": "pleuve", "nous": "pleuvions", "vous": "pleuviez", "ils": "pleuvent"}
}

def clean_fr_en(lemma, fr_dict):
    if lemma in FR_VERB_EN_OVERRIDES:
        return FR_VERB_EN_OVERRIDES[lemma]
    raw = (fr_dict.get(lemma) or {}).get("en", "")
    if not raw:
        return f"to {lemma}"
    # Strip bracketed/parenthetical annotations and keep concise primary senses
    txt = re.sub(r'\[[^\]]*\]', '', raw)
    txt = re.sub(r'\([^)]*\)', '', txt)
    clauses = [c.strip(" ,;:") for c in txt.split(";") if c.strip(" ,;:")]
    picked = clauses[0] if clauses else txt.strip()
    if len(picked) > 55:
        parts = [p.strip() for p in picked.split(",") if p.strip()]
        picked = ", ".join(parts[:2])
    if picked and not picked.lower().startswith(("to ", "can", "may", "must")):
        picked = "to " + picked
    return picked or f"to {lemma}"

def _apply_ortho_e(stem):
    if stem.endswith("g"):
        return stem + "e"
    if stem.endswith("c"):
        return stem[:-1] + "ç"
    return stem

IMPERSONAL_PERSONS = {
    "falloir": ("il",),
    "pleuvoir": ("il", "ils"),
}

def complete_fr_conjugation(lemma, indicatif, subjonctif):
    pres = indicatif.setdefault("present", {})
    imp = indicatif.setdefault("imparfait", {})
    fut = indicatif.setdefault("futur_simple", {})
    cnd = indicatif.setdefault("conditionnel_present", {})
    subj = subjonctif.setdefault("present", {})

    if lemma in IMPERSONAL_PERSONS:
        allowed = set(IMPERSONAL_PERSONS[lemma])
        for td in (pres, imp, fut, cnd, subj):
            for k in list(td.keys()):
                if k not in allowed:
                    td.pop(k, None)
        fstem = FR_FUTURE_STEMS.get(lemma, fut.get("il", "")[:-1] if fut.get("il", "").endswith("a") else "")
        if fstem:
            for k in allowed:
                fut.setdefault(k, fstem + ("a" if k == "il" else "ont"))
                cnd.setdefault(k, fstem + ("ait" if k == "il" else "aient"))
        return

    if lemma == "faillir":
        # Defective verb: keep attested forms without inventing non-existent present/subjunctive forms
        return

    if lemma.endswith("faire"):
        px = lemma[:-5]
        for k, v in {"je": px + "fais", "tu": px + "fais", "il": px + "fait", "nous": px + "faisons", "vous": px + "faites", "ils": px + "font"}.items():
            pres.setdefault(k, v)
        for k, v in {"je": px + "faisais", "tu": px + "faisais", "il": px + "faisait", "nous": px + "faisions", "vous": px + "faisiez", "ils": px + "faisaient"}.items():
            imp.setdefault(k, v)
        for k, v in {"je": px + "ferai", "tu": px + "feras", "il": px + "fera", "nous": px + "ferons", "vous": px + "ferez", "ils": px + "feront"}.items():
            fut.setdefault(k, v)
        for k, v in {"je": px + "ferais", "tu": px + "ferais", "il": px + "ferait", "nous": px + "ferions", "vous": px + "feriez", "ils": px + "feraient"}.items():
            cnd.setdefault(k, v)
        for k, v in {"je": px + "fasse", "tu": px + "fasses", "il": px + "fasse", "nous": px + "fassions", "vous": px + "fassiez", "ils": px + "fassent"}.items():
            subj.setdefault(k, v)
        return

    # 1. Present tense completion (regular -er, -ir(-iss-), -re/-oir stem)
    if lemma.endswith("er") and lemma not in ("aller", "envoyer"):
        stem = lemma[:-2]
        # Infer nous stem / singular stem if boot verb already present
        sg_stem = pres.get("je")[:-1] if pres.get("je", "").endswith("e") else (stem[:-1] + "i" if stem.endswith("y") and lemma.endswith(("oyer", "uyer")) else stem)
        pl_stem = pres.get("nous")[:-3] if pres.get("nous", "").endswith("ons") else _apply_ortho_e(stem) if stem.endswith(("g", "c")) else stem
        if stem.endswith("g"):
            nous_form = stem + "eons"
        elif stem.endswith("c"):
            nous_form = stem[:-1] + "çons"
        else:
            nous_form = stem + "ons"
        reg_pres = {
            "je": sg_stem + "e",
            "tu": sg_stem + "es",
            "il": sg_stem + "e",
            "nous": pres.get("nous") or nous_form,
            "vous": stem + "ez",
            "ils": sg_stem + "ent"
        }
        for k, v in reg_pres.items():
            if not pres.get(k) or pres.get(k) == lemma:
                pres[k] = v
    elif lemma.endswith("ir") and len(pres.get("ils", "")) and pres.get("ils", "").endswith("issent"):
        rad = lemma[:-2]
        reg_pres = {"je": rad + "is", "tu": rad + "is", "il": rad + "it", "nous": rad + "issons", "vous": rad + "issez", "ils": rad + "issent"}
        for k, v in reg_pres.items():
            if not pres.get(k) or pres.get(k) == lemma:
                pres[k] = v
    else:
        # Handle missing 'nous'/'vous' in regular -re / -oir / 3rd group from attested counterpart
        if (not pres.get("nous") or pres.get("nous") == lemma) and pres.get("vous", "").endswith("ez"):
            pres["nous"] = pres["vous"][:-2] + "ons"
        if (not pres.get("vous") or pres.get("vous") == lemma) and pres.get("nous", "").endswith("ons"):
            pres["vous"] = pres["nous"][:-3] + "ez"
        elif not pres.get("vous") or pres.get("vous") == lemma:
            if lemma == "faire":
                pres["vous"] = "faites"
            elif lemma == "dire":
                pres["vous"] = "dites"
            elif lemma == "être":
                pres["vous"] = "êtes"
            elif lemma.endswith("re"):
                pres["vous"] = lemma[:-2] + "ez"
        if (not pres.get("tu") or pres.get("tu") == lemma) and pres.get("je", "").endswith(("s", "x")):
            pres["tu"] = pres["je"]
        # Fill remaining singulars for -re if needed
        if lemma.endswith("re") and not pres.get("je"):
            rad = lemma[:-2]
            for k, v in {"je": rad + "s", "tu": rad + "s", "il": rad, "nous": rad + "ons", "vous": rad + "ez", "ils": rad + "ent"}.items():
                pres.setdefault(k, v)

    # 2. Futur simple stem
    fstem = None
    if fut.get("je", "").endswith("ai") and fut.get("je") != lemma:
        fstem = fut["je"][:-2]
    elif fut.get("ils", "").endswith("ont"):
        fstem = fut["ils"][:-3]
    elif lemma in FR_FUTURE_STEMS:
        fstem = FR_FUTURE_STEMS[lemma]
    elif lemma.endswith("er"):
        fstem = lemma[:-2] + "er"
    elif lemma.endswith("ir"):
        fstem = lemma
    elif lemma.endswith("re"):
        fstem = lemma[:-1]
    elif lemma.endswith("oir"):
        fstem = lemma[:-3] + "evr"
    if fstem:
        fut_ends = {"je": "ai", "tu": "as", "il": "a", "nous": "ons", "vous": "ez", "ils": "ont"}
        for k, end in fut_ends.items():
            fut.setdefault(k, fstem + end)
        cnd_ends = {"je": "ais", "tu": "ais", "il": "ait", "nous": "ions", "vous": "iez", "ils": "aient"}
        for k, end in cnd_ends.items():
            cnd.setdefault(k, fstem + end)

    # 3. Imparfait: prefer attested imparfait stem first, then present nous stem (except être -> ét-)
    if lemma == "être":
        ist_sg = ist_pl = "ét"
    else:
        attested_imp = (
            imp.get("il", "")[:-3] if imp.get("il", "").endswith("ait") else
            imp.get("ils", "")[:-5] if imp.get("ils", "").endswith("aient") else
            imp.get("je", "")[:-3] if imp.get("je", "").endswith("ais") else
            imp.get("vous", "")[:-3] if imp.get("vous", "").endswith("iez") else ""
        )
        nous_p = pres.get("nous", "")
        raw_stem = attested_imp or (nous_p[:-3] if nous_p.endswith("ons") else (lemma[:-2] if lemma.endswith(("er", "re")) or (lemma.endswith("ir") and not lemma.endswith("oir")) else ""))
        if lemma.endswith("ger") and raw_stem.endswith("ge") and not attested_imp:
            ist_sg = raw_stem
            ist_pl = raw_stem[:-1]
        elif lemma.endswith("cer") and raw_stem.endswith("ç") and not attested_imp:
            ist_sg = raw_stem
            ist_pl = raw_stem[:-1] + "c"
        else:
            ist_sg = ist_pl = raw_stem
    if ist_sg:
        for k, end in {"je": "ais", "tu": "ais", "il": "ait", "ils": "aient"}.items():
            imp.setdefault(k, ist_sg + end)
        for k, end in {"nous": "ions", "vous": "iez"}.items():
            imp.setdefault(k, ist_pl + end)

    # 4. Subjonctif présent
    if lemma in FR_IRREG_SUBJ:
        for k, v in FR_IRREG_SUBJ[lemma].items():
            subj.setdefault(k, v)
    else:
        ils_p = pres.get("ils", "")
        nous_p = pres.get("nous", "")
        s_sg = ils_p[:-3] if ils_p.endswith("ent") else (pres.get("je", "")[:-1] if pres.get("je", "").endswith("e") else (lemma[:-2] if lemma.endswith("er") else ""))
        s_pl = nous_p[:-3] if nous_p.endswith("ons") else s_sg
        if lemma.endswith("ger") and s_pl.endswith("ge"):
            s_pl = s_pl[:-1]
        if lemma.endswith("cer") and s_pl.endswith("ç"):
            s_pl = s_pl[:-1] + "c"
        if s_sg:
            for k, end in {"je": "e", "tu": "es", "il": "e", "ils": "ent"}.items():
                subj.setdefault(k, s_sg + end)
        if s_pl:
            for k, end in {"nous": "ions", "vous": "iez"}.items():
                subj.setdefault(k, s_pl + end)

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

            if not lemme or not ortho or '-' in ortho:
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
                        if ortho == lemme and mood_tense != "inf":
                            continue
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

    fr_dict = {}
    if FR_DICT_PATH.exists():
        with open(FR_DICT_PATH, "r", encoding="utf-8") as df:
            fr_dict = json.load(df)

    print(f"Writing {len(top_verbs)} verb files into {VERBS_OUT_DIR}...")
    for lemma in top_verbs:
        vinfo = verb_data[lemma]
        pp = vinfo["participePasse"] or (lemma[:-2] + "é" if lemma.endswith("er") else lemma[:-1])
        pp_p = pp + "s" if not pp.endswith("s") else pp
        is_etre = lemma in ETRE_VERBS
        aux_pres = ETRE_AUX_PRES if is_etre else AVOIR_AUX_PRES
        aux_imp = ETRE_AUX_IMP if is_etre else AVOIR_AUX_IMP

        indicatif = {}
        for mood_tense, persons in vinfo["forms"].items():
            if mood_tense.startswith("indicatif."):
                tense_name = mood_tense.split(".")[1]
                indicatif[tense_name] = dict(persons)

        subjonctif = {}
        for mood_tense, persons in vinfo["forms"].items():
            if mood_tense.startswith("subjonctif."):
                tense_name = mood_tense.split(".")[1]
                subjonctif[tense_name] = dict(persons)

        complete_fr_conjugation(lemma, indicatif, subjonctif)

        # Synthesize compound tenses: passé composé & plus-que-parfait
        pc = {}
        pqp = {}
        allowed_pc = IMPERSONAL_PERSONS.get(lemma, ("je", "tu", "il", "nous", "vous", "ils"))
        for pers in allowed_pc:
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
                "infinitivo": clean_fr_en(lemma, fr_dict)
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

    if "--verbs-only" not in sys.argv:
        print(f"Writing {len(verb_index):,} forms to {VERB_INDEX_FILE}...")
        with open(VERB_INDEX_FILE, "w", encoding="utf-8") as f:
            json.dump(verb_index, f, ensure_ascii=False, indent=2)
    else:
        print("Skipping verb-index.json write (--verbs-only).")

    print("French verbs processing complete.")

if __name__ == "__main__":
    main()
