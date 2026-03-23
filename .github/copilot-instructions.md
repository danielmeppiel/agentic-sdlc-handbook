# Copilot Instructions — apm-handbook

## Project overview

This is a Quarto book ("The Agentic SDLC Handbook") published to GitHub Pages at `danielmeppiel.github.io/apm-handbook/`. It covers AI-native software development methodology, the PROSE framework, and APM.

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

- PDF: `https://danielmeppiel.github.io/apm-handbook/The-Agentic-SDLC-Handbook.pdf`
- EPUB: `https://danielmeppiel.github.io/apm-handbook/The-Agentic-SDLC-Handbook.epub`
- Online: `https://danielmeppiel.github.io/apm-handbook/`

These URLs are used in the Kit email automation (incentive email) and must not change.

## Growth engine integration

The book site connects to a Kit (ConvertKit) email automation:

1. **Email gate**: `download.qmd` embeds a Kit form (UID: `6bee764071`). Visitors enter email → get PDF/EPUB links instantly via Kit incentive email.
2. **Tagging**: Kit rule auto-tags subscribers with `handbook-downloader` on form submit.
3. **Welcome sequence**: 3 follow-up emails over 8 days (PROSE intro, anti-patterns, APM story). After completion, subscribers get tagged `newsletter-subscriber`.
4. **CTAs**: Footer CTA on every page + inline CTAs in ch01, ch10, ch14 all point to `download.qmd`.
5. **Analytics**: Plausible script in `_quarto.yml` header (requires Plausible account activation).

## Key files

| File | Purpose |
|------|---------|
| `_quarto.yml` | Book config — chapters, formats, Plausible analytics, footer CTA |
| `index.qmd` | Preface — "Why This Book Exists", author bio, subscribe CTA |
| `download.qmd` | Email-gated download page with Kit form embed |
| `scripts/build-downloads.sh` | Local PDF/EPUB build script |
| `.github/workflows/publish.yml` | CI — HTML render + deploy to gh-pages |
| `career/growth-engine-status.md` | Remaining growth engine tasks and Kit setup status |
| `career/growth-implementation-plan.md` | Full implementation plan with email copy, LinkedIn posts, etc. |

## Content conventions

- Chapters are in `handbook/chNN-slug.qmd`
- Use Quarto callouts (`.callout-tip`, `.callout-note`) for CTAs
- CTAs link to `download.qmd` (relative: `../download.qmd` from chapters)
- No toolbar PDF/EPUB downloads — removed intentionally to funnel through email gate
