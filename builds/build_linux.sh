#!/usr/bin/env bash
set -e

mkdir -p builds/linux

uv run python -m nuitka \
    --standalone \
    --onefile \
    --output-filename=familybudget \
    --enable-plugin=pyside6 \
    --include-data-dir=src/locales=locales \
    --include-data-dir=src/ui/shared=ui/shared \
    --include-data-file=src/ui/shared/icon.svg=ui/shared/icon.svg \
    --include-data-file=src/ui/shared/icon.ico=ui/shared/icon.ico \
    --include-data-file=src/ui/shared/icon.icns=ui/shared/icon.icns \
    --output-dir=builds/linux \
    src/main.py

rm -rf builds/linux/main.build
rm -rf builds/linux/main.dist
rm -rf builds/linux/main.onefile-build

echo "Linux build complete → builds/linux/familybudget"