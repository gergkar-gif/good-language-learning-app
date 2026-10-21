"""Spain vs Latin American vocabulary for es-es and es-latam (user, 2026-10-16).

Each course uses its own words: es-es *zumo, coche, ordenador, móvil,
patata, billete, camarero, salón*; es-latam *jugo, carro, computadora,
celular, papa, boleto, mesero, sala*. Only words that are clearly one side's
are listed; words both sides use (*conducir, chaqueta, autobús, ducha,
apartamento, sándwich, pastel*) and words whose sense decides (*piso* flat
or floor, *vale* OK or costs) are not.

Used by check-content (`course-variant`), fix_variant_vocab.py and
fix_story_metadata.py. `convert(text, course)` rewrites one string into the
course's words, fixing the article before a noun whose gender changes
(*el salón* -> *la sala*, *del ordenador* -> *de la computadora*); it
refuses (leaves the word and reports it) when a gendered word right before
or after the noun would also have to change (*la sala nueva*).
"""
import re

# (source sg, source pl, source gender, target sg, target pl, target gender)
NOUNS_TO_LATAM = [
    ("zumo", "zumos", "m", "jugo", "jugos", "m"),
    ("coche", "coches", "m", "carro", "carros", "m"),
    ("ordenador", "ordenadores", "m", "computadora", "computadoras", "f"),
    ("móvil", "móviles", "m", "celular", "celulares", "m"),
    ("patata", "patatas", "f", "papa", "papas", "f"),
    ("melocotón", "melocotones", "m", "durazno", "duraznos", "m"),
    ("judía", "judías", "f", "frijol", "frijoles", "m"),
    (None, "gafas", "f", None, "lentes", "m"),
    ("camarero", "camareros", "m", "mesero", "meseros", "m"),
    ("camarera", "camareras", "f", "mesera", "meseras", "f"),
    ("billete", "billetes", "m", "boleto", "boletos", "m"),
    ("aparcamiento", "aparcamientos", "m", "estacionamiento", "estacionamientos", "m"),
    ("nevera", "neveras", "f", "refrigerador", "refrigeradores", "m"),
    ("frigorífico", "frigoríficos", "m", "refrigerador", "refrigeradores", "m"),
    ("tarta", "tartas", "f", "pastel", "pasteles", "m"),
    ("gamba", "gambas", "f", "camarón", "camarones", "m"),
    ("salón", "salones", "m", "sala", "salas", "f"),
    ("bocadillo", "bocadillos", "m", "sándwich", "sándwiches", "m"),
]
NOUNS_TO_ES = [
    ("jugo", "jugos", "m", "zumo", "zumos", "m"),
    ("carro", "carros", "m", "coche", "coches", "m"),
    ("computadora", "computadoras", "f", "ordenador", "ordenadores", "m"),
    ("celular", "celulares", "m", "móvil", "móviles", "m"),
    ("papa", "papas", "f", "patata", "patatas", "f"),
    ("durazno", "duraznos", "m", "melocotón", "melocotones", "m"),
    ("frijol", "frijoles", "m", "judía", "judías", "f"),
    (None, "lentes", "m", None, "gafas", "f"),
    ("mesero", "meseros", "m", "camarero", "camareros", "m"),
    ("mesera", "meseras", "f", "camarera", "camareras", "f"),
    ("boleto", "boletos", "m", "billete", "billetes", "m"),
    ("estacionamiento", "estacionamientos", "m", "aparcamiento", "aparcamientos", "m"),
    ("refrigerador", "refrigeradores", "m", "nevera", "neveras", "f"),
    ("camarón", "camarones", "m", "gamba", "gambas", "f"),
    ("sala", "salas", "f", "salón", "salones", "m"),
]
VERBS_TO_LATAM = {
    "coger": "tomar", "cojo": "tomo", "coges": "tomas", "coge": "toma", "cogemos": "tomamos", "cogéis": "tomáis",
    "cogen": "toman", "cogí": "tomé", "cogiste": "tomaste", "cogió": "tomó", "cogimos": "tomamos",
    "cogieron": "tomaron", "cogía": "tomaba", "cogías": "tomabas", "cogían": "tomaban", "cogido": "tomado",
    "cogiendo": "tomando", "coja": "tome", "cojas": "tomes", "cojan": "tomen", "cogeré": "tomaré",
    "cogerá": "tomará", "cogerlo": "tomarlo", "cogerla": "tomarla", "cogerlos": "tomarlos", "cogerlas": "tomarlas",
    "aparcar": "estacionar", "aparco": "estaciono", "aparcas": "estacionas", "aparca": "estaciona",
    "aparcamos": "estacionamos", "aparcan": "estacionan", "aparqué": "estacioné", "aparcó": "estacionó",
    "aparcaron": "estacionaron", "aparcado": "estacionado", "aparcando": "estacionando", "aparque": "estacione",
    "aparquen": "estacionen", "aparcaba": "estacionaba",
}
VERBS_TO_ES = {v: k for k, v in VERBS_TO_LATAM.items() if k.startswith("aparc") or k.startswith("aparq")}
# es-es says *fuera*/*dentro* (user, 2026-10-21); es-latam keeps *afuera*/*adentro* (both are used there)
VERBS_TO_ES.update({"afuera": "fuera", "adentro": "dentro"})
# enfadar(se) / enojar(se) and their forms: a prefix swap (enfado -> enojo, enfadada -> enojada)
PREFIX = {"es-latam": ("enfad", "enoj"), "es-es": ("enoj", "enfad")}

# Context in which a listed word is the other sense, or a name: left alone.
_ROOMS = r"\s+de\s+(estar|espera|clases?|reuniones|conferencias|cine|conciertos|profesores|juntas|urgencias|operaciones|exposiciones|baile|lectura|belleza|té|actos|fiestas|eventos|juegos|la\s+fama|computación|ordenadores)\b"
_MONEY = r"\s+de\s+(\d|diez|veinte|cincuenta|cien|doscientos|quinientos|mil|dólar|peso|euro)"
KEEP_AFTER = {
    "es-latam": {"billete": _MONEY, "billetes": r"(" + _MONEY + r"|\s+y\s+monedas)",
                 "salón": _ROOMS, "salones": _ROOMS},
    "es-es": {"sala": _ROOMS, "salas": _ROOMS, "carro": r"\s+de\s+la\s+compra",
              "lentes": r"\s+de\s+contacto"},
}
# *móvil* the adjective: *banca móvil*, *aplicación móvil* (mobile banking/app) in both
KEEP_BEFORE = {"es-es": {"adentro": r"\bMar\s+$"}, "es-latam": {"móvil": r"\b(banca|aplicación|app|telefonía|unidad)\s+$",
                            "móviles": r"\b(aplicaciones|apps|unidades)\s+$"}}
DET = {"el": "la", "los": "las", "un": "una", "unos": "unas", "este": "esta", "estos": "estas", "ese": "esa",
       "esos": "esas", "aquel": "aquella", "aquellos": "aquellas", "nuestro": "nuestra", "nuestros": "nuestras",
       "vuestro": "vuestra", "vuestros": "vuestras", "otro": "otra", "otros": "otras", "mucho": "mucha",
       "muchos": "muchas", "ningún": "ninguna", "algún": "alguna", "primer": "primera", "todo": "toda", "todos": "todas"}
DET_F = {v: k for k, v in DET.items()}
# Words ending in -o/-a that are not gendered adjectives (safe next to a noun whose gender changes)
SAFE = set("a o para como cuando ahora nunca sobre contra hasta desde entre hacia pero porque mientras también "
           "tampoco muy está estaba era esta estas cerca encima debajo fuera dentro afuera arriba abajo enfrente "
           "allá acá ya nada algo poco mucho todavía siempre pronto tarde temprano luego después antes "
           "y e u en de con sin que más menos aquí ahí allí".split())
WORD = r"[\wáéíóúüñÁÉÍÓÚÜÑ]+"


def _table(course):
    nouns = NOUNS_TO_LATAM if course == "es-latam" else NOUNS_TO_ES
    forms = {}
    for s_sg, s_pl, s_g, t_sg, t_pl, t_g in nouns:
        if s_sg:
            forms[s_sg] = (t_sg, s_g, t_g, False)
        forms[s_pl] = (t_pl, s_g, t_g, True)
    for s, t in (VERBS_TO_LATAM if course == "es-latam" else VERBS_TO_ES).items():
        forms.setdefault(s, (t, None, None, False))
    return forms


def _case(src, new):
    if src.isupper() and len(src) > 1:
        return new.upper()
    return new[0].upper() + new[1:] if src[0].isupper() else new


def _sentence_start(text, i):
    j = i - 1
    while j >= 0 and text[j] in " \t\n\"'«“*(¡¿-—":
        j -= 1
    return j < 0 or text[j] in ".!?:;/"


def convert(text, course):
    """(new text, [(old, new)], [refused words]) for one string."""
    if course not in ("es-es", "es-latam") or not isinstance(text, str):
        return text, [], []
    forms = _table(course)
    pre_from, pre_to = PREFIX[course]
    pattern = re.compile(r"(?<![\wáéíóúüñ])(" + "|".join(sorted(map(re.escape, forms), key=len, reverse=True))
                         + "|" + pre_from + WORD[:-1] + "*)(?![\\wáéíóúüñ])", re.I)
    out, changes, refused, last = [], [], [], 0
    for m in pattern.finditer(text):
        word, low = m.group(1), m.group(1).lower()
        if low.startswith(pre_from) and low not in forms:
            new_word, g_from, g_to = pre_to + low[len(pre_from):], None, None
        elif low in forms:
            new_word, g_from, g_to, _pl = forms[low]
        else:
            continue
        if word[0].isupper() and not _sentence_start(text, m.start()):
            continue  # a name (*Salón de la Fama*, *el Papa*)
        keep = KEEP_AFTER.get(course, {}).get(low)
        if keep and re.match(keep, text[m.end():], re.I):
            continue
        keep = KEEP_BEFORE.get(course, {}).get(low)
        if keep and re.search(keep, text[:m.start()], re.I):
            continue
        start, prefix_new = m.start(), None
        if g_from and g_to and g_from != g_to:
            before = text[last:m.start()]
            pm = re.search(r"(?:(?<![\wáéíóúüñ])(" + WORD + r")\s+)?(?<![\wáéíóúüñ])(" + WORD + r")\s+$", before)
            nm = re.match(r"\s+(?:(?:más|muy|tan|bien|tan)\s+)?(" + WORD + r")", text[m.end():], re.I)
            prev = pm.group(2) if pm else ""
            plow = prev.lower()
            if nm and re.search(r"(o|a|os|as|or|ora|ores|oras|és|esa|ón|ona)$", nm.group(1).lower()) and nm.group(1).lower() not in SAFE:
                refused.append(f"{word} (followed by {nm.group(1)})")
                continue
            to_f = g_to == "f"
            if plow in ("del", "al") and to_f:
                prefix_new = ("de la " if plow == "del" else "a la ")
            elif plow == "la" and pm.group(1) and pm.group(1).lower() in ("de", "a") and not to_f:
                prefix_new = "del " if pm.group(1).lower() == "de" else "al "
                start = last + pm.start(1)
                prev = pm.group(1) + " " + prev
            elif to_f and plow in DET:
                prefix_new = DET[plow] + " "
            elif not to_f and plow in DET_F:
                prefix_new = DET_F[plow] + " "
            elif plow and re.search(r"(o|a|os|as)$", plow) and plow not in SAFE and plow not in (
                    "mi", "mis", "tu", "tus", "su", "sus", "la", "las", "una", "unas"):
                refused.append(f"{word} (after {prev})")
                continue
            if prefix_new is not None:
                if start == m.start():
                    start = last + pm.start(2)
                prefix_new = _case(prev, prefix_new)
                # *Esta es la sala* -> *Este es el salón*: the pronoun before *es* agrees too
                dm = re.search(r"(?<![\wáéíóúüñ])(esta|este|esa|ese|aquella|aquel)(\s+es\s+)$", text[last:start], re.I)
                if dm:
                    pron = dm.group(1)
                    flip = DET.get(pron.lower()) if to_f else DET_F.get(pron.lower())
                    if flip:
                        prefix_new = _case(pron, flip) + dm.group(2) + prefix_new
                        start = last + dm.start(1)
        out.append(text[last:start])
        new = (prefix_new or "") + _case(word, new_word)
        old = text[start:m.end()]
        out.append(new)
        changes.append((old, new))
        last = m.end()
    out.append(text[last:])
    return "".join(out), changes, refused


def to_course(text, course):
    return convert(text, course)[0]


def find(text, course):
    """The other side's words in one string: changed or refused by convert()."""
    _, changes, refused = convert(text, course)
    return [o for o, _ in changes] + refused


def convert_data(node, course, skip=("id", "unitIds", "targetSkills", "cefrLevel", "interlocutorVoice")):
    """A JSON value with every string put in the course's words (keys in `skip` kept)."""
    if isinstance(node, str):
        return to_course(node, course)
    if isinstance(node, list):
        return [convert_data(v, course, skip) for v in node]
    if isinstance(node, dict):
        return {k: (v if k in skip else convert_data(v, course, skip)) for k, v in node.items()}
    return node


def latam_voice(node):
    """es-ES TTS voices -> es-MX for es-latam (scenarios set to es-AR, es-CO … keep theirs)."""
    if isinstance(node, list):
        return [latam_voice(v) for v in node]
    if isinstance(node, dict):
        return {k: ("es-MX" if k == "interlocutorVoice" and v == "es-ES" else latam_voice(v)) for k, v in node.items()}
    return node
