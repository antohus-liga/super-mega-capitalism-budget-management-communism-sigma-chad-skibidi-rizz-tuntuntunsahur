from PySide6.QtGui import QGuiApplication, Qt


def is_dark_mode() -> bool:
    scheme = QGuiApplication.styleHints().colorScheme()
    return scheme == Qt.ColorScheme.Dark