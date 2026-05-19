from pathlib import Path
from platformdirs import PlatformDirs


dirs: PlatformDirs = PlatformDirs("FamilyBudget")

BASE_DIR: Path = Path(__file__).resolve().parent.parent
DOCUMENTS_DIR: Path = Path(dirs.user_documents_dir)
ICONS_THEME_DIR: Path = BASE_DIR / "ui" / "shared"
TRANSLATIONS_DIR: Path = BASE_DIR / "locales"
SPREADSHEETS_DIR: Path = DOCUMENTS_DIR / "FamilyBudget" / "spreadsheets"

SPREADSHEETS_DIR.mkdir(parents = True, exist_ok = True)

DARK_THEME_PATH: Path = ICONS_THEME_DIR / "dark.qss"
LIGHT_THEME_PATH: Path = ICONS_THEME_DIR / "light.qss"