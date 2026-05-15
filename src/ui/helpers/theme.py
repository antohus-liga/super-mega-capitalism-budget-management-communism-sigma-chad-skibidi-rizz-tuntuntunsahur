from PySide6.QtGui import QColor, QGuiApplication, QPalette


def is_dark_mode() -> bool:
    palette: QPalette = QGuiApplication.palette()
    window_color: QColor= palette.window().color()
    return window_color.lightness() < 128 