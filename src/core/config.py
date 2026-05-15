from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
THEME_DIR = BASE_DIR / "ui" / "shared"

LIGHT_THEME = THEME_DIR / "light.qss"
DARK_THEME = THEME_DIR / "dark.qss"