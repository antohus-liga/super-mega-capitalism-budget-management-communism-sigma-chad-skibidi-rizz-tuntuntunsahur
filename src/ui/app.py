import os
os.environ["QT_LOGGING_RULES"] = "qt.qpa.wayland.warning=false" # this is /
# needed here to hide a warning that Qt throws about Wayland while holding /
# the backspace when entering values

import sys

from pathlib import Path
from typing import Never

from PySide6.QtCore import QLocale # this is needed here for correct number /
# formatting

from PySide6.QtWidgets import QApplication

from core.config import DARK_THEME, LIGHT_THEME
from services.currency_service import CurrencyService
from ui.shared.theme import is_dark_mode
from ui.widgets.main_window import MainWindow
from viewmodels.app_viewmodel import AppViewModel


def run_app() -> Never:
    app: QApplication = QApplication(sys.argv)

    QLocale.setDefault(QLocale.system())

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