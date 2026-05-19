import os
os.environ["QT_LOGGING_RULES"] = "*.warning=false" # this is needed here to /
# hide a warning that Qt throws about Wayland while holding the backspace when /
# entering values and also for some reason when do escape key while choosing /
# an option from the option box

import sys

from pathlib import Path
from typing import Never

from PySide6.QtCore import QLocale
from PySide6.QtWidgets import QApplication

from core.config import DARK_THEME_PATH, ICONS_THEME_DIR, LIGHT_THEME_PATH
from services.currency_service import CurrencyService
from services.translation_service import TranslationService
from ui.shared.theme import is_dark_mode
from ui.widgets.main_window import MainWindow
from viewmodels.app_viewmodel import AppViewModel

def run_app() -> Never:
    app: QApplication = QApplication(sys.argv)

    system_lang: str = QLocale.system().name()

    translation: TranslationService = TranslationService(lang = system_lang)

    QLocale.setDefault(QLocale.system()) # currency related

    qss_file: Path = DARK_THEME_PATH if is_dark_mode() else LIGHT_THEME_PATH

    with open(file = qss_file, mode = "r") as f:
        app.setStyleSheet(f.read()) # loading the correct style based on the /
        # theme that the user is using here seems an acceptable idea

    if sys.platform.startswith("win"):
        icon_path: Path = ICONS_THEME_DIR / "icon.ico"
    elif sys.platform == "darwin":
        icon_path = ICONS_THEME_DIR / "icon.icns"
    else:
        icon_path = ICONS_THEME_DIR / "icon.svg"

    currency_service: CurrencyService = CurrencyService()
    app_viewmodel: AppViewModel = AppViewModel(
    currency_service = currency_service)

    window: MainWindow = MainWindow(app_viewmodel = app_viewmodel,
    translation = translation, icon_path = icon_path)
    window.show()

    sys.exit(app.exec())