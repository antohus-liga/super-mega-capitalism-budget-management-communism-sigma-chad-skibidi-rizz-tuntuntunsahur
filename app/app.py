import os
os.environ["QT_LOGGING_RULES"] = "*.warning=false"

import sys
from pathlib import Path
from typing import Never

from PySide6.QtCore import QLocale
from PySide6.QtWidgets import QApplication

from app.core.config import DARK_THEME_PATH, ICONS_THEME_DIR, LIGHT_THEME_PATH
from app.core.theme import is_dark_mode
from app.services.currency import CurrencyService
from app.services.translation import TranslationService
from app.widgets.main_window import MainWindow
from app.views.app import AppViewModel


class App:
    def __init__(self) -> None:
        self.app: QApplication = QApplication(sys.argv)

        self.translation: TranslationService
        self.icon_path: Path
        self.viewmodel: AppViewModel
        self.window: MainWindow

    def setup_locale(self) -> None:
        system_lang = QLocale.system().name()
        self.translation = TranslationService(lang=system_lang)
        QLocale.setDefault(QLocale.system())

    def apply_theme(self) -> None:
        qss_file = DARK_THEME_PATH if is_dark_mode() else LIGHT_THEME_PATH
        with open(qss_file, "r") as f:
            self.app.setStyleSheet(f.read())

    def resolve_icon(self) -> None:
        if sys.platform.startswith("win"):
            self.icon_path = ICONS_THEME_DIR / "icon.ico"
        elif sys.platform == "darwin":
            self.icon_path = ICONS_THEME_DIR / "icon.icns"
        else:
            self.icon_path = ICONS_THEME_DIR / "icon.svg"

    def setup_services(self) -> None:
        currency_service = CurrencyService()
        self.viewmodel = AppViewModel(currency_service=currency_service)

    def create_main_window(self) -> None:
        self.window = MainWindow(
            app_viewmodel=self.viewmodel,
            translation=self.translation,
            icon_path=self.icon_path
        )

    def run(self) -> Never:
        self.setup_locale()
        self.apply_theme()
        self.resolve_icon()
        self.setup_services()
        self.create_main_window()

        self.window.show()
        sys.exit(self.app.exec())