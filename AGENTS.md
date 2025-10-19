# Repository Guidelines

## Project Structure & Module Organization
- Top-level folders like `ai/`, `biology/`, `business/`, `development/`, and `psychology/` host curated note collections; prefer adding new topics inside the nearest domain folder.
- Technical references live under `development/` (e.g., `development/python/`, `development/js/`), while reusable assets sit in `static/` and helper scripts in `tools/`.
- Experiments and integration scaffolds are under `test/` (Docker, Terraform, Swagger), so place runnable samples or sandboxes there.

## Build, Test, and Development Commands
- `pre-commit run --all-files` checks Markdown, JS, and Python changes with the configured hooks.
- `npx markdownlint "**/*.md"` enforces prose formatting before publishing a new note.
- `npx eslint development/js --ext .js` validates JavaScript snippets; adjust the path for other folders.
- `python -m unittest discover -s test` executes the Python samples in `test/`.

## Coding Style & Naming Conventions
- Mirror `CONVENTIONS.md`: match Markdown titles to filenames, add `## Table of Contents`, and keep tone instructional.
- Prefer 4-space indentation for code snippets; Python follows `.flake8` (88 char lines), and JavaScript adheres to `eslint:recommended`.
- Keep filenames lowercase-with-dashes, e.g., `development/python/type-hints.md`; store assets with descriptive snake_case names inside `static/`.

## Testing Guidelines
- Python examples use `unittest`; name files `*_test.py` like `example_test.py` and isolate fixtures in `setUp`.
- When adding CLI or infrastructure samples, mirror the existing folder (e.g., `test/docker-compose/`) and document usage in a `README.md`.
- Capture notable outputs in Markdown tables rather than console dumps.

## Commit & Pull Request Guidelines
- Follow the short, trunk-based history: use present-tense subjects (`note`, `docs: update changelog`) and keep summaries under 50 chars when possible.
- Bundle related note edits per domain and avoid rebases; open PRs straight from `main`.
- PRs should include: purpose summary, affected folders, manual verification steps, and links to related issues or context screenshots.

## Tooling & Automation
- Install `pre-commit` locally (`pip install pre-commit`) and run `pre-commit install` once so hooks guard future commits.
- Security-sensitive notes should reference `SECURITY.md`; for secrets, never commit `.env` files—store guidance under `others/`.
