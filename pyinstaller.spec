# -*- mode: python ; coding: utf-8 -*-

import os
from PyInstaller.utils.hooks import collect_submodules

project_root = os.getcwd()

datas = [
    (os.path.join(project_root, "src", "locales"), "locales"),
    (os.path.join(project_root, "src", "ui", "shared"), "ui/shared"),
]

hiddenimports = collect_submodules("PySide6")

icon_file = os.path.join(project_root, "src", "ui", "shared", "icon.ico")

a = Analysis(
    ["src/main.py"],
    pathex=[project_root],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name="familybudget",
    icon=icon_file,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    name="familybudget",
    destdir=os.path.join(project_root, "builds", "windows"),
)