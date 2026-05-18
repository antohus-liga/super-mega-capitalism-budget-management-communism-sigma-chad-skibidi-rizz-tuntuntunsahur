from pathlib import Path


BASE_DIR: Path = Path(__file__).resolve().parent.parent
ICONS_THEME_DIR: Path = BASE_DIR / "ui" / "shared"
TRANSLATIONS_DIR: Path = BASE_DIR / "locales"

DARK_THEME_PATH: Path = ICONS_THEME_DIR / "dark.qss"
LIGHT_THEME_PATH: Path = ICONS_THEME_DIR / "light.qss"