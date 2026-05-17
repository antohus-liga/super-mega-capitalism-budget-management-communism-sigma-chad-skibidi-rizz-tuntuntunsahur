import os
os.environ["QT_LOGGING_RULES"] = "qt.qpa.wayland.warning=false" # this is /
# needed here to hide a warning that Qt throws about Wayland while holding /
# the backspace when entering values

import sys

from pathlib import Path
from typing import Never

from PySide6.QtCore import QLocale, QTranslator

from PySide6.QtWidgets import QApplication

from core.config import DARK_THEME, LIGHT_THEME
# from locales import linguistic_rc
from services.currency_service import CurrencyService
from ui.shared.theme import is_dark_mode
from ui.widgets.main_window import MainWindow
from viewmodels.app_viewmodel import AppViewModel


def load_translation(app: QApplication) -> None:
    system_locale: str = QLocale.system().name()
    translator: QTranslator = QTranslator()

    # 1st try -> exact variant
    if translator.load(f":/i18n/app_{system_locale}.qm"):
        _ = app.installTranslator(translator)
        return

    # 2nd try -> available variant
    lang: str = system_locale.split(sep = "_")[0]
    fallback_locale: str | None = {
        "pt": "pt_PT",
        "en": "en_GB"
    }.get(lang)

    if fallback_locale and translator.load(f":/i18n/app_{fallback_locale}.qm"):
        _ = app.installTranslator(translator)
        return

    # 3rd try -> emergency fallback
    _ = translator.load(":/i18n/app_en_GB.qm")
    _ = app.installTranslator(translator)

def run_app() -> Never:
    # linguistic_rc.qInitResources()

    app: QApplication = QApplication(sys.argv)

    load_translation(app)

    QLocale.setDefault(QLocale.system()) # currency related

    qss_file: Path = DARK_THEME if is_dark_mode() else LIGHT_THEME

    with open(file = qss_file, mode = "r") as f:
        app.setStyleSheet(f.read()) # loading the correct style based on the /
        # theme that the user is using here seems an acceptable idea

    currency_service: CurrencyService = CurrencyService()
    app_viewmodel: AppViewModel = AppViewModel(
    currency_service = currency_service)

    window: MainWindow = MainWindow(app_viewmodel = app_viewmodel)
    window.show()

    sys.exit(app.exec())