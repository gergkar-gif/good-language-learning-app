# Parlour

*A place for language.*

Learn with lessons. Read stories. Practise with purpose. Remember what matters.

A modular, content-driven language curriculum (CEFR A1–C1). The Spanish and Hungarian courses are both live through B1, DELE-aligned for Spanish; B2/C1 content is not yet built for either.

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
and `styles/` holds the CSS — see `content/es/schemas/README.md` for the
content schemas and `docs/CURRICULUM_ROADMAP.md` for how a lesson becomes
part of the Learn tab.

## Development

One task → one test → one commit. Never large rewrites. Always keep the app working.

Install the Python validation dependency once per checkout, then validate the
content corpus before committing:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe scripts\validate-content.py es
```
