# Parlour — Credits & Attributions

Parlour is a language-learning application for Spanish and Hungarian.  
This file records the third-party data sources used in the application, along with their licences and required attributions.

---

## AI-Assisted Content

Parlour's curriculum, lessons, grammar explanations, exercises, vocabulary lists, and stories were **co-produced with AI assistance** (OpenAI ChatGPT and Anthropic Claude). The project owner directed all design decisions, reviewed all content for pedagogical accuracy, and edited where necessary. AI was used as a production tool, not a replacement for human judgement.

All content in `content/es/` and `content/hu/` is original to Parlour unless noted in the **Classic Stories** section below.

---

## Data Sources

### 1. Spanish Verb Conjugation Data
- **Source**: [miko3k/verbos](https://github.com/miko3k/verbos) on GitHub  
- **Original author**: Fred Jehle, Indiana University–Purdue University Fort Wayne  
- **Used for**: All Spanish verb conjugation tables across 657 verbs  
- **Licence**: [Creative Commons Attribution–NonCommercial–ShareAlike 3.0 Unported (CC BY-NC-SA 3.0)](https://creativecommons.org/licenses/by-nc-sa/3.0/)  
- **Files in this repo**: `imports/verbs/`

> ⚠️ **Non-commercial restriction**: This data is licensed for non-commercial use only. If Parlour ever operates commercially, this dataset must be replaced with a commercially-licensed alternative.

---

### 2. Spanish–English Dictionary & Inflection Index
- **Source**: [doozan/spanish_data](https://github.com/doozan/spanish_data) on GitHub  
- **Derived from**: Spanish Wiktionary (via Wiktionary extractors)  
- **Used for**: Spanish word lookup, word inflection (allforms), and lemma frequency ranking  
- **Licence**: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)  
- **Files in this repo**: `imports/dictionary/es-en.data.raw`, `es_allforms.csv.raw`, `frequency.csv.raw`; processed outputs in `generated/indexes/`

---

### 3. Hungarian–English Dictionary
- **Source**: [kaikki.org](https://kaikki.org/dictionary/Hungarian/) — machine-readable Wiktionary extracts by Tatu Ylonen  
- **Derived from**: English Wiktionary, Hungarian entries  
- **Used for**: Hungarian word lookup and the word index  
- **Licence**: [Creative Commons Attribution–ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/) and [GNU Free Documentation Licence (GFDL)](https://www.gnu.org/licenses/fdl-1.3.html)  
- **Files in this repo**: `imports/dictionary/hu-wiktionary.jsonl.raw`; processed output in `content/hu/indexes/word-index.json`

> ⚠️ **Share-alike requirement**: Any derivative database must also be published under CC BY-SA 4.0 or a compatible licence.

---

### 4. Hungarian Word Frequency Database
- **Source**: [petyaracz/hungarian-word-frequencies](https://huggingface.co/datasets/petyaracz/hungarian-word-frequencies) on Hugging Face  
- **Author**: Péter Rácz, 2025 — derived from Hungarian Webcorpus 2  
- **Used for**: Hungarian lemma frequency ranking  
- **Licence**: ⚠️ **To be verified** — the licence for this dataset has not yet been confirmed. Until resolved, this data is used in good faith for non-commercial, educational purposes.  
- **Files in this repo**: `imports/dictionary/hu-frequencies.db.raw`; processed output in `content/hu/indexes/frequency.json`

---

## Classic Stories

The following classic literary works are adapted in the Parlour Library as simplified Spanish reading texts for language learners. All original works listed here are in the **public domain**. The simplified adaptations are original to Parlour and were written (with AI assistance) for educational use.

| Author | Work | Notes |
|---|---|---|
| Miguel de Cervantes | *Don Quijote de la Mancha* | Simplified adaptation for language learners. Original work is in the public domain. |
| The Brothers Grimm | *Fairy tales* | Simplified Spanish adaptation. Original works are in the public domain. |
| Gustavo Adolfo Bécquer | *Cartas desde mi celda* | Simplified adaptation. Public domain. |
| José Martí | *Crónicas* | Simplified adaptation. Public domain. |
| Horacio Quiroga | *Cuentos de la selva* | Simplified adaptation. Public domain. |
| Ricardo Palma | *Tradiciones peruanas* | Simplified adaptation. Public domain. |
| Benito Pérez Galdós | *Marianela*, *Trafalgar* | Simplified adaptation. Public domain. |
| Juan Valera | *Pepita Jiménez* | Simplified adaptation. Public domain. |
| Domingo Faustino Sarmiento | *Facundo* | Simplified adaptation. Public domain. |
| Rubén Darío | *El pájaro azul* | Simplified adaptation. Public domain. |
| Leopoldo Alas "Clarín" | *Paliques* | Simplified adaptation. Public domain. |
| Herman Melville | *Bartleby, the Scrivener* | Simplified Spanish adaptation. Public domain. |
| Jules Verne | Selected works | Simplified Spanish adaptation. Public domain. |
| Louisa May Alcott | *Little Women* | Simplified Spanish adaptation. Public domain. |
| Jean-Jacques Rousseau | *Émile* | Simplified Spanish adaptation. Public domain. |
| Franz Kafka | *The Metamorphosis* | Simplified Spanish adaptation. Public domain. |
| Charlotte Perkins Gilman | *The Yellow Wallpaper* | Simplified Spanish adaptation. Public domain. |
| Homer | *The Odyssey* | Simplified Spanish adaptation. Public domain. |
| Aesop | Traditional fables | Simplified Spanish adaptation. Public domain. |
| Simón Bolívar | *Carta de Jamaica* | Simplified historical text. Public domain. |

Stories in the **World** track and **Original** track are fully original texts written for Parlour and do not reproduce any copyrighted work.

---

## Open-Source Tools (Development Only)

The following tools are used during development but are **not shipped** with the application:

| Tool | Purpose | Licence |
|---|---|---|
| [jsonschema](https://github.com/python-jsonschema/jsonschema) | Content schema validation | MIT |

---

## Service Providers

The following third-party services are used operationally. They are service providers, not content sources, and do not require attribution under their terms of service.

| Service | Purpose |
|---|---|
| GitHub Issues API | In-app bug reporting |
| Resend | Magic-link login emails for cloud sync |
| Cloudflare Workers & D1 | Cloud sync backend |
| Cloudflare Workers AI | CEFR formative grading (Writing/Speaking Studio) |
| Google Cloud Text-to-Speech | Reader's spoken narration (Journey/Studio voices) |

---

## Licence Notices

The **application code** (`engine/`, `styles/`, `scripts/`, `cloudflare-worker/`) is © the project owner. All rights reserved unless otherwise noted.

The **curriculum content** (`content/es/`, `content/hu/`) is original to Parlour and © the project owner. All rights reserved.

Third-party data sources retain their own licences as noted above.
