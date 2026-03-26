#!/usr/bin/env bash
set -euo pipefail

# Pre-render script: stamps build metadata into _variables.yml
# Preserves the manual `version` field, adds/updates build-date and build-hash.

cd "$(git rev-parse --show-toplevel)"

VARIABLES_FILE="_variables.yml"

# Read current version
VERSION=$(grep '^version:' "$VARIABLES_FILE" | sed 's/version: *"\(.*\)"/\1/')

# Get last commit date and short hash
BUILD_DATE=$(git log -1 --format=%cd --date=format:'%B %Y')
BUILD_HASH=$(git rev-parse --short HEAD)

# Rewrite _variables.yml with all fields
cat > "$VARIABLES_FILE" <<EOF
version: "${VERSION}"
build-date: "${BUILD_DATE}"
build-hash: "${BUILD_HASH}"
EOF

echo "Stamped: version=${VERSION}, build-date=${BUILD_DATE}, build-hash=${BUILD_HASH}"

python3 scripts/generate_cover_asset.py
