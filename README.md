# Parlour

*A place for language.*

Learn with lessons. Read stories. Practise with purpose. Remember what matters.

A modular, content-driven language curriculum (CEFR A1–C1). The Spanish (Spain and Latin America) and Hungarian courses are both live through B1, DELE-aligned for Spanish; B2/C1 content is not yet built for either.

## Philosophy

- **Pedagogy first.** Technology serves education, not the reverse.
- **Engine/content separation.** The engine is reusable; Spanish is the first content pack.
- **No frameworks.** HTML, CSS, vanilla JavaScript, JSON.
- **Reuse external resources.** Do not reinvent dictionaries, conjugations, or frequency lists.

## Quick Start

The app loads its content with `fetch`, so serve the project locally rather
than opening `index.html` through `file://`.

```powershell
.\.venv\Scripts\python.exe scripts\dev-server.py
```

Then open `http://localhost:8131`.

## Folder Structure

`engine/` holds the reusable app logic, `content/<lang>/` holds one
language's curriculum (lessons, grammar, exercises, vocabulary, stories),
`styles/` holds the CSS, and `scripts/` the build, check and import tools
(see `scripts/README.md`). `content/<lang>/schemas/README.md` describes the
content schemas; `AGENTS.md` ("Wiring a new unit into the app") explains how a
lesson becomes part of the Learn tab.

## Documentation

| Document | What it is |
|---|---|
| `AGENTS.md` | Rules for anyone writing content or code: validator, exercise metadata, teaching and exercise principles, wiring a unit, adding a course |
| `DESIGN.md`, `PRODUCT.md` | The visual system (with the prototype in `docs/overhaul-prototype/`) and the product brief |
| `ROADMAP.md` | What is open and planned |
| `ACHIEVED.md` | What has shipped, with the archived queue items |
| `docs/SERVICES.md` | Setting up the Cloudflare Workers and third-party services (bug reports, cloud sync, Google Sign-In, grader, speech-to-text) |
| `docs/feature-guidance-copy.md` | The copy for first-week guidance notes |
| `CREDITS.md` | Data sources and licences |
| `docs/archive/`, `scripts/archive/` | History only; nothing there is current guidance |

## Development

One task → one test → one commit. Never large rewrites. Always keep the app working.

Install the Python validation dependency once per checkout, then validate the
content corpus before committing:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe scripts\validate-content.py --changed
```
