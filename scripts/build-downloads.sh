#!/usr/bin/env bash
set -euo pipefail

# Build PDF and EPUB locally, then push them to gh-pages.
# Mermaid diagrams require local Chrome/Chromium — too slow for CI.
#
# Usage: ./scripts/build-downloads.sh

cd "$(git rev-parse --show-toplevel)"

PDF="_book/The-Agentic-SDLC-Handbook.pdf"
EPUB="_book/The-Agentic-SDLC-Handbook.epub"

echo "Rendering PDF..."
quarto render --to pdf

# Save PDF before EPUB render clears _book/
cp "$PDF" /tmp/handbook-build.pdf

echo "Rendering EPUB..."
quarto render --to epub

# Restore PDF alongside EPUB
cp /tmp/handbook-build.pdf "$PDF"
rm -f /tmp/handbook-build.pdf

if [[ -f "$PDF" && -f "$EPUB" ]]; then
    echo ""
    echo "Build complete:"
    echo "  PDF:  $PDF ($(du -h "$PDF" | cut -f1))"
    echo "  EPUB: $EPUB ($(du -h "$EPUB" | cut -f1))"
    echo ""
    echo "To update downloads on the live site, push these to gh-pages:"
    echo "  git stash && git checkout gh-pages"
    echo "  cp _book/*.pdf _book/*.epub ."
    echo "  git add *.pdf *.epub && git commit -m 'chore: update PDF/EPUB' && git push"
    echo "  git checkout main && git stash pop"
else
    echo "ERROR: Build failed — missing output files" >&2
    exit 1
fi
