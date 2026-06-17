import shutil
import subprocess

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENTRYPOINT = PROJECT_ROOT / "main.py"
DIST_DIR = PROJECT_ROOT / "builds" / "windows" / "dist"
BUILD_DIR = PROJECT_ROOT / "builds" / "windows" / "build"
SPEC_FILE = PROJECT_ROOT / "builds" / "windows" / "app.spec"

APP_NAME = "OrçamentoFamiliar"

def clean_previous_builds():
    for path in [DIST_DIR, BUILD_DIR, SPEC_FILE]:
        if path.exists():
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()

    global_build = PROJECT_ROOT / "build"
    global_dist = PROJECT_ROOT / "dist"
    global_spec = PROJECT_ROOT / f"{APP_NAME}.spec"

    for path in [global_build, global_dist, global_spec]:
        if path.exists():
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()

def run_pyinstaller():
    cmd = [
        "pyinstaller",
        "--onefile",
        "--noconfirm",
        "--clean",
        f"--name={APP_NAME}",
        f"--distpath={DIST_DIR}",
        f"--workpath={BUILD_DIR}",
        f"--specpath={BUILD_DIR}",
        f"--add-data={PROJECT_ROOT}/app/locales;app/locales",
        f"--add-data={PROJECT_ROOT}/app/resources/themes;app/resources/themes",
        f"--add-data={PROJECT_ROOT}/app/resources/icons;app/resources/icons",
        str(ENTRYPOINT)
    ]

    print("Running PyInstaller...")
    subprocess.run(cmd, check=True)

def main():
    print("Cleaning previous builds...")
    clean_previous_builds()

    print("Building executable...")
    run_pyinstaller()

    print(f"Build complete! Executable is located in:\n{DIST_DIR}")

if __name__ == "__main__":
    main()