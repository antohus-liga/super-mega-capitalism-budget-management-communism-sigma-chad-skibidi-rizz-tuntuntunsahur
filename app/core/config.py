import sys
from pathlib import Path
from platformdirs import PlatformDirs


def get_base_dir() -> Path:
    meipass = getattr(sys, "_MEIPASS", None)
    if meipass:
        return Path(meipass)
    return Path(__file__).resolve().parents[2]

dirs: PlatformDirs = PlatformDirs("FamilyBudget")

BASE_DIR: Path = get_base_dir()

DOCUMENTS_DIR: Path = Path(dirs.user_documents_dir)

ICONS_THEME_DIR: Path = BASE_DIR / "app" / "resources" / "themes"
TRANSLATIONS_DIR: Path = BASE_DIR / "app" / "locales"

SPREADSHEETS_DIR: Path = DOCUMENTS_DIR / "FamilyBudget" / "spreadsheets"
SPREADSHEETS_DIR.mkdir(parents = True, exist_ok = True)

DARK_THEME_PATH: Path = ICONS_THEME_DIR / "dark.qss"
LIGHT_THEME_PATH: Path = ICONS_THEME_DIR / "light.qss"

FREQUENCY_MULTIPLIERS: dict[str, int] = {
    "Monthly": 12,
    "Quarterly": 4,
    "Biannual": 2,
    "Annual": 1,
}