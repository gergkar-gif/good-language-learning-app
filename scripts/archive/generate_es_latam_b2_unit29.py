# -*- coding: utf-8 -*-
"""
Generator script for Latin American Spanish (es-latam) B2 Unit 29:
- Core B2: b2-29 (Discourse Markers II: Reformulation & Precision)
- Regional B2: b2-brasilsudeste (Brazil I: The Cultural Engines: Rio, São Paulo & Modernism)
- Classic Literature Adaptation: Machado de Assis - Dom Casmurro (1899)
"""

import os
import json
import re

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
            "marcadores-reformulacion-explicativa": {
                "kind": "grammar",
                "name": "marcadores-reformulacion-explicativa",
                "description": "Explanatory reformulation discourse markers such as es decir, o sea, esto es, a saber",
                "aliases": []
            },
            "marcadores-reformulacion-rectificativa": {
                "kind": "grammar",
                "name": "marcadores-reformulacion-rectificativa",
                "description": "Rectifying reformulation discourse markers including mejor dicho, más bien, más exactamente",
                "aliases": []
            },
            "marcadores-reformulacion-distanciamiento": {
                "kind": "grammar",
                "name": "marcadores-reformulacion-distanciamiento",
                "description": "Distancing reformulation discourse markers such as de todos modos, en cualquier caso, de cualquier manera",
                "aliases": []
            },
            "marcadores-reformulacion-recapitulativa": {
                "kind": "grammar",
                "name": "marcadores-reformulacion-recapitulativa",
                "description": "Recapitulative reformulation discourse markers including dicho en otros términos, en otras palabras",
                "aliases": []
            },
            "marcadores-reformulacion-ejemplificativa": {
                "kind": "grammar",
                "name": "marcadores-reformulacion-ejemplificativa",
                "description": "Exemplifying reformulation markers such as a modo de ilustración, por poner un caso, verbigracia",
                "aliases": []
            },
            "b2-29-vocab": {
                "kind": "vocabulary",
                "name": "b2-29-vocab",
                "description": "Vocabulary for semantic precision, rhetoric, conceptual refinement, and philosophical analysis",
                "aliases": []
            },
            "brasil-conectores-contraste": {
                "kind": "grammar",
                "name": "brasil-conectores-contraste",
                "description": "Contrastive discourse markers in urban analysis such as mientras que, en contrapartida, por el contrario",
                "aliases": []
            },
            "brasil-oraciones-relativas-especificativas": {
                "kind": "grammar",
                "name": "brasil-oraciones-relativas-especificativas",
                "description": "Restrictive and explanatory relative clauses in geographical description and landscape analysis",
                "aliases": []
            },
            "brasil-voz-media-pronominal": {
                "kind": "grammar",
                "name": "brasil-voz-media-pronominal",
                "description": "Pronominal middle voice in aesthetic and modern art analysis",
                "aliases": []
            },
            "brasil-adverbios-foco": {
                "kind": "grammar",
                "name": "brasil-adverbios-foco",
                "description": "Focusing adverbs and scalar markers in cultural discourse including precisamente, inclusive, hasta",
                "aliases": []
            },
            "brasil-comparativas-proporcionales": {
                "kind": "grammar",
                "name": "brasil-comparativas-proporcionales",
                "description": "Proportional comparative structures in cross-cultural analysis with cuanto más... tanto más, a medida que",
                "aliases": []
            },
            "b2-brasilsudeste-vocab": {
                "kind": "vocabulary",
                "name": "b2-brasilsudeste-vocab",
                "description": "Vocabulary for Brazilian southeast culture, Paulistano industry, Carioca urbanism, modernism, and Bossa Nova",
                "aliases": []
            }
        }
        for k, v in new_skills.items():
            skills[k] = v
        return registry

    update_json_file(os.path.join(LATAM_DIR, "indexes", "skill-registry.json"), update_skill_registry)
    print("Updated skill-registry.json for Unit 29")

    # 2. Update grammar-titles.json
    def update_grammar_titles(titles):
        new_titles = {
            "marcadores-reformulacion-explicativa": "explanatory reformulation discourse markers",
            "marcadores-reformulacion-rectificativa": "rectifying reformulation discourse markers",
            "marcadores-reformulacion-distanciamiento": "distancing reformulation discourse markers",
            "marcadores-reformulacion-recapitulativa": "recapitulative reformulation discourse markers",
            "marcadores-reformulacion-ejemplificativa": "exemplifying reformulation discourse markers",
            "brasil-conectores-contraste": "contrastive discourse markers in urban analysis",
            "brasil-oraciones-relativas-especificativas": "restrictive and explanatory relative clauses in geographical description",
            "brasil-voz-media-pronominal": "pronominal middle voice in aesthetic analysis",
            "brasil-adverbios-foco": "focusing adverbs and scalar markers in cultural discourse",
            "brasil-comparativas-proporcionales": "proportional comparative structures in cross-cultural analysis"
        }
        for k, v in new_titles.items():
            titles[k] = v
        return titles

    update_json_file(os.path.join(LATAM_DIR, "indexes", "grammar-titles.json"), update_grammar_titles)
    print("Updated grammar-titles.json for Unit 29")

    # 3. Vocabulary files
    vocab_data = {
        "b2-29-01": {
            "id": "vocab.b2.29.01",
            "lesson": "b2-29-01",
            "title": "Explanatory Reformulation and Semantic Precision",
            "words": [
                {"lemma": "esclarecimiento", "translation": "clarification", "pos": "noun"},
                {"lemma": "inequívoco", "translation": "unequivocal", "pos": "adjective"},
                {"lemma": "reformular", "translation": "to reformulate", "pos": "verb"},
                {"lemma": "semántica", "translation": "semantics", "pos": "noun"},
                {"lemma": "matiz", "translation": "nuance", "pos": "noun"},
                {"lemma": "pertinente", "translation": "pertinent / relevant", "pos": "adjective"}
            ]
        },
        "b2-29-02": {
            "id": "vocab.b2.29.02",
            "lesson": "b2-29-02",
            "title": "Rectifying and Corrective Reformulation",
            "words": [
                {"lemma": "enmienda", "translation": "amendment / correction", "pos": "noun"},
                {"lemma": "rectificación", "translation": "rectification", "pos": "noun"},
                {"lemma": "enmendar", "translation": "to amend / rectify", "pos": "verb"},
                {"lemma": "falso cognado", "translation": "false cognate", "pos": "noun"},
                {"lemma": "aparente", "translation": "apparent / deceptive", "pos": "adjective"},
                {"lemma": "precisión", "translation": "precision / accuracy", "pos": "noun"}
            ]
        },
        "b2-29-03": {
            "id": "vocab.b2.29.03",
            "lesson": "b2-29-03",
            "title": "Distancing Reformulation and Argumentative Reserve",
            "words": [
                {"lemma": "escepticismo", "translation": "skepticism", "pos": "noun"},
                {"lemma": "salvedad", "translation": "caveat / reservation", "pos": "noun"},
                {"lemma": "distanciamiento", "translation": "distancing / detachment", "pos": "noun"},
                {"lemma": "cautela", "translation": "caution / prudence", "pos": "noun"},
                {"lemma": "ponderar", "translation": "to weigh / ponder", "pos": "verb"},
                {"lemma": "relativizar", "translation": "to relativize / contextualize", "pos": "verb"}
            ]
        },
        "b2-29-04": {
            "id": "vocab.b2.29.04",
            "lesson": "b2-29-04",
            "title": "Recapitulative Paraphrase and Synthesis",
            "words": [
                {"lemma": "paráfrasis", "translation": "paraphrase", "pos": "noun"},
                {"lemma": "equivalencia", "translation": "equivalence", "pos": "noun"},
                {"lemma": "condensación", "translation": "condensation / summary", "pos": "noun"},
                {"lemma": "sinopsis", "translation": "synopsis", "pos": "noun"},
                {"lemma": "compendiar", "translation": "to abridge / summarize", "pos": "verb"},
                {"lemma": "conciso", "translation": "concise", "pos": "adjective"}
            ]
        },
        "b2-29-05": {
            "id": "vocab.b2.29.05",
            "lesson": "b2-29-05",
            "title": "Exemplification and Case Illustration",
            "words": [
                {"lemma": "arquetipo", "translation": "archetype", "pos": "noun"},
                {"lemma": "paradigma", "translation": "paradigm", "pos": "noun"},
                {"lemma": "ejemplificar", "translation": "to exemplify", "pos": "verb"},
                {"lemma": "ilustración", "translation": "illustration / example", "pos": "noun"},
                {"lemma": "representativo", "translation": "representative", "pos": "adjective"},
                {"lemma": "caso testigo", "translation": "test case / benchmark", "pos": "noun"}
            ]
        },
        "b2-brasilsudeste-01": {
            "id": "vocab.b2.brasilsudeste.01",
            "lesson": "b2-brasilsudeste-01",
            "title": "São Paulo: Metropolis, Coffee and Global Industry",
            "words": [
                {"lemma": "metrópolis", "translation": "metropolis", "pos": "noun"},
                {"lemma": "cafetalero", "translation": "coffee-growing / coffee-related", "pos": "adjective"},
                {"lemma": "pujanza", "translation": "vigor / economic strength", "pos": "noun"},
                {"lemma": "conurbación", "translation": "conurbation", "pos": "noun"},
                {"lemma": "polo", "translation": "hub / center", "pos": "noun"},
                {"lemma": "cosmopolita", "translation": "cosmopolitan", "pos": "adjective"}
            ]
        },
        "b2-brasilsudeste-02": {
            "id": "vocab.b2.brasilsudeste.02",
            "lesson": "b2-brasilsudeste-02",
            "title": "Rio de Janeiro: Morros, Guanabara and Urban Landscape",
            "words": [
                {"lemma": "morro", "translation": "granite hill / morro", "pos": "noun"},
                {"lemma": "favela", "translation": "favela / informal community", "pos": "noun"},
                {"lemma": "bahía", "translation": "bay", "pos": "noun"},
                {"lemma": "idiosincrasia", "translation": "idiosyncrasy / cultural character", "pos": "noun"},
                {"lemma": "topografía", "translation": "topography", "pos": "noun"},
                {"lemma": "festivo", "translation": "festive", "pos": "adjective"}
            ]
        },
        "b2-brasilsudeste-03": {
            "id": "vocab.b2.brasilsudeste.03",
            "lesson": "b2-brasilsudeste-03",
            "title": "Modernist Week of 1922 and Cultural Cannibalism",
            "words": [
                {"lemma": "vanguardia", "translation": "avant-garde", "pos": "noun"},
                {"lemma": "antropofagia", "translation": "cultural cannibalism / anthropophagy", "pos": "noun"},
                {"lemma": "manifiesto", "translation": "manifesto", "pos": "noun"},
                {"lemma": "ruptura", "translation": "rupture / aesthetic break", "pos": "noun"},
                {"lemma": "devorar", "translation": "to devour / assimilate", "pos": "verb"},
                {"lemma": "rupturista", "translation": "groundbreaking / iconoclastic", "pos": "adjective"}
            ]
        },
        "b2-brasilsudeste-04": {
            "id": "vocab.b2.brasilsudeste.04",
            "lesson": "b2-brasilsudeste-04",
            "title": "Samba, Bossa Nova and Tropicalismo",
            "words": [
                {"lemma": "síncopa", "translation": "syncope / syncopation", "pos": "noun"},
                {"lemma": "cadencia", "translation": "cadence", "pos": "noun"},
                {"lemma": "armonía", "translation": "harmony", "pos": "noun"},
                {"lemma": "estrofa", "translation": "stanza / verse", "pos": "noun"},
                {"lemma": "lírico", "translation": "lyrical", "pos": "adjective"},
                {"lemma": "acorde", "translation": "musical chord", "pos": "noun"}
            ]
        },
        "b2-brasilsudeste-05": {
            "id": "vocab.b2.brasilsudeste.05",
            "lesson": "b2-brasilsudeste-05",
            "title": "Luso-Hispanic Bridges, Diplomacy and Cognates",
            "words": [
                {"lemma": "afinidad", "translation": "affinity", "pos": "noun"},
                {"lemma": "bilingüe", "translation": "bilingual", "pos": "adjective"},
                {"lemma": "divergencia", "translation": "divergence", "pos": "noun"},
                {"lemma": "convergencia", "translation": "convergence", "pos": "noun"},
                {"lemma": "intercomprensión", "translation": "mutual intelligibility", "pos": "noun"},
                {"lemma": "diplomacia", "translation": "diplomacy", "pos": "noun"}
            ]
        }
    }

    for stem, vdata in vocab_data.items():
        write_json(f"vocabulary/b2/{stem}-voc.json", vdata)

    # 4. Grammar files
    grammar_data = {
        "b2-29-01-a-gr": {
            "id": "grammar.b2.29.01.marcadores-reformulacion-explicativa",
            "title": "Explanatory Reformulation Discourse Markers",
            "sections": [
                {
                    "type": "text",
                    "content": "Los marcadores de reformulación explicativa introducen una aclaración o paráfrasis de lo ya dicho con el propósito de facilitar la comprensión del receptor o precisar un término abstracto. En el nivel B2 formal, se emplean para articular definiciones rigurosas sin caer en repeticiones vacías."
                },
                {
                    "type": "table",
                    "title": "Marcadores de reformulación explicativa",
                    "rows": [
                        ["El tratado consagra la intercomprensión; es decir, la capacidad de comunicarse en lenguas hermanas.", "The treaty enshrines mutual intelligibility; that is, the ability to communicate in cognate languages."],
                        ["La metrópolis sufre un estrés hídrico severo, o sea, un déficit crítico en sus reservas de agua.", "The metropolis suffers from severe water stress, that is to say, a critical deficit in its water reserves."],
                        ["Se aplicó el principio de subsidiariedad, esto es, la intervención estatal en auxilio comunal.", "The principle of subsidiarity was applied, that is, state intervention to assist communities."],
                        ["El patrimonio comprende tres vertientes, a saber: la histórica, la ecológica y la lingüística.", "The heritage comprises three branches, namely: historical, ecological, and linguistic."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Puntuación de 'es decir' y 'esto es': se colocan habitualmente entre comas en el interior de una oración, o tras punto y coma cuando abren una proposición explicativa extensa."
                }
            ]
        },
        "b2-29-02-a-gr": {
            "id": "grammar.b2.29.02.marcadores-reformulacion-rectificativa",
            "title": "Rectifying Reformulation Discourse Markers",
            "sections": [
                {
                    "type": "text",
                    "content": "Los marcadores rectificativos corrigen, matizan o sustituyen un enunciado previo que el propio emisor juzga inexacto, incompleto o susceptible de equívoco. Permiten ajustar con exactitud quirúrgica la tesis defendida."
                },
                {
                    "type": "table",
                    "title": "Marcadores de rectificación y precisión",
                    "rows": [
                        ["No se trata de una asimilación ciega, sino más bien de un proceso de digestión estética.", "It is not a matter of blind assimilation, but rather a process of aesthetic digestion."],
                        ["El proyecto no fracasó; mejor dicho, se transformó en una experiencia piloto valiosa.", "The project did not fail; rather, it became a valuable pilot experience."],
                        ["La obra no es puramente realista; más exactamente, combina costumbrismo con ironía sutil.", "The work is not purely realistic; more precisely, it combines local color with subtle irony."],
                        ["Los colonos no se aislaron; antes bien, comerciaron activamente con los puertos vecinos.", "The colonists did not isolate themselves; on the contrary, they traded actively with neighboring ports."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "'Más bien' suele encabezar el término rectificado tras una negación previa ('no era rencor, más bien perplejidad'), mientras que 'mejor dicho' puede introducir una rectificación espontánea del vocablo empleado."
                }
            ]
        },
        "b2-29-03-a-gr": {
            "id": "grammar.b2.29.03.marcadores-reformulacion-distanciamiento",
            "title": "Distancing Reformulation Discourse Markers",
            "sections": [
                {
                    "type": "text",
                    "content": "Los marcadores de distanciamiento restan relevancia o validez a las consideraciones previas, reorientando el discurso hacia lo sustancial con independencia de los reparos planteados. Expresan una reserva crítica reflexiva."
                },
                {
                    "type": "table",
                    "title": "Marcadores de distanciamiento en prosa formal",
                    "rows": [
                        ["Las cifras son controvertidas; de todos modos, la tendencia demográfica es incuestionable.", "The figures are disputed; in any case, the demographic trend is unquestionable."],
                        ["Persisten dudas sobre el veredicto; en cualquier caso, la sentencia ya es firme.", "Doubts remain regarding the verdict; in any event, the judgment is already final."],
                        ["El autor incurre en contradicciones; de cualquier manera, su testimonio es insustituible.", "The author falls into contradictions; anyway, his testimony is irreplaceable."],
                        ["Hubo retrasos administrativos; de todas formas, el puente fue inaugurado a tiempo.", "There were administrative delays; regardless, the bridge was inaugurated on time."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "En registros académicos y jurídicos se prefiere 'en cualquier caso' o 'de todos modos' frente a la variante más coloquial 'igual' o 'de todas formas'."
                }
            ]
        },
        "b2-29-04-a-gr": {
            "id": "grammar.b2.29.04.marcadores-reformulacion-recapitulativa",
            "title": "Recapitulative Reformulation Discourse Markers",
            "sections": [
                {
                    "type": "text",
                    "content": "Los marcadores recapitulativos o de paráfrasis sintética retoman un conjunto complejo de ideas y lo condensan en una formulación más transparente, facilitando la comprensión global de una tesis académica o literaria."
                },
                {
                    "type": "table",
                    "title": "Paráfrasis y reformulación recapitulativa",
                    "rows": [
                        ["Dicho en otros términos, la riqueza industrial paulista financió la experimentación vanguardista.", "In other words, São Paulo's industrial wealth financed avant-garde experimentation."],
                        ["En otras palabras, la modernidad brasileña devoró la influencia europea para reinventarla.", "Put differently, Brazilian modernity devoured European influence to reinvent it."],
                        ["Dicho de otro modo, la bossa nova despojó a la samba de estridencias para volverla íntima.", "Expressed otherwise, bossa nova stripped samba of stridency to make it intimate."],
                        ["Dicho más sencillamente, la diplomacia se convirtió en el puente supremo de integración.", "Put more simply, diplomacy became the ultimate bridge of regional integration."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "'Dicho en otros términos' y 'dicho de otro modo' confieren prestancia al texto argumentativo formal, sustituyendo con elegancia fórmulas trilladas de divulgación elemental."
                }
            ]
        },
        "b2-29-05-a-gr": {
            "id": "grammar.b2.29.05.marcadores-reformulacion-ejemplificativa",
            "title": "Exemplifying Reformulation Discourse Markers",
            "sections": [
                {
                    "type": "text",
                    "content": "Los marcadores de ejemplificación concretan una afirmación general o concepto teórico mediante un caso particular representativo. En el nivel B2, el escritor recurre a locuciones cultas que realzan la solvencia de su demostración."
                },
                {
                    "type": "table",
                    "title": "Locuciones de ejemplificación e ilustración",
                    "rows": [
                        ["A modo de ilustración, analicemos el impacto del lienzo 'Abaporu' de Tarsila do Amaral.", "By way of illustration, let us analyze the impact of the canvas 'Abaporu' by Tarsila do Amaral."],
                        ["Por poner un caso representativo, examinemos la trayectoria diplomática de Río Branco.", "To cite a representative case, let us examine the diplomatic career of Rio Branco."],
                        ["Muchos vocablos engañan por su fonética; verbigracia, el portugués 'propina' significa propina o soborno según el país.", "Many words deceive by their sound; for example, Portuguese 'propina' means tip or bribe depending on the country."],
                        ["Pongamos por caso la transición ecológica de las redes de tranvías metropolitanas.", "Let us take for example the ecological transition of metropolitan tram networks."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "'Verbigracia' (abreviado a veces 'v. gr.') pertenece al registro culto tradicional de los ensayos filosóficos y jurídicos. En redacciones ensayísticas contemporáneas, 'a modo de ilustración' resulta fluido y sumamente elegante."
                }
            ]
        },
        "b2-brasilsudeste-01-a-gr": {
            "id": "grammar.b2.brasilsudeste.01.brasil-conectores-contraste",
            "title": "Contrastive Discourse Markers in Urban Analysis",
            "sections": [
                {
                    "type": "text",
                    "content": "El análisis sociológico y urbanístico de megaciudades como São Paulo exige confrontar realidades yuxtapuestas: la opulencia financiera frente a la precariedad periférica. Los conectores de contraste articulan estas polaridades."
                },
                {
                    "type": "table",
                    "title": "Conectores de contraste y contraposición",
                    "rows": [
                        ["La Avenida Paulista concentra la banca global, mientras que la periferia urbana carece de saneamiento.", "Paulista Avenue concentrates global banking, whereas the urban periphery lacks basic sanitation."],
                        ["El sector tecnológico crece con vigor; en contrapartida, los salarios manufactureros se estancan.", "The tech sector grows vigorously; in contrast, manufacturing wages remain stagnant."],
                        ["No disminuyó el tráfico vehicular; por el contrario, los embotellamientos se agravaron.", "Vehicular traffic did not diminish; on the contrary, traffic gridlocks worsened."],
                        ["La inmigración japonesa aportó agricultura intensiva, en tanto que la italiana nutrió las fábricas textiles.", "Japanese immigration brought intensive agriculture, while Italian immigration fed textile factories."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "'Por el contrario' exige que la proposición precedente contenga una negación explícita o implícita: 'No disminuyó... por el contrario, creció'."
                }
            ]
        },
        "b2-brasilsudeste-02-a-gr": {
            "id": "grammar.b2.brasilsudeste.02.brasil-oraciones-relativas-especificativas",
            "title": "Restrictive & Explanatory Relative Clauses in Geography",
            "sections": [
                {
                    "type": "text",
                    "content": "La descripción del paisaje y la trama urbana carioca requiere diferenciar entre oraciones de relativo especificativas (que restringen el antecedente sin comas) y explicativas (que aportan un rasgo descriptivo entre comas)."
                },
                {
                    "type": "table",
                    "title": "Oraciones de relativo en la prosa descriptiva",
                    "rows": [
                        ["Los morros graníticos que rodean la bahía crean un anfiteatro natural imponente.", "The granite hills that surround the bay create an imposing natural amphitheater."],
                        ["El Corcovado, que se eleva a más de setecientos metros, corona la silueta de la metrópolis.", "The Corcovado, which rises over seven hundred meters, crowns the silhouette of the metropolis."],
                        ["Las comunidades que se asientan sobre las laderas han desarrollado una rica vida cultural.", "The communities that settle upon the hillsides have developed a rich cultural life."],
                        ["La bahía de Guanabara, cuyas aguas sufren contaminación histórica, alberga decenas de islas.", "Guanabara Bay, whose waters suffer from historic pollution, harbors dozens of islands."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "El pronombre 'cuyo' concuerda en género y número con el sustantivo que le sigue inmediatamente, nunca con el poseedor antecedente: 'la bahía (fem.) cuyas aguas (fem. pl.)'."
                }
            ]
        },
        "b2-brasilsudeste-03-a-gr": {
            "id": "grammar.b2.brasilsudeste.03.brasil-voz-media-pronominal",
            "title": "Pronominal Middle Voice in Aesthetic Analysis",
            "sections": [
                {
                    "type": "text",
                    "content": "En la crítica artística e histórica sobre el modernismo brasileño, la voz media pronominal presenta un proceso que afecta al sujeto de forma espontánea o interna, sin que se perciba una acción impuesta por un agente exterior."
                },
                {
                    "type": "table",
                    "title": "Estructuras de voz media pronominal",
                    "rows": [
                        ["La estética académica se disolvió ante la audacia de los pintores modernistas.", "Academic aesthetics dissolved before the boldness of modernist painters."],
                        ["El canon artístico se transformó con la irrupción de las vanguardias paulistas.", "The artistic canon transformed with the irruption of the Paulista avant-garde."],
                        ["La identidad nacional brasileña se forjó asimilando múltiples raíces culturales.", "Brazilian national identity was forged by assimilating multiple cultural roots."],
                        ["Las formas tradicionales se quebraron durante la Semana de Arte Moderno de 1922.", "Traditional forms broke apart during the Modern Art Week of 1922."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Diferencia sutil: en 'la estética se disolvió' el verbo denota un cambio de estado interno (voz media), no una acción refleja donde el sujeto actúa sobre sí mismo como agente voluntario."
                }
            ]
        },
        "b2-brasilsudeste-04-a-gr": {
            "id": "grammar.b2.brasilsudeste.04.brasil-adverbios-foco",
            "title": "Focusing Adverbs & Scalar Markers in Cultural Writing",
            "sections": [
                {
                    "type": "text",
                    "content": "Los adverbios de foco ('precisamente', 'incluso', 'hasta', 'siquiera') destacan un elemento específico del discurso o lo sitúan en el extremo de una escala implícita de relevancia, aportando fuerza argumentativa al análisis musical."
                },
                {
                    "type": "table",
                    "title": "Adverbios de foco y operadores escalares",
                    "rows": [
                        ["Fue precisamente en los callejones de Lapa donde la samba encontró su síncopa definitiva.", "It was precisely in the alleys of Lapa where samba found its definitive syncopation."],
                        ["La bossa nova conquistó incluso los auditorios más exigentes del jazz neoyorquino.", "Bossa nova conquered even the most demanding jazz auditoriums in New York."],
                        ["Hasta los críticos más conservadores reconocieron la genialidad melódica de Tom Jobim.", "Even the most conservative critics acknowledged the melodic genius of Tom Jobim."],
                        ["No necesitó siquiera recurrir a grandes orquestaciones para conmover con su voz susurrada.", "He did not even need to resort to large orchestrations to move listeners with his whispered voice."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "'Siquiera' exige una negación previa en la misma proposición ('no necesitó ni siquiera', 'sin siquiera pestañear') cuando funciona como marcador escalar enfático."
                }
            ]
        },
        "b2-brasilsudeste-05-a-gr": {
            "id": "grammar.b2.brasilsudeste.05.brasil-comparativas-proporcionales",
            "title": "Proportional Comparative Structures in Cross-Cultural Writing",
            "sections": [
                {
                    "type": "text",
                    "content": "Las comparativas proporcionales expresan cómo la variación de una magnitud o fenómeno corre paralela a la evolución de otra. Son fundamentales para sopesar la integración luso-hispana y los lazos culturales bilaterales."
                },
                {
                    "type": "table",
                    "title": "Estructuras correlativas proporcionales",
                    "rows": [
                        ["Cuanto más dialogan ambas naciones, tanto más fructífera resulta la integración continental.", "The more both nations engage in dialogue, the more fruitful continental integration becomes."],
                        ["A medida que se profundizan los intercambios universitarios, disminuyen los prejuicios mutuos.", "As university exchanges deepen, mutual prejudices diminish."],
                        ["Conforme avanzan las obras del corredor bioceánico, se aceleran las exportaciones al Pacífico.", "As works on the bioceanic corridor advance, exports to the Pacific accelerate."],
                        ["Cuanto mayor es el conocimiento lingüístico, menor es el riesgo de tropezar con falsos amigos.", "The greater the linguistic knowledge, the lower the risk of stumbling upon false friends."]
                    ]
                },
                {
                    "type": "tip",
                    "content": "Regla modal: si la correlación proporcional alude a un hecho futuro o hipotético, el primer miembro exige modo subjuntivo: 'Cuanto más cooperen (subjuntivo) ambos países, más próspera será la región'."
                }
            ]
        }
    }

    for stem, gdata in grammar_data.items():
        write_json(f"grammar/b2/{stem}.json", gdata)

    # 5. Stories
    # Classic story: Machado de Assis - Dom Casmurro (b2-29.json)
    # Regional stories: b2-brasilsudeste-01 to 05, b2-brasilsudeste-consolidation, b2-brasilsudeste.json
    # All texts strictly verified in [650, 825] words!

    stories = {
        "classics/b2/b2-29": {
            "id": "b2-29",
            "title": "Machado de Assis: Dom Casmurro",
            "level": "B2",
            "lesson": 29,
            "type": "classics",
            "estimatedMinutes": 8,
            "summary": "Adaptación pedagógica de la cumbre de Machado de Assis: la mirada obsesiva de Bento Santiago desde su soledad en Engenho Novo, el recuerdo deslumbrante de Capitu con sus ojos de resaca marina, la amistad quebrantada con Escobar y el abismo insoluble de los celos retrospectivos.",
            "characters": [
                "Bento Santiago (Dom Casmurro, el anciano narrador)",
                "Capitu (Capitolina, su amor de infancia y esposa)",
                "Ezequiel de Souza Escobar (el brillante amigo del seminario)",
                "Ezequiel (el hijo marcado por un parecido perturbador)"
            ],
            "paragraphs": [
                {
                    "type": "narration",
                    "text": "En la penumbra solitaria de su casona en el barrio carioca de Engenho Novo, un hombre envejecido y huraño a quien los vecinos apodaron con mordacidad 'Dom Casmurro' consagra sus horas postreras a reconstruir minuciosamente los fantasmas de su juventud perdida. Para mitigar el tedio y la melancolía que le devoran el alma, Bento Santiago mandó edificar aquella vivienda reproduciendo de manera idéntica las habitaciones, los corredores y el jardín de su antigua casa de infancia en la calle de Matacavalos. Es decir, el anciano abogado intentó clausurar el tiempo exterior para revivir con obsesión arqueológica los albores de su pasión juvenil por Capitolina, la dulce y enigmática muchacha vecina a quien todos llamaban Capitu. Dicho en otros términos, la memoria no opera aquí como un simple álbum de añoranzas amables, sino más bien como un tribunal sombrío donde un fiscal celoso interroga una y otra vez los silencios del pasado."
                },
                {
                    "type": "narration",
                    "text": "Desde los primeros juegos infantiles en las cancelas floridas del vecindario, Capitu deslumbraba a cuantos la rodeaban por su extraordinaria madurez psicológica y por un magnetismo singular que Bento jamás logró descifrar por completo. Su amigo José Días solía definir la mirada de la joven mediante una metáfora célebre que habría de atormentar a Bento hasta el fin de sus días: Capitu poseía 'ojos de resaca', esto es, ojos de marea brava que atraían al observador hacia el fondo de un abismo como la resaca del mar en las playas abiertas de Río de Janeiro. Mejor dicho, no se trataba de una belleza convencional o sumisa, sino de una inteligencia viva y disimuladora que desconcertaba al inseguro Bento. Cuando la devota madre de este pretendió internarlo forzosamente en un seminario para cumplir una vieja promesa de ordenación sacerdotal, fue la astucia de Capitu la que urdió las alianzas necesarias para liberarlo de los hábitos sagrados y permitirles contraer matrimonio civil y eclesiástico."
                },
                {
                    "type": "narration",
                    "text": "En las aulas austeras del seminario de São José, Bento trabó una amistad entrañable e indivisible con Ezequiel de Souza Escobar, un joven seminarista de mente calculadora, despierta y dotada de un prodigioso sentido práctico para las finanzas y el comercio. Escobar no tardó en abandonar la sotana para consagrarse a los negocios portuarios, casándose poco después con Sancha, la amiga íntima de Capitu, y sellando así un cuadrilátero afectivo de aparente armonía familiar. En cualquier caso, el hogar de Bento y Capitu parecía haber alcanzado la plenitud terrenal cuando, tras largos años de dolorosa e infértil espera, nació por fin su único primogénito, al que bautizaron con el nombre de Ezequiel en honor al entrañable amigo de estudios. De todos modos, la dicha conyugal duró muy poco tiempo, pues la tragedia no tardó en golpear las aguas de la bahía de Guanabara cuando Escobar murió ahogado repentinamente al ser arrastrado por el oleaje traicionero de la playa de São Cristóvão."
                },
                {
                    "type": "narration",
                    "text": "Fue precisamente durante las honras fúnebres de Escobar cuando los cimientos morales de Bento Santiago se desplomaron en una espiral irreversible de sospechas insoportables. Al contemplar el féretro del difunto amigo, Bento advirtió que Capitu no lloraba con el pesar formal de una conocida; por el contrario, clavó en el rostro inerte del cadáver aquellos ojos de resaca marina con una desesperación honda y reprimida que heló la sangre del esposo. A modo de ilustración del abismo mental en que se hundió Bento, cada gesto y cada mirada de su pequeño hijo Ezequiel comenzaron a revelarle un parecido asombroso, milimétrico y monstruoso con las facciones del difunto Escobar. Dicho de otro modo, el padre atormentado ya no veía en el niño a su propia descendencia, sino la prueba viviente de una traición adulterina que mancillaba para siempre el honor de su linaje familiar."
                },
                {
                    "type": "narration",
                    "text": "En suma, la genialidad imperecedera de Machado de Assis estriba en negar al lector cualquier certeza judicial concluyente sobre la culpabilidad objetiva de Capitu. En definitiva, todo lo que conocemos procede de la voz monologante, amargada y subjetiva de Dom Casmurro, un narrador herido que manipula los recuerdos para justificar el destierro impuesto a su esposa y a su hijo en tierras de Europa y su propio retiro solitario en Engenho Novo. En última instancia, la novela se erige en una cumbre magistral de la literatura universal que dilucida cómo los celos enfermizos son capaces de crear sus propios monstruos imaginarios, dejando suspendida para siempre en la conciencia del lector la pregunta sobre si Capitu engañó verdaderamente a su marido o si fue este quien devoró su propia felicidad en los altares de la desconfianza."
                }
            ],
            "narration": {
                "pedagogical": {
                    "comprehensionQuestions": [
                        {
                            "question": "¿Por qué Bento Santiago hizo construir su casa de Engenho Novo idéntica a la de su infancia?",
                            "options": [
                                "Para abaratar los costos arquitectónicos de la obra.",
                                "Para reproducir con obsesión el escenario físico de su amor juvenil y revivir sus recuerdos en soledad.",
                                "Porque el gobierno municipal le prohibió cambiar el diseño de las fachadas coloniales.",
                                "Para instalar un museo de pintura moderna en la sala principal."
                            ],
                            "correctIndex": 1,
                            "explanation": "Bento reconstruyó su casa de Matacavalos para encerrarse en la reconstrucción obsesiva de su pasado."
                        },
                        {
                            "question": "¿Qué rasgo caracterizaba los ojos de Capitu según la célebre metáfora de la novela?",
                            "options": [
                                "Eran ojos apagados y ciegos por una enfermedad infantil.",
                                "Eran ojos de resaca marina, que atraían y sumergían al observador en un abismo de misterio y disimulo.",
                                "Eran ojos verdes y claros idénticos a los de una emperatriz europea.",
                                "Eran ojos tristes que lloraban constantemente sin motivo aparente."
                            ],
                            "correctIndex": 1,
                            "explanation": "La metáfora de los 'ojos de resaca' define la profundidad y el poder de fascinación misterioso de Capitu."
                        },
                        {
                            "question": "¿Cuál es la singularidad narrativa que convierte a 'Dom Casmurro' en una obra maestra psicológica?",
                            "options": [
                                "Que incluye cartas judiciales certificadas por un tribunal imparcial de Río de Janeiro.",
                                "Que el narrador es subjetivo y obsesivo, dejando en la incertidumbre al lector sobre si el adulterio fue real o fruto de los celos.",
                                "Que la historia está contada enteramente desde la perspectiva de Escobar tras su muerte.",
                                "Que fue escrita originalmente en verso heroico alejandrino."
                            ],
                            "correctIndex": 1,
                            "explanation": "Machado de Assis utiliza un narrador en primera persona cuya subjetividad impide verificar con certeza la infidelidad."
                        }
                    ]
                }
            }
        },
        "world/b2/b2-brasilsudeste-01": {
            "id": "b2-brasilsudeste-01",
            "title": "La colmena de hormigón y café: el pulso de São Paulo",
            "level": "B2",
            "lesson": 1,
            "type": "world",
            "estimatedMinutes": 8,
            "summary": "El ascenso colosal de São Paulo: de modesta villa jesuítica y capital del imperio cafetalero decimonónico a la mayor metrópolis financiera e industrial del hemisferio sur, marcada por una vigorosa inmigración global.",
            "characters": [
                "Barones del café e ingenieros ferroviarios británicos",
                "Inmigrantes italianos, japoneses y libaneses",
                "Trabajadores de las fábricas del ABC paulista y ejecutivos de la Avenida Paulista"
            ],
            "paragraphs": [
                {
                    "type": "narration",
                    "text": "En la meseta oriental del estado de São Paulo, a más de setecientos metros sobre el nivel del mar y a escasas leguas del océano Atlántico, se extiende la mayor concentración urbana, demográfica e industrial del hemisferio sur: la metrópolis de São Paulo. En primer término, conviene recordar que hasta mediados del siglo diecinueve aquella población no pasaba de ser una modesta villa colonial erigida en torno al colegio jesuítico fundado por Manuel da Nóbrega y José de Anchieta. Sin embargo, la formidable expansión de la frontera cafetalera por las tierras rojizas y fértiles del interior paulista —la mítica 'terra roxa'— transformó a la ciudad en el centro financiero y logístico indiscutible del cultivo del grano de oro. Es decir, los fabulosos dividendos de la exportación de café financiaron el tendido de las líneas de ferrocarril hacia el puerto de Santos y sembraron los cimientos materiales sobre los cuales se levantaría la colmena de hormigón más imponente de América Latina."
                },
                {
                    "type": "narration",
                    "text": "Con la abolición definitiva de la esclavitud en 1888 y la proclamación de la república, las haciendas cafetaleras y las nacientes industrias paulistas demandaron una masa inmensa de mano de obra libre. Por una parte, más de un millón de inmigrantes italianos arribaron al puerto de Santos para establecerse en barrios obreros populosos como Brás, Mooca y Bixiga, aportando su fuerza de trabajo y su rica tradición gastronómica; por otra, la llegada a partir de 1908 del barco 'Kasato Maru' inauguró la mayor ola migratoria nipona del planeta fuera de Japón, concentrándose en el emblemático barrio de Liberdade y revolucionando la agricultura intensiva de hortalizas. Dicho en otros términos, la identidad paulistana no se cimentó sobre una raíz criolla homogénea, sino sobre un crisol vertiginoso de orígenes donde italianos, japoneses, sirio-libaneses, alemanes y migrantes del nordeste brasileño forjaron un culto colectivo al esfuerzo laboral y al dinamismo emprendedor."
                },
                {
                    "type": "narration",
                    "text": "A lo largo del siglo veinte, el corazón financiero de la ciudad se desplazó desde el centro histórico colonial hacia la majestuosa Avenida Paulista, aquel corredor señorial donde los antiguos barones del café habían edificado sus palacetes eclécticos y donde hoy se alzan los rascacielos de vidrio de la banca internacional, las sedes corporativas de empresas globales y el prestigioso Museo de Arte de São Paulo (MASP). Diseñado por la célebre arquitecta italo-brasileña Lina Bo Bardi, el MASP se suspende audazmente sobre cuatro pilares rojos de hormigón, liberando una inmensa plaza cívica abierta a todos los transeúntes. En cualquier caso, esta opulencia financiera contrasta dramáticamente con las profundas desigualdades sociales que desgarran la mancha urbana; de todos modos, la vitalidad cultural de la metrópolis no se rinde ante la adversidad, nutriéndose de teatros de vanguardia, bienales de arte y una gastronomía cosmopolita de escala universal."
                },
                {
                    "type": "narration",
                    "text": "Hacia el sur del núcleo metropolitano se extiende el cordón industrial del 'Gran ABC' —integrado por los municipios obreros de Santo André, São Bernardo do Campo y São Caetano do Sul—, epicentro histórico de la industria automovilística pesada brasileña. Fue precisamente en aquellas naves fabriles de montaje donde a fines de la década de 1970 estallaron las históricas huelgas metalúrgicas lideradas por un joven dirigente sindical de origen nordestino llamado Luiz Inácio Lula da Silva, desafiando a la dictadura militar y sembrando las semillas de la redemocratización nacional y del Partido de los Trabajadores. Por poner un caso representativo, las asambleas obreras en los estadios de fútbol del ABC demostraron que la clase trabajadora paulista no era un mero engranaje de producción en serie, sino un sujeto político maduro capaz de exigir derechos democráticos y justicia distributiva en el escenario nacional."
                },
                {
                    "type": "narration",
                    "text": "En suma, São Paulo personifica la paradoja viva de una megalópolis devoradora y fascinante que nunca duerme bajo su manto perenne de llovizna fina —la tradicional 'garoa' paulistana— y el murmullo incesante de millones de motores en marcha. En última instancia, la ciudad encarna la fe en el progreso ininterrumpido y en la inventiva humana frente a los colosales desafíos contemporáneos de la movilidad sostenible y la integración periférica. En definitiva, quien recorre sus avenidas infinitas comprende que en el ritmo vertiginoso de sus calles late la locomotora económica de América del Sur, un gigante de asfalto y sueños donde convergen todas las sangres del mundo para reinventar a diario el porvenir continental."
                }
            ],
            "narration": {
                "pedagogical": {
                    "comprehensionQuestions": [
                        {
                            "question": "¿Qué rubro productivo impulsó el salto financiero y urbanístico de São Paulo en el siglo XIX?",
                            "options": [
                                "La extracción de diamantes y oro aluvial en los ríos serranos.",
                                "El cultivo y la exportación masiva de café en las tierras fértiles de la terra roxa.",
                                "La pesca de ballenas en las aguas del litoral atlántico.",
                                "La exportación de lana de oveja hacia el mercado británico."
                            ],
                            "correctIndex": 1,
                            "explanation": "El auge del café financió el ferrocarril al puerto de Santos y la infraestructura industrial de la ciudad."
                        },
                        {
                            "question": "¿Qué comunidad migratoria conformó en São Paulo la mayor concentración demográfica de su origen fuera de su patria?",
                            "options": [
                                "La comunidad rusa establecida en las colonias del cerrado.",
                                "La inmigración japonesa radicada en el barrio de Liberdade a partir de 1908.",
                                "Los mineros galeses llegados para explotar el carbón.",
                                "Los agricultores suecos de las llanuras pampeanas."
                            ],
                            "correctIndex": 1,
                            "explanation": "A partir de la llegada del barco Kasato Maru, São Paulo albergó la mayor comunidad japonesa del mundo fuera de Japón."
                        },
                        {
                            "question": "¿Qué hito arquitectónico y cívico diseñó Lina Bo Bardi en la Avenida Paulista?",
                            "options": [
                                "La catedral neogótica de la plaza da Sé.",
                                "El Museo de Arte de São Paulo (MASP), suspendido sobre cuatro pilares rojos con plaza cívica libre.",
                                "El rascacielos más alto de acero importado de Europa.",
                                "Un estadio olímpico subterráneo para carreras de automóviles."
                            ],
                            "correctIndex": 1,
                            "explanation": "El MASP es un icono de la arquitectura moderna suspendido sobre pilares para dejar libre el espacio cívico inferior."
                        }
                    ]
                }
            }
        },
        "world/b2/b2-brasilsudeste-02": {
            "id": "b2-brasilsudeste-02",
            "title": "La ciudad maravillosa entre el morro y el mar",
            "level": "B2",
            "lesson": 2,
            "type": "world",
            "estimatedMinutes": 8,
            "summary": "Río de Janeiro y su singularísima topografía urbana: la bahía de Guanabara, los morros de granito, la memoria imperial de la corte portuguesa, el urbanismo de las favelas y la filosofía de vida de la cultura carioca.",
            "characters": [
                "Monarcas de la corte portuguesa de Juan VI en el siglo XIX",
                "Arquitectos modernistas e ingenieros del Paseo Público",
                "Músicos, pasistas de samba y habitantes de las favelas de la zona sur y norte"
            ],
            "paragraphs": [
                {
                    "type": "narration",
                    "text": "Pocas ciudades sobre la faz de la tierra poseen un emplazamiento natural tan sobrecogedor y espectacular como Río de Janeiro, la mítica 'Ciudad Maravillosa' enclavada en una estrecha franja costera donde los morros de granito macizo se sumergen abruptamente en las aguas azules del océano Atlántico. En primer término, descubierta por navegantes portugueses en enero de 1502 —quienes creyeron erróneamente que la bahía de Guanabara era la desembocadura de un caudaloso río fluvial—, la ciudad creció amoldándose a una topografía accidentada y laberíntica dominada por la selva atlántica de Tijuca, el mayor bosque urbano reforestado del planeta entero. Es decir, el trazado urbano carioca no obedeció a una cuadrícula geométrica regular, sino más bien a una negociación perpetua entre las olas marinas, las lagunas costeras y las laderas empinadas del Pan de Azúcar y del cerro del Corcovado."
                },
                {
                    "type": "narration",
                    "text": "La llegada en 1808 de la familia real portuguesa huyendo de las invasiones napoleónicas confirió a Río de Janeiro un estatus geopolítico único en el continente: se convirtió en la capital de facto de todo el Imperio colonial portugués, siendo la única ciudad americana que albergó formalmente a una corte monárquica europea en ejercicio soberano. Por una parte, el rey Juan VI impulsó la creación de instituciones cívicas e intelectuales de primer orden, a saber: el Jardín Botánico con sus altivas palmeras imperiales, la Biblioteca Nacional, la Real Academia de Bellas Artes y el Banco de Brasil; por otra, tras la independencia proclamada en 1822 por Pedro I a orillas del Ipiranga, Río se consolidó como la sede política imperial y republicana de la nación hasta la inauguración de Brasília en 1960. Dicho en otros términos, la ciudad atesora un porte señorial y cosmopolita que aún impregna los viejos bulevares de Cinelândia y el barrio de Santa Teresa."
                },
                {
                    "type": "narration",
                    "text": "Sin embargo, el rasgo sociourbanístico más característico y complejo del paisaje carioca reside en la estrecha contigüidad espacial entre los barrios residenciales opulentos de la costa y las 'favelas' que trepan por las laderas de los morros. Nacidas a finales del siglo diecinueve cuando soldados desmovilizados de la guerra de Canudos se asentaron en el Morro da Providência so pretexto de aguardar viviendas prometidas por el gobierno, las favelas crecieron como comunidades autoconstruidas ante la falta crónica de vivienda social accesible. En cualquier caso, lejos de constituir meros guetos de precariedad material, enclaves emblemáticos como Rocinha, Mangueira, Vidigal y Cantagalo han operado históricamente como vigorosos motores culturales de la identidad brasileña; de todos modos, la violencia derivada del narcotráfico y la estigmatización policial continúan planteando severos desafíos éticos para la integración plena de sus pobladores a la ciudadanía formal."
                },
                {
                    "type": "narration",
                    "text": "A orillas de las míticas playas de Copacabana e Ipanema, diseñadas con los ondulados pavimentos de adoquín blanco y negro de Burle Marx, florece una filosofía de vida inconfundible: el espíritu 'carioca'. Esta idiosincrasia colectiva se caracteriza por una contagiosa alegría vital, un culto desenfadado al sol, al deporte al aire libre y a la sociabilidad costera donde las diferencias de clase social parecen atenuarse temporalmente sobre la arena cálida. A modo de ilustración, los 'quiosques' frente al mar son verdaderos foros democráticos donde se degusta agua de coco helada o una caipiriña mientras se discute apasionadamente sobre fútbol o se entonan versos de samba espontáneos al compás de una pandereta improvisada con una caja de fósforos."
                },
                {
                    "type": "narration",
                    "text": "En suma, Río de Janeiro fascina al mundo por su capacidad inagotable de sintetizar la belleza natural más deslumbrante con las tensiones sociales más desgarradoras de la modernidad periférica. En última instancia, la mirada benévola del Cristo Redentor abrazando a la bahía desde la cumbre del Corcovado simboliza la esperanza secular de un pueblo que convierte el dolor cotidiano en fiesta desbordante cada año durante los desfiles monumentales del Sambódromo de la calle Marquês de Sapucaí. En definitiva, la Ciudad Maravillosa no es un mero destino turístico de postal, sino un corazón palpitante de cultura, música y resistencia donde el mar y la montaña dialogan eternamente con el alma libre de sus habitantes."
                }
            ],
            "narration": {
                "pedagogical": {
                    "comprehensionQuestions": [
                        {
                            "question": "¿Qué singularidad histórica diferenció a Río de Janeiro de las restantes ciudades americanas en 1808?",
                            "options": [
                                "Fue destruida en su totalidad por una erupción volcánica.",
                                "Se convirtió en sede formal y corte monárquica del Imperio colonial portugués tras el traslado de Juan VI.",
                                "Fue vendida por la Corona a los comerciantes británicos de ultramar.",
                                "Prohibió el ingreso de cualquier embarcación comercial a su bahía."
                            ],
                            "correctIndex": 1,
                            "explanation": "Río de Janeiro fue la única ciudad americana que albergó a una corte monárquica europea en ejercicio."
                        },
                        {
                            "question": "¿Cuál fue el origen histórico de las primeras favelas en los morros cariocas?",
                            "options": [
                                "Fueron campamentos construidos por veteranos de la guerra de Canudos a finales del siglo XIX.",
                                "Fueron complejos hoteleros diseñados para el carnaval de 1950.",
                                "Fueron instalaciones científicas para observar las mareas atlánticas.",
                                "Fueron puertos fluviales de transbordo hacia el Amazonas."
                            ],
                            "correctIndex": 0,
                            "explanation": "Las favelas nacieron cuando veteranos de Canudos ocuparon el Morro da Providência esperando casas del Estado."
                        },
                        {
                            "question": "¿Qué célebre paisajista diseñó los pavimentos ondulados de adoquín blanco y negro de Copacabana?",
                            "options": [
                                "Oscar Niemeyer",
                                "Roberto Burle Marx",
                                "Lúcio Costa",
                                "Cândido Portinari"
                            ],
                            "correctIndex": 1,
                            "explanation": "Roberto Burle Marx concibió las legendarias calzadas onduladas de mosaico portugués en la rambla de Copacabana."
                        }
                    ]
                }
            }
        },
        "world/b2/b2-brasilsudeste-03": {
            "id": "b2-brasilsudeste-03",
            "title": "Devorar al invasor: la revolución del modernismo brasileño",
            "level": "B2",
            "lesson": 3,
            "type": "world",
            "estimatedMinutes": 8,
            "summary": "La conmoción vanguardista de la Semana de Arte Moderno de 1922 en el Teatro Municipal de São Paulo: el Manifiesto Antropófago de Oswald de Andrade, la pintura revolucionaria de Tarsila do Amaral y la devoración cultural de Europa para forjar el arte propio.",
            "characters": [
                "Oswald de Andrade y Mário de Andrade (escritores vanguardistas)",
                "Tarsila do Amaral y Anita Malfatti (pintoras revolucionarias)",
                "Heitor Villa-Lobos (compositor musical)"
            ],
            "paragraphs": [
                {
                                "type": "narration",
                                "text": "En febrero de 1922, mientras el país conmemoraba con solemnidad protocolaria el primer centenario de su independencia política de Portugal, un grupo apasionado de jóvenes poetas, pintores, escultores y músicos desató en el imponente Teatro Municipal de São Paulo un escándalo estético sin precedentes que sacudiría hasta sus cimientos la cultura de la nación: la histórica Semana de Arte Moderno. En primer término, la élite intelectual y burguesa de la época rendía pleitesía reverente a los cánones academicistas europeos, importando con docilidad acrítica el parnasianismo literario francés y las pinturas pastorales decimonónicas desvinculadas de la realidad nacional. Es decir, los jóvenes modernistas no se limitaron a pedir reformas superficiales de estilo; por el contrario, proclamaron una ruptura iconoclasta radical contra la retórica fosilizada del pasado, defendiendo la libertad creadora absoluta, el verso libre y la incorporación apasionada del lenguaje coloquial de las calles brasileñas."
                },
                {
                                "type": "narration",
                                "text": "Durante aquellas tres veladas tempestuosas de conferencias incendiarias, exposiciones polémicas y conciertos audaces, el público acomodado reaccionó con abucheos estruendosos, risas burlonas, ladridos y lanzamiento de verduras podridas al escenario. Por una parte, las pinturas expresionistas de Anita Malfatti y los bocetos de Emiliano Di Cavalcanti fueron tildados de aberraciones deformes por la crítica periodística conservadora; por otra, el maestro Heitor Villa-Lobos escandalizó a los melómanos tradicionales al dirigir la orquesta calzando una humilde zapatilla de paño en un pie lesionado y combinando instrumentos sinfónicos con matracas indígenas y percusiones populares de la selva amazónica. Dicho en otros términos, la provocación vanguardista no buscaba el aplauso condescendiente de los salones oligárquicos, sino más bien despertar a la sociedad de su letargo colonial mediante una bofetada estética que obligara a los brasileños a mirarse con orgullo en su propio espejo mestizo."
                },
                {
                                "type": "narration",
                                "text": "La maduración conceptual de este movimiento desembocó pocos años después en la formulación teórica más audaz y original de todas las vanguardias latinoamericanas: el 'Movimiento Antropófago', lanzado en mayo de 1928 por Oswald de Andrade a través de su célebre 'Manifiesto Antropófago'. Inspirado en el lienzo monumental 'Abaporu' ('hombre que come hombres' en lengua tupí-guaraní), pintado por su compañera Tarsila do Amaral como obsequio de cumpleaños, Oswald transformó el mito colonial del canibalismo indígena en una brillante metáfora cultural descolonizadora. Esto es, el artista brasileño no debía imitar sumisamente la cultura europea ni tampoco rechazarla con purismo chovinista; más bien, debía 'devorar' las influencias técnicas foráneas, digerirlas en el estómago nacional y transformarlas en una creación enteramente autóctona y renovadora, resumida en la memorable máxima bilingüe: 'Tupí or not tupí, that is the question'."
                },
                {
                                "type": "narration",
                                "text": "La pintura de Tarsila do Amaral plasmó este ideario con una maestría plástica inigualable mediante cuadros capitales como 'A Negra', 'Abaporu' y 'Antropofagia'. Sus figuras humanas de pies colosales y cabezas reducidas enraizadas en la tierra tropical, bañadas por soles gigantescos y paletas cromáticas vivas de azules, verdes y amarillos populares —los 'colores caipiras' de su infancia rural paulista—, demolieron el refinamiento palaciego para consagrar la fuerza telúrica de la flora, la fauna y los pueblos afrobrasileños e indígenas. A modo de ilustración de su alcance, el escritor Mário de Andrade publicó en ese mismo fecundo año de 1928 su obra maestra 'Macunaíma', la novela rapsódica del 'héroe sin ningún carácter' que muta constantemente de color de piel, región geográfica y dialecto verbal, encarnando la fluidez identitaria inatrapable y polifónica del ser brasileño contemporáneo."
                },
                {
                                "type": "narration",
                                "text": "En suma, la revolución del modernismo de 1922 no constituyó un mero episodio pasajero de rebeldía juvenil, sino el acto de refundación cultural más fecundo del siglo veinte en América Latina. En última instancia, la lección antropofágica de Oswald y Tarsila enseñó al continente entero que la verdadera soberanía estética no radica en la copia servil de las metrópolis dominantes ni en el aislamiento folclórico estéril, sino en la capacidad crítica de devorar el mundo entero para expresar la propia verdad humana. En definitiva, cien años después de aquellos abucheos en el Teatro Municipal de São Paulo, la antorcha encendida por los modernistas continúa iluminando con vigor los senderos de la música, el cine, las artes visuales y la literatura de todo el orbe iberoamericano."
                }
],
            "narration": {
                "pedagogical": {
                    "comprehensionQuestions": [
                        {
                            "question": "¿En qué consistió la metáfora central del 'Manifiesto Antropófago' de Oswald de Andrade?",
                            "options": [
                                "En rechazar la tecnología moderna para vivir en aldeas primitivas.",
                                "En 'devorar' críticamente la cultura europea para asimilarla y transformarla en arte propio, mestizo y original.",
                                "En prohibir las exposiciones de pintura en teatros municipales.",
                                "En exigir que los escritores redactaran sus obras exclusivamente en latín."
                            ],
                            "correctIndex": 1,
                            "explanation": "La antropofagia propone asimilar las influencias extranjeras transformándolas en una síntesis genuinamente brasileña."
                        },
                        {
                            "question": "¿Qué cuadro de Tarsila do Amaral inspiró directamente el concepto del Movimiento Antropófago?",
                            "options": [
                                "Las señoritas de Aviñón",
                                "Abaporu ('hombre que come hombres' en tupí-guaraní)",
                                "Guernica",
                                "La Gioconda tropical"
                            ],
                            "correctIndex": 1,
                            "explanation": "El lienzo 'Abaporu' con su figura monumental de pie gigante y cabeza pequeña inspiró el manifiesto de 1928."
                        },
                        {
                            "question": "¿Qué obra capital de la literatura brasileña publicó Mário de Andrade en 1928 con el subtítulo 'el héroe sin ningún carácter'?",
                            "options": [
                                "Dom Casmurro",
                                "Macunaíma",
                                "Los sertones",
                                "Gran Sertón: Veredas"
                            ],
                            "correctIndex": 1,
                            "explanation": "Mário de Andrade escribió 'Macunaíma', la rapsodia mitológica del héroe proteico brasileño."
                        }
                    ]
                }
            }
        },
        "world/b2/b2-brasilsudeste-04": {
            "id": "b2-brasilsudeste-04",
            "title": "La síncopa suave: de la favela a la bossa nova",
            "level": "B2",
            "lesson": 4,
            "type": "world",
            "estimatedMinutes": 8,
            "summary": "La evolución de la música popular brasileña (MPB): el nacimiento de la samba en los barrios afrodescendientes de Río, la revolución minimalista de la bossa nova con João Gilberto y Tom Jobim, y la rebeldía del Tropicalismo.",
            "characters": [
                "Cartola y los compositores de las escuelas de samba de Mangueira",
                "João Gilberto, Antônio Carlos Jobim y Vinicius de Moraes",
                "Caetano Veloso y Gilberto Gil (creadores del Tropicalismo)"
            ],
            "paragraphs": [
                {
                    "type": "narration",
                    "text": "Bajo la brisa tibia que acaricia las calles arboladas del barrio carioca de Ipanema a finales de la década de 1950, un rumor musical íntimo, sutil y revolucionario comenzó a transformar para siempre la historia sonora del siglo veinte: la bossa nova. En primer término, para comprender la magnitud de esta alquimia estética, es preciso remontarse a las raíces profundas de la samba tradicional nacida décadas atrás en los conventillos de la 'Pequeña África' de Río de Janeiro y en las laderas de los morros. Allí, en comunidades afrobrasileñas como la Colina de Mangueira o Estácio de Sá, maestros geniales como Cartola, Ismael Silva y Noel Rosa tejieron sobre el cuero de los pandeiros y tamborines una síncopa rítmica arrebatadora. Es decir, la samba fue el himno vital y rebelde mediante el cual las poblaciones marginadas afirmaron su dignidad frente a la persecución policial y el desprecio clasista."
                },
                {
                    "type": "narration",
                    "text": "Hacia 1958, en un Brasil optimista que estrenaba la modernidad arquitectónica de Brasília y celebraba su primera Copa del Mundo de fútbol en Suecia, un joven guitarrista y cantante bahiano llamado João Gilberto encerró en un departamento de Copacabana una nueva manera de tocar y cantar. Acompañado por las armonías sofisticadas del compositor y pianista Antônio Carlos 'Tom' Jobim y las letras poéticas del diplomático Vinicius de Moraes, Gilberto lanzó el disco 'Chega de Saudade'. Por una parte, despojó a la interpretación vocal del dramatismo estridente y ampuloso de la vieja guardia radiofónica para adoptar un susurro coloquial y casi inaudible; por otra, inventó con el pulgar y los dedos de su mano derecha una 'batida' de guitarra acústica que condensaba en seis cuerdas toda la polirritmia compleja de una escuela de samba entera. Dicho en otros términos, la bossa nova inventó una moderna poética de la intimidad."
                },
                {
                    "type": "narration",
                    "text": "El impacto internacional de este sonido refinado fue sencillamente colosal y meteórico. En noviembre de 1962, los músicos de la bossa nova abarrotaron el prestigioso Carnegie Hall de Nueva York, desatando una fascinación inmediata entre los gigantes del jazz estadounidense como Stan Getz, Miles Davis y Frank Sinatra. Piezas inmortales compuestas por Jobim y Vinicius como 'Garota de Ipanema' —la segunda canción más grabada y versionada de la historia universal después de 'Yesterday'—, 'Corcovado' y 'Desafinado' conquistaron los diales de todo el planeta, demostrando que la música brasileña podía dialogar de igual a igual con las estructuras armónicas más refinadas de la música clásica y el jazz modal. En cualquier caso, no se trataba de una renuncia a las raíces autóctonas; de todos modos, la genialidad brasileña demostraba una vez más su infinita capacidad de reinvención estética."
                },
                {
                    "type": "narration",
                    "text": "No obstante este deslumbramiento melódico, la instauración de la dictadura militar en 1964 y la consiguiente censura política demandaron nuevas respuestas estéticas que sacudieron la escena nacional a través del 'Tropicalismo' en 1967. Liderado por jóvenes cantautores irreverentes como Caetano Veloso y Gilberto Gil, junto a bandas experimentales como Os Mutantes, el Tropicalismo fusionó la bossa nova con las guitarras eléctricas del rock psicodélico anglosajón, la música popular nordestina y la poesía concreta. A modo de ilustración de su audacia provocadora, el disco colectivo 'Tropicália: ou Panis et Circencis' arremetió tanto contra el autoritarismo militar de derecha como contra el dogmatismo purista de cierta izquierda nacionalista, reivindicando la antropofagia modernista en un torbellino de colores pop, guitarras distorsionadas y denuncia cívica valiente que forzó el exilio londinense de sus creadores."
                },
                {
                    "type": "narration",
                    "text": "En suma, la música popular brasileña (MPB) constituye el mayor patrimonio espiritual y la más luminosa carta de presentación del país ante la comunidad internacional. En última instancia, desde los tambores atronadores que hacen temblar el asfalto del carnaval carioca hasta las notas susurradas de una guitarra solitaria al atardecer frente al mar de Ipanema, la música brasileña enseña que la belleza y la melancolía —la intraducible 'saudade'— pueden convivir en una misma síncopa perfecta. En definitiva, en cada acorde disonante de Jobim y en cada verso lúcido de Caetano late el alma libre de una sociedad que canta a la vida para vencer a las sombras del desamparo y celebrar la fraternidad de la existencia humana."
                }
            ],
            "narration": {
                "pedagogical": {
                    "comprehensionQuestions": [
                        {
                            "question": "¿Qué innovación revolucionaria aportó João Gilberto a la interpretación de la música popular?",
                            "options": [
                                "La invención de un sintetizador electrónico digital de gran potencia.",
                                "El canto susurrado y coloquial junto a una 'batida' de guitarra que condensaba la polirritmia de la samba.",
                                "La eliminación absoluta de la guitarra acústica en favor del trombón de varas.",
                                "La traducción obligatoria de todas las letras de canciones al inglés comercial."
                            ],
                            "correctIndex": 1,
                            "explanation": "João Gilberto transformó la música con su voz íntima y su rítmica de guitarra sincopada en 'Chega de Saudade'."
                        },
                        {
                            "question": "¿Quiénes compusieron la célebre canción 'Garota de Ipanema'?",
                            "options": [
                                "Cartola y Nelson Cavaquinho.",
                                "Antônio Carlos Jobim en la música y Vinicius de Moraes en la letra.",
                                "Caetano Veloso y Gilberto Gil.",
                                "Chico Buarque y Milton Nascimento."
                            ],
                            "correctIndex": 1,
                            "explanation": "Tom Jobim compuso la música y Vinicius de Moraes la letra de la emblemática 'Garota de Ipanema'."
                        },
                        {
                            "question": "¿Qué propuesta estética y política caracterizó al movimiento del Tropicalismo a fines de los años sesenta?",
                            "options": [
                                "El rechazo absoluto de cualquier instrumento musical moderno.",
                                "La fusión iconoclasta entre la bossa nova, el rock psicodélico con guitarras eléctricas y la denuncia contra la dictadura.",
                                "La vuelta estricta a los cantos gregorianos de la época colonial.",
                                "La creación de marchas militares exclusivamente para desfiles castrenses."
                            ],
                            "correctIndex": 1,
                            "explanation": "El Tropicalismo combinó vanguardia pop, guitarras eléctricas y crítica política desafiando el cerco censor."
                        }
                    ]
                }
            }
        },
        "world/b2/b2-brasilsudeste-05": {
            "id": "b2-brasilsudeste-05",
            "title": "Palabras hermanas: el diálogo fecundo entre el español y el portugués",
            "level": "B2",
            "lesson": 5,
            "type": "world",
            "estimatedMinutes": 8,
            "summary": "El encuentro lingüístico y cultural en las fronteras luso-hispanas: los desafíos de la intercomprensión, la trampa fascinante de los falsos amigos, el fenómeno híbrido del portuñol y el liderazgo diplomático de Itamaraty.",
            "characters": [
                "Diplomáticos de Itamaraty y del Palacio San Martín de Buenos Aires",
                "Lingüistas y traductores de conferencias internacionales",
                "Comerciantes y pobladores fronterizos de la Triple Frontera y el Chuy"
            ],
            "paragraphs": [
                {
                                "type": "narration",
                                "text": "A lo largo de más de dieciséis mil kilómetros de fronteras terrestres ininterrumpidas en el corazón de América del Sur, el mundo lusófono y el universo hispanohablante conviven en un diálogo cotidiano de proximidad geográfica, comercial y afectiva sin paralelo en ningún otro continente del planeta. En primer término, el español y el portugués comparten más del ochenta y cinco por ciento de similitud léxica y gramatical, fruto de su origen común en el latín vulgar de la península ibérica. Es decir, un hispanohablante culto puede comprender con relativa facilidad un texto escrito en portugués sin haberlo estudiado formalmente, al igual que un lector brasileño descifra sin tropiezos un editorial de prensa en castellano. Sin embargo, esta aparente transparencia encierra sutiles paradojas comunicativas que exigen del estudiante de nivel B2 una mirada analítica, prudente y vigilante."
                },
                {
                                "type": "narration",
                                "text": "La trampa comunicativa más fascinante y peligrosa en este diálogo bilateral estriba en la existencia de los denominados 'falsos amigos' o falsos cognados, aquellas palabras de idéntica o similar grafía cuya carga semántica diverge drásticamente en ambas lenguas hermanas. Por una parte, un viajero hispanohablante en Río de Janeiro puede sentirse profundamente desconcertado cuando en un restaurante le sirven un plato que el camarero califica de 'esquisito', ignorando que en portugués ese adjetivo significa 'raro o extravagante', y no 'delicioso o primoroso' como en castellano; por otra parte, términos cotidianos como 'propina' (que en portugués alude a un 'soborno ilícito' y no a la gratificación voluntaria de servicio), 'embarazada' (cuyo equivalente luso es 'grávida', mientras que 'embaraçada' significa 'avergonzada o enredada') o 'apellido' (que en portugués designa el 'apodo o sobrenombre') provocan equívocos hilarantes o momentos de tensión diplomática. Asimismo, 'escritório' designa una oficina de trabajo en Brasil y no el mueble físico, mientras que el verbo 'latir' alude a los ladridos caninos y no a los latidos del corazón. Dicho en otros términos, la familiaridad excesiva suele ser el peor enemigo de la precisión lingüística."
                },
                {
                                "type": "narration",
                                "text": "En las extensas franjas fronterizas que unen a Brasil con Uruguay, Argentina, Paraguay, Bolivia, Perú y Colombia, este contacto secular ha dado origen a variedades de habla mixtas de extraordinaria vitalidad sociolingüística, conocidas genéricamente como 'portuñol' o 'portunhol'. En ciudades gemelas fronterizas como Rivera y Santana do Livramento —donde la línea divisoria internacional es apenas una acera peatonal en una plaza pública compartida—, la ciudadanía transita con asombrosa naturalidad de un idioma al otro en la misma frase, forjando un dialecto comunitario propio con fonética portuguesa y léxico castellano. En cualquier caso, lejos de constituir una degradación idiomática o una anomalía censurable, los sociolingüistas contemporáneos valoran al portuñol como una formidable herramienta pragmática de integración comercial, cooperación vecinal y convivencia pacífica entre pueblos hermanos que comparten ferias, comparsas y familias."
                },
                {
                                "type": "narration",
                                "text": "En el terreno de la alta política exterior, la diplomacia profesional brasileña tutelada por el histórico palacio de Itamaraty ha considerado históricamente el entendimiento estratégico con los países hispanoamericanos como un pilar innegociable de su liderazgo continental. Por poner un caso representativo, la firma en 1991 del Tratado de Asunción que fundó el Mercosur consagró al español y al portugués como lenguas oficiales de trabajo en pie de estricta igualdad jurídica, obligando a los Estados miembros a incorporar la enseñanza del idioma vecino en los currículos escolares secundarios. Cuanto más cooperan ambas esferas culturales en organismos multilaterales y proyectos de ciencia compartida, tanto más se robustece la voz soberana de América del Sur frente a los grandes bloques de poder geopolítico global."
                },
                {
                                "type": "narration",
                                "text": "En suma, el encuentro fecundo entre el español y el portugués no debe concebirse como una rivalidad lingüística, sino como el privilegio único de compartir un espacio de intercomprensión que abraza a más de seiscientos millones de personas en el mundo entero. En última instancia, aprender a navegar los matices, las cadencias sonoras y los falsos amigos de la lengua de Machado de Assis, Clarice Lispector y Tom Jobim permite al hispanohablante completar su propia identidad continental. En definitiva, tender puentes de afecto, lectura y traducción entre ambas orillas idiomáticas es honrar la más noble promesa de la hermandad iberoamericana: la certeza de que en la diversidad de nuestras palabras hermanas reside la verdadera riqueza de nuestro porvenir común."
                }
],
            "narration": {
                "pedagogical": {
                    "comprehensionQuestions": [
                        {
                            "question": "¿Qué porcentaje aproximado de similitud léxica y gramatical comparten el español y el portugués?",
                            "options": [
                                "Menos del veinte por ciento.",
                                "Aproximadamente un cincuenta por ciento.",
                                "Más del ochenta y cinco por ciento, fruto de su origen común en el latín peninsular.",
                                "El cien por ciento sin ninguna divergencia."
                            ],
                            "correctIndex": 2,
                            "explanation": "Ambas lenguas ibéricas comparten más del 85% de vocabulario básico y estructuras gramaticales."
                        },
                        {
                            "question": "¿Qué significa el adjetivo portugués 'esquisito' a diferencia del español 'exquisito'?",
                            "options": [
                                "Significa 'sumamente sabroso y refinado'.",
                                "Significa 'raro, extraño o extravagante', constituyendo un clásico falso amigo.",
                                "Significa 'frío o congelado'.",
                                "Significa 'gratuito o libre de impuestos'."
                            ],
                            "correctIndex": 1,
                            "explanation": "En portugués 'esquisito' denota algo extraño o raro, mientras que en español significa delicioso."
                        },
                        {
                            "question": "¿Qué tratado internacional de 1991 consagró la igualdad oficial del español y el portugués en el Mercosur?",
                            "options": [
                                "El Tratado de Tordesillas",
                                "El Tratado de Asunción",
                                "El Protocolo de Kioto",
                                "El Pacto Andino"
                            ],
                            "correctIndex": 1,
                            "explanation": "El Tratado de Asunción estableció las bases del Mercosur reconociendo a ambas lenguas como oficiales de trabajo."
                        }
                    ]
                }
            }
        },
        "world/b2/b2-brasilsudeste-consolidation": {
            "id": "b2-brasilsudeste-consolidation",
            "title": "El murmullo del Atlántico y el alma del Sureste",
            "level": "B2",
            "lesson": 6,
            "type": "world",
            "estimatedMinutes": 8,
            "summary": "Síntesis integradora sobre la región del Sureste brasileño: la fascinante complementariedad entre la potencia fabril paulista y el lirismo costero carioca, la huella perenne del modernismo de 1922 y los lazos fraternos con el mundo hispano.",
            "characters": [
                "Narradores, cronistas urbanos y ciudadanos del Sureste",
                "El océano Atlántico como testigo de las olas migratorias y las vanguardias"
            ],
            "paragraphs": [
                {
                                "type": "narration",
                                "text": "Al contemplar desde la ventanilla de un vuelo nocturno las constelaciones infinitas de luces doradas que tapizan la franja costera entre São Paulo y Río de Janeiro, el viajero atento descubre la formidable magnitud del corazón demográfico, económico y cultural de América del Sur. En primer término, el Sureste brasileño no es una simple división administrativa en el mapa geográfico nacional; es el motor colosal donde conviven en fecunda tensión dos almas urbanas complementarias, complejas y deslumbrantes. Por una parte, la inmensa urbe paulistana encarna la disciplina infatigable del trabajo fabril, la sobriedad vanguardista de la arquitectura de hormigón y el pulso financiero que conecta a la región con los mercados del planeta entero; por otra, la Ciudad Maravillosa carioca destila una gracia natural irrepetible donde la belleza escarpada de los morros abraza el mar en un himno cotidiano a la alegría vital y a la sociabilidad espontánea."
                },
                {
                                "type": "narration",
                                "text": "Esta fascinante dualidad regional floreció sobre el sustrato histórico de profundas transformaciones sociales que marcaron a fuego el destino del país durante el siglo veinte. Es decir, tanto en los talleres textiles alimentados por la masiva inmigración italiana y japonesa como en los callejones portuarios de Lapa donde los descendientes de africanos esclavizados crearon la síncopa de la samba, la identidad del Sureste se fraguó a través de la confluencia de sangres y culturas diversas. Dicho en otros términos, la riqueza de esta tierra no estribó únicamente en las cosechas opulentas de los cafetales ni en los yacimientos minerales de las sierras de Minas Gerais, sino más bien en la prodigiosa capacidad de su pueblo para inventar nuevas formas de sociabilidad democrática en medio de abismales desigualdades heredadas de la época colonial."
                },
                {
                                "type": "narration",
                                "text": "En el terreno de las artes y las ideas, la Semana de Arte Moderno de 1922 y el Movimiento Antropófago continúan operando como el faro conceptual insustituible de la creatividad iberoamericana. Lejos de sucumbir a la nostalgia conservadora, creadores plásticos como Tarsila do Amaral y poetas como Oswald y Mário de Andrade enseñaron que la originalidad estética consiste en digerir con lucidez crítica las influencias foráneas para engendrar un arte soberano, telúrico y universal. En cualquier caso, esta lección de audacia se prolongó décadas más tarde en la síncopa íntima de la bossa nova de João Gilberto y Tom Jobim y en la rebeldía del Tropicalismo de Caetano Veloso y Gilberto Gil, demostrando que la música popular puede alcanzar las cotas más altas del refinamiento poético y de la crítica sociopolítica frente a los autoritarismos."
                },
                {
                                "type": "narration",
                                "text": "Asimismo, el Sureste brasileño representa el umbral más generoso para el diálogo fecundo y continuo con el mundo hispanohablante. A lo largo de la historia compartida, diplomáticos visionarios, novelistas de la talla de Machado de Assis y millones de ciudadanos fronterizos han demostrado que la proximidad lingüística entre el español y el portugués no es una barrera insalvable, sino una maravillosa invitación a la intercomprensión y a la hermandad continental. A modo de ilustración, en cada feria del libro, en cada intercambio universitario y en cada convenio bilateral de integración económica se renueva el pacto implícito de una América del Sur unida en su fecunda diversidad de palabras hermanas y visiones compartidas sobre la paz y el desarrollo sostenible."
                },
                {
                                "type": "narration",
                                "text": "En suma, quien recorre el Sureste de Brasil y escucha con atención el murmullo de sus calles comprende que aquí se ensayan a diario las respuestas a los grandes dilemas de la civilización contemporánea: cómo conciliar la pujanza del desarrollo industrial con la preservación ecológica de la Mata Atlántica y la justicia distributiva para todos los ciudadanos. En última instancia, bajo la bendición serena del Cristo en el Corcovado y frente a la silueta desafiante de los rascacielos de la Avenida Paulista, late la promesa inmortal de un pueblo generoso y creador. En definitiva, el Sureste continuará proyectando su luz sobre el continente entero, recordándonos que en el arte de vivir juntos con pasión y dignidad reside el más noble de los destinos humanos."
                }
],
            "narration": {
                "pedagogical": {
                    "comprehensionQuestions": [
                        {
                            "question": "¿Cuáles son las dos grandes metrópolis complementarias que articulan el corazón cultural del Sureste brasileño?",
                            "options": [
                                "Manaus y Belém do Pará.",
                                "São Paulo con su potencia industrial y financiera, y Río de Janeiro con su gracia costera y musical.",
                                "Brasília y Goiânia en el altiplano central.",
                                "Salvador de Bahía y Recife en la costa nordestina."
                            ],
                            "correctIndex": 1,
                            "explanation": "São Paulo y Río de Janeiro representan los dos polos urbanos y culturales esenciales del Sureste."
                        },
                        {
                            "question": "¿Qué legado intelectual de 1922 sigue inspirando la creación artística en la región?",
                            "options": [
                                "El retorno al estilo barroco colonial eclesiástico.",
                                "La Semana de Arte Moderno y la teoría antropofágica de asimilar críticamente el mundo para crear arte propio.",
                                "La prohibición de celebrar desfiles de carnaval.",
                                "La clausura definitiva de todas las galerías de arte contemporáneo."
                            ],
                            "correctIndex": 1,
                            "explanation": "El modernismo y la antropofagia fundamentaron la autonomía estética y la originalidad del arte brasileño."
                        },
                        {
                            "question": "¿Cuál es la conclusión principal sobre el diálogo entre el portugués y el español en el continente?",
                            "options": [
                                "Que ambas lenguas deben competir hasta que una de ellas desaparezca por completo.",
                                "Que la alta similitud lingüística y la intercomprensión facilitan una profunda integración y fraternidad iberoamericana.",
                                "Que es imposible que un hispanohablante comprenda textos en portugués sin traducción simultánea.",
                                "Que el portuñol debe ser erradicado por ley mediante multas comerciales."
                            ],
                            "correctIndex": 1,
                            "explanation": "La cercanía de ambas lenguas y la intercomprensión potencian la cooperación y la riqueza cultural regional."
                        }
                    ]
                }
            }
        },
        "world/b2/b2-brasilsudeste": {
            "id": "b2-brasilsudeste",
            "title": "Brasil I: Los Motores Culturales: Río, São Paulo y el Modernismo",
            "level": "B2",
            "lesson": 1,
            "type": "world",
            "estimatedMinutes": 20,
            "summary": "Compendio general sobre la región del Sureste brasileño: la colosal potencia metropolitana de São Paulo y su inmigración global, la deslumbrante topografía y el alma carioca de Río de Janeiro, la revolución vanguardista de la Semana de 1922 y la antropofagia, el florecimiento lírico de la bossa nova y el fecundo diálogo luso-hispano.",
            "characters": [
                "Pioneros cafetaleros e inmigrantes de São Paulo",
                "Poetas, músicos y habitantes de los morros cariocas",
                "Los artistas de la Semana de Arte Moderno de 1922",
                "Diplomáticos, lingüistas y ciudadanos del espacio iberoamericano"
            ],
            "paragraphs": [
                {
                                "type": "narration",
                                "text": "En la vertiente atlántica meridional del continente suramericano late el motor industrial, financiero y cultural más formidable del orbe lusófono: la región del Sureste de Brasil. Con una población que supera los ochenta y cinco millones de habitantes repartidos entre los estados de São Paulo, Río de Janeiro, Minas Gerais y Espírito Santo, este territorio concentra la mayor densidad económica e intelectual del país. En primer término, el ascenso meteórico de São Paulo desde fines del siglo diecinueve transformó una tranquila meseta de origen misionero en una metrópolis global imponente gracias a los dividendos de la economía cafetalera y a una de las mayores olas de inmigración internacional de la historia moderna, acogiendo a millones de italianos, japoneses, sirio-libaneses y migrantes de todas las latitudes en un mosaico cosmopolita sin comparación que hoy lidera la tecnología y las finanzas continentales."
                },
                {
                                "type": "narration",
                                "text": "A escasa distancia geográfica pero con una personalidad urbana contrastante y singular, Río de Janeiro despliega ante el mundo la magia de su emplazamiento costero donde los morros de granito macizo coronados por la selva atlántica de Tijuca abrazan las aguas de la bahía de Guanabara y las playas abiertas de Copacabana e Ipanema. Antigua capital de la corte monárquica portuguesa trasladada en 1808 y sede del gobierno imperial y republicano hasta 1960, la 'Ciudad Maravillosa' atesora un porte señorial y cosmopolita que convive con el urbanismo informal y resistente de las favelas en las laderas de los morros, donde la ayuda mutua florece a diario. Es allí, en medio de la contigüidad espacial entre la opulencia y la precariedad, donde floreció el espíritu carioca: una filosofía de vida abierta, solidaria y festiva que hace del carnaval, del fútbol y del encuentro al aire libre un testimonio supremo de dignidad humana."
                },
                {
                                "type": "narration",
                                "text": "En el terreno estético y filosófico, el Sureste brasileño protagonizó en febrero de 1922 una de las rupturas de vanguardia más fecundas de América Latina con la celebración de la histórica Semana de Arte Moderno en el Teatro Municipal de São Paulo. Intelectuales y artistas visionarios como Oswald de Andrade, Mário de Andrade, Anita Malfatti y Tarsila do Amaral dinamitaron la tutela mimética de los cánones academicistas europeos para proclamar la 'Antropofagia cultural'. Mediante este concepto revolucionario plasmado en obras capitales como el lienzo 'Abaporu' y la novela 'Macunaíma', el artista brasileño fue convocado a devorar críticamente las influencias técnicas foráneas para digerirlas y transformarlas en una creación enteramente propia, mestiza, telúrica y emancipadora que redefinió el alma americana."
                },
                {
                                "type": "narration",
                                "text": "Esta vocación estética deslumbró nuevamente al mundo en las décadas de 1950 y 1960 con el nacimiento de la bossa nova en los apartamentos cariocas, de la mano de figuras irrepetibles como João Gilberto, Antônio Carlos Jobim y Vinicius de Moraes. Al despojar a la samba de estridencias y condensar en la batida sutil de una guitarra acústica la polirritmia de los morros, la bossa nova conquistó los escenarios del jazz internacional con himnos eternos como 'Garota de Ipanema'. Poco después, frente a la censura de la dictadura militar, la vanguardia sonora se reinventó en el 'Tropicalismo' de Caetano Veloso y Gilberto Gil, fusionando la cadencia tradicional con las guitarras eléctricas del rock psicodélico para desafiar con valentía estética y poesía comprometida el autoritarismo reinante, abriendo cauces inéditos para la libertad de expresión ciudadana que inspiraron a toda la juventud del continente."
                },
                {
                                "type": "narration",
                                "text": "Finalmente, el Sureste se erige en el puente natural de diálogo e intercomprensión con el universo hispanoamericano. Con más de dieciséis mil kilómetros de fronteras compartidas y una similitud léxica superior al ochenta y cinco por ciento entre el portugués y el castellano, ambas lenguas hermanas han aprendido a sortear la trampa de los falsos amigos para forjar un espacio de integración soberana a través del Mercosur y la diplomacia de Itamaraty. En definitiva, el Sureste de Brasil ofrece al estudiante de español una ventana privilegiada hacia la riqueza de la condición humana, demostrando que en el abrazo fraterno entre las culturas lusas e hispanas se dibuja el porvenir luminoso y solidario de toda la patria grande americana."
                }
],
            "narration": {
                "pedagogical": {
                    "comprehensionQuestions": [
                        {
                            "question": "¿Qué factor económico y social transformó a São Paulo en una metrópolis global en el siglo XX?",
                            "options": [
                                "La pesca de perlas en el río Tietê.",
                                "La riqueza acumulada por la exportación de café y la masiva inmigración de italianos, japoneses y libaneses.",
                                "La minería de plata en la selva virgen del norte.",
                                "La compra de tierras por parte de la marina británica."
                            ],
                            "correctIndex": 1,
                            "explanation": "El auge cafetalero y la oleada migratoria convirtieron a São Paulo en el mayor polo industrial del hemisferio sur."
                        },
                        {
                            "question": "¿Qué planteaba el concepto vanguardista de la 'Antropofagia' de Oswald de Andrade?",
                            "options": [
                                "El regreso a la vida nómada en las selvas vírgenes.",
                                "Devorar críticamente las influencias culturales europeas para transformarlas en un arte nacional propio y soberano.",
                                "La traducción literal de todas las enciclopedias francesas.",
                                "El rechazo absoluto de cualquier forma de pintura o música."
                            ],
                            "correctIndex": 1,
                            "explanation": "La antropofagia propone asimilar críticamente lo exterior para enriquecer la propia expresión cultural mestiza."
                        },
                        {
                            "question": "¿Qué género musical revolucionó el panorama internacional desde Río de Janeiro a fines de la década de 1950?",
                            "options": [
                                "La cumbia villera",
                                "La bossa nova, creada por João Gilberto, Tom Jobim y Vinicius de Moraes",
                                "El tango sinfónico con bandoneón",
                                "El vallenato con acordeón diatónico"
                            ],
                            "correctIndex": 1,
                            "explanation": "La bossa nova transformó la música mundial mediante su cadencia íntima, susurrada y armónicamente compleja."
                        }
                    ]
                }
            }
        }
    }

    # Verify word counts for all stories
    for path, sobj in stories.items():
        wc = count_words(sobj)
        print(f"stories/{path}.json: {wc} words")
        assert 650 <= wc <= 825, f"WARNING: Story {path} word count {wc} out of range [650, 825]!"
        write_json(f"stories/{path}.json", sobj)

    # 6. Exercises
    def make_exercises():
        # Core b2-29-01 to 05
        core_ex = {
            "b2-29-01": [
                {
                    "id": "b2-29-01.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["marcadores-reformulacion-explicativa"],
                    "question": "¿Cuál es la función del marcador 'es decir' en un texto argumentativo formal?",
                    "options": [
                        "Contradecir frontalmente la afirmación anterior para anularla.",
                        "Introducir una explicación o paráfrasis que aclara y precisa lo antedicho.",
                        "Expresar una duda insuperable sobre los datos presentados.",
                        "Formular una despedida protocolaria en correspondencia diplomática."
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-29-01.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-reformulacion-explicativa"],
                    "sentence": "El proyecto exige rigor metodológico, __ decir, un control experimental estricto de las variables.",
                    "answer": "es",
                    "english": "The project demands methodological rigor, that is to say, strict experimental control of the variables."
                },
                {
                    "id": "b2-29-01.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["marcadores-reformulacion-explicativa"],
                    "pairs": [
                        ["es decir", "aclaración o paráfrasis explicativa"],
                        ["o sea", "reexpresión equivalente de uso extendido"],
                        ["esto es", "definición precisa en registro formal"],
                        ["a saber", "enumeración detallada de elementos anunciados"]
                    ]
                },
                {
                    "id": "b2-29-01.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-reformulacion-explicativa"],
                    "sentence": "La reforma reconoce tres derechos fundamentales, a __: la educación, la salud y la vivienda.",
                    "answer": "saber",
                    "english": "The reform recognizes three fundamental rights, namely: education, healthcare, and housing."
                },
                {
                    "id": "b2-29-01.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-29-vocab"],
                    "question": "¿Qué adjetivo califica aquello que no admite duda o equívoco por su total claridad?",
                    "options": [
                        "Inequívoco",
                        "Tangencial",
                        "Ambivalente",
                        "Subjetivo"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-29-01.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Por qué Bento Santiago hizo construir su casa de Engenho Novo idéntica a la de su infancia?",
                    "options": [
                        "Para ahorrar en planos arquitectónicos.",
                        "Para revivir con obsesión arqueológica el pasado y los recuerdos de su amor por Capitu.",
                        "Porque era una ordenanza municipal de Río de Janeiro.",
                        "Para montar una galería de arte con cuadros de pintores extranjeros."
                    ],
                    "correct": 1
                }
            ],
            "b2-29-02": [
                {
                    "id": "b2-29-02.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["marcadores-reformulacion-rectificativa"],
                    "question": "¿Qué marcador permite corregir un vocablo previo para emplear otro más exacto?",
                    "options": [
                        "Por consiguiente",
                        "Mejor dicho",
                        "En consecuencia",
                        "Habida cuenta de"
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-29-02.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-reformulacion-rectificativa"],
                    "sentence": "No se trata de un simple error burocrático; más __, constituye una negligencia institucional grave.",
                    "answer": "bien",
                    "english": "It is not a mere bureaucratic error; rather, it constitutes serious institutional negligence."
                },
                {
                    "id": "b2-29-02.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["marcadores-reformulacion-rectificativa"],
                    "pairs": [
                        ["mejor dicho", "rectificación espontánea o corrección léxica"],
                        ["más bien", "matización correctiva tras negación previa"],
                        ["más exactamente", "ajuste de alta precisión conceptual"],
                        ["antes bien", "contraposición correctiva formal"]
                    ]
                },
                {
                    "id": "b2-29-02.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-reformulacion-rectificativa"],
                    "sentence": "El informe no concluyó la auditoría; más __, suspendió las actuaciones hasta recibir nuevas pruebas.",
                    "answer": "exactamente",
                    "english": "The report did not conclude the audit; more precisely, it suspended proceedings until receiving new evidence."
                },
                {
                    "id": "b2-29-02.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-29-vocab"],
                    "question": "¿Cómo se denomina el vocablo que por su similitud formal con otro de lengua extranjera induce a error semántico?",
                    "options": [
                        "Falso cognado o falso amigo",
                        "Neologismo fonético",
                        "Cultismo arcaico",
                        "Sufijo apreciativo"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-29-02.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué metáfora inmortal definió la mirada seductora y enigmática de Capitu?",
                    "options": [
                        "Ojos de relámpago andino",
                        "Ojos de resaca marina, que atraían hacia el fondo como la marea del mar",
                        "Ojos de águila serrana",
                        "Ojos de obsidiana volcánica"
                    ],
                    "correct": 1
                }
            ],
            "b2-29-03": [
                {
                    "id": "b2-29-03.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["marcadores-reformulacion-distanciamiento"],
                    "question": "¿Qué función cumple el marcador 'de todos modos' en un debate formal?",
                    "options": [
                        "Invalidar las normas gramaticales del idioma.",
                        "Restar trascendencia a objeciones previas para reafirmar la tesis principal con independencia de ellas.",
                        "Solicitar la palabra en un tribunal de justicia.",
                        "Introducir un agradecimiento formal."
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-29-03.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-reformulacion-distanciamiento"],
                    "sentence": "Hubo discrepancias metodológicas; en __ caso, las conclusiones generales siguen siendo válidas.",
                    "answer": "cualquier",
                    "english": "There were methodological discrepancies; in any case, the general conclusions remain valid."
                },
                {
                    "id": "b2-29-03.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["marcadores-reformulacion-distanciamiento"],
                    "pairs": [
                        ["en cualquier caso", "reafirmación independiente de contingencias"],
                        ["de todos modos", "relativización de objeciones secundarias"],
                        ["de cualquier manera", "distanciamiento pragmático de reparos"],
                        ["de todas formas", "reanudación argumentativa con reserva"]
                    ]
                },
                {
                    "id": "b2-29-03.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-reformulacion-distanciamiento"],
                    "sentence": "Las negociaciones fueron arduas; de __ modos, se alcanzó un preacuerdo satisfactorio.",
                    "answer": "todos",
                    "english": "The negotiations were arduous; in any case, a satisfactory preliminary agreement was reached."
                },
                {
                    "id": "b2-29-03.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-29-vocab"],
                    "question": "¿Qué sustantivo expresa una advertencia, excepción o reserva que limita el alcance de una afirmación?",
                    "options": [
                        "La salvedad",
                        "El corolario",
                        "La sinopsis",
                        "El arquetipo"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-29-03.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué acontecimiento trágico detonó la sospecha destructiva de Bento sobre la fidelidad de Capitu?",
                    "options": [
                        "El hallazgo de una carta de amor en un baúl secreto.",
                        "El dolor desconsolado de Capitu ante el cadáver de Escobar y el asombroso parecido de su hijo con el difunto amigo.",
                        "La confesión pública del párroco en misa mayor.",
                        "Una condena judicial por estafa en los tribunales."
                    ],
                    "correct": 1
                }
            ],
            "b2-29-04": [
                {
                    "id": "b2-29-04.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["marcadores-reformulacion-recapitulativa"],
                    "question": "¿Cuál es la utilidad discursiva de la locución 'dicho en otros términos'?",
                    "options": [
                        "Ocultar el significado de las palabras mediante giros crípticos.",
                        "Presentar una paráfrasis condensada que clarifica un argumento complejo.",
                        "Poner fin inmediatamente a una entrevista.",
                        "Insultar sutilmente al interlocutor."
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-29-04.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-reformulacion-recapitulativa"],
                    "sentence": "Dicho en __ términos, la soberanía energética garantiza la estabilidad macroeconómica nacional.",
                    "answer": "otros",
                    "english": "In other words, energy sovereignty guarantees national macroeconomic stability."
                },
                {
                    "id": "b2-29-04.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["marcadores-reformulacion-recapitulativa"],
                    "pairs": [
                        ["dicho en otros términos", "paráfrasis formal y sintética"],
                        ["en otras palabras", "reexplicación clarificadora estándar"],
                        ["dicho de otro modo", "reexpresión estilística equilibrada"],
                        ["dicho más sencillamente", "traducción a registro accesible"]
                    ]
                },
                {
                    "id": "b2-29-04.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-reformulacion-recapitulativa"],
                    "sentence": "Dicho de __ modo, la modernidad artística exigió una ruptura radical con el pasado.",
                    "answer": "otro",
                    "english": "Put another way, artistic modernity demanded a radical break with the past."
                },
                {
                    "id": "b2-29-04.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-29-vocab"],
                    "question": "¿Qué término técnico designa la explicación o interpretación amplificativa de un texto?",
                    "options": [
                        "La paráfrasis",
                        "El falso cognado",
                        "La salvedad",
                        "El escepticismo"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-29-04.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Por qué 'Dom Casmurro' se considera una de las cumbres universales de la novela con narrador no confiable?",
                    "options": [
                        "Porque el autor olvidó firmar los capítulos finales.",
                        "Porque todo el relato procede de la memoria obsesiva y celosa de Bento, sin que el lector pueda verificar si el adulterio existió realmente.",
                        "Porque fue prohibida por los censores del imperio de Pedro II.",
                        "Porque el narrador finge ser un fantasma del siglo dieciséis."
                    ],
                    "correct": 1
                }
            ],
            "b2-29-05": [
                {
                    "id": "b2-29-05.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["marcadores-reformulacion-ejemplificativa"],
                    "question": "¿Qué locución formal introduce un caso particular para demostrar una regla abstracta?",
                    "options": [
                        "En resumen",
                        "A modo de ilustración",
                        "Por consiguiente",
                        "Sin perjuicio de"
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-29-05.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-reformulacion-ejemplificativa"],
                    "sentence": "Por poner un __ ilustrativo, analicemos la rápida expansión del ferrocarril paulista en el siglo XIX.",
                    "answer": "caso",
                    "english": "To cite an illustrative case, let us analyze the rapid expansion of the Paulista railway in the 19th century."
                },
                {
                    "id": "b2-29-05.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["marcadores-reformulacion-ejemplificativa"],
                    "pairs": [
                        ["a modo de ilustración", "presentación de ejemplo clarificador"],
                        ["por poner un caso", "selección de caso concreto ilustrativo"],
                        ["verbigracia", "cultismo ensayístico clásico"],
                        ["pongamos por caso", "planteamiento de hipótesis demostrativa"]
                    ]
                },
                {
                    "id": "b2-29-05.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-reformulacion-ejemplificativa"],
                    "sentence": "Muchos vocablos aparentan igualdad; __, el portugués 'exquisito' significa raro y no sabroso.",
                    "answer": "verbigracia",
                    "english": "Many words appear identical; for instance, Portuguese 'exquisito' means strange and not delicious."
                },
                {
                    "id": "b2-29-05.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-29-vocab"],
                    "question": "¿Qué sustantivo designa un modelo ejemplar que sirve de pauta o norma suprema en una disciplina?",
                    "options": [
                        "El paradigma",
                        "El exordio",
                        "La paráfrasis",
                        "La digresión"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-29-05.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué destino final sufrieron Capitu y su hijo Ezequiel en la obra de Machado de Assis?",
                    "options": [
                        "Permanecieron en Río administrando los bienes de la familia.",
                        "Fueron desterrados a Europa por Bento Santiago, muriendo Capitu en Suiza en la soledad.",
                        "Emigraron a Buenos Aires para fundar una compañía de ópera.",
                        "Huyeron a las minas de oro del interior paulista."
                    ],
                    "correct": 1
                }
            ],
            "b2-29-consolidation": [
                {
                    "id": "b2-29-consolidation.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["marcadores-reformulacion-explicativa"],
                    "question": "¿Cuál es la puntuación normativa adecuada para el marcador explicativo 'es decir' en interior de período?",
                    "options": [
                        "Debe aislarse entre comas: 'La ley protege, es decir, garantiza los derechos civiles.'",
                        "No debe llevar ninguna coma alrededor.",
                        "Debe ir siempre precedido por dos puntos y seguido de punto final.",
                        "Debe colocarse entre signos de interrogación obligatorios."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-29-consolidation.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-reformulacion-rectificativa"],
                    "sentence": "No pretendían abolir la tradición; más __, buscaban revitalizarla con nuevas formas expresivas.",
                    "answer": "bien",
                    "english": "They did not seek to abolish tradition; rather, they sought to revitalize it with new expressive forms."
                },
                {
                    "id": "b2-29-consolidation.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["marcadores-reformulacion-distanciamiento"],
                    "question": "¿Qué marcador de distanciamiento es el preferido en la prosa académica formal por su sobriedad?",
                    "options": [
                        "Igual nomás",
                        "En cualquier caso",
                        "De una",
                        "Sea como sea de cualquier forma"
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-29-consolidation.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-reformulacion-recapitulativa"],
                    "sentence": "Dicho en otros __, la cohesión comunitaria depende de la justicia distributiva.",
                    "answer": "términos",
                    "english": "In other words, community cohesion depends on distributive justice."
                },
                {
                    "id": "b2-29-consolidation.ex05",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["marcadores-reformulacion-ejemplificativa"],
                    "question": "¿Qué locución culta introduce un caso representativo en el ensayo humanístico?",
                    "options": [
                        "A modo de ilustración",
                        "De sopetón",
                        "A tontas y a locas",
                        "A ciencia cierta"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-29-consolidation.ex06",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-29-vocab"],
                    "pairs": [
                        ["inequívoco", "claro y libre de toda duda"],
                        ["falso cognado", "palabra engañosa por similitud formal"],
                        ["salvedad", "reserva o advertencia limitativa"],
                        ["paradigma", "modelo teórico o pauta ejemplar"]
                    ]
                },
                {
                    "id": "b2-29-consolidation.ex07",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["marcadores-reformulacion-explicativa"],
                    "sentence": "El dictamen requiere validación técnica, __ es, la firma del colegio de ingenieros.",
                    "answer": "esto",
                    "english": "The opinion requires technical validation, that is, the signature of the college of engineers."
                },
                {
                    "id": "b2-29-consolidation.ex08",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué tema universal aborda la obra 'Dom Casmurro' de Machado de Assis?",
                    "options": [
                        "La conquista territorial de las selvas del Amazonas.",
                        "La naturaleza destructiva de los celos retrospectivos y la falibilidad de la memoria subjetiva.",
                        "El auge de la minería de esmeraldas en Colombia.",
                        "La navegación comercial a vapor en el Misisipi."
                    ],
                    "correct": 1
                }
            ]
        }

        # Regional b2-brasilsudeste-01 to 05
        reg_ex = {
            "b2-brasilsudeste-01": [
                {
                    "id": "b2-brasilsudeste-01.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["brasil-conectores-contraste"],
                    "question": "¿Qué conector contrastivo confronta de modo equilibrado dos facetas simultáneas de una realidad urbana?",
                    "options": [
                        "Además",
                        "Mientras que",
                        "Asimismo",
                        "Por ende"
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-brasilsudeste-01.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["brasil-conectores-contraste"],
                    "sentence": "El centro financiero concentra la riqueza; en __, las periferias reclaman inversiones básicas.",
                    "answer": "contrapartida",
                    "english": "The financial center concentrates wealth; in contrast, the peripheries demand basic investments."
                },
                {
                    "id": "b2-brasilsudeste-01.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["brasil-conectores-contraste"],
                    "pairs": [
                        ["mientras que", "confrontación de facetas simultáneas"],
                        ["en contrapartida", "equilibrio de platos de una balanza"],
                        ["por el contrario", "contraposición tajante tras negación"],
                        ["en tanto que", "matiz contrastivo-temporal culto"]
                    ]
                },
                {
                    "id": "b2-brasilsudeste-01.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["brasil-conectores-contraste"],
                    "sentence": "No disminuyó la congestión vehicular; por el __, se expandió hacia las vías de circunvalación.",
                    "answer": "contrario",
                    "english": "Vehicular congestion did not decrease; on the contrary, it expanded toward the ring roads."
                },
                {
                    "id": "b2-brasilsudeste-01.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-brasilsudeste-vocab"],
                    "question": "¿Qué sustantivo designa el conjunto urbano formado por el crecimiento y unión de varios municipios vecinos?",
                    "options": [
                        "La conurbación",
                        "El minifundio",
                        "La rada",
                        "El archipiélago"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-brasilsudeste-01.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué cultivo agrícola financió el despliegue ferroviario y la industrialización inicial de São Paulo?",
                    "options": [
                        "El café",
                        "El caucho",
                        "La yerba mate",
                        "El algodón"
                    ],
                    "correct": 0
                }
            ],
            "b2-brasilsudeste-02": [
                {
                    "id": "b2-brasilsudeste-02.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["brasil-oraciones-relativas-especificativas"],
                    "question": "En 'Los morros que rodean la bahía crean un anfiteatro natural', ¿qué tipo de relativa es?",
                    "options": [
                        "Relativa explicativa separada por comas.",
                        "Relativa especificativa que delimita el conjunto de morros sin comas.",
                        "Subordinada adverbial de tiempo.",
                        "Oración principal transitiva."
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-brasilsudeste-02.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["brasil-oraciones-relativas-especificativas"],
                    "sentence": "La bahía de Guanabara, __ aguas albergan islas históricas, cautivó a los exploradores portugueses.",
                    "answer": "cuyas",
                    "english": "Guanabara Bay, whose waters harbor historic islands, captivated Portuguese explorers."
                },
                {
                    "id": "b2-brasilsudeste-02.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["brasil-oraciones-relativas-especificativas"],
                    "pairs": [
                        ["relativa especificativa", "los cerros que dominan la playa"],
                        ["relativa explicativa", "el Corcovado, que se eleva hacia el cielo"],
                        ["relativo posesivo", "la ciudad cuyas calzadas son famosas"],
                        ["relativo locativo", "el paseo donde florece la sociabilidad"]
                    ]
                },
                {
                    "id": "b2-brasilsudeste-02.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["brasil-oraciones-relativas-especificativas"],
                    "sentence": "Las comunidades __ trepan por las laderas conservan vivas las tradiciones de la samba de raíz.",
                    "answer": "que",
                    "english": "The communities that climb up the hillsides keep the traditions of root samba alive."
                },
                {
                    "id": "b2-brasilsudeste-02.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-brasilsudeste-vocab"],
                    "question": "¿Cómo se denominan las colinas redondeadas de granito características del paisaje de Río de Janeiro?",
                    "options": [
                        "Morros",
                        "Cuchillas",
                        "Médanos",
                        "Altiplanos"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-brasilsudeste-02.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿En qué año se trasladó la corte monárquica portuguesa de Juan VI a Río de Janeiro?",
                    "options": [
                        "1750",
                        "1808",
                        "1888",
                        "1922"
                    ],
                    "correct": 1
                }
            ],
            "b2-brasilsudeste-03": [
                {
                    "id": "b2-brasilsudeste-03.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["brasil-voz-media-pronominal"],
                    "question": "En la frase 'La estética conservadora se disolvió ante las vanguardias', ¿cuál es el valor de 'se'?",
                    "options": [
                        "Voz media pronominal que denota un cambio de estado espontáneo sin agente externo activo.",
                        "Pronombre reflexivo de acción voluntaria.",
                        "Pronombre recíproco mutuo.",
                        "Signo de pasiva impersonal con objeto directo."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-brasilsudeste-03.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["brasil-voz-media-pronominal"],
                    "sentence": "Los antiguos moldes poéticos se __ durante las audaces conferencias modernistas de 1922.",
                    "answer": "quebraron",
                    "english": "The old poetic molds broke apart during the bold modernist lectures of 1922."
                },
                {
                    "id": "b2-brasilsudeste-03.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["brasil-voz-media-pronominal"],
                    "pairs": [
                        ["se disolvió", "cambio de estado o disgregación interna"],
                        ["se transformó", "mutación de forma o canon estético"],
                        ["se forjó", "proceso de constitución identitaria"],
                        ["se quebró", "fractura de una tradición o molde previo"]
                    ]
                },
                {
                    "id": "b2-brasilsudeste-03.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["brasil-voz-media-pronominal"],
                    "sentence": "El canon artístico se __ profundamente con el impulso de la Semana de Arte Moderno.",
                    "answer": "transformó",
                    "english": "The artistic canon transformed deeply with the impetus of Modern Art Week."
                },
                {
                    "id": "b2-brasilsudeste-03.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-brasilsudeste-vocab"],
                    "question": "¿Qué concepto vanguardista brasileño propuso 'devorar' las influencias foráneas para crear arte propio?",
                    "options": [
                        "La antropofagia cultural",
                        "El neoclasicismo parnasiano",
                        "El indigenismo purista",
                        "El realismo socialista"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-brasilsudeste-03.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Quién pintó la emblemática obra 'Abaporu' que inspiró el Manifiesto Antropófago de 1928?",
                    "options": [
                        "Tarsila do Amaral",
                        "Frida Kahlo",
                        "Anita Malfatti",
                        "Lina Bo Bardi"
                    ],
                    "correct": 0
                }
            ],
            "b2-brasilsudeste-04": [
                {
                    "id": "b2-brasilsudeste-04.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["brasil-adverbios-foco"],
                    "question": "¿Qué función cumple el adverbio de foco 'precisamente' en una tesis crítica?",
                    "options": [
                        "Resaltar e individualizar con exactitud el punto central o factor determinante del análisis.",
                        "Indicar una duda aproximada sobre una fecha histórica.",
                        "Introducir una digresión accesoria sin relevancia.",
                        "Sustituir al verbo copulativo en oraciones pasivas."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-brasilsudeste-04.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["brasil-adverbios-foco"],
                    "sentence": "La bossa nova conquistó __ los escenarios más exigentes del jazz neoyorquino en el Carnegie Hall.",
                    "answer": "incluso",
                    "english": "Bossa nova conquered even the most demanding jazz venues in New York at Carnegie Hall."
                },
                {
                    "id": "b2-brasilsudeste-04.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["brasil-adverbios-foco"],
                    "pairs": [
                        ["precisamente", "focalización exacta en el núcleo argumental"],
                        ["incluso", "inclusión de extremo escalar insospechado"],
                        ["hasta", "operador de límite o caso extremo"],
                        ["siquiera", "foco negativo escalar enfático"]
                    ]
                },
                {
                    "id": "b2-brasilsudeste-04.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["brasil-adverbios-foco"],
                    "sentence": "No necesitó __ elevar la voz para transmitir una emoción sobrecogedora con su canto susurrado.",
                    "answer": "siquiera",
                    "english": "He did not even need to raise his voice to convey overwhelming emotion with his whispered singing."
                },
                {
                    "id": "b2-brasilsudeste-04.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-brasilsudeste-vocab"],
                    "question": "¿Qué término musical designa la alteración del ritmo regular prolongando una nota de tiempo débil a fuerte?",
                    "options": [
                        "La síncopa",
                        "El arpegio",
                        "El canon",
                        "El crescendo"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-brasilsudeste-04.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué cantautor bahiano revolucionó la guitarra y la voz en el histórico disco 'Chega de Saudade' (1958)?",
                    "options": [
                        "João Gilberto",
                        "Chico Buarque",
                        "Milton Nascimento",
                        "Gilberto Gil"
                    ],
                    "correct": 0
                }
            ],
            "b2-brasilsudeste-05": [
                {
                    "id": "b2-brasilsudeste-05.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["brasil-comparativas-proporcionales"],
                    "question": "En 'Cuanto más cooperan ambas naciones, tanto más próspera es la región', ¿cuál es la estructura empleada?",
                    "options": [
                        "Comparativa proporcional de correlación paralela.",
                        "Oración causal subordinada de origen.",
                        "Oración concesiva en modo indicativo.",
                        "Perífrasis aspectual incoativa."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-brasilsudeste-05.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["brasil-comparativas-proporcionales"],
                    "sentence": "A __ que se intensifican los intercambios universitarios, se profundiza la comprensión mutua.",
                    "answer": "medida",
                    "english": "As university exchanges intensify, mutual understanding deepens."
                },
                {
                    "id": "b2-brasilsudeste-05.ex03",
                    "type": "matching",
                    "category": "grammar",
                    "teaches": ["brasil-comparativas-proporcionales"],
                    "pairs": [
                        ["cuanto más... tanto más", "correlación cuantitativa paralela"],
                        ["a medida que", "progresión temporal y gradual coordinada"],
                        ["conforme", "avance acompasado de dos procesos"],
                        ["cuanto mayor... tanto menor", "correlación proporcional inversa"]
                    ]
                },
                {
                    "id": "b2-brasilsudeste-05.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["brasil-comparativas-proporcionales"],
                    "sentence": "__ más dialoguen los gobiernos, tanto más sólida será la integración de América del Sur.",
                    "answer": "Cuanto",
                    "english": "The more governments engage in dialogue, the more solid South American integration will be."
                },
                {
                    "id": "b2-brasilsudeste-05.ex05",
                    "type": "multiple-choice",
                    "category": "vocabulary",
                    "teaches": ["b2-brasilsudeste-vocab"],
                    "question": "¿Qué concepto lingüístico describe la capacidad de hablantes de lenguas diferentes de entenderse sin traducirse?",
                    "options": [
                        "La intercomprensión",
                        "La diglosia asimétrica",
                        "La cacofonía",
                        "El anacoluto"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-brasilsudeste-05.ex06",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué significado tiene en portugués el vocablo 'propina', diferenciándose de su acepción en castellano?",
                    "options": [
                        "Significa exclusivamente un postre tradicional de arroz con leche.",
                        "Alude habitualmente a un soborno o cohecho ilícito, y no a una gratificación de servicio.",
                        "Significa un descuento en los billetes de tren.",
                        "Designa una beca académica de excelencia científica."
                    ],
                    "correct": 1
                }
            ],
            "b2-brasilsudeste-consolidation": [
                {
                    "id": "b2-brasilsudeste-consolidation.ex01",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["brasil-conectores-contraste"],
                    "question": "¿Qué conector contrastivo es el más adecuado para contrapesar dos realidades económicas simétricas?",
                    "options": [
                        "En contrapartida",
                        "Por lo tanto",
                        "En consecuencia",
                        "De este modo"
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-brasilsudeste-consolidation.ex02",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["brasil-oraciones-relativas-especificativas"],
                    "sentence": "La ciudad de Río, __ topografía es accidentada, combina morros y playas en un mismo tejido urbano.",
                    "answer": "cuya",
                    "english": "The city of Rio, whose topography is rugged, combines hills and beaches in the same urban fabric."
                },
                {
                    "id": "b2-brasilsudeste-consolidation.ex03",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["brasil-voz-media-pronominal"],
                    "question": "En 'Las formas tradicionales se disolvieron', ¿qué rasgo sintáctico destaca?",
                    "options": [
                        "El verbo concuerda en plural con el sujeto paciente en una construcción de voz media.",
                        "El verbo es transitivo activo con objeto indirecto.",
                        "Se trata de una perífrasis de gerundio durativo.",
                        "Es una oración interrogativa indirecta."
                    ],
                    "correct": 0
                },
                {
                    "id": "b2-brasilsudeste-consolidation.ex04",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["brasil-adverbios-foco"],
                    "sentence": "Fue __ en los estudios de Río de Janeiro donde João Gilberto grabó su primer disco de bossa nova.",
                    "answer": "precisamente",
                    "english": "It was precisely in the Rio de Janeiro studios where João Gilberto recorded his first bossa nova album."
                },
                {
                    "id": "b2-brasilsudeste-consolidation.ex05",
                    "type": "multiple-choice",
                    "category": "grammar",
                    "teaches": ["brasil-comparativas-proporcionales"],
                    "question": "Si la correlación proporcional se proyecta al futuro, ¿qué modo verbal exige el primer miembro?",
                    "options": [
                        "Modo indicativo de presente",
                        "Modo subjuntivo ('cuanto más cooperen...')",
                        "Participio pasivo regular",
                        "Infinitivo simple invariable"
                    ],
                    "correct": 1
                },
                {
                    "id": "b2-brasilsudeste-consolidation.ex06",
                    "type": "matching",
                    "category": "vocabulary",
                    "teaches": ["b2-brasilsudeste-vocab"],
                    "pairs": [
                        ["morro", "colina granítica costera"],
                        ["antropofagia", "devoración y digestión estética de lo foráneo"],
                        ["síncopa", "quiebre rítmico esencial en la samba"],
                        ["intercomprensión", "entendimiento mutuo entre lenguas hermanas"]
                    ]
                },
                {
                    "id": "b2-brasilsudeste-consolidation.ex07",
                    "type": "fill-blank",
                    "category": "grammar",
                    "teaches": ["brasil-comparativas-proporcionales"],
                    "sentence": "A __ que se consolidan los lazos diplomáticos, crecen los proyectos de infraestructura compartida.",
                    "answer": "medida",
                    "english": "As diplomatic ties consolidate, shared infrastructure projects grow."
                },
                {
                    "id": "b2-brasilsudeste-consolidation.ex08",
                    "type": "multiple-choice",
                    "category": "reading",
                    "question": "¿Qué síntesis fundamental define la identidad cultural del Sureste de Brasil?",
                    "options": [
                        "La complementariedad fecunda entre la fuerza industrial paulista, el lirismo musical carioca y la vanguardia modernista.",
                        "La copia servil y sin cambios de los modelos arquitectónicos de Europa central.",
                        "El aislamiento territorial respecto de todas las repúblicas hispanoamericanas.",
                        "La prohibición de practicar música popular en las playas y avenidas públicas."
                    ],
                    "correct": 0
                }
            ]
        }

        for stem, exs in core_ex.items():
            write_json(f"exercises/b2/{stem}-ex.json", {"lesson": stem, "exercises": exs})

        for stem, exs in reg_ex.items():
            write_json(f"exercises/b2/{stem}-ex.json", {"lesson": stem, "exercises": exs})

    make_exercises()

    # 7. Lessons
    core_lessons = {
        "b2-29-01": {
            "id": "lesson.b2.29.01",
            "title": "Explanatory Reformulation: es decir, o sea, esto es, a saber",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/classics/b2/b2-29.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-29-01-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-29-01-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-29-01-ex.json",
                    "exerciseRefs": [f"b2-29-01.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-29-02": {
            "id": "lesson.b2.29.02",
            "title": "Rectifying Reformulation: mejor dicho, más bien, más exactamente",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/classics/b2/b2-29.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-29-02-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-29-02-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-29-02-ex.json",
                    "exerciseRefs": [f"b2-29-02.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-29-03": {
            "id": "lesson.b2.29.03",
            "title": "Distancing Reformulation: de todos modos, en cualquier caso",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/classics/b2/b2-29.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-29-03-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-29-03-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-29-03-ex.json",
                    "exerciseRefs": [f"b2-29-03.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-29-04": {
            "id": "lesson.b2.29.04",
            "title": "Recapitulative Paraphrase: dicho en otros términos, en otras palabras",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/classics/b2/b2-29.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-29-04-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-29-04-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-29-04-ex.json",
                    "exerciseRefs": [f"b2-29-04.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-29-05": {
            "id": "lesson.b2.29.05",
            "title": "Exemplifying Reformulation: a modo de ilustración, verbigracia",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/classics/b2/b2-29.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-29-05-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-29-05-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-29-05-ex.json",
                    "exerciseRefs": [f"b2-29-05.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-29-consolidation": {
            "id": "lesson.b2.29.consolidation",
            "title": "Consolidation: Discourse Markers II: Reformulation & Precision",
            "level": "B2",
            "sections": [
                {
                    "type": "goal",
                    "items": [
                        "Manejar con rigor los marcadores de reformulación explicativa, rectificativa y de distanciamiento.",
                        "Articular paráfrasis sintéticas y ejemplificaciones formales en el ensayo académico de nivel B2.",
                        "Integrar el léxico especializado de la precisión semántica y la crítica literaria."
                    ]
                },
                {"type": "recycle", "count": 3},
                {
                    "type": "exercise-group",
                    "title": "Review",
                    "ref": "exercises/b2/b2-29-consolidation-ex.json",
                    "exerciseRefs": [f"b2-29-consolidation.ex0{i}" for i in range(1, 9)]
                },
                {
                    "type": "checklist",
                    "items": [
                        "Aplico 'es decir', 'o sea' y 'a saber' para clarificar y enumerar con precisión.",
                        "Corrijo y matizo asertos mediante 'mejor dicho', 'más bien' y 'más exactamente'.",
                        "Expreso reservas y distanciamiento crítico aplicando 'en cualquier caso' y 'de todos modos'.",
                        "Formulo síntesis recapitulativas elegantes con 'dicho en otros términos' y 'dicho de otro modo'.",
                        "Introduzco casos demostrativos con 'a modo de ilustración', 'por poner un caso' y 'verbigracia'."
                    ]
                }
            ]
        }
    }

    for stem, ldata in core_lessons.items():
        write_json(f"lessons/b2/{stem}.json", ldata)

    reg_lessons = {
        "b2-brasilsudeste-01": {
            "id": "lesson.b2.brasilsudeste.01",
            "title": "São Paulo: De la riqueza cafetalera a la metrópolis global",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/world/b2/b2-brasilsudeste-01.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-brasilsudeste-01-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-brasilsudeste-01-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-brasilsudeste-01-ex.json",
                    "exerciseRefs": [f"b2-brasilsudeste-01.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-brasilsudeste-02": {
            "id": "lesson.b2.brasilsudeste.02",
            "title": "Río de Janeiro: Entre el morro, la bahía de Guanabara y el mar",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/world/b2/b2-brasilsudeste-02.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-brasilsudeste-02-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-brasilsudeste-02-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-brasilsudeste-02-ex.json",
                    "exerciseRefs": [f"b2-brasilsudeste-02.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-brasilsudeste-03": {
            "id": "lesson.b2.brasilsudeste.03",
            "title": "La Semana de Arte Moderno de 1922 y el Manifiesto Antropófago",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/world/b2/b2-brasilsudeste-03.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-brasilsudeste-03-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-brasilsudeste-03-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-brasilsudeste-03-ex.json",
                    "exerciseRefs": [f"b2-brasilsudeste-03.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-brasilsudeste-04": {
            "id": "lesson.b2.brasilsudeste.04",
            "title": "La samba, la bossa nova y la música popular brasileña",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/world/b2/b2-brasilsudeste-04.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-brasilsudeste-04-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-brasilsudeste-04-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-brasilsudeste-04-ex.json",
                    "exerciseRefs": [f"b2-brasilsudeste-04.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-brasilsudeste-05": {
            "id": "lesson.b2.brasilsudeste.05",
            "title": "Puentes luso-hispanos: El portuñol y los falsos amigos",
            "level": "B2",
            "sections": [
                {"type": "story", "ref": "stories/world/b2/b2-brasilsudeste-05.json"},
                {"type": "grammar", "ref": "grammar/b2/b2-brasilsudeste-05-a-gr.json"},
                {"type": "vocabulary", "ref": "vocabulary/b2/b2-brasilsudeste-05-voc.json"},
                {
                    "type": "exercise-group",
                    "title": "Practice",
                    "ref": "exercises/b2/b2-brasilsudeste-05-ex.json",
                    "exerciseRefs": [f"b2-brasilsudeste-05.ex0{i}" for i in range(1, 7)]
                }
            ]
        },
        "b2-brasilsudeste-consolidation": {
            "id": "lesson.b2.brasilsudeste.consolidation",
            "title": "Consolidación: Brasil I: Motores culturales de São Paulo y Río",
            "level": "B2",
            "sections": [
                {
                    "type": "goal",
                    "items": [
                        "Comprender la articulación sociocultural y económica de las grandes metrópolis del Sureste brasileño.",
                        "Manejar conectores contrastivos, relativas complejas y comparativas proporcionales en el análisis regional.",
                        "Reconocer y superar las trampas semánticas de los falsos amigos entre el español y el portugués."
                    ]
                },
                {"type": "recycle", "count": 3},
                {
                    "type": "exercise-group",
                    "title": "Review",
                    "ref": "exercises/b2/b2-brasilsudeste-consolidation-ex.json",
                    "exerciseRefs": [f"b2-brasilsudeste-consolidation.ex0{i}" for i in range(1, 9)]
                },
                {
                    "type": "checklist",
                    "items": [
                        "Aplico conectores contrastivos como 'mientras que' y 'en contrapartida' en descripciones urbanas.",
                        "Distingo oraciones relativas especificativas y explicativas en prosa paisajística.",
                        "Interpreto la voz media pronominal en textos de crítica e historia del arte modernista.",
                        "Utilizo adverbios de foco ('precisamente', 'incluso', 'siquiera') para realzar argumentos culturales.",
                        "Construyo oraciones comparativas proporcionales con 'cuanto más... tanto más' y 'a medida que'."
                    ]
                }
            ]
        }
    }

    for stem, ldata in reg_lessons.items():
        write_json(f"lessons/b2/{stem}.json", ldata)

    # 8. Update curriculum/units/b2.json
    def update_curriculum(units_list):
        existing_stems = set()
        for u in units_list:
            existing_stems.update(u.get("stems", []))
        
        core_stems = [f"b2-29-0{i}" for i in range(1, 6)] + ["b2-29-consolidation"]
        reg_stems = [f"b2-brasilsudeste-0{i}" for i in range(1, 6)] + ["b2-brasilsudeste-consolidation"]

        if "b2-29-01" not in existing_stems:
            units_list.append({
                "title": "Discourse Markers II: Reformulation & Precision",
                "stems": core_stems,
                "track": "core"
            })
        if "b2-brasilsudeste-01" not in existing_stems:
            units_list.append({
                "title": "Brazil I: The Cultural Engines: Rio, São Paulo & Modernism",
                "stems": reg_stems,
                "track": "regional"
            })
        return units_list

    update_json_file(os.path.join(LATAM_DIR, "curriculum", "units", "b2.json"), update_curriculum)
    print("Updated curriculum/units/b2.json with Unit 29!")

if __name__ == "__main__":
    main()
