import sys

from pathlib import Path
from PySide6.QtWidgets import QApplication
from typing import Never

from core.config import DARK_THEME, LIGHT_THEME
from ui.controllers.main_controller import MainController
from ui.helpers.theme import is_dark_mode
from ui.widgets.main_window import MainWindow


def run_app() -> Never:
    app: QApplication = QApplication(sys.argv)

    qss_file: Path = DARK_THEME if is_dark_mode() else LIGHT_THEME

    with open(file = qss_file, mode = "r") as f:
        app.setStyleSheet(f.read()) # loading the correct style based on the /
        # theme that the user is using here seems an acceptable idea

    window: MainWindow = MainWindow()
    _controller: MainController = MainController(window) # _ is needed here /
    # otherwise pyright throws a warning about variable not being accessed
    window.show()

    sys.exit(app.exec())