New-Item -ItemType Directory -Force -Path builds/windows | Out-Null

uv run python -m nuitka `
    --standalone `
    --onefile `
    --output-filename=familybudget `
    --enable-plugin=pyside6 `
    --include-data-dir=src/locales=locales `
    --include-data-dir=src/ui/shared=ui/shared `
    --include-data-file=src/ui/shared/icon.svg=ui/shared/icon.svg `
    --include-data-file=src/ui/shared/icon.ico=ui/shared/icon.ico `
    --include-data-file=src/ui/shared/icon.icns=ui/shared/icon.icns `
    --windows-icon-from-ico=src/ui/shared/icon.ico `
    --output-dir=builds/windows `
    src/main.py

Remove-Item -Recurse -Force builds/windows/main.build -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force builds/windows/main.dist -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force builds/windows/main.onefile-build -ErrorAction SilentlyContinue

Write-Host "Windows build complete → builds/windows/familybudget.exe"