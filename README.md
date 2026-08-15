# Parlour

*A place for language.*

Learn with lessons. Read stories. Practise with purpose. Remember what matters.

A modular, content-driven language curriculum (CEFR A1–C1). The Spanish course is DELE-aligned; Hungarian is planned.

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

See `STRUCTURE.md` for the full directory map and ownership rules.

## Development

One task → one test → one commit. Never large rewrites. Always keep the app working.

Install the Python validation dependency once per checkout, then validate the
content corpus before committing:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe scripts\validate-content.py es
```
