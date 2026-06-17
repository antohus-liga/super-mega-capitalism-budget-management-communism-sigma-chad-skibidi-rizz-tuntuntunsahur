#!/usr/bin/env bash

set -e

PROJECT_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
ENTRYPOINT="$PROJECT_ROOT/main.py"
DIST_DIR="$PROJECT_ROOT/builds/macos/dist"
BUILD_DIR="$PROJECT_ROOT/builds/macos/build"
SPEC_FILE="$PROJECT_ROOT/builds/macos/app.spec"

APP_NAME="OrçamentoFamiliar"

echo "Cleaning previous builds..."

rm -rf "$DIST_DIR" "$BUILD_DIR" "$SPEC_FILE"

rm -rf "$PROJECT_ROOT/build" \
    "$PROJECT_ROOT/dist" \
    "$PROJECT_ROOT/$APP_NAME.spec"

echo "Building executable..."

pyinstaller \
    --onefile \
    --noconfirm \
    --clean \
    --name="$APP_NAME" \
    --distpath="$DIST_DIR" \
    --workpath="$BUILD_DIR" \
    --specpath="$BUILD_DIR" \
    --add-data "$PROJECT_ROOT/app/locales:app/locales" \
    --add-data "$PROJECT_ROOT/app/resources/themes:app/resources/themes" \
    --add-data "$PROJECT_ROOT/app/resources/icons:app/resources/icons" \
    "$ENTRYPOINT"

echo "Build complete!"
echo "Executable is located at:"
echo "$DIST_DIR"