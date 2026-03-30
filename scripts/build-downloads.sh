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
    # Always keep a stable copy in dist/ (survives _book/ wipes from format re-renders)
    mkdir -p dist
    cp "$PDF"  dist/
    cp "$EPUB" dist/
    echo ""
    echo "Build complete:"
    echo "  PDF:  $PDF ($(du -h "$PDF" | cut -f1))"
    echo "  EPUB: $EPUB ($(du -h "$EPUB" | cut -f1))"
    echo "  Copies in dist/"
    echo ""
    echo "To publish to the live site and tag the release:"
    echo "  ./scripts/publish.sh            # push to gh-pages + create version tag"
    echo "  ./scripts/publish.sh --dry-run  # preview without changing anything"
else
    echo "ERROR: Build failed — missing output files" >&2
    exit 1
fi
