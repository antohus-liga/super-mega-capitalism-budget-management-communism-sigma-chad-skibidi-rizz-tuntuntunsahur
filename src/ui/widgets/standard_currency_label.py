from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QWidget


class StandardCurrencyLabel(QLabel):
    def __init__(self, parent:
        QWidget |None = None) -> None:
        super().__init__("€", parent)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft |
        Qt.AlignmentFlag.AlignVCenter)
        self.setMaximumWidth(20)