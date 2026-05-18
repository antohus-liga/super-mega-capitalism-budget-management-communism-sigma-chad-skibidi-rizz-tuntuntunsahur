#!/usr/bin/env bash
set -e

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
    --macos-app-icon=src/ui/shared/icon.icns \
    --output-dir=builds/macos \
    src/main.py