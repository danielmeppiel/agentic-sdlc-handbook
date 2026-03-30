#!/usr/bin/env bash
set -euo pipefail

# Publish PDF/EPUB to gh-pages and tag the release.
#
# Prerequisites:
#   - Run ./scripts/build-downloads.sh first (PDF/EPUB must exist in dist/)
#   - Clean working tree (no uncommitted changes)
#
# Usage:
#   ./scripts/publish.sh            # publish dist/ files to gh-pages + tag
#   ./scripts/publish.sh --dry-run  # show what would happen without changing anything

cd "$(git rev-parse --show-toplevel)"

# ── Flags ────────────────────────────────────────────────────────
DRY_RUN=false
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=true ;;
    *) echo "Unknown flag: $arg"; echo "Usage: $0 [--dry-run]"; exit 1 ;;
  esac
done

# ── Read version ─────────────────────────────────────────────────
VERSION=$(grep '^version:' _variables.yml | sed 's/version: *"\(.*\)"/\1/')
TAG="v${VERSION}"

echo "Publishing v${VERSION}"
echo ""

# ── Validate dist/ ───────────────────────────────────────────────
PDF="dist/The-Agentic-SDLC-Handbook.pdf"
EPUB="dist/The-Agentic-SDLC-Handbook.epub"

if [[ ! -f "$PDF" || ! -f "$EPUB" ]]; then
  echo "ERROR: dist/ is missing PDF or EPUB." >&2
  echo "Run ./scripts/build-downloads.sh first." >&2
  exit 1
fi

PDF_SIZE=$(du -h "$PDF" | cut -f1)
EPUB_SIZE=$(du -h "$EPUB" | cut -f1)
echo "  PDF:  $PDF ($PDF_SIZE)"
echo "  EPUB: $EPUB ($EPUB_SIZE)"
echo ""

# ── Validate clean working tree ─────────────────────────────────
if [[ -n "$(git status --porcelain)" ]]; then
  echo "WARNING: Working tree has uncommitted changes."
  echo "Commit or stash them first to ensure the tag points to a clean state."
  echo ""
  read -r -p "Continue anyway? [y/N] " REPLY
  [[ "$REPLY" =~ ^[Yy]$ ]] || exit 0
fi

# ── Dry-run gate ─────────────────────────────────────────────────
if $DRY_RUN; then
  echo "[dry-run] Would push PDF/EPUB to gh-pages branch"
  if git rev-parse "$TAG" >/dev/null 2>&1; then
    echo "[dry-run] Tag $TAG already exists — would skip tagging"
  else
    echo "[dry-run] Would create annotated tag $TAG"
  fi
  echo ""
  echo "Done (dry run — nothing changed)."
  exit 0
fi

# ── Push PDF/EPUB to gh-pages ────────────────────────────────────
WORKTREE_DIR=$(mktemp -d)
trap 'git worktree remove --force "$WORKTREE_DIR" 2>/dev/null; rm -rf "$WORKTREE_DIR"' EXIT

echo "Updating gh-pages branch..."
git fetch origin gh-pages
git worktree add --quiet "$WORKTREE_DIR" gh-pages

cp "$PDF"  "$WORKTREE_DIR/"
cp "$EPUB" "$WORKTREE_DIR/"

(
  cd "$WORKTREE_DIR"
  git add The-Agentic-SDLC-Handbook.pdf The-Agentic-SDLC-Handbook.epub

  if git diff --cached --quiet; then
    echo "  gh-pages already has identical files — nothing to push."
  else
    git commit --quiet -m "chore: update PDF/EPUB for ${TAG}"
    git push --quiet origin gh-pages
    echo "  Pushed PDF/EPUB to gh-pages."
  fi
)

# ── Tag ──────────────────────────────────────────────────────────
if git rev-parse "$TAG" >/dev/null 2>&1; then
  echo ""
  echo "Tag $TAG already exists — skipping."
else
  git tag -a "$TAG" -m "${TAG} — Pre-release Edition"
  git push origin "$TAG"
  echo ""
  echo "Created and pushed tag $TAG."
fi

# ── Summary ──────────────────────────────────────────────────────
echo ""
echo "✅ Published ${TAG}"
echo "   PDF/EPUB on gh-pages → https://danielmeppiel.github.io/agentic-sdlc-handbook/"
echo "   Tag: $TAG"
