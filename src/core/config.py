from pathlib import Path


BASE_DIR: Path = Path(__file__).resolve().parent.parent
THEME_DIR: Path = BASE_DIR / "ui" / "shared"

LIGHT_THEME: Path = THEME_DIR / "light.qss"
DARK_THEME: Path = THEME_DIR / "dark.qss"

FREQUENCY_MULTIPLIERS: dict[str, int] = {
    "Mensal": 12,
    "Trimestral": 4,
    "Semestral": 2,
    "Anual": 1,
}