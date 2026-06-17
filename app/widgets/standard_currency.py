from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QWidget


class StandardCurrencyLabel(QLabel):
    def __init__(self, currency_symbol: str, parent:
        QWidget | None = None) -> None:
        super().__init__(currency_symbol, parent)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setMaximumWidth(30)