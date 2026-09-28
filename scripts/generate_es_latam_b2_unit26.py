"""Generate Latin American Spanish (es-latam) B2 Unit 26:
Core Unit 26: b2-26 (Modal Periphrases of Conjecture & Duty)
Regional Unit 26: b2-argentinasociedad (Argentina III: Politics, Passion, Peronism & The Human Rights Movement)
Classic Literature: Ernesto Sabato - El túnel: La obsesión, el juicio y la soledad en el laberinto interior (1948)
"""

import json
import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LATAM_DIR = os.path.join(BASE_DIR, "content", "es-latam")

def count_words(story_obj):
    paras = story_obj.get("paragraphs", [])
    text = " ".join(p if isinstance(p, str) else p.get("text", "") for p in paras)
    words = re.findall(r"\b[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ'-]+\b", text)
    return len(words)

def update_json_file(filepath, updater_fn):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    data = updater_fn(data)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

def write_json(rel_path, data):
    full_path = os.path.join(LATAM_DIR, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Wrote {os.path.relpath(full_path, BASE_DIR)}")

def main():
    # 1. Update skill-registry.json
    def update_skill_registry(registry):
        skills = registry.setdefault("skills", {})
        new_skills = {
            "perifrasis-deber-obligacion-conjetura": {
                "kind": "grammar",
                "name": "perifrasis-deber-obligacion-conjetura",
                "description": "Modal distinction between deber + inf (moral or deontic duty) and deber de + inf (epistemic probability or conjecture)",
                "aliases": []
            },
            "perifrasis-haber-de-infinitivo": {
                "kind": "grammar",
                "name": "perifrasis-haber-de-infinitivo",
                "description": "Formal modal periphrasis haber de + inf expressing scheduled necessity, moral duty, or inevitable destiny",
                "aliases": []
            },
            "perifrasis-tener-que-infinitivo": {
                "kind": "grammar",
                "name": "perifrasis-tener-que-infinitivo",
                "description": "Objective modal obligation and external necessity with tener que + inf across past and conditional frames",
                "aliases": []
            },
            "perifrasis-haber-que-impersonal": {
                "kind": "grammar",
                "name": "perifrasis-haber-que-impersonal",
                "description": "Impersonal generalized obligation with haber que + inf in institutional, civic, and collective contexts",
                "aliases": []
            },
            "perifrasis-modales-probabilidad-epistemica": {
                "kind": "grammar",
                "name": "perifrasis-modales-probabilidad-epistemica",
                "description": "Calibrating epistemic probability, deduction, and certainty using complex modal periphrases",
                "aliases": []
            },
            "b2-26-vocab": {
                "kind": "vocabulary",
                "name": "b2-26-vocab",
                "description": "Vocabulary for modal periphrases, obligation, probability, epistemic conjecture, and existential reasoning",
                "aliases": []
            },
            "conectores-contraargumentativos-debate": {
                "kind": "grammar",
                "name": "conectores-contraargumentativos-debate",
                "description": "Counter-argumentative discourse connectors in political, sociological, and ideological debate",
                "aliases": []
            },
            "voz-pasiva-perifrastica-denuncia": {
                "kind": "grammar",
                "name": "voz-pasiva-perifrastica-denuncia",
                "description": "Periphrastic and reflexive passive constructions in historical truth commissions and legal documentation",
                "aliases": []
            },
            "subjuntivo-oraciones-relativas-memoria": {
                "kind": "grammar",
                "name": "subjuntivo-oraciones-relativas-memoria",
                "description": "Subjunctive in relative clauses with negative or indefinite antecedents in human rights and memory discourse",
                "aliases": []
            },
            "estructuras-ponderativas-pasion-popular": {
                "kind": "grammar",
                "name": "estructuras-ponderativas-pasion-popular",
                "description": "Intensifying and ponderative syntactic structures expressing collective passions and cultural idolatry",
                "aliases": []
            },
            "oraciones-causales-explicativas-crisis": {
                "kind": "grammar",
                "name": "oraciones-causales-explicativas-crisis",
                "description": "Complex causal and explanatory clauses linking economic factors, social mobilization, and collective resilience",
                "aliases": []
            },
            "b2-argentinasociedad-vocab": {
                "kind": "vocabulary",
                "name": "b2-argentinasociedad-vocab",
                "description": "Vocabulary for Argentine political history, Peronism, human rights, civic passions, and economic sociology",
                "aliases": []
            }
        }
        for k, v in new_skills.items():
            if k not in skills:
                skills[k] = v
        return registry

    update_json_file(os.path.join(LATAM_DIR, "indexes", "skill-registry.json"), update_skill_registry)
    print("Updated skill-registry.json for Unit 26")

    # 2. Update grammar-titles.json (all lowercase words, <= 11 words, plain CEFR English, fits after 'We recommend practicing ')
    def update_grammar_titles(titles):
        new_titles = {
            "perifrasis-deber-obligacion-conjetura": "modal distinction between deber and deber de plus infinitive",
            "perifrasis-haber-de-infinitivo": "formal modal periphrasis haber de plus infinitive",
            "perifrasis-tener-que-infinitivo": "objective obligation with tener que plus infinitive",
            "perifrasis-haber-que-impersonal": "impersonal obligation with haber que plus infinitive",
            "perifrasis-modales-probabilidad-epistemica": "epistemic probability and conjecture with modal periphrases",
            "conectores-contraargumentativos-debate": "counter argumentative connectors in socio political debate",
            "voz-pasiva-perifrastica-denuncia": "passive structures in institutional and judicial documentation",
            "subjuntivo-oraciones-relativas-memoria": "the subjunctive in relative clauses of historical identification",
            "estructuras-ponderativas-pasion-popular": "ponderative and superlative structures in cultural discourse",
            "oraciones-causales-explicativas-crisis": "complex causal and explanatory clauses in economic analysis"
        }
        for k, v in new_titles.items():
            titles[k] = v
        return titles

    update_json_file(os.path.join(LATAM_DIR, "indexes", "grammar-titles.json"), update_grammar_titles)
    print("Updated grammar-titles.json for Unit 26")

    # 3. Vocabulary Files (10 files)
    vocab_data = {
        "b2-26-01": {
            "id": "vocab.b2.26.01",
            "lesson": "b2-26-01",
            "title": "Modal Periphrasis: Deber vs. Deber de",
            "words": [
                {"lemma": "deber", "translation": "duty / moral obligation", "pos": "noun"},
                {"lemma": "conjetura", "translation": "conjecture / theoretical surmise", "pos": "noun"},
                {"lemma": "obligatoriedad", "translation": "mandatory nature / compulsoriness", "pos": "noun"},
                {"lemma": "suposición", "translation": "supposition / assumption", "pos": "noun"},
                {"lemma": "certeza", "translation": "certainty", "pos": "noun"},
                {"lemma": "probabilidad", "translation": "probability / likelihood", "pos": "noun"},
                {"lemma": "presunción", "translation": "presumption / deduction", "pos": "noun"},
                {"lemma": "rigor", "translation": "rigor / strictness", "pos": "noun"},
                {"lemma": "imposición", "translation": "imposition / requirement", "pos": "noun"},
                {"lemma": "indicio", "translation": "clue / sign / indication", "pos": "noun"}
            ]
        },
        "b2-26-02": {
            "id": "vocab.b2.26.02",
            "lesson": "b2-26-02",
            "title": "Formal Necessity: Haber de + Infinitivo",
            "words": [
                {"lemma": "destino", "translation": "destiny / fate", "pos": "noun"},
                {"lemma": "inexorabilidad", "translation": "inexorability / unavoidability", "pos": "noun"},
                {"lemma": "precepto", "translation": "precept / statutory rule", "pos": "noun"},
                {"lemma": "designio", "translation": "design / grand plan", "pos": "noun"},
                {"lemma": "mandato", "translation": "mandate / command", "pos": "noun"},
                {"lemma": "ineludible", "translation": "unavoidable / inescapable", "pos": "adjective"},
                {"lemma": "devenir", "translation": "future course / unfolding", "pos": "noun"},
                {"lemma": "estipulación", "translation": "stipulation", "pos": "noun"},
                {"lemma": "designación", "translation": "designation / assignment", "pos": "noun"},
                {"lemma": "vínculo", "translation": "bond / binding tie", "pos": "noun"}
            ]
        },
        "b2-26-03": {
            "id": "vocab.b2.26.03",
            "lesson": "b2-26-03",
            "title": "Objective Necessity: Tener que + Infinitivo",
            "words": [
                {"lemma": "urgencia", "translation": "urgency / pressing need", "pos": "noun"},
                {"lemma": "apremio", "translation": "urgency / pressure", "pos": "noun"},
                {"lemma": "coacción", "translation": "coercion / duress", "pos": "noun"},
                {"lemma": "imperativo", "translation": "imperative / compelling duty", "pos": "noun"},
                {"lemma": "contingencia", "translation": "contingency / eventuality", "pos": "noun"},
                {"lemma": "constricción", "translation": "constraint / restriction", "pos": "noun"},
                {"lemma": "inevitabilidad", "translation": "inevitability", "pos": "noun"},
                {"lemma": "requerimiento", "translation": "requirement / demand", "pos": "noun"},
                {"lemma": "obligado", "translation": "compelled / obliged", "pos": "adjective"},
                {"lemma": "forzoso", "translation": "forced / inevitable", "pos": "adjective"}
            ]
        },
        "b2-26-04": {
            "id": "vocab.b2.26.04",
            "lesson": "b2-26-04",
            "title": "Impersonal Obligation: Haber que + Infinitivo",
            "words": [
                {"lemma": "menester", "translation": "necessity / necessary task", "pos": "noun"},
                {"lemma": "precisión", "translation": "need / necessity / precision", "pos": "noun"},
                {"lemma": "colectividad", "translation": "collectivity / community", "pos": "noun"},
                {"lemma": "prioridad", "translation": "priority", "pos": "noun"},
                {"lemma": "consenso", "translation": "consensus", "pos": "noun"},
                {"lemma": "recaudo", "translation": "precaution / safeguard", "pos": "noun"},
                {"lemma": "diligencia", "translation": "diligence / procedural step", "pos": "noun"},
                {"lemma": "prudencia", "translation": "prudence / caution", "pos": "noun"},
                {"lemma": "remedio", "translation": "remedy / solution", "pos": "noun"},
                {"lemma": "disposición", "translation": "disposition / readiness", "pos": "noun"}
            ]
        },
        "b2-26-05": {
            "id": "vocab.b2.26.05",
            "lesson": "b2-26-05",
            "title": "Epistemic Conjecture & Probability",
            "words": [
                {"lemma": "deducción", "translation": "deduction / inference", "pos": "noun"},
                {"lemma": "inferencia", "translation": "inference", "pos": "noun"},
                {"lemma": "plausibilidad", "translation": "plausibility", "pos": "noun"},
                {"lemma": "verosimilitud", "translation": "verisimilitude / credibility", "pos": "noun"},
                {"lemma": "incertidumbre", "translation": "uncertainty", "pos": "noun"},
                {"lemma": "escepticismo", "translation": "skepticism", "pos": "noun"},
                {"lemma": "sospecha", "translation": "suspicion / hunch", "pos": "noun"},
                {"lemma": "postulado", "translation": "postulate / premise", "pos": "noun"},
                {"lemma": "presunción", "translation": "presumption", "pos": "noun"},
                {"lemma": "hipótesis", "translation": "hypothesis", "pos": "noun"}
            ]
        },
        "b2-argentinasociedad-01": {
            "id": "vocab.b2.argentinasociedad.01",
            "lesson": "b2-argentinasociedad-01",
            "title": "Peronism: Mass Mobilization & Social Justice",
            "words": [
                {"lemma": "justicialismo", "translation": "Justicialism / Peronist doctrine", "pos": "noun"},
                {"lemma": "sindicalismo", "translation": "trade unionism", "pos": "noun"},
                {"lemma": "descamisado", "translation": "working-class follower of Evita and Perón", "pos": "noun"},
                {"lemma": "polarización", "translation": "political polarization", "pos": "noun"},
                {"lemma": "proscripción", "translation": "proscription / political banning", "pos": "noun"},
                {"lemma": "doctrina", "translation": "doctrine", "pos": "noun"},
                {"lemma": "reivindicación", "translation": "rights demand / reclamation", "pos": "noun"},
                {"lemma": "hegemonía", "translation": "hegemony / predominance", "pos": "noun"},
                {"lemma": "lealtad", "translation": "loyalty / allegiance", "pos": "noun"},
                {"lemma": "movilización", "translation": "mass mobilization", "pos": "noun"}
            ]
        },
        "b2-argentinasociedad-02": {
            "id": "vocab.b2.argentinasociedad.02",
            "lesson": "b2-argentinasociedad-02",
            "title": "The Military Dictatorship & Malvinas War",
            "words": [
                {"lemma": "dictadura", "translation": "military dictatorship", "pos": "noun"},
                {"lemma": "represión", "translation": "state repression", "pos": "noun"},
                {"lemma": "desaparecido", "translation": "forcibly disappeared person", "pos": "noun"},
                {"lemma": "clandestino", "translation": "clandestine / covert", "pos": "adjective"},
                {"lemma": "soberanía", "translation": "national sovereignty", "pos": "noun"},
                {"lemma": "bélico", "translation": "warlike / belligerent", "pos": "adjective"},
                {"lemma": "censura", "translation": "censorship", "pos": "noun"},
                {"lemma": "autoritarismo", "translation": "authoritarianism", "pos": "noun"},
                {"lemma": "impunidad", "translation": "impunity", "pos": "noun"},
                {"lemma": "exilio", "translation": "exile", "pos": "noun"}
            ]
        },
        "b2-argentinasociedad-03": {
            "id": "vocab.b2.argentinasociedad.03",
            "lesson": "b2-argentinasociedad-03",
            "title": "Madres & Abuelas de Plaza de Mayo: Memory & Truth",
            "words": [
                {"lemma": "pañuelo", "translation": "white headscarf (emblem of Madres)", "pos": "noun"},
                {"lemma": "antropología", "translation": "forensic anthropology", "pos": "noun"},
                {"lemma": "identidad", "translation": "identity", "pos": "noun"},
                {"lemma": "genética", "translation": "genetics / DNA identification", "pos": "noun"},
                {"lemma": "apropiación", "translation": "illegal child appropriation", "pos": "noun"},
                {"lemma": "memoria", "translation": "historical memory", "pos": "noun"},
                {"lemma": "ronda", "translation": "weekly Thursday circular march", "pos": "noun"},
                {"lemma": "restitución", "translation": "restitution / identity recovery", "pos": "noun"},
                {"lemma": "tribunal", "translation": "judicial court", "pos": "noun"},
                {"lemma": "testimonio", "translation": "witness testimony", "pos": "noun"}
            ]
        },
        "b2-argentinasociedad-04": {
            "id": "vocab.b2.argentinasociedad.04",
            "lesson": "b2-argentinasociedad-04",
            "title": "Football as Secular Religion: Maradona & Messi",
            "words": [
                {"lemma": "ídolo", "translation": "idol / revered icon", "pos": "noun"},
                {"lemma": "potrero", "translation": "vacant lot / rough street pitch", "pos": "noun"},
                {"lemma": "fervor", "translation": "fervor / passionate zeal", "pos": "noun"},
                {"lemma": "catarsis", "translation": "catharsis / collective emotional release", "pos": "noun"},
                {"lemma": "hinchada", "translation": "supporter group / stadium fan base", "pos": "noun"},
                {"lemma": "mística", "translation": "mystique / spiritual aura", "pos": "noun"},
                {"lemma": "consagración", "translation": "world title consecration", "pos": "noun"},
                {"lemma": "gambeta", "translation": "dribble / deceptive body feint", "pos": "noun"},
                {"lemma": "devoción", "translation": "devotion", "pos": "noun"},
                {"lemma": "épica", "translation": "epic narrative / heroism", "pos": "noun"}
            ]
        },
        "b2-argentinasociedad-05": {
            "id": "vocab.b2.argentinasociedad.05",
            "lesson": "b2-argentinasociedad-05",
            "title": "Economic Crises, the Corralito & Social Resilience",
            "words": [
                {"lemma": "corralito", "translation": "bank freeze / cash withdrawal limit", "pos": "noun"},
                {"lemma": "hiperinflación", "translation": "hyperinflation", "pos": "noun"},
                {"lemma": "resiliencia", "translation": "resilience", "pos": "noun"},
                {"lemma": "trueque", "translation": "barter / direct exchange network", "pos": "noun"},
                {"lemma": "asamblea", "translation": "neighborhood popular assembly", "pos": "noun"},
                {"lemma": "cacerolazo", "translation": "pot-banging street protest", "pos": "noun"},
                {"lemma": "devaluación", "translation": "currency devaluation", "pos": "noun"},
                {"lemma": "colapso", "translation": "economic collapse", "pos": "noun"},
                {"lemma": "solidaridad", "translation": "community solidarity", "pos": "noun"},
                {"lemma": "recuperación", "translation": "recovery / reclaiming", "pos": "noun"}
            ]
        }
    }

    for voc_stem, voc_obj in vocab_data.items():
        write_json(f"vocabulary/b2/{voc_stem}-voc.json", voc_obj)

    # 4. Grammar Files (10 files) - Valid grammar.schema.json format
    grammar_data = {
        "b2-26-01-a": {
            "id": "grammar.b2.26.01.deber-obligacion-conjetura",
            "title": "Perífrasis modales: Deber vs. Deber de + infinitivo",
            "sections": [
                {
                    "type": "text",
                    "content": "La gramática normativa distingue con rigor dos valores modales en las perífrasis construidas con *deber*. La estructura sin preposición, *deber + infinitivo*, expresa obligación deontológica, necesidad moral o mandato legal (*debes respetar las leyes*). Por el contrario, la variante con preposición, *deber de + infinitivo*, expresa conjetura epistémica, probabilidad o deducción tentativa basada en indicios observables (*debe de tener unos treinta años* = supongo que tiene esa edad)."
                },
                {
                    "type": "table",
                    "title": "Contraste entre Obligación Moral y Conjetura",
                    "rows": [
                        ["El pintor debe entregar el retrato antes de que concluya el plazo fijado.", "The painter must deliver the portrait before the agreed deadline expires."],
                        ["María no responde al teléfono; debe de haber salido a caminar por el parque.", "María does not answer the phone; she must have gone out for a walk in the park."],
                        ["Debemos analizar con objetividad las pruebas forenses del archivo.", "We must objectively analyze the forensic evidence from the archive."],
                        ["A juzgar por las luces encendidas, el testigo debe de estar todavía en su despacho.", "Judging by the lights on, the witness must still be in his office."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "En la norma culta formal, el uso de *deber de* para indicar obligación (*debes de estudiar más*) se considera inapropiado y debe evitarse. En cambio, *deber* sin preposición se admite con frecuencia creciente en la lengua hablada para expresar probabilidad, aunque en textos ensayísticos se prefiere mantener la distinción nítida."
                }
            ]
        },
        "b2-26-02-a": {
            "id": "grammar.b2.26.02.haber-de-infinitivo",
            "title": "Modalidad culta: Haber de + infinitivo",
            "sections": [
                {
                    "type": "text",
                    "content": "La perífrasis modal *haber de + infinitivo* pertenece al registro formal y literario. Puede expresar dos valores fundamentales: una obligación o necesidad atenuada equivalente a un deber moral o institucional fijado de antemano (*hemos de reconocer la verdad*), o bien un destino ineludible o prospección fatal que orienta el porvenir de los acontecimientos (*aquel suceso habría de marcar para siempre su destino*)."
                },
                {
                    "type": "table",
                    "title": "Valores de Haber de + infinitivo en prosa formal",
                    "rows": [
                        ["Hemos de admitir que la memoria histórica constituye el cimiento de la democracia.", "We must admit that historical memory constitutes the foundation of democracy."],
                        ["Aquel encuentro en el Salón de Primavera había de desencadenar una tragedia irreparable.", "That meeting at the Spring Salon was destined to unleash an irreparable tragedy."],
                        ["Si has de juzgar mis actos, hazlo examinando las circunstancias que los motivaron.", "If you are to judge my actions, do so by examining the circumstances that motivated them."],
                        ["Los historiadores habrán de revisar minuciosamente los documentos recién desclasificados.", "Historians will have to scrutinize meticulously the newly declassified documents."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "En pretérito imperfecto (*había de...*) o condicional simple (*habría de...*), esta perífrasis actúa frecuentemente en biografías y relatos históricos para anunciar hechos futuros respecto del tiempo narrativo principal."
                }
            ]
        },
        "b2-26-03-a": {
            "id": "grammar.b2.26.03.tener-que-infinitivo",
            "title": "Necesidad objetiva: Tener que + infinitivo",
            "sections": [
                {
                    "type": "text",
                    "content": "A diferencia de *deber + infinitivo* (que apela a un imperativo ético o moral interno), *tener que + infinitivo* expresa una obligación ineludible impuesta por circunstancias externas, necesidades materiales imperiosas o exigencias institucionales forzosas. En tiempos del pasado (*tuve que declarar*), constata la realización efectiva de la acción forzada."
                },
                {
                    "type": "table",
                    "title": "Usos de Tener que en distintos marcos temporales",
                    "rows": [
                        ["Ante la gravedad de la crisis bancaria, el gobierno tuvo que decretar el estado de emergencia.", "Faced with the severity of the banking crisis, the government had to decree a state of emergency."],
                        ["Los ciudadanos tuvieron que organizarse en asambleas barriales para sostener comedores comunitarios.", "Citizens had to organize into neighborhood assemblies to sustain community soup kitchens."],
                        ["Para comprender la magnitud de la tragedia, tendríamos que examinar los legajos de la CONADEP.", "To understand the magnitude of the tragedy, we would have to examine the CONADEP files."],
                        ["El testigo tuvo que comparecer ante el tribunal penal bajo estrictas medidas de seguridad.", "The witness had to appear before the criminal court under strict security measures."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "En enunciados condicionales contraargumentativos, *tener que + infinitivo* en condicional (*tendrías que haberlo sabido*) expresa reproche ante una negligencia o descuido imputable al interlocutor."
                }
            ]
        },
        "b2-26-04-a": {
            "id": "grammar.b2.26.04.haber-que-impersonal",
            "title": "Obligación generalizada: Haber que + infinitivo",
            "sections": [
                {
                    "type": "text",
                    "content": "La perífrasis impersonal *haber que + infinitivo* expresa necesidad u obligación universal sin atribuirla a un sujeto agente específico. Se conjuga únicamente en tercera persona del singular de todos los tiempos verbales (*hay que*, *había que*, *hubo que*, *habrá que*, *habría que*). Es el recurso por excelencia en editoriales periodísticos, manifiestos cívicos y análisis sociológicos para formular prioridades colectivas."
                },
                {
                    "type": "table",
                    "title": "La obligación impersonal en el análisis sociopolítico",
                    "rows": [
                        ["Hay que preservar la independencia judicial para garantizar la vigencia del estado de derecho.", "One must preserve judicial independence to guarantee the rule of law."],
                        ["Tras el colapso del 2001, hubo que reinventar los mecanismos de solidaridad barrial.", "After the 2001 collapse, it was necessary to reinvent neighborhood solidarity mechanisms."],
                        ["Habrá que diseñar políticas monetarias que protejan el poder adquisitivo de los asalariados.", "It will be necessary to design monetary policies that protect the purchasing power of wage earners."],
                        ["Para sanar las heridas del autoritarismo, habría que promover juicios con garantías plenas.", "To heal the wounds of authoritarianism, one ought to promote trials with full guarantees."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "La forma en condicional, *habría que + infinitivo*, es ideal en debates formales de nivel B2 para formular sugerencias o recomendaciones con cortesía argumentativa y distancia prudente."
                }
            ]
        },
        "b2-26-05-a": {
            "id": "grammar.b2.26.05.perifrasis-modales-probabilidad-epistemica",
            "title": "Calibración epistémica de probabilidad y conjetura",
            "sections": [
                {
                    "type": "text",
                    "content": "En la argumentación formal de nivel B2, el emisor calibra su grado de certeza o escepticismo combinando perífrasis modales con adverbios epistémicos. Las fórmulas *debe de haber sido*, *puede que haya ocurrido* y *habrá de considerarse* permiten matizar hipótesis complejas en la reconstrucción de hechos históricos o en la introspección psicológica de obras literarias."
                },
                {
                    "type": "table",
                    "title": "Escala de certeza y conjetura epistémica",
                    "rows": [
                        ["El acusado debió de planificar su coartada con minuciosa antelación.", "The accused must have planned his alibi with meticulous forethought."],
                        ["Las declaraciones contradictorias de los testigos deben de haber desconcertado a los jueces.", "The witnesses' contradictory statements must have bewildered the judges."],
                        ["Castel no podía admitir que María tuviera una vida impenetrable fuera de su cuadro.", "Castel could not admit that María might have an impenetrable life outside his painting."],
                        ["Aquel silencio prolongado debió de alimentar sus más oscuras sospechas de infidelidad.", "That prolonged silence must have fed his darkest suspicions of infidelity."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "El pretérito perfecto compuesto modal (*debe de haber estado*) sitúa la deducción en el presente pero proyectada hacia un hecho concluido: *Debe de haber sido muy duro vivir en la clandestinidad durante la dictadura*."
                }
            ]
        },
        "b2-argentinasociedad-01-a": {
            "id": "grammar.b2.argentinasociedad.01.conectores-contraargumentativos-debate",
            "title": "Conectores contraargumentativos en el debate sociopolítico",
            "sections": [
                {
                    "type": "text",
                    "content": "En el análisis del fenómeno peronista y la polarización política argentina, los conectores contraargumentativos (*no obstante*, *sin embargo*, *ahora bien*, *por el contrario*, *antes bien*) permiten estructurar antítesis rigurosas. Facilitan confrontar visiones opuestas sobre la justicia social, el personalismo de masas y las tensiones institucionales sin caer en descalificaciones simplistas."
                },
                {
                    "type": "table",
                    "title": "Conectores de contraste en el ensayo político",
                    "rows": [
                        ["El peronismo otorgó derechos laborales inéditos; no obstante, concentró un poder estatal hegemónico.", "Peronism granted unprecedented labor rights; nevertheless, it concentrated hegemonic state power."],
                        ["Las clases altas repudiaron el protagonismo obrero; por el contrario, los sindicatos lo vivieron como dignidad.", "Upper classes rejected worker protagonism; on the contrary, trade unions lived it as dignity."],
                        ["El régimen fomentó la industrialización por sustitución; ahora bien, dependió de la renta agropecuaria.", "The regime fostered import substitution industrialization; however, it depended on agricultural rent."],
                        ["La proscripción no extinguió el movimiento; antes bien, afianzó su mística de resistencia clandestina.", "The proscription did not extinguish the movement; rather, it reinforced its mystique of clandestine resistance."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "*Antes bien* es un marcador de oposición exclusiva muy culto: refuta la primera proposición para afirmar enérgicamente la segunda (*No debilitó la causa; antes bien, la fortaleció*)."
                }
            ]
        },
        "b2-argentinasociedad-02-a": {
            "id": "grammar.b2.argentinasociedad.02.voz-pasiva-perifrastica-denuncia",
            "title": "Estructuras pasivas en la documentación de derechos humanos",
            "sections": [
                {
                    "type": "text",
                    "content": "En los informes judiciales, testimonios notariales y obras de memoria histórica sobre el terrorismo de Estado (1976–1983), se recurre frecuentemente a la voz pasiva analítica (*ser + participio*) y a la pasiva refleja (*se + verbo en tercera persona*) para poner el foco sintáctico en los crímenes de lesa humanidad y en las víctimas, manteniendo un tono formal, objetivo y despersonalizado."
                },
                {
                    "type": "table",
                    "title": "La voz pasiva en el discurso jurídico e histórico",
                    "rows": [
                        ["Los centros clandestinos de detención fueron instalados sistemáticamente en unidades militares.", "Clandestine detention centers were systematically set up in military units."],
                        ["Miles de ciudadanos fueron secuestrados sin orden judicial durante la madrugada.", "Thousands of citizens were kidnapped without judicial warrants during the early morning hours."],
                        ["En el histórico Juicio a las Juntas, se aportaron pruebas concluyentes sobre el plan represivo.", "In the historic Trial of the Juntas, conclusive evidence about the repressive plan was submitted."],
                        ["Las sentencias condenatorias fueron ratificadas por los tribunales federales tras la nulidad de las leyes de impunidad.", "The guilty verdicts were confirmed by federal courts after the annulment of impunity laws."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Recuerda que en la pasiva analítica el participio concuerda rigurosamente en género y número con el sujeto paciente (*las víctimas fueron identificadas*, *el informe fue publicado*)."
                }
            ]
        },
        "b2-argentinasociedad-03-a": {
            "id": "grammar.b2.argentinasociedad.03.subjuntivo-oraciones-relativas-memoria",
            "title": "Subjuntivo en relativas de búsqueda e identificación",
            "sections": [
                {
                    "type": "text",
                    "content": "En la labor de las Madres y Abuelas de Plaza de Mayo y del Equipo Argentino de Antropología Forense (EAAF), las oraciones de relativo con antecedente indefinido o negado rigen de modo estricto el subjuntivo. Este uso refleja la búsqueda constante de personas y restos cuya identidad o paradero exacto aún se desconoce en el plano factual (*buscan a nietos que hayan nacido en cautiverio*)."
                },
                {
                    "type": "table",
                    "title": "Relativas con subjuntivo en la reconstrucción de identidad",
                    "rows": [
                        ["Las Abuelas buscan a jóvenes que sospechen sobre su verdadera identidad biológica.", "The Abuelas look for youths who may suspect their true biological identity."],
                        ["No hay prueba científica que pueda sustituir la certeza brindada por el banco de datos genéticos.", "There is no scientific proof that can substitute the certainty provided by the genetic database."],
                        ["El tribunal requiere testigos presenciales que hayan observado los traslados clandestinos.", "The court requires eyewitnesses who may have observed the clandestine transfers."],
                        ["Cualquier ciudadano que tenga información fidedigna debe aportarla a la secretaría de derechos humanos.", "Any citizen who has reliable information must submit it to the human rights secretariat."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Cuando el antecedente pasa de indefinido a concreto y constatado, la cláusula de relativo cambia obligatoriamente al indicativo: *Encontraron al nieto que buscaban desde hacía cuarenta años*."
                }
            ]
        },
        "b2-argentinasociedad-04-a": {
            "id": "grammar.b2.argentinasociedad.04.estructuras-ponderativas-pasion-popular",
            "title": "Estructuras ponderativas en la épica cultural y deportiva",
            "sections": [
                {
                    "type": "text",
                    "content": "El análisis sociológico del fútbol como religión laica en la Argentina recurre a estructuras sintácticas de intensificación y ponderación afectiva: construcciones consecutivas ponderativas (*tal fue la euforia que...*), superlativos absolutos cultos (*un fervor celebérrimo*), oraciones enfáticas de relieve (*fue en el potrero donde nació su magia*) y fórmulas exclamativas de trascendencia colectiva."
                },
                {
                    "type": "table",
                    "title": "Ponderación sintáctica en el ensayo deportivo",
                    "rows": [
                        ["Tal era la devoción por Maradona que su figura trascendió las fronteras del deporte para convertirse en mito cívico.", "Such was the devotion to Maradona that his figure transcended the borders of sport to become a civic myth."],
                        ["Fue en las canchas de barro de los barrios humildes donde floreció la picardía incomparable de la gambeta criolla.", "It was in the muddy pitches of humble neighborhoods where the incomparable cunning of the criollo dribble flourished."],
                        ["La consagración en Qatar desató una marea humana tan multitudinaria que desbordó las principales avenidas porteñas.", "The consecration in Qatar unleashed a human tide so massive that it overflowed the main avenues of Buenos Aires."],
                        ["Pocas expresiones culturales despiertan un fervor tan unánime como el abrazo colectivo tras un gol decisivo.", "Few cultural expressions awaken such unanimous fervor as the collective embrace after a decisive goal."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Las estructuras hendidas de relieve (*fue en... donde...*, *es mediante... como...*) permiten destacar un factor causal o espacial específico en la argumentación de nivel B2."
                }
            ]
        },
        "b2-argentinasociedad-05-a": {
            "id": "grammar.b2.argentinasociedad.05.oraciones-causales-explicativas-crisis",
            "title": "Cláusulas causales complejas en el análisis socioeconómico",
            "sections": [
                {
                    "type": "text",
                    "content": "La explicación de crisis económicas recurrentes (como el colapso del corralito en 2001) y la emergencia de redes de resiliencia popular exige el dominio de locuciones causales complejas del registro ensayístico: *dado que*, *puesto que*, *en vista de que*, *a causa de que*, *merced a que*, *comoquiera que*. Estas locuciones estructuran cadenas de causa y efecto con rigor lógico."
                },
                {
                    "type": "table",
                    "title": "Conectores causales en el ensayo socioeconómico",
                    "rows": [
                        ["Dado que el sistema bancario confiscó los ahorros de la clase media, estalló una rebelión ciudadana generalizada.", "Given that the banking system confiscated middle-class savings, a generalized citizen rebellion erupted."],
                        ["En vista de que la moneda oficial perdió liquidez, proliferaron los clubes de trueque con bonos comunitarios.", "In view of the fact that the official currency lost liquidity, barter clubs proliferated using community vouchers."],
                        ["Puesto que las instituciones estatales perdieron legitimidad, los vecinos se autoorganizaron en asambleas populares.", "Since state institutions lost legitimacy, neighbors organized themselves into popular assemblies."],
                        ["Merced a la solidaridad comunitaria y a la ayuda mutua, los barrios más vulnerables lograron sortear la emergencia.", "Thanks to community solidarity and mutual aid, the most vulnerable neighborhoods managed to overcome the emergency."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "*Dado que* y *puesto que* rigen habitualmente modo indicativo en la prosa explicativa formal porque introducen causas que el emisor presenta como hechos comprobados y compartidos por la audiencia."
                }
            ]
        }
    }

    for stem, gdata in grammar_data.items():
        write_json(f"grammar/b2/{stem}-gr.json", gdata)

    # 5. Stories (8 files) - EXACT story.schema.json FORMAT & STRICT 650-825 WORDS!

    story_core_26 = {
        "id": "b2-26",
        "title": "El túnel: La obsesión, el juicio y la soledad en el laberinto interior",
        "level": "B2",
        "lesson": 26,
        "type": "classics",
        "estimatedMinutes": 8,
        "summary": "Una adaptación literaria de 'El túnel' (1948), la célebre novela existencialista de Ernesto Sabato: el pintor Juan Pablo Castel relata desde su celda carcelaria la obsesiva búsqueda de María Iribarne tras contemplar la ventanita de su cuadro en el Salón de Primavera, el encadenamiento de conjeturas y deberes autoimpuestos, y la trágica soledad de dos seres incomunicados en túneles paralelos.",
        "characters": [
            "Juan Pablo Castel",
            "María Iribarne",
            "Allende",
            "Hunter"
        ],
        "paragraphs": [
            {
                "type": "narration",
                "text": "Desde el encierro claustrofóbico de mi celda en la penitenciaría, he de comenzar este relato sin recurrir a vanas justificaciones morales ni a falsas disculpas ante los hombres que se arrogan el derecho de juzgarme. Bastará decir que soy Juan Pablo Castel, el pintor que mató a María Iribarne. Me mueve únicamente la imperiosa necesidad de que una sola persona, al menos un alma lúcida sobre la tierra, pueda llegar a comprender los laberintos intrincados y las deducciones matemáticas que me empujaron inevitablemente hacia el abismo. Todo comenzó en el Salón de Primavera de Buenos Aires, durante la exposición anual en que exhibí mi cuadro titulado *Maternidad*. En la parte superior izquierda del lienzo, casi inadvertida para los críticos vanidosos que hablaban con pedantería de armonías cromáticas, había pintado una ventanita abierta sobre una playa solitaria, donde una mujer inmóvil contemplaba la inmensidad del mar embravecido como esperando algo angustioso y lejano."
            },
            {
                "type": "narration",
                "text": "Nadie pareció prestar la menor atención a aquel detalle recóndito, que constituía en verdad la única parte entrañable y auténtica de mi obra, excepto una muchacha desconocida de mirada penetrante y ademanes sobrios. Se detuvo largamente frente a la ventanita, ensimismada en un silencio tan denso y elocuente que comprendí de inmediato que ella debía de haber intuido el mensaje secreto de mi alma. Debió de haber sentido el mismo frío cósmico y la misma desesperación metafísica que me devoraban desde la infancia. Sin embargo, antes de que pudiera vencer mi timidez montaraz para abordarla, la mujer desapareció entre la multitud de curiosos. A partir de esa tarde fatídica, mi existencia entera se transformó en un torbellino monomaníaco: tenía que encontrarla a cualquier precio; debía de hallarse en algún rincón de la urbe, caminando por las calles céntricas o trabajando en algún edificio gubernamental."
            },
            {
                "type": "narration",
                "text": "Durante meses interminables recorrí las avenidas porteñas con la mirada febril de un detective alucinado, ensayando en mi mente cientos de diálogos hipotéticos para el instante en que el destino me la devolviera. Cuando finalmente la divisé una mañana cruzando la calle San Martín hacia el edificio de la compañía de transportes donde trabajaba, sentí que las piernas me temblaban como si una corriente eléctrica me atravesara el pecho. Tuve que obligarme a avanzar con aplomo, reprimir los latidos desbocados del corazón y cerrarle el paso con una brusquedad que la alarmó al principio. 'Tengo que hablar con usted de la ventanita de mi cuadro', le dije con una voz ronca que parecía pertenecer a otro hombre. Ella palideció ligeramente, reconoció al autor de la tela y admitió en voz baja que recordaba la escena con una nitidez asombrosa."
            },
            {
                "type": "narration",
                "text": "Así comenzaron nuestros encuentros en las plazas solitarias de Buenos Aires y en la penumbra de mi taller, donde habríamos de edificar una relación tortuosa gobernada por mis interrogatorios implacables y mis celos destructivos. María era un enigma insondable: estaba casada con un hombre ciego de refinada cortesía llamado Allende, frecuentaba la estancia campestre de su primo Hunter en la provincia de Buenos Aires y dosificaba sus confesiones con una parquedad que me enloquecía de incertidumbre. En mi afán obsesivo por desentrañar cada instante de su vida, me encerraba en el taller a formular silogismos geométricos: si María amaba a su esposo ciego, no debía de engañarlo; pero si me buscaba a mí, forzosamente tenía que mentirle a él; y si mentía a Allende con semejante naturalidad, ¿por qué no habría de engañarme a mí también con Hunter en las noches de campo?"
            },
            {
                "type": "narration",
                "text": "Aquella inferencia diabólica terminó por envenenar por completo mi entendimiento. Me convencí de que Hunter debía de ser su amante y de que sus aparentes silencios de complicidad espiritual no eran más que la máscara perversa de una hipocresía sistemática. Viajé en secreto a la estancia bajo una lluvia torrencial, oculto entre los matorrales del parque oscuro mientras vigilaba las ventanas iluminadas de la mansión. Al advertir que María se retiraba a su dormitorio tras pasear a solas con su primo, di por probada mi teoría condenatoria sin admitir la menor posibilidad de refutación. Trepé por la cornisa empapada, irrumpí en la habitación con el cuchillo empuñado y clavé la hoja en su pecho mientras sus ojos desmesurados me miraban con una tristeza infinita y desamparada, sin el más leve reproche."
            },
            {
                "type": "narration",
                "text": "Hoy comprendo, desde la desolación irrevocable de mi celda, que toda mi existencia fue un túnel oscuro y solitario en el que transcurrí mi infancia, mi juventud y mi madurez. En un destello ilusorio creí que María caminaba por un túnel semejante y que en algún punto misterioso nuestras trayectorias se habían cruzado para redimirnos del desamparo existencial. Pero qué estúpida ceguera: los túneles eran paralelos y las paredes de vidrio que nos separaban jamás permitieron que una sola palabra de verdadero amor cruzara el abismo. María observaba mi penumbra desde afuera como una espectadora compasiva ante una fiera enjaulada, mientras yo continuaba encerrado para siempre en la cárcel inexpugnable de mi propia mente en tinieblas."
            }
        ],
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Qué elemento del cuadro 'Maternidad' despierta la conexión inicial entre Juan Pablo Castel y María Iribarne?",
                        "options": [
                            "La figura imponente de la madre que ocupa el centro de la escena.",
                            "Una pequeña ventana abierta hacia una playa solitaria en el ángulo superior izquierdo.",
                            "Los colores vivos utilizados para pintar el vestido de la campesina.",
                            "La firma estilizada del autor grabada en relieve sobre el marco dorado."
                        ],
                        "correctIndex": 1,
                        "explanation": "La ventanita con la mujer solitaria contemplando el mar es el detalle inadvertido que solo María observa con detenimiento."
                    },
                    {
                        "question": "¿Cuál es el defecto psicológico central que corroe la relación de Castel con María a lo largo de la novela?",
                        "options": [
                            "Su ambición desmedida por obtener reconocimiento financiero y premios internacionales.",
                            "Su desprecio absoluto por la pintura al óleo y los encargos oficiales.",
                            "Su obsesión analítica implacable, alimentada por celos paranoides e interrogatorios agotadores.",
                            "Su deseo recurrente de abandonar la ciudad de Buenos Aires para vivir en Europa."
                        ],
                        "correctIndex": 2,
                        "explanation": "Castel analiza cada gesto de María con deducciones obsesivas que lo sumergen en la desconfianza destructiva."
                    },
                    {
                        "question": "¿Qué metáfora existencial sintetiza el desenlace de la obra respecto al destino humano?",
                        "options": [
                            "La del túnel solitario y paralelo, que simboliza la irremediable incomunicación entre las almas.",
                            "La del faro costero que ilumina a los barcos perdidos en medio de la tormenta.",
                            "La del puente levadizo que permite unir dos mundos opuestos gracias a la verdad.",
                            "La de la plaza pública donde todas las clases sociales se reconcilian fraternalmente."
                        ],
                        "correctIndex": 0,
                        "explanation": "Castel concluye que cada ser transita por su propio túnel oscuro y que la conexión perfecta fue solo una ilusión."
                    }
                ]
            }
        }
    }

    # Verify and write classic story
    w_count_classic = count_words(story_core_26)
    print(f"stories/classics/b2/b2-26.json: {w_count_classic} words")
    assert 650 <= w_count_classic <= 825, f"Classic story has {w_count_classic} words (must be 650-825)"
    write_json("stories/classics/b2/b2-26.json", story_core_26)

    # Regional Stories (5 lesson stories + 1 consolidation + 1 library stitched story)
    regional_story_texts = {
        "b2-argentinasociedad-01": [
            "Pocos fenómenos políticos y sociológicos en la historia contemporánea de América Latina han despertado pasiones tan telúricas, lealtades tan inquebrantables y antagonismos tan viscerales como el peronismo. Nacido en el fragor de la Segunda Guerra Mundial y consolidado el 17 de octubre de 1945 —cuando una marea multitudinaria e incontenible de trabajadores marchó desde los suburbios industriales de Berisso, Avellaneda y La Matanza hacia la Plaza de Mayo para exigir la liberación del coronel Juan Domingo Perón—, el movimiento justicialista reconfiguró de manera irreversible el contrato social y la cartografía ciudadana de la República Argentina. Aquellos manifestantes estigmatizados despectivamente por las clases acomodadas porteñas como 'grasitas' o 'descamisados', que refrescaban sus pies cansados en las fuentes señoriales de la plaza cívica bajo un sol primaveral abrasador, inauguraron una era de protagonismo obrero insoslayable que quebró para siempre las viejas jerarquías oligárquicas.",
            "Durante su primera presidencia a partir de 1946, el gobierno de Perón desplegó una política de audaz soberanía económica, nacionalización de servicios públicos estratégicos como los ferrocarriles británicos y los teléfonos, y una legislación laboral de vanguardia continental. Se instituyeron el aguinaldo obligatorio, las vacaciones pagadas, la indemnización por despido arbitrario y el reconocimiento jurídico pleno de los sindicatos aglutinados en la Confederación General del Trabajo (CGT), convirtiendo a los delegados de fábrica en actores centrales de la vida fabril. Si bien la burguesía terrateniente y amplios sectores de la intelectualidad universitaria denunciaron con alarma el cariz autoritario del régimen, la censura a los medios opositores y el personalismo verticalista inculcado en el aparato estatal y educativo, para millones de familias trabajadoras el peronismo significó por primera vez el acceso tangible a la dignidad material, la salud pública universal, el turismo social en balnearios populares y el ascenso social de sus hijos a través de la universidad gratuita.",
            "En el epicentro emocional de esta formidable mística popular resplandeció la figura mítica de María Eva Duarte de Perón, inmortalizada simplemente como 'Evita'. Actriz de origen provinciano humilde que conoció en carne propia las privaciones y el desprecio del interior postergado, Evita encarnó el puente pasional e irreductible entre el líder y los sectores más desposeídos de la sociedad. A través de la Fundación Eva Perón, canalizó recursos masivos para la construcción de policlínicos modernos, asilos de ancianos, ciudades infantiles y la distribución directa de viviendas, ropa, juguetes y ayuda social de emergencia. Su liderazgo apasionado y vehemente resultó determinante para la histórica sanción en 1947 de la ley del voto femenino en la Argentina, que otorgó plenos derechos cívicos y políticos a las mujeres de la nación, consagrándola como un símbolo inmortal de rebeldía combativa antes de su prematura muerte a los treinta y tres años.",
            "El violento golpe cívico-militar de septiembre de 1955, autoproclamado 'Revolución Libertadora', derrocó a Perón tras bombardear criminalmente a la población civil en la Plaza de Mayo e inauguró una proscripción política implacable que se prolongó durante casi dos décadas. Se prohibió por decreto militar mencionar el nombre del presidente depuesto, entonar la marcha partidaria justicialista o exhibir retratos oficiales bajo pena de reclusión carcelaria. No obstante la persecución sistemática y el exilio forzado del líder en Madrid, la clase trabajadora argentina desplegó una tenaz y creativa resistencia en las fábricas clandestinas, las huelgas generales y los barrios obreros, demostrando que la identidad justicialista no era un mero artefacto partidario coyuntural, sino una cultura política arraigada en las fibras íntimas de la conciencia colectiva que ningún bando castrense fue capaz de extirpar de raíz.",
            "Hoy en día, el peronismo continúa siendo la columna vertebral insustituible y el enigma principal del sistema democrático argentino. Atravesado históricamente por tensiones ideológicas fratricidas que abarcaron desde la izquierda revolucionaria montonera hasta la derecha sindical ortodoxa, y desde las privatizaciones neoliberales de los años noventa hasta las políticas estatistas y de ampliación de derechos del siglo veintiuno, el justicialismo conserva su vocación hegemónica de poder y su arraigo territorial en los sectores populares urbanos. Comprender la Argentina moderna exige, ineludiblemente, descifrar este movimiento de masas proteico que, entre luces indiscutibles de justicia distributiva y sombras de polarización visceral, sigue moldeando el destino político de la patria con una vitalidad asombrosa y permanentemente renovada."
        ],
        "b2-argentinasociedad-02": [
            "El 24 de marzo de 1976, una junta militar encabezada por los comandantes generales de las tres fuerzas armadas derrocó al débil gobierno constitucional de María Estela Martínez de Perón e instauró en la Argentina la dictadura más sangrienta, atroz y destructiva de su historia republicana, autodenominada eufemísticamente 'Proceso de Reorganización Nacional'. Amparados en la Doctrina de la Seguridad Nacional y coordinados continentalmente con otros regímenes dictatoriales del Cono Sur a través del siniestro Plan Cóndor, los jerarcas castrenses desplegaron una maquinaria de terrorismo de Estado sistemática, deliberada y clandestina concebida para aniquilar cualquier forma de disidencia política, gremial, estudiantil o intelectual en las fábricas y claustros, subordinando la sociedad entera a un régimen de terror paralizante donde la arbitrariedad armada anuló cualquier garantía constitucional elemental y clausuró las instituciones democráticas.",
            "A lo largo y ancho del país, las fuerzas represivas montaron más de setecientos centros clandestinos de detención y tortura en guarniciones del ejército, bases navales como la tristemente célebre Escuela de Mecánica de la Armada (ESMA), comisarías policiales y dependencias estatales camufladas. Miles de ciudadanos inocentes —dirigentes obreros, abogados laboralistas, estudiantes secundarios y universitarios, periodistas críticos, sacerdotes comprometidos con los barrios humildes y jóvenes militantes idealistas— fueron secuestrados en redadas nocturnas sin orden judicial, sometidos a tormentos aberrantes y posteriormente asesinados en los tenebrosos 'vuelos de la muerte', arrojados vivos y sedados a las aguas profundas del Río de la Plata y del Océano Atlántico. La figura jurídica y humana del 'desaparecido' emergió así como el doloroso símbolo de una categoría criminal inédita destinada a negar los cuerpos y borrar las huellas del genocidio sistemático.",
            "De manera paralela a la carnicería represiva, la dictadura militar impuso un programa económico de corte ultraliberal tutelado por José Alfredo Martínez de Hoz que desmanteló deliberadamente el aparato productivo nacional y endeudó a futuras generaciones. La apertura indiscriminada de importaciones, la desregulación financiera desbocada, la especulación de la denominada 'plata dulce' y un endeudamiento externo descomunal arruinaron a miles de pequeñas y medianas industrias nacionales, pulverizaron los salarios reales de los trabajadores fabriles y multiplicaron la pobreza estructural en un país que históricamente se había enorgullecido de sus sólidas clases medias educadas. La censura de prensa implacable, la quema masiva de libros prohibidos en plazas públicas y la prohibición terminante de toda actividad política y gremial completaron el asfixiante cuadro de dominación autoritaria.",
            "En abril de 1982, acorralada por una crisis económica desbordada y por el creciente descontento popular que comenzaba a desafiar abiertamente el estado de sitio en las calles con masivas marchas obreras y reclamos de pan y trabajo, la junta militar liderada por el general Leopoldo Galtieri ejecutó una desesperada y cínica maniobra de legitimación patriótica: la recuperación armada de las islas Malvinas, territorio irredento ocupado colonialmente por Gran Bretaña desde 1833. Si bien la causa soberana de Malvinas convocó un apoyo popular sincero, emotivo y fervoroso en todos los estratos de la sociedad argentina, la conducción castrense del conflicto fue improvisada, negligente y criminal. Miles de soldados conscriptos adolescentes sufrieron torturas, hambre y privaciones extremas en las trincheras heladas del archipiélago austral antes de capitular ante la fuerza de choque británica tras setenta y cuatro días de combates heroicos y profundamente desiguales.",
            "La derrota bélica inapelable en las islas Malvinas aceleró el derrumbe definitivo de la dictadura militar, forzando la convocatoria urgente a elecciones democráticas libres que consagraron en diciembre de 1983 la presidencia de Raúl Alfonsín y abrieron el camino al histórico Juicio a las Juntas Militares. Sin embargo, las heridas abiertas por el terrorismo de Estado, la desaparición forzada sistemática de treinta mil personas y la pérdida irreparable de seiscientos cuarenta y nueve combatientes en el Atlántico Sur dejaron una marca indeleble en la memoria nacional. Malvinas y los derechos humanos se entrelazaron desde entonces en la conciencia cívica argentina como dos imperativos morales indeclinables que recuerdan a las nuevas generaciones el costo inconmensurable de la soberanía popular y el valor sagrado de la vida democrática frente a la barbarie castrense."
        ],
        "b2-argentinasociedad-03": [
            "En medio de la noche más oscura del terrorismo de Estado, cuando el miedo paralizaba a la sociedad argentina y los tribunales de justicia rechazaban con indolencia cómplice los miles de recursos de hábeas corpus interpuestos por familiares angustiados, un grupo de mujeres desarmadas protagonizó una de las mayores hazañas éticas del siglo veinte. El 30 de abril de 1977, catorce madres encabezadas por Azucena Villaflor de De Vincenti se reunieron en la histórica Plaza de Mayo, frente a las ventanas cerradas de la Casa Rosada, para exigir colectivamente noticias sobre el paradero de sus hijos secuestrados por las fuerzas armadas. Al conminarlas la policía militar a dispersarse bajo el argumento de que el estado de sitio prohibía reuniones públicas, las mujeres comenzaron a marchar de a dos, entrelazando sus brazos en una ronda silenciosa alrededor de la Pirámide de Mayo.",
            "Aquellas 'locas de Plaza de Mayo', como las calificó despectivamente la propaganda oficial de la dictadura para descalificar su reclamo humanitario, transformaron el dolor desgarrador de la ausencia en una lucha política no violenta de trascendencia universal. Para identificarse entre la multitud en las peregrinaciones religiosas de Luján, comenzaron a cubrir sus cabezas con un pañal de tela blanca de sus propios hijos, que con el paso de los meses se convirtió en el icónico pañuelo blanco bordado con los nombres de los desaparecidos: el símbolo universal más potente de la defensa incondicional de los derechos humanos. Ni el secuestro y posterior asesinato de la propia Azucena Villaflor y de dos monjas francesas a manos de un grupo de tareas de la ESMA logró quebrar la determinación inquebrantable de las Madres.",
            "De manera paralela, un grupo de aquellas mismas mujeres advirtió una atrocidad complementaria perpetrada por el régimen militar: el secuestro sistemático de bebés y niños nacidos durante el cautiverio clandestino de sus madres embarazadas, quienes eran entregados con identidades falsas a familias militares, policías o allegados al poder. Nacieron así las Abuelas de Plaza de Mayo, lideradas históricamente por mujeres corajudas como Chicha Mariani y Estela de Carlotto, resueltas a consagrar el resto de sus vidas a la búsqueda científica y judicial de sus nietos apropiados. Con asombrosa intuición pionera, las Abuelas viajaron a las principales universidades del mundo convocando a genetistas insignes para desarrollar el 'índice de abuelidad', una fórmula biológica basada en el ADN capaz de determinar con precisión matemática la filiación entre abuelos y nietos ante la ausencia física de los padres asesinados.",
            "Con la recuperación democrática en 1983, el testimonio heroico de Madres y Abuelas nutrió las páginas concluyentes del informe Nunca Más redactado por la Comisión Nacional sobre la Desaparición de Personas (CONADEP) y presidido por el escritor Ernesto Sabato. Aquel documento histórico sirvió de sustento probatorio fundamental para el Juicio a las Juntas Militares de 1985, un proceso penal inédito en el que un tribunal civil de la república juzgó y condenó a los dictadores militares que habían asolado el país. Si bien leyes posteriores de impunidad como Obediencia Debida y Punto Final intentaron clausurar los juicios, la perseverancia incansable de los organismos de derechos humanos logró su nulidad parlamentaria definitiva en 2003, permitiendo la reapertura de cientos de causas judiciales y la condena firme de más de un millar de represores.",
            "Hasta la fecha, las Abuelas de Plaza de Mayo han logrado restituir la identidad biológica y familiar a más de ciento treinta y cinco hombres y mujeres que vivían bajo nombres falsificados, devolviéndoles su historia, su memoria y su verdad arrebatada. Cada restitución de un nieto recuperado es celebrada en la Argentina como una victoria colectiva de la vida sobre la muerte y de la luz sobre las sombras. La marcha semanal de los jueves en la Plaza de Mayo continúa realizándose puntualmente, recordando al mundo entero que, mientras existan pueblos dispuestos a luchar sin descanso por la Memoria, la Verdad y la Justicia, ningún poder criminal sobre la tierra podrá decretar el olvido definitivo de los vencidos."
        ],
        "b2-argentinasociedad-04": [
            "Para comprender la fisonomía emocional, el pulso identitario y la psicología colectiva de la sociedad argentina, resulta indispensable adentrarse en los estadios de fútbol, donde este deporte trasciende con creces la condición de mero espectáculo atlético para erigirse en una auténtica religión laica de masas. Nacido a finales del siglo diecinueve en los clubes británicos de Buenos Aires y Rosario como una práctica aristocrática rigurosamente normada, el juego fue rápidamente reapropiado y reinventado por los hijos de la inmigración obrera en los descampados suburbanos conocidos entrañablemente como 'potreros'. En esas canchas polvorientas de tierra y cascotes floreció la 'nuestra': una estética futbolística singular caracterizada por el toque corto y pausado, el engaño corporal de la gambeta impredecible, la picardía criolla y la improvisación artística frente al rigor físico sajón.",
            "En ese crisol de pasiones barriales nació el mito absoluto de Diego Armando Maradona, el muchacho de Villa Fiorito que conquistó la cima del planeta deportivo con la zurda más prodigiosa y desafiante de la historia. Para millones de argentinos, Maradona representó mucho más que un futbolista excepcional; encarnó la revancha simbólica del descamisado humilde frente a las élites arrogantes y la restitución del orgullo nacional tras las heridas sangrantes de la dictadura militar y la guerra de Malvinas. Su consagración definitiva en el Mundial de México 1986, coronada en el partido histórico contra Inglaterra con 'la mano de Dios' y 'el gol del siglo' —una obra de arte irrepetible donde eludió a medio equipo rival arrancando desde su propio campo ante el asombro del mundo entero—, transformó su figura en una deidad cívica inmortal cuya partida física en noviembre de 2020 conmovió las fibras más íntimas de la nación entera, paralizando al país en un duelo nacional unánime.",
            "Décadas más tarde, la aparición providencial de Lionel Messi completó la parábola mística del fútbol argentino con un relato conmovedor de maduración, perseverancia y estoicismo admirable. Nacido en Rosario y forjado deportivamente en Barcelona tras superar complejas dificultades hormonales en su infancia, Messi debió transitar un camino espinoso antes de conquistar el corazón unánime de sus compatriotas. Sometido durante años a comparaciones desmesuradas e injustas con el carisma volcánico de Maradona y derrotado en dolorosas finales continentales y ecuménicas, Messi jamás renunció a vestir la camiseta celeste y blanca. Su liderazgo maduro, sereno, paternal y genial en el Mundial de Qatar 2022 condujo a la Argentina a su tercera corona ecuménica en una final memorable ante Francia que muchos especialistas consideran el mejor partido jamás disputado en la historia del deporte mundial.",
            "La coronación de Messi y la selección nacional desató en diciembre de 2022 la mayor movilización popular pacífica registrada en la historia de la República Argentina: más de cinco millones de ciudadanos colmaron espontáneamente las avenidas céntricas de Buenos Aires alrededor del Obelisco, fundiéndose en un abrazo colectivo que borró por unos días las profundas grietas políticas y las angustias económicas cotidianas. Familias enteras, ancianos conmovidos que habían celebrado con Maradona en 1986 y niños que vestían orgullosos la camiseta número diez de Messi lloraron juntos de emoción en las calles, confirmando que la 'scaloneta' había operado como una formidable catarsis comunitaria en un país profundamente urgido de alegrías y esperanzas compartidas tras años de sacrificios.",
            "En cada clásico barrial entre Boca Juniors y River Plate, en las míticas gradas de La Bombonera y El Monumental donde las hinchadas alientan sin cesar con cánticos ensordecedores y banderas monumentales que desafían la imaginación coreográfica, el fútbol argentino refrenda cada fin de semana su pacto sagrado con el alma popular. No se trata simplemente de ganar o perder noventa minutos de juego reglamentario sobre el césped; se trata de una ceremonia colectiva de pertenencia, lealtad barrial comunitaria y reafirmación de un sentido identitario indoblegable que resiste a todas las crisis. Así, los clubes sociales y deportivos de barrio continúan funcionando como verdaderos bastiones de contención comunitaria donde convergen el deporte, la merienda popular, las actividades culturales y la memoria afectiva de varias generaciones de familias argentinas, demostrando que la pasión es el único idioma universal capaz de detener el tiempo."
        ],
        "b2-argentinasociedad-05": [
            "A lo largo del último medio siglo, la República Argentina ha convivido con ciclos macroeconómicos recurrentes de hiperinflación traumática, endeudamiento externo asfixiante, devaluaciones bruscas de la moneda y profundas crisis de gobernabilidad política que pusieron a prueba la cohesión misma del tejido social y familiar. Entre todos estos episodios turbulentos, ninguno dejó una huella tan indeleble y traumática en la memoria colectiva contemporánea como el colapso financiero, político e institucional de diciembre de 2001. El agotamiento definitivo del plan de convertibilidad monetaria —que durante una década entera había atado artificialmente el valor del peso al dólar estadounidense a costa de la desindustrialización masiva, el cierre de talleres y el endeudamiento especulativo— desembocó en una catástrofe social sin precedentes en la historia republicana del Cono Sur.",
            "A comienzos de diciembre de 2001, ante una corrida bancaria imparable provocada por la fuga masiva de capitales especulativos al exterior y el pánico financiero, el gobierno decretó el temido 'corralito': una medida de congelamiento bancario que restringió drásticamente el retiro de dinero en efectivo de las cuentas salariales y de ahorro. La confiscación efectiva de los depósitos bancarios de millones de trabajadores, pequeños comerciantes y jubilados desató una indignación ciudadana incontenible en todas las clases sociales. La noche del 19 de diciembre, mientras el presidente Fernando de la Rúa anunciaba por cadena nacional la instauración del estado de sitio para aplacar la rebelión, cientos de miles de vecinos de Buenos Aires y de las principales ciudades salieron espontáneamente a las esquinas golpeando ollas y sartenes en el primer gran 'cacerolazo' masivo de la era moderna, confluyendo pacíficamente hacia la Plaza de Mayo al grito unánime de '¡Que se vayan todos, que no quede ni uno solo!'.",
            "La represión policial ordenada por el gobierno nacional en las inmediaciones de la histórica plaza cívica dejó un trágico saldo de treinta y nueve manifestantes asesinados en todo el país, forzando la renuncia apresurada y la huida en helicóptero del primer mandatario desde el techo de la Casa Rosada en una tarde aciaga. En el lapso vertiginoso de apenas dos semanas, la república vio desfilar a cinco presidentes sucesivos designados de urgencia por la asamblea legislativa mientras el país declaraba la mayor cesación de pagos de deuda externa de la historia financiera global y el peso argentino perdía en escasas jornadas más del setenta por ciento de su valor adquisitivo, empujando a más de la mitad de la población trabajadora por debajo de la línea de pobreza extrema.",
            "No obstante la magnitud aterradora del descalabro económico y la parálisis de las instituciones públicas tradicionales, la sociedad civil argentina desplegó una asombrosa capacidad de resiliencia comunitaria y autoorganización solidaria para garantizar la subsistencia cotidiana. Ante la escasez absoluta de dinero circulante, millones de ciudadanos crearon los Clubes del Trueque, una gigantesca economía popular alternativa donde se intercambiaban alimentos, servicios profesionales y manufacturas hogareñas mediante bonos o 'créditos' impresos localmente. En los barrios porteños y del conurbano proliferaron las Asambleas Populares autoconvocadas en plazas y esquinas para coordinar ollas populares, compras comunitarias y actividades culturales, mientras los obreros de centenares de fábricas metalúrgicas y textiles en quiebra recuperaban las instalaciones para ponerlas a producir bajo régimen de cooperativas autogestionadas con el apoyo activo del vecindario.",
            "Aquella dolorosa fragua cívica del 2001 dejó lecciones sociológicas permanentes sobre la naturaleza del pueblo argentino. Si bien las crisis económicas continúan manifestándose con recurrencia a través de tensiones inflacionarias crónicas y debates polarizados sobre el rol del Estado, el gasto social y los acuerdos con el Fondo Monetario Internacional, la experiencia histórica demostró que bajo la superficie de la fragilidad económica late una vigorosa trama de solidaridad comunitaria, creatividad asociativa y movilización popular capaz de resistir las peores tormentas. En la Argentina, las crisis no congelan la vida cívica ni adormecen a la ciudadanía; por el contrario, reafirman la certeza de que el destino común se construye y se defiende colectivamente en el espacio público compartido, donde la dignidad ciudadana prevalece sobre cualquier descalabro financiero."
        ],
        "b2-argentinasociedad-consolidation": [
            "Analizar la trayectoria cívica, política y cultural de la República Argentina a lo largo de las últimas décadas equivale a sumergirse en una trama de intensidad dramática incomparable, donde las contradicciones más profundas de la condición humana y colectiva se manifiestan sin medias tintas. Pocas naciones han experimentado con tanta virulencia los vaivenes que median entre la conquista heroica de derechos sociales de vanguardia y los abismos sangrientos del autoritarismo represivo; entre la exaltación desbordada del triunfo deportivo y el desgarro angustioso de colapsos económicos devastadores. Esta fragua cívica permanente no ha paralizado a la sociedad argentina; antes bien, ha templado un carácter ciudadano singular, caracterizado por una irreductible pulsión por la vida pública deliberativa y una defensa inclaudicable de la dignidad popular frente a cualquier adversidad institucional o financiera que amenace el bienestar común.",
            "El peronismo, como movimiento de masas hegemónico y columna vertebral de la política nacional desde mediados del siglo veinte, demostró que la incorporación de las clases trabajadoras a la mesa de decisiones no fue una graciosa concesión de las élites tradicionales, sino el fruto de una movilización obrera consciente de su propio poder histórico transformador. Si bien el justicialismo alimentó polarizaciones ideológicas que dividieron familias y fracturaron consensos institucionales durante generaciones enteras, su impronta doctrinaria afianzó en la conciencia popular una premisa irrenunciable: la justicia social no es una dádiva paternalista, sino un derecho inalienable que la ciudadanía tiene el deber moral de defender activamente frente a cualquier intento de regresión económica o conculcación de conquistas laborales consagradas por la ley.",
            "Por su parte, la respuesta ética y pacífica de la sociedad argentina ante el horror planificado del terrorismo de Estado inauguró un paradigma universal en materia de memoria y derechos humanos. La marcha incesante de las Madres y Abuelas de Plaza de Mayo con sus emblemáticos pañuelos blancos, la rigurosa documentación testimonial del informe Nunca Más y la valentía civil del Juicio a las Juntas Militares demostraron que la memoria histórica y la búsqueda incansable de la verdad son los únicos cimientos sobre los cuales es posible edificar una democracia duradera. La restitución paulatina de identidades arrebatadas a los nietos y la condena judicial firme a los genocidas enseñaron al mundo entero que los crímenes de lesa humanidad no prescriben jamás y que la impunidad siempre termina por sucumbir ante la perseverancia pacífica y legal de la justicia.",
            "En el plano de las pasiones colectivas, la devoción ecuménica por el fútbol encarna el canal catártico privilegiado a través del cual la nación tramita sus anhelos de redención, trascendencia y comunión fraterna. Desde la épica rebelde, barroca y callejera de Diego Armando Maradona en los potreros del mundo hasta la consagración perseverante, serena y conmovedora de Lionel Messi en Qatar, el fútbol opera como un milagroso puente de cohesión ciudadana donde todas las divisiones partidarias se desvanecen en un abrazo unánime y festivo. Asimismo, ante las recurrentes crisis económicas que despojaron a familias de sus ahorros en episodios traumáticos como la hiperinflación y el corralito de 2001, la resiliencia popular demostró que las redes de solidaridad barrial, las asambleas comunitarias, el trueque y las fábricas recuperadas por sus propios trabajadores son el escudo supremo de una comunidad que jamás se resigna a la desesperanza ni al desamparo.",
            "La Argentina se revela, en última instancia, como una sociedad en estado de deliberación cívica y asamblearia perpetua, donde la calle, la plaza y el estadio constituyen los santuarios sagrados e inalienables de una ciudadanía vigilante, apasionada y profundamente politizada. Comprender este país austral implica renunciar a los juicios sumarios simplistas y abrazar la fecunda complejidad de su laberinto histórico, reconociendo con lucidez que en el corazón palpitante de sus debates cívicos late la irrevocable convicción de que solo un pueblo que defiende activamente su memoria, su justicia y su alegría colectiva es verdaderamente digno de conquistar y preservar su propio porvenir democrático ante los complejos desafíos del nuevo milenio."
        ]
    }

    regional_titles_summaries = {
        "b2-argentinasociedad-01": (
            "El peronismo: Fenómeno de masas, justicia social y polarización",
            "Un ensayo sociopolítico sobre la emergencia del peronismo el 17 de octubre de 1945: las conquistas laborales de la primera presidencia de Juan Domingo Perón, la mística popular de Evita y el voto femenino, la proscripción militar y la cultura política de masas.",
            ["Historiador del movimiento obrero Hernán", "Sindicalista de la CGT Don Roberto", "Investigadora social Camila", "Militante barrial Soledad"],
            1
        ),
        "b2-argentinasociedad-02": (
            "La última dictadura militar (1976–1983) y la guerra de Malvinas",
            "Una crónica sobre el terrorismo de Estado en la Argentina: los centros clandestinos de detención y tortura, la figura del desaparecido, el desmantelamiento económico, la guerra de Malvinas en 1982 y el colapso final del régimen autoritario.",
            ["Sociólogo e investigador de la memoria Julián", "Sobreviviente de centro clandestino Laura", "Excombatiente de Malvinas Esteban", "Abogada de causas federales Mariana"],
            2
        ),
        "b2-argentinasociedad-03": (
            "Las Madres y Abuelas de Plaza de Mayo: El triunfo de la memoria",
            "Un retrato de la lucha de derechos humanos más trascendente del siglo XX: las rondas de los jueves con pañuelos blancos, la búsqueda de nietos apropiados, el índice de abuelidad genético, el Juicio a las Juntas y la nulidad de las leyes de impunidad.",
            ["Madre de Plaza de Mayo Doña Nora", "Nieto restituido por Abuelas Matías", "Antropóloga forense del EAAF Clara", "Periodista de derechos humanos Facundo"],
            3
        ),
        "b2-argentinasociedad-04": (
            "El fútbol como religión laica: De Maradona a Messi",
            "Un análisis de la pasión futbolística argentina como fenómeno sociológico y afectivo: la cultura del potrero y la gambeta criolla, el mito inmortal de Diego Armando Maradona, la consagración de Lionel Messi en Qatar 2022 y la catarsis colectiva.",
            ["Periodista y cronista deportivo Gonzalo", "Hincha y sociólogo de tribuna Santiago", "Entrenador de fútbol infantil Don Celso", "Historiadora de la cultura popular Lucía"],
            4
        ),
        "b2-argentinasociedad-05": (
            "Crisis económicas recurrentes, el corralito y la resiliencia social",
            "Una crónica sobre el estallido socioeconómico e institucional de diciembre de 2001: el corralito financiero, los cacerolazos multitudinarios, la renuncia presidencial, los clubes de trueque, las asambleas barriales y las fábricas recuperadas.",
            ["Economista e historiador bancario Martín", "Vecina de asamblea barrial Marcela", "Trabajador de fábrica recuperada Don Evaristo", "Socióloga de la protesta urbana Valentina"],
            5
        ),
        "b2-argentinasociedad-consolidation": (
            "Consolidación: La fragua cívica argentina",
            "Una síntesis comprensiva de las tensiones, pasiones y lecciones democráticas de la sociedad argentina: el peronismo y los derechos obreros, la memoria y la justicia de Madres y Abuelas, el fervor del fútbol de potrero y la resiliencia comunitaria.",
            ["Ensayista y filósofo político Bautista", "Historiadora de la ciudadanía Laura", "Docente universitaria Soledad", "Sociólogo del espacio público Bruno"],
            6
        )
    }

    # Verify and write regional stories
    for stem, text_paras in regional_story_texts.items():
        rel_path = f"stories/world/b2/{stem}.json"
        title, summary, characters, lesson_num = regional_titles_summaries[stem]
        story_obj = {
            "id": stem,
            "title": title,
            "level": "B2",
            "lesson": lesson_num,
            "type": "world",
            "estimatedMinutes": 8,
            "summary": summary,
            "characters": characters,
            "paragraphs": [{"type": "narration", "text": p} for p in text_paras],
            "narration": {
                "pedagogical": {
                    "comprehensionQuestions": [
                        {
                            "question": "¿Cuál es la tesis central que articula este texto respecto a la historia cívica y social argentina?",
                            "options": [
                                "Que la sociedad argentina ha sido pasiva y desinteresada frente a los acontecimientos políticos.",
                                "Que las conquistas de derechos, la resistencia al autoritarismo y la resiliencia comunitaria definieron una ciudadanía participativa.",
                                "Que los problemas económicos se resolvieron rápida y pacíficamente sin tensiones colectivas.",
                                "Que el fútbol y la cultura popular sustituyeron por completo la preocupación por la justicia y la memoria."
                            ],
                            "correctIndex": 1,
                            "explanation": "El texto resalta cómo las luchas obreras, la memoria de derechos humanos y la organización barrial forjaron un carácter cívico indeclinable."
                        },
                        {
                            "question": "¿Qué factor común destaca el texto en la respuesta social ante momentos extremos como la dictadura o el 2001?",
                            "options": [
                                "La resignación fatalista y el abandono de los espacios públicos cívicos.",
                                "La confianza ciega en las promesas de los organismos financieros internacionales.",
                                "La emergencia de redes de solidaridad comunitaria, creatividad asociativa y movilización pacífica.",
                                "La emigración forzada de la totalidad de la población trabajadora hacia otros continentes."
                            ],
                            "correctIndex": 2,
                            "explanation": "Tanto Madres de Plaza de Mayo como las asambleas del 2001 y los clubes de trueque ejemplifican la autoorganización comunitaria."
                        },
                        {
                            "question": "¿Cómo se describe la relación entre las pasiones culturales y la identidad política en la Argentina?",
                            "options": [
                                "Como esferas profundamente interconectadas donde el espacio público funciona como ágora de deliberación y catarsis.",
                                "Como compartimentos aislados sin ningún tipo de comunicación o influencia mutua.",
                                "Como distracciones diseñadas exclusivamente para desmovilizar los reclamos de los trabajadores.",
                                "Como fenómenos secundarios frente a la primacía de las modas importadas de Europa."
                            ],
                            "correctIndex": 0,
                            "explanation": "La plaza, la calle y el estadio son espacios de afirmación identitaria y expresión cívica compartida."
                        }
                    ]
                }
            }
        }

        # Check word count
        w_count = count_words(story_obj)
        print(f"{rel_path}: {w_count} words")
        assert 650 <= w_count <= 825, f"Story {rel_path} has {w_count} words (must be 650-825)"
        write_json(rel_path, story_obj)

    # Consolidated library story: b2-argentinasociedad.json (25 paragraphs from lessons 1-5)
    stitched_paragraphs = []
    for i in range(1, 6):
        stem = f"b2-argentinasociedad-0{i}"
        for p in regional_story_texts[stem]:
            stitched_paragraphs.append({"type": "narration", "text": p})

    assert len(stitched_paragraphs) == 25, f"Stitched library story must have 25 paragraphs, got {len(stitched_paragraphs)}"

    stitched_story = {
        "id": "b2-argentinasociedad",
        "title": "Argentina III: Política, Pasión, Peronismo y Derechos Humanos",
        "level": "B2",
        "lesson": 1,
        "type": "world",
        "estimatedMinutes": 20,
        "summary": "Un compendio integral sobre la fragua cívica argentina contemporánea: el peronismo y los derechos laborales de Evita, el terrorismo de Estado y la guerra de Malvinas, la gesta ética de Madres y Abuelas de Plaza de Mayo, la pasión comunitaria del fútbol de Maradona a Messi, y la resiliencia social frente al colapso del corralito de 2001.",
        "characters": [
            "Militantes y trabajadores justicialistas",
            "Sobrevivientes y testigos de la memoria histórica",
            "Madres y Abuelas de Plaza de Mayo",
            "Ídolos populares y aficionados de fútbol",
            "Vecinos y asambleístas comunitarios"
        ],
        "paragraphs": stitched_paragraphs,
        "narration": {
            "pedagogical": {
                "comprehensionQuestions": [
                    {
                        "question": "¿Cuál fue el impacto social central de la movilización popular del 17 de octubre de 1945?",
                        "options": [
                            "La inauguración de un régimen aristocrático favorable a los grandes terratenientes.",
                            "La irrupción protagónica de la clase trabajadora en el centro de la escena política argentina.",
                            "El desarme inmediato de las organizaciones sindicales en los suburbios de Buenos Aires.",
                            "La firma de tratados comerciales exclusivos con las potencias del Eje europeo."
                        ],
                        "correctIndex": 1,
                        "explanation": "El 17 de octubre consagró el ascenso de la clase obrera y dio origen histórico al movimiento peronista."
                    },
                    {
                        "question": "¿Qué contradicción histórica marcó el conflicto de las islas Malvinas en 1982?",
                        "options": [
                            "La dictadura utilizó una causa de soberanía nacional legítima para intentar perpetuarse en el poder en medio de su crisis.",
                            "Los soldados conscriptos contaban con armamento nuclear que decidieron no emplear por razones éticas.",
                            "El gobierno británico cedió pacíficamente las islas tras las primeras negociaciones diplomáticas en la ONU.",
                            "La población civil argentina se negó unánimemente a apoyar a los combatientes que viajaban al archipiélago."
                        ],
                        "correctIndex": 0,
                        "explanation": "La junta militar instrumentalizó la causa patriótica de Malvinas para frenar el descontento y ocultar los crímenes del terrorismo de Estado."
                    },
                    {
                        "question": "¿Qué innovación científica revolucionaria impulsaron las Abuelas de Plaza de Mayo en su búsqueda?",
                        "options": [
                            "El desarrollo de técnicas de radar satelital para localizar archivos militares secretos.",
                            "El diseño del índice de abuelidad genético para identificar la filiación biológica entre abuelos y nietos.",
                            "La creación de cámaras de microfilmación para proteger los expedientes notariales de la colonia.",
                            "La invención de un sistema de radio clandestino para comunicarse entre los centros de detención."
                        ],
                        "correctIndex": 1,
                        "explanation": "Las Abuelas recurrieron a genetistas internacionales para crear la prueba de ADN que determina la filiación ante la ausencia de los padres."
                    },
                    {
                        "question": "¿Qué representó la figura de Diego Armando Maradona para los sectores populares argentinos?",
                        "options": [
                            "Un modelo exclusivo de disciplina militarizada dentro de los campos deportivos.",
                            "La revancha simbólica del descamisado humilde frente a las élites y la reivindicación del orgullo patrio herido.",
                            "Un funcionario estatal encargado de administrar los fondos de la educación pública.",
                            "Un crítico severo de las tradiciones y costumbres folclóricas de la vida barrial."
                        ],
                        "correctIndex": 1,
                        "explanation": "Maradona encarnó el triunfo del chico de potrero y la reivindicación popular frente a las injusticias sociales."
                    },
                    {
                        "question": "¿Cómo respondió la sociedad civil argentina ante la confiscación de depósitos del 'corralito' en 2001?",
                        "options": [
                            "Aceptando pasivamente las medidas bancarias sin formular ninguna protesta callejera.",
                            "Creando redes de trueque popular, asambleas barriales autoconvocadas y cooperativas de fábricas recuperadas.",
                            "Destruyendo la totalidad de las plazas públicas y centros culturales de la ciudad.",
                            "Exigiendo la intervención de tropas extranjeras para restablecer el orden financiero."
                        ],
                        "correctIndex": 1,
                        "explanation": "La ciudadanía desplegó mecanismos de economía alternativa y solidaridad comunitaria para sortear la emergencia extrema."
                    }
                ]
            }
        }
    }
    write_json("stories/world/b2/b2-argentinasociedad.json", stitched_story)

    # 6. Exercises (12 files)
    exercise_files = {
        # Core Unit 26
        "b2-26-01-ex": {
            "lesson": "b2-26-01",
            "exercises": [
                {
                    "id": "b2-26-01.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["perifrasis-deber-obligacion-conjetura"],
                    "question": "¿Qué matiz distingue a 'deber + infinitivo' de 'deber de + infinitivo' en la norma culta formal?",
                    "options": [
                        "'Deber' sin preposición denota obligación moral o necesidad estricta; 'deber de' expresa probabilidad o conjetura epistémica.",
                        "'Deber' expresa futuro incierto y 'deber de' expresa pasado inmediato retrospectivo.",
                        "'Deber de' es un arcaísmo medieval completamente desaconsejado en todos los contextos.",
                        "Ambas formas son estrictamente sinónimas e intercambiables sin variación estilística alguna."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-26-01.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["perifrasis-deber-obligacion-conjetura"],
                    "sentence": "Para salvaguardar la vigencia del estado de derecho, los magistrados __ actuar con absoluta probidad e independencia.",
                    "answer": "deben",
                    "english": "In order to safeguard the rule of law, magistrates must act with absolute integrity and independence."
                },
                {
                    "id": "b2-26-01.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["perifrasis-deber-obligacion-conjetura"],
                    "question": "¿Cuál de las siguientes oraciones formula una conjetura o deducción tentativa basada en indicios?",
                    "options": [
                        "Debemos presentar los recursos de hábeas corpus antes de las doce.",
                        "A juzgar por las luces encendidas en el archivo, el juez debe de estar revisando los legajos.",
                        "Tienes que acatar las órdenes emitidas por el tribunal electoral.",
                        "Hay que promover la educación en derechos humanos en todas las escuelas."
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-26-01.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["perifrasis-deber-obligacion-conjetura"],
                    "sentence": "No contesta a mis llamadas insistentes; María debe __ haber salido a caminar por la ribera.",
                    "answer": "de",
                    "english": "She does not answer my persistent calls; María must have gone out for a walk along the riverbank."
                },
                {
                    "id": "b2-26-01.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-26-vocab"],
                    "pairs": [
                        ["el deber moral", "the moral duty / obligation"],
                        ["la conjetura epistémica", "the epistemic conjecture / surmise"],
                        ["el indicio observable", "the observable clue / sign"],
                        ["la obligatoriedad legal", "the legal compulsoriness"]
                    ]
                },
                {
                    "id": "b2-26-01.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "En 'El túnel' de Ernesto Sabato, ¿por qué Juan Pablo Castel decide narrar el crimen desde su celda?",
                    "options": [
                        "Para pedir clemencia a los jueces y reducir su condena penitenciaria.",
                        "Porque abriga la esperanza de que al menos una persona lúcida llegue a comprender sus razones.",
                        "Para demostrar que los críticos de arte conspiraron para destruir su prestigio profesional.",
                        "Porque su abogado le exigió escribir un texto exculpatorio para publicar en los diarios."
                    ],
                    "correct": 1
                }
            ]
        },
        "b2-26-02-ex": {
            "lesson": "b2-26-02",
            "exercises": [
                {
                    "id": "b2-26-02.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["perifrasis-haber-de-infinitivo"],
                    "question": "¿Qué valor discursivo adquiere 'haber de + infinitivo' en pretérito imperfecto en: 'Aquel cuadro expuesto en el salón había de transformar su vida'?",
                    "options": [
                        "Señala una obligación laboral impuesta por el jurado de la exposición.",
                        "Anticipa un destino ineludible o acontecimiento crucial proyectado hacia el porvenir narrativo.",
                        "Expresa una prohibición legal que impidió la venta de la pintura.",
                        "Denota una acción repentina e involuntaria iniciada en ese mismo instante."
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-26-02.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["perifrasis-haber-de-infinitivo"],
                    "sentence": "Los pueblos que pretenden vivir en paz han __ enfrentar con valentía las verdades más dolorosas de su historia.",
                    "answer": "de",
                    "english": "Peoples who aspire to live in peace must bravely face the most painful truths of their history."
                },
                {
                    "id": "b2-26-02.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["perifrasis-haber-de-infinitivo"],
                    "question": "¿A qué registro lingüístico pertenece fundamentalmente la perífrasis 'haber de + infinitivo'?",
                    "options": [
                        "Al registro coloquial informal propio del lunfardo arrabalero.",
                        "Al registro formal, literario y ensayístico de corte culto.",
                        "Al lenguaje técnico exclusivo de la contabilidad agropecuaria.",
                        "Al dialecto infantil empleado en canciones de cuna."
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-26-02.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["perifrasis-haber-de-infinitivo"],
                    "sentence": "Si has de emitir un veredicto definitivo, __ examinando la totalidad de los testimonios presentados.",
                    "answer": "hazlo",
                    "english": "If you are to deliver a definitive verdict, do so by examining the totality of the testimonies presented."
                },
                {
                    "id": "b2-26-02.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-26-vocab"],
                    "pairs": [
                        ["el designio ineludible", "the inescapable grand design"],
                        ["la inexorabilidad del tiempo", "the inexorability of time"],
                        ["el precepto constitucional", "the constitutional precept"],
                        ["el mandato popular", "the popular mandate"]
                    ]
                },
                {
                    "id": "b2-26-02.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué representaba para Castel la pequeña ventana pintada en su cuadro 'Maternidad'?",
                    "options": [
                        "Una crítica irónica a las técnicas académicas de pintura del siglo diecinueve.",
                        "El único mensaje auténtico y desgarrador sobre su profunda soledad existencial.",
                        "Un simple detalle decorativo para equilibrar la composición de luces y sombras.",
                        "Un homenaje nostálgico a la casa de campo de sus abuelos en la provincia."
                    ],
                    "correct": 1
                }
            ]
        },
        "b2-26-03-ex": {
            "lesson": "b2-26-03",
            "exercises": [
                {
                    "id": "b2-26-03.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["perifrasis-tener-que-infinitivo"],
                    "question": "¿Qué diferencia semántica existe entre 'tener que + infinitivo' y 'deber + infinitivo'?",
                    "options": [
                        "'Tener que' expresa obligación impuesta por presiones externas o necesidades ineludibles; 'deber' apela al deber moral o ético interno.",
                        "'Tener que' se utiliza únicamente para el clima, mientras 'deber' se aplica a contratos.",
                        "'Deber' exige subjuntivo en oraciones afirmativas, mientras 'tener que' solo admite infinitivo pasivo.",
                        "Ambas perífrasis expresan exactamente el mismo matiz de cortesía formal."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-26-03.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["perifrasis-tener-que-infinitivo"],
                    "sentence": "Ante la gravedad de la crisis cambiaria en diciembre de 2001, el gobierno __ que decretar la inmovilización de fondos.",
                    "answer": "tuvo",
                    "english": "Faced with the severity of the exchange crisis in December 2001, the government had to decree the freezing of funds."
                },
                {
                    "id": "b2-26-03.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["perifrasis-tener-que-infinitivo"],
                    "question": "¿Qué valor adquiere 'tener que + infinitivo' en condicional en: 'Para comprender la magnitud de la tragedia, tendríamos que examinar los legajos'?",
                    "options": [
                        "Plantea un requisito hipotético indispensable para alcanzar un entendimiento cabal del hecho.",
                        "Confirma que los documentos ya fueron destruidos por las autoridades judiciales.",
                        "Prohíbe terminantemente la consulta de archivos clasificados por razones de seguridad.",
                        "Indica una acción que acaba de completarse hace escasos segundos."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-26-03.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["perifrasis-tener-que-infinitivo"],
                    "sentence": "Los testigos de las causas federales tuvieron que __ con custodia especial debido a las amenazas.",
                    "answer": "comparecer",
                    "english": "Witnesses in federal cases had to appear under special protection due to threats."
                },
                {
                    "id": "b2-26-03.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-26-vocab"],
                    "pairs": [
                        ["el apremio financiero", "the pressing financial urgency"],
                        ["la coacción externa", "the external coercion / duress"],
                        ["la constricción presupuestaria", "the budgetary constraint"],
                        ["el requerimiento judicial", "the judicial requirement"]
                    ]
                },
                {
                    "id": "b2-26-03.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Por qué Castel se siente angustiado y confundido tras sus primeros encuentros con María?",
                    "options": [
                        "Porque ella le exige grandes sumas de dinero a cambio de posar como modelo.",
                        "Porque María resulta impenetrable en sus secretos y se niega a someterse a sus deducciones.",
                        "Porque el marido de María amenaza con clausurar su taller de pintura en La Boca.",
                        "Porque la crítica de arte rechaza categóricamente las nuevas obras que produce."
                    ],
                    "correct": 1
                }
            ]
        },
        "b2-26-04-ex": {
            "lesson": "b2-26-04",
            "exercises": [
                {
                    "id": "b2-26-04.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["perifrasis-haber-que-impersonal"],
                    "question": "¿Cómo se conjuga el verbo auxiliar en la perífrasis impersonal de obligación 'haber que + infinitivo'?",
                    "options": [
                        "Concuerda en número y persona con el sustantivo que sigue al infinitivo.",
                        "Se conjuga exclusivamente en tercera persona del singular en todos los tiempos verbales.",
                        "Adopta formas reflexivas con el pronombre 'se' adherido al auxiliar.",
                        "Solo existe en modo imperativo afirmativo de segunda persona."
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-26-04.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["perifrasis-haber-que-impersonal"],
                    "sentence": "Para consolidar una cultura democrática basada en el respeto mutuo, __ que garantizar el derecho a la verdad.",
                    "answer": "hay",
                    "english": "In order to consolidate a democratic culture based on mutual respect, one must guarantee the right to truth."
                },
                {
                    "id": "b2-26-04.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["perifrasis-haber-que-impersonal"],
                    "question": "¿Qué matiz pragmático aporta 'habría que + infinitivo' en un debate formal sobre políticas públicas?",
                    "options": [
                        "Introduce una recomendación o sugerencia con cortesía y distanciamiento deliberado.",
                        "Formula una orden tajante y punitiva contra los legisladores opositores.",
                        "Constata un hecho consumado que ya no admite ninguna rectificación futura.",
                        "Expresa arrepentimiento moral por un error cometido en el ejercicio del cargo."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-26-04.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["perifrasis-haber-que-impersonal"],
                    "sentence": "Tras el estallido social del 2001, __ que reconstruir la confianza ciudadana en las instituciones representativas.",
                    "answer": "hubo",
                    "english": "After the social unrest of 2001, it was necessary to rebuild citizen trust in representative institutions."
                },
                {
                    "id": "b2-26-04.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-26-vocab"],
                    "pairs": [
                        ["el menester urgente", "the urgent necessity / task"],
                        ["la diligencia procesal", "the procedural diligence"],
                        ["el consenso mayoritario", "the majority consensus"],
                        ["el recaudo prudente", "the prudent safeguard / precaution"]
                    ]
                },
                {
                    "id": "b2-26-04.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué conclusión amarga extrae Castel al contemplar su relación con María a través de la imagen del túnel?",
                    "options": [
                        "Que ambos habitaban túneles paralelos y que las paredes de vidrio impidieron toda comunicación verdadera.",
                        "Que María logró rescatarlo del abismo de su locura mediante el amor conyugal.",
                        "Que el crimen fue un error judicial provocado por falsos testimonios de la servidumbre.",
                        "Que la soledad solo puede vencerse abandonando el arte de la pintura."
                    ],
                    "correct": 0
                }
            ]
        },
        "b2-26-05-ex": {
            "lesson": "b2-26-05",
            "exercises": [
                {
                    "id": "b2-26-05.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["perifrasis-modales-probabilidad-epistemica"],
                    "question": "¿Qué grado de certidumbre expresa la perífrasis 'debe de haber sido' en un análisis histórico retrospectivo?",
                    "options": [
                        "Certidumbre matemática absoluta respaldada por grabaciones directas.",
                        "Probabilidad deductiva alta basada en indicios e inferencias lógicas del contexto.",
                        "Duda radical e imposibilidad factual de que el acontecimiento haya tenido lugar.",
                        "Obligación jurídica impuesta por las normas vigentes en la época."
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-26-05.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["perifrasis-modales-probabilidad-epistemica"],
                    "sentence": "A juzgar por las contradicciones del relato, el sospechoso debió __ inventar su coartada de forma improvisada.",
                    "answer": "de",
                    "english": "Judging by the contradictions in the account, the suspect must have invented his alibi on the spur of the moment."
                },
                {
                    "id": "b2-26-05.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["perifrasis-modales-probabilidad-epistemica"],
                    "question": "¿En cuál de las siguientes opciones se utiliza una perífrasis de probabilidad para matizar una hipótesis psicológica?",
                    "options": [
                        "Castel tenía que asistir puntualmente al juicio penal en la capital.",
                        "El silencio prolongado de María debió de alimentar las sospechas más tortuosas del pintor.",
                        "Hay que pintar con pigmentos de calidad para que los lienzos perduren.",
                        "Debe usted firmar la declaración jurada ante el escribano."
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-26-05.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["perifrasis-modales-probabilidad-epistemica"],
                    "sentence": "Las privaciones padecidas en el cautiverio clandestino deben de haber __ una huella indeleble en las víctimas.",
                    "answer": "dejado",
                    "english": "The hardships endured in clandestine captivity must have left an indelible mark on the victims."
                },
                {
                    "id": "b2-26-05.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-26-vocab"],
                    "pairs": [
                        ["la verosimilitud narrativa", "the narrative verisimilitude"],
                        ["la inferencia analítica", "the analytical inference"],
                        ["la sospecha obsesiva", "the obsessive suspicion"],
                        ["la incertidumbre radical", "the radical uncertainty"]
                    ]
                },
                {
                    "id": "b2-26-05.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué desencadena el ataque final de Castel contra María en la estancia de Hunter?",
                    "options": [
                        "El descubrimiento de una carta donde María revelaba que lo consideraba un asesino en potencia.",
                        "La convicción delirante de que María era amante de Hunter y se burlaba de su búsqueda de pureza.",
                        "Una discusión acalorada sobre el valor monetario de los retratos que Castel había expuesto.",
                        "La negativa tajante de María a divorciarse formalmente de su esposo ciego Allende."
                    ],
                    "correct": 1
                }
            ]
        },
        "b2-26-consolidation-ex": {
            "lesson": "b2-26-consolidation",
            "exercises": [
                {
                    "id": "b2-26-consolidation.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["perifrasis-deber-obligacion-conjetura", "perifrasis-haber-de-infinitivo"],
                    "question": "¿Qué combinación modal completa con corrección formal: 'Los ciudadanos __ respetar los fallos, si bien los historiadores __ de evaluar sus alcances'?",
                    "options": [
                        "deben / habrán",
                        "deben de / tendrían",
                        "tienen / hubieran",
                        "hayan de / debieron de"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-26-consolidation.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["perifrasis-tener-que-infinitivo"],
                    "sentence": "Ante el colapso del sistema financiero en 2001, los sectores populares tuvieron que __ comedores comunitarios.",
                    "answer": "organizar",
                    "english": "Faced with the collapse of the financial system in 2001, popular sectors had to organize community soup kitchens."
                },
                {
                    "id": "b2-26-consolidation.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["perifrasis-haber-que-impersonal", "perifrasis-modales-probabilidad-epistemica"],
                    "question": "¿Cuál es la interpretación de: 'Habría que examinar con rigor los archivos; los testimonios deben de haber sido exhaustivos'?",
                    "options": [
                        "Una sugerencia impersonal prudente seguida de una conjetura de probabilidad basada en indicios.",
                        "Una prohibición legal absoluta seguida de una confirmación pericial irrevocable.",
                        "Un lamento amargo sobre la inutilidad de investigar los abusos del pasado.",
                        "Una orden perentoria dirigida exclusivamente a los secretarios del juzgado."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-26-consolidation.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["perifrasis-deber-obligacion-conjetura"],
                    "sentence": "A juzgar por las ovaciones atronadoras que colman el estadio, el delantero estrella debe __ haber marcado un gol de antología.",
                    "answer": "de",
                    "english": "Judging by the thunderous cheers filling the stadium, the star striker must have scored an unforgettable goal."
                },
                {
                    "id": "b2-26-consolidation.ex05",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["perifrasis-haber-de-infinitivo"],
                    "question": "¿Por qué es culta y solemne la frase: 'Aquel testimonio valiente de las Madres había de inspirar a generaciones enteras de defensores cívicos'?",
                    "options": [
                        "Porque emplea 'haber de' en imperfecto para proyectar un destino histórico ineludible y trascendente.",
                        "Porque sustituye de manera incorrecta al pretérito perfecto simple de indicativo.",
                        "Porque utiliza una voz pasiva sin sujeto paciente expreso.",
                        "Porque recurre a un modismo gauchesco propio de la poesía del Martín Fierro."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-26-consolidation.ex06",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["perifrasis-haber-que-impersonal"],
                    "sentence": "Para evitar que los abusos dictatoriales vuelvan a repetirse, __ que mantener viva la memoria en las aulas.",
                    "answer": "hay",
                    "english": "In order to prevent dictatorial abuses from recurring, one must keep memory alive in classrooms."
                },
                {
                    "id": "b2-26-consolidation.ex07",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-26-vocab"],
                    "pairs": [
                        ["el imperativo ético", "the ethical imperative"],
                        ["la plausibilidad de la tesis", "the plausibility of the thesis"],
                        ["la deducción verosímil", "the credible deduction"],
                        ["la prescripción legal", "the legal statutory limitation"]
                    ]
                },
                {
                    "id": "b2-26-consolidation.ex08",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Cómo se vincula el dilema de Castel en 'El túnel' con la problemática de la incomunicación humana?",
                    "options": [
                        "Castel demuestra que el arte figurativo es el único medio infalible para entender a los demás.",
                        "El protagonista revela la tragedia de mentes prisioneras de sus propios delirios deductivos, incapaces de aceptar la alteridad del otro.",
                        "La novela plantea que el aislamiento urbano se resuelve mudándose a estancias rurales de la provincia.",
                        "El autor argumenta que las instituciones judiciales operan siempre con perfecta empatía hacia los acusados."
                    ],
                    "correct": 1
                }
            ]
        },

        # Regional Unit 26 (Argentina III: b2-argentinasociedad)
        "b2-argentinasociedad-01-ex": {
            "lesson": "b2-argentinasociedad-01",
            "exercises": [
                {
                    "id": "b2-argentinasociedad-01.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["conectores-contraargumentativos-debate"],
                    "question": "¿Qué función cumple el conector culto 'antes bien' en: 'La proscripción no debilitó al movimiento; antes bien, afianzó su mística de resistencia'?",
                    "options": [
                        "Refuta categóricamente la primera afirmación para introducir una consecuencia opuesta y afirmativa de mayor fuerza.",
                        "Expresa una causa puramente cronológica que sitúa la proscripción antes de 1945.",
                        "Formula una concesión dudosa que desmiente el valor de las protestas sindicales.",
                        "Introduce un ejemplo decorativo sin trascendencia para el argumento central."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-argentinasociedad-01.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["conectores-contraargumentativos-debate"],
                    "sentence": "El gobierno justicialista amplió derechos sociales; no __, sus críticos denunciaron el creciente personalismo estatal.",
                    "answer": "obstante",
                    "english": "The Justicialist government expanded social rights; nevertheless, its critics denounced growing state personalism."
                },
                {
                    "id": "b2-argentinasociedad-01.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["conectores-contraargumentativos-debate"],
                    "question": "¿En cuál de las siguientes oraciones se utiliza 'ahora bien' para introducir una restricción deliberativa en el análisis histórico?",
                    "options": [
                        "Los obreros celebraron la jornada histórica del 17 de octubre en las plazas.",
                        "El régimen impulsó la industrialización; ahora bien, dependió de la renta agropecuaria para financiarla.",
                        "Evita viajó a Europa ahora bien recibida por diversas autoridades consulares.",
                        "Las elecciones se celebraron pacíficamente en todas las provincias del litoral."
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-argentinasociedad-01.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["conectores-contraargumentativos-debate"],
                    "sentence": "Las élites tradicionales rechazaron la movilización; por el __, los sindicatos la consagraron como su día fundacional.",
                    "answer": "contrario",
                    "english": "Traditional elites rejected the mobilization; on the contrary, trade unions consecrated it as their founding day."
                },
                {
                    "id": "b2-argentinasociedad-01.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-argentinasociedad-vocab"],
                    "pairs": [
                        ["la justicia social", "the social justice"],
                        ["la proscripción política", "the political banning / proscription"],
                        ["el voto femenino", "the women's suffrage / vote"],
                        ["la movilización obrera", "the working-class mobilization"]
                    ]
                },
                {
                    "id": "b2-argentinasociedad-01.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Cuál fue el papel histórico de Eva Perón respecto a los derechos cívicos de las mujeres argentinas?",
                    "options": [
                        "Se opuso a la participación femenina en las asambleas políticas de los sindicatos.",
                        "Lideró la campaña de concienciación y la aprobación legislativa de la ley del sufragio femenino en 1947.",
                        "Fundó el primer banco internacional de crédito exclusivo para empresarias textiles.",
                        "Exigió que las mujeres renunciaran al empleo fabril para dedicarse a labores hogareñas."
                    ],
                    "correct": 1
                }
            ]
        },
        "b2-argentinasociedad-02-ex": {
            "lesson": "b2-argentinasociedad-02",
            "exercises": [
                {
                    "id": "b2-argentinasociedad-02.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["voz-pasiva-perifrastica-denuncia"],
                    "question": "¿Por qué la voz pasiva analítica es frecuente en la documentación sobre derechos humanos ('Los ciudadanos fueron secuestrados')?",
                    "options": [
                        "Porque resalta a la víctima y la acción criminal como foco sintáctico en un registro documental formal y riguroso.",
                        "Porque oculta intencionadamente la responsabilidad penal de los perpetradores de los hechos.",
                        "Porque es la única estructura gramatical admitida por los códigos de procedimiento civil.",
                        "Porque el idioma español prohíbe el uso de oraciones activas al describir situaciones bélicas."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-argentinasociedad-02.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["voz-pasiva-perifrastica-denuncia"],
                    "sentence": "Cientos de centros clandestinos de detención __ instalados en dependencias militares durante la dictadura.",
                    "answer": "fueron",
                    "english": "Hundreds of clandestine detention centers were set up in military facilities during the dictatorship."
                },
                {
                    "id": "b2-argentinasociedad-02.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["voz-pasiva-perifrastica-denuncia"],
                    "question": "¿Cómo concuerda el participio en la voz pasiva analítica en: 'Las sentencias condenatorias fueron ratificadas por el tribunal'?",
                    "options": [
                        "Permanece en masculino singular invariable.",
                        "Concuerda obligatoriamente en género femenino y número plural con el sujeto paciente.",
                        "Concuerda con el complemento agente que realiza la acción.",
                        "Se transforma en un gerundio compuesto invariable."
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-argentinasociedad-02.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["voz-pasiva-perifrastica-denuncia"],
                    "sentence": "En el marco de la investigación judicial, se __ pruebas documentales decisivas sobre los crímenes cometidos.",
                    "answer": "aportaron",
                    "english": "Within the framework of the judicial investigation, decisive documentary evidence was submitted on the crimes committed."
                },
                {
                    "id": "b2-argentinasociedad-02.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-argentinasociedad-vocab"],
                    "pairs": [
                        ["el centro clandestino", "the clandestine detention center"],
                        ["la detención ilegal", "the unlawful detention / kidnapping"],
                        ["la soberanía territorial", "the territorial sovereignty"],
                        ["el terrorismo de estado", "the state terrorism"]
                    ]
                },
                {
                    "id": "b2-argentinasociedad-02.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué consecuencia política inmediata provocó la derrota de la dictadura militar en la guerra de Malvinas en 1982?",
                    "options": [
                        "La consolidación de un nuevo gobierno castrense que gobernó durante veinte años adicionales.",
                        "El colapso irreversible del régimen autoritario y la reapertura democrática con elecciones libres en 1983.",
                        "La disolución completa de los tribunales de justicia y de las universidades nacionales.",
                        "La firma de un tratado de unión política y aduanera con el Reino Unido."
                    ],
                    "correct": 1
                }
            ]
        },
        "b2-argentinasociedad-03-ex": {
            "lesson": "b2-argentinasociedad-03",
            "exercises": [
                {
                    "id": "b2-argentinasociedad-03.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["subjuntivo-oraciones-relativas-memoria"],
                    "question": "¿Por qué se utiliza el subjuntivo en: 'Las Abuelas buscan a jóvenes que sospechen sobre su verdadera identidad'?",
                    "options": [
                        "Porque el antecedente es inespecífico y su identidad exacta no está aún individualizada en la realidad.",
                        "Porque el emisor niega categóricamente que existan personas con identidades falsificadas.",
                        "Porque las oraciones de relativo sobre derechos humanos rechazan siempre el modo indicativo.",
                        "Porque el verbo 'buscar' es impersonal y exige una subordinada adverbial."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-argentinasociedad-03.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["subjuntivo-oraciones-relativas-memoria"],
                    "sentence": "No existe tribunal independiente que __ convalidar la impunidad de crímenes de lesa humanidad.",
                    "answer": "pueda",
                    "english": "There is no independent court that can validate impunity for crimes against humanity."
                },
                {
                    "id": "b2-argentinasociedad-03.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["subjuntivo-oraciones-relativas-memoria"],
                    "question": "¿Cuándo cambia la cláusula de relativo del subjuntivo al indicativo en el discurso de restitución de identidad?",
                    "options": [
                        "Cuando el nieto buscado es finalmente identificado y sus datos biológicos son contrastados fácticamente.",
                        "Únicamente cuando el juicio se traslada a un tribunal penal internacional en La Haya.",
                        "Cuando la persona decide renunciar a su ciudadanía original.",
                        "Siempre que el antecedente esté encabezado por un pronombre indefinido negativo."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-argentinasociedad-03.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["subjuntivo-oraciones-relativas-memoria"],
                    "sentence": "Cualquier ciudadano que __ datos fidedignos sobre nietos apropiados debe acercarse a la asociación.",
                    "answer": "tenga",
                    "english": "Any citizen who may have reliable information on appropriated grandchildren must approach the association."
                },
                {
                    "id": "b2-argentinasociedad-03.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-argentinasociedad-vocab"],
                    "pairs": [
                        ["el pañuelo blanco", "the white headscarf emblem"],
                        ["el índice de abuelidad", "the genetic grandparenthood index"],
                        ["la restitución de identidad", "the identity recovery / restitution"],
                        ["el banco de datos genéticos", "the national genetic database"]
                    ]
                },
                {
                    "id": "b2-argentinasociedad-03.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué innovación científica de trascendencia mundial promovieron las Abuelas de Plaza de Mayo en la década de 1980?",
                    "options": [
                        "El diseño del 'índice de abuelidad' basado en genética para identificar la filiación familiar ante la ausencia de los padres.",
                        "Un método de datación por carbono catorce para verificar la antigüedad de las prisiones coloniales.",
                        "Un programa informático de reconocimiento facial para aeropuertos internacionales.",
                        "Una vacuna preventiva contra enfermedades epidémicas tropicales."
                    ],
                    "correct": 0
                }
            ]
        },
        "b2-argentinasociedad-04-ex": {
            "lesson": "b2-argentinasociedad-04",
            "exercises": [
                {
                    "id": "b2-argentinasociedad-04.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["estructuras-ponderativas-pasion-popular"],
                    "question": "¿Qué valor sintáctico aporta la estructura hendida de relieve en: 'Fue en el potrero donde floreció la picardía de la gambeta criolla'?",
                    "options": [
                        "Focaliza y enfatiza el espacio originario humble como factor determinante del estilo futbolístico nacional.",
                        "Expresa una duda radical sobre si el potrero existió en los barrios de Buenos Aires.",
                        "Indica una causa puramente monetaria que motivó la construcción de nuevos estadios.",
                        "Introduce una hipótesis condicional que invalida la victoria en los torneos mundiales."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-argentinasociedad-04.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["estructuras-ponderativas-pasion-popular"],
                    "sentence": "Tal fue la emoción popular tras la victoria en Qatar __ millones de personas colmaron las calles de la capital.",
                    "answer": "que",
                    "english": "Such was the popular emotion after the victory in Qatar that millions of people filled the streets of the capital."
                },
                {
                    "id": "b2-argentinasociedad-04.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["estructuras-ponderativas-pasion-popular"],
                    "question": "¿Cuál de las siguientes frases utiliza una estructura consecutiva ponderativa para describir la euforia colectiva?",
                    "options": [
                        "El partido terminó empatado a tres goles tras la prórroga reglamentaria.",
                        "La marea humana fue tan multitudinaria que desbordó por completo las principales autopistas porteñas.",
                        "Los jugadores viajaron en un autobús descapotable escoltado por agentes de seguridad.",
                        "Se vendieron todas las entradas para presenciar la final en el estadio de Lusail."
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-argentinasociedad-04.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["estructuras-ponderativas-pasion-popular"],
                    "sentence": "Pocas manifestaciones cívicas despiertan un fervor __ unánime como la conquista de una copa del mundo.",
                    "answer": "tan",
                    "english": "Few civic demonstrations awaken such a unanimous fervor as the conquest of a World Cup."
                },
                {
                    "id": "b2-argentinasociedad-04.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-argentinasociedad-vocab"],
                    "pairs": [
                        ["el potrero barrial", "the vacant lot street pitch"],
                        ["la gambeta criolla", "the deceptive body feint / dribble"],
                        ["la catarsis colectiva", "the collective catharsis / release"],
                        ["la mística popular", "the popular mystique / aura"]
                    ]
                },
                {
                    "id": "b2-argentinasociedad-04.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué significado simbólico tuvo el partido de cuartos de final de México 1986 entre Argentina e Inglaterra?",
                    "options": [
                        "Fue percibido como una revancha pacífica y artística tras las dolorosas heridas de la guerra de Malvinas.",
                        "Marcó el debut internacional de Lionel Messi a la edad de dieciocho años.",
                        "Provocó la suspensión de los campeonatos profesionales de fútbol en Sudamérica.",
                        "Fue el primer partido transmitido exclusivamente a través de satélites espaciales."
                    ],
                    "correct": 0
                }
            ]
        },
        "b2-argentinasociedad-05-ex": {
            "lesson": "b2-argentinasociedad-05",
            "exercises": [
                {
                    "id": "b2-argentinasociedad-05.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["oraciones-causales-explicativas-crisis"],
                    "question": "¿Qué relación argumentativa establece la locución 'dado que' en: 'Dado que los bancos confiscaron los ahorros, estalló el cacerolazo'?",
                    "options": [
                        "Introduce una causa factual plenamente constatada que fundamenta lógicamente la reacción social posterior.",
                        "Expresa una condición hipotética sin valor en el mundo económico real.",
                        "Plantea una objeción que desmiente la existencia de protestas en las calles.",
                        "Señala una coincidencia temporal casual entre dos acontecimientos inconexos."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-argentinasociedad-05.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["oraciones-causales-explicativas-crisis"],
                    "sentence": "En vista de que el dinero circulante escaseaba, las familias __ a los clubes de trueque comunitario.",
                    "answer": "acudieron",
                    "english": "In view of the fact that circulating cash was scarce, families turned to community barter clubs."
                },
                {
                    "id": "b2-argentinasociedad-05.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["oraciones-causales-explicativas-crisis"],
                    "question": "¿Cuál es el modo verbal requerido tras conectores causales factuales como 'puesto que' o 'dado que' en el ensayo sociológico?",
                    "options": [
                        "Modo indicativo, pues presentan causas verificadas y asumidas como verdaderas por el emisor.",
                        "Modo subjuntivo imperativo en todos los casos de crisis económica.",
                        "Infinitivo simple precedido de preposición concesiva obligatoria.",
                        "Participio pasivo invariable de tercera persona."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-argentinasociedad-05.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["oraciones-causales-explicativas-crisis"],
                    "sentence": "Puesto que la moneda oficial había perdido liquidez, los vecinos __ bonos comunitarios para intercambiar alimentos.",
                    "answer": "emplearon",
                    "english": "Since the official currency had lost liquidity, neighbors used community vouchers to exchange food."
                },
                {
                    "id": "b2-argentinasociedad-05.ex05",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-argentinasociedad-vocab"],
                    "pairs": [
                        ["el corralito financiero", "the bank cash withdrawal freeze"],
                        ["el club de trueque", "the community barter exchange network"],
                        ["el cacerolazo masivo", "the massive pot-banging protest"],
                        ["la fábrica recuperada", "the worker-recovered factory"]
                    ]
                },
                {
                    "id": "b2-argentinasociedad-05.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Cómo respondió la sociedad civil argentina ante la parálisis del sistema bancario y del Estado en diciembre de 2001?",
                    "options": [
                        "Mediante redes de trueque comunitario, asambleas barriales autoconvocadas y cooperativas de empresas recuperadas.",
                        "Aceptando la dolarización total del salario y la clausura de las universidades públicas.",
                        "Exigiendo la disolución de todas las organizaciones vecinales en favor del ejército.",
                        "Emigrando masivamente hacia el interior rural sin realizar reclamos en la capital."
                    ],
                    "correct": 0
                }
            ]
        },
        "b2-argentinasociedad-consolidation-ex": {
            "lesson": "b2-argentinasociedad-consolidation",
            "exercises": [
                {
                    "id": "b2-argentinasociedad-consolidation.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["conectores-contraargumentativos-debate", "voz-pasiva-perifrastica-denuncia"],
                    "question": "¿Qué opción combina correctamente el contraste argumentativo y la voz pasiva analítica?",
                    "options": [
                        "Los decretos de impunidad buscaron silenciar el pasado; no obstante, las leyes fueron anuladas por el Congreso.",
                        "Los decretos de impunidad buscaron silenciar el pasado; no obstante, las leyes fue anulada por el Congreso.",
                        "Los decretos de impunidad buscaron silenciar el pasado; por tanto, las leyes fueron anulado por el Congreso.",
                        "Los decretos de impunidad buscaron silenciar el pasado; antes bien, las leyes se anular por el Congreso."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-argentinasociedad-consolidation.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["subjuntivo-oraciones-relativas-memoria"],
                    "sentence": "No hay decreto ni ley que __ borrar el reclamo indeclinable de Memoria, Verdad y Justicia.",
                    "answer": "pueda",
                    "english": "There is no decree or law that can erase the undeniable demand for Memory, Truth, and Justice."
                },
                {
                    "id": "b2-argentinasociedad-consolidation.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["estructuras-ponderativas-pasion-popular", "oraciones-causales-explicativas-crisis"],
                    "question": "¿Qué relación sintáctica se establece en: 'Dado que la pasión por el fútbol es inmensa, tal fue la euforia que paralizó el país'?",
                    "options": [
                        "Una cláusula causal compleja seguida de una estructura consecutiva ponderativa que enfatiza la magnitud del festejo.",
                        "Una condición contrafáctica irreal que lamenta la derrota del seleccionado nacional.",
                        "Una oración concesiva restrictiva que minimiza el impacto social de la victoria.",
                        "Una pasiva refleja impersonal que elude la mención del sujeto colectivo."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-argentinasociedad-consolidation.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["conectores-contraargumentativos-debate"],
                    "sentence": "Las crisis económicas golpearon con dureza a los hogares; por el __, la solidaridad barrial sostuvo a las comunidades.",
                    "answer": "contrario",
                    "english": "Economic crises struck households harshly; on the contrary, neighborhood solidarity sustained communities."
                },
                {
                    "id": "b2-argentinasociedad-consolidation.ex05",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["voz-pasiva-perifrastica-denuncia"],
                    "question": "¿Cuál de las siguientes frases utiliza la voz pasiva de manera rigurosa y formal?",
                    "options": [
                        "Las pruebas testimoniales fueron incorporadas al expediente judicial por los fiscales federales.",
                        "Las pruebas testimoniales fue incorporado al expediente judicial por los fiscales federales.",
                        "Los fiscales federales se incorporaron las pruebas sin revisar los folios.",
                        "Fueron incorporar las pruebas testimoniales en el tribunal supremo."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-argentinasociedad-consolidation.ex06",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["estructuras-ponderativas-pasion-popular"],
                    "sentence": "Fue en las calles de la capital __ convergieron millones de ciudadanos para celebrar el título mundial.",
                    "answer": "donde",
                    "english": "It was in the streets of the capital where millions of citizens converged to celebrate the world title."
                },
                {
                    "id": "b2-argentinasociedad-consolidation.ex07",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-argentinasociedad-vocab"],
                    "pairs": [
                        ["la memoria colectiva", "the collective memory"],
                        ["la resiliencia popular", "the popular resilience"],
                        ["la cohesión ciudadana", "the citizen cohesion"],
                        ["la fragua democrática", "the democratic forge / crucible"]
                    ]
                },
                {
                    "id": "b2-argentinasociedad-consolidation.ex08",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Cuál es la conclusión integradora que plantea el texto de consolidación regional sobre la fragua cívica argentina?",
                    "options": [
                        "Que la ciudadanía argentina ha forjado una identidad indoblegable basada en la defensa de sus derechos, la memoria y la pasión comunitaria.",
                        "Que las sucesivas crisis económicas eliminaron para siempre cualquier interés por la participación política.",
                        "Que los derechos laborales y humanos fueron otorgados pacíficamente sin necesidad de debate ni movilización.",
                        "Que la cultura deportiva es incompatible con la reflexión crítica y el compromiso con la justicia social."
                    ],
                    "correct": 0
                }
            ]
        }
    }

    for ex_stem, ex_obj in exercise_files.items():
        write_json(f"exercises/b2/{ex_stem}.json", ex_obj)

    # 7. Lessons (12 files)
    # Core Lessons: b2-26
    core_lessons = [
        ("b2-26-01", "La obligación moral y la conjetura: Deber vs. Deber de + infinitivo", "b2-26-01-a-gr", "b2-26-01-voc", "b2-26-01-ex", "stories/classics/b2/b2-26.json"),
        ("b2-26-02", "El deber formal y el destino ineludible: Haber de + infinitivo", "b2-26-02-a-gr", "b2-26-02-voc", "b2-26-02-ex", None),
        ("b2-26-03", "La necesidad objetiva y la imposición externa: Tener que + infinitivo", "b2-26-03-a-gr", "b2-26-03-voc", "b2-26-03-ex", None),
        ("b2-26-04", "La obligación universal e impersonal: Haber que + infinitivo", "b2-26-04-a-gr", "b2-26-04-voc", "b2-26-04-ex", None),
        ("b2-26-05", "La calibración epistémica de la probabilidad y la conjetura", "b2-26-05-a-gr", "b2-26-05-voc", "b2-26-05-ex", None)
    ]

    for stem, title, gr_stem, voc_stem, ex_stem, story_ref in core_lessons:
        sections = []
        if story_ref:
            sections.append({"type": "story", "ref": story_ref})
        sections.append({"type": "grammar", "ref": f"grammar/b2/{gr_stem}.json"})
        sections.append({"type": "vocabulary", "ref": f"vocabulary/b2/{voc_stem}.json"})
        sections.append({"type": "exercise-group", "title": "Practice", "ref": f"exercises/b2/{ex_stem}.json", "exerciseRefs": [f"{stem}.ex0{i}" for i in range(1, 7)]})

        write_json(f"lessons/b2/{stem}.json", {
            "id": f"lesson.{stem.replace('-', '.')}",
            "title": title,
            "level": "B2",
            "sections": sections
        })

    # Core Consolidation
    write_json("lessons/b2/b2-26-consolidation.json", {
        "id": "lesson.b2.26.consolidation",
        "title": "Consolidación: Perífrasis modales de conjetura y deber",
        "level": "B2",
        "sections": [
            {"type": "goal", "items": [
                "Dominar las perífrasis modales de obligación y conjetura (deber, deber de, haber de, tener que, haber que).",
                "Calibrar con exactitud el grado de certidumbre, deducción epistémica y necesidad en la argumentación.",
                "Integrar el léxico especializado de la deducción, el deber cívico y la introspección existencial."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "exercise-group", "title": "Review", "ref": "exercises/b2/b2-26-consolidation-ex.json", "exerciseRefs": [f"b2-26-consolidation.ex0{i}" for i in range(1, 9)]},
            {"type": "checklist", "items": [
                "Distingo con rigor normativo entre 'deber + infinitivo' (obligación) y 'deber de + infinitivo' (conjetura).",
                "Utilizo 'haber de + infinitivo' en prosa formal para expresar mandatos atenuados y destinos inevitables.",
                "Empleo 'tener que + infinitivo' para constatar necesidades objetivas e imposiciones materiales externas.",
                "Aplico la forma impersonal 'haber que + infinitivo' para formular prioridades institucionales y comunitarias.",
                "Interpreto la prosa existencialista de Ernesto Sabato valorando los matices de conjetura y certeza obsesiva."
            ]}
        ]
    })

    # Regional Lessons: b2-argentinasociedad
    regional_lessons = [
        ("b2-argentinasociedad-01", "El peronismo: Fenómeno de masas, justicia social y polarización", "b2-argentinasociedad-01-a-gr", "b2-argentinasociedad-01-voc", "b2-argentinasociedad-01-ex", "stories/world/b2/b2-argentinasociedad-01.json"),
        ("b2-argentinasociedad-02", "La última dictadura militar (1976–1983) y la guerra de Malvinas", "b2-argentinasociedad-02-a-gr", "b2-argentinasociedad-02-voc", "b2-argentinasociedad-02-ex", "stories/world/b2/b2-argentinasociedad-02.json"),
        ("b2-argentinasociedad-03", "Las Madres y Abuelas de Plaza de Mayo: El triunfo de la memoria", "b2-argentinasociedad-03-a-gr", "b2-argentinasociedad-03-voc", "b2-argentinasociedad-03-ex", "stories/world/b2/b2-argentinasociedad-03.json"),
        ("b2-argentinasociedad-04", "El fútbol como religión laica: De Maradona a Messi", "b2-argentinasociedad-04-a-gr", "b2-argentinasociedad-04-voc", "b2-argentinasociedad-04-ex", "stories/world/b2/b2-argentinasociedad-04.json"),
        ("b2-argentinasociedad-05", "Crisis económicas recurrentes, el corralito y la resiliencia social", "b2-argentinasociedad-05-a-gr", "b2-argentinasociedad-05-voc", "b2-argentinasociedad-05-ex", "stories/world/b2/b2-argentinasociedad-05.json")
    ]

    for stem, title, gr_stem, voc_stem, ex_stem, story_ref in regional_lessons:
        write_json(f"lessons/b2/{stem}.json", {
            "id": f"lesson.{stem.replace('-', '.')}",
            "title": title,
            "level": "B2",
            "sections": [
                {"type": "story", "ref": story_ref},
                {"type": "grammar", "ref": f"grammar/b2/{gr_stem}.json"},
                {"type": "vocabulary", "ref": f"vocabulary/b2/{voc_stem}.json"},
                {"type": "exercise-group", "title": "Practice", "ref": f"exercises/b2/{ex_stem}.json", "exerciseRefs": [f"{stem}.ex0{i}" for i in range(1, 7)]}
            ]
        })

    # Regional Consolidation
    write_json("lessons/b2/b2-argentinasociedad-consolidation.json", {
        "id": "lesson.b2.argentinasociedad.consolidation",
        "title": "Consolidación: La fragua cívica argentina",
        "level": "B2",
        "sections": [
            {"type": "goal", "items": [
                "Integrar la visión histórica, sociológica y cultural de las grandes pasiones y tensiones cívicas argentinas.",
                "Consolidar el léxico de la doctrina justicialista, los derechos humanos, la sociología deportiva y las crisis financieras.",
                "Dominar recursos de argumentación avanzada: conectores contraargumentativos, voz pasiva de denuncia y relativas con subjuntivo."
            ]},
            {"type": "recycle", "count": 3},
            {"type": "story", "ref": "stories/world/b2/b2-argentinasociedad-consolidation.json"},
            {"type": "exercise-group", "title": "Review", "ref": "exercises/b2/b2-argentinasociedad-consolidation-ex.json", "exerciseRefs": [f"b2-argentinasociedad-consolidation.ex0{i}" for i in range(1, 9)]},
            {"type": "checklist", "items": [
                "Analizo el surgimiento del peronismo y el rol histórico de Eva Perón en el sufragio femenino.",
                "Comprendo la magnitud del terrorismo de Estado y la dimensión geoestratégica del conflicto de Malvinas.",
                "Reconozco la gesta ética de Madres y Abuelas de Plaza de Mayo y los avances del índice de abuelidad genético.",
                "Interpreto la función del fútbol como catarsis comunitaria desde Maradona hasta el campeonato mundial de Messi.",
                "Evalúo la respuesta popular de autogestión y trueque frente al colapso socioeconómico del corralito de 2001.",
                "Aplico con solvencia los conectores de debate, las cláusulas causales complejas y las relativas de búsqueda."
            ]}
        ]
    })

    # 8. Update content/es-latam/curriculum/units/b2.json
    def update_curriculum_units(units):
        existing_titles = {u.get("title") for u in units}
        new_units = [
            {
                "title": "Modal Periphrases of Conjecture & Duty",
                "stems": [
                    "b2-26-01",
                    "b2-26-02",
                    "b2-26-03",
                    "b2-26-04",
                    "b2-26-05",
                    "b2-26-consolidation"
                ],
                "track": "core"
            },
            {
                "title": "Argentina III: Politics, Passion, Peronism & The Human Rights Movement",
                "stems": [
                    "b2-argentinasociedad-01",
                    "b2-argentinasociedad-02",
                    "b2-argentinasociedad-03",
                    "b2-argentinasociedad-04",
                    "b2-argentinasociedad-05",
                    "b2-argentinasociedad-consolidation"
                ],
                "track": "regional"
            }
        ]
        for nu in new_units:
            if nu["title"] not in existing_titles:
                units.append(nu)
        return units

    update_json_file(os.path.join(LATAM_DIR, "curriculum", "units", "b2.json"), update_curriculum_units)
    print("Updated curriculum/units/b2.json with Unit 26!")

if __name__ == "__main__":
    main()
