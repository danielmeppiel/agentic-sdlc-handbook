# Copilot Instructions — agentic-sdlc-handbook

## Project overview

This is a Quarto book ("The Agentic SDLC Handbook") published to GitHub Pages at `danielmeppiel.github.io/agentic-sdlc-handbook/`. It covers AI-native software development methodology, the PROSE framework, and APM.

## Build & deploy workflow

### HTML (automated via CI)

Every push to `main` triggers `.github/workflows/publish.yml`:
1. Renders HTML only (`quarto render --to html`)
2. Restores PDF and EPUB from the previous `gh-pages` deploy
3. Publishes everything to `gh-pages` branch

CI does NOT render PDF or EPUB — Mermaid diagrams require local Chromium and are too slow in CI.

### PDF & EPUB (local build, manual push)

```bash
./scripts/build-downloads.sh
```

This renders PDF and EPUB locally using Quarto + TinyTeX + Chromium (for Mermaid→PNG). After building, push the files to `gh-pages`:

```bash
git stash && git checkout gh-pages
cp _book/*.pdf _book/*.epub .
git add *.pdf *.epub && git commit -m 'chore: update PDF/EPUB' && git push
git checkout main && git stash pop
```

### Download URLs (stable, always latest)

- PDF: `https://danielmeppiel.github.io/agentic-sdlc-handbook/The-Agentic-SDLC-Handbook.pdf`
- EPUB: `https://danielmeppiel.github.io/agentic-sdlc-handbook/The-Agentic-SDLC-Handbook.epub`
- Online: `https://danielmeppiel.github.io/agentic-sdlc-handbook/`

## Key files

| File | Purpose |
|------|---------|
| `_quarto.yml` | Book config — chapters, formats, analytics, footer CTA |
| `index.qmd` | Preface — "Why This Book Exists", author bio, download CTA |
| `download.qmd` | Download page with email signup form |
| `scripts/build-downloads.sh` | Local PDF/EPUB build script |
| `.github/workflows/publish.yml` | CI — HTML render + deploy to gh-pages |

## Content conventions

- Chapters are in `handbook/chNN-slug.qmd`
- Use Quarto callouts (`.callout-tip`, `.callout-note`) for CTAs
- CTAs link to `download.qmd` (relative: `../download.qmd` from chapters)
