from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QWidget # QWidget import is needed /
# otherwise pyright throws a warning about not knowing about parent parameter /
# type


class StandardLabel(QLabel):
    def __init__(self, text: str = "", max_width: int = 300, parent:
        QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.setMaximumWidth(max_width)
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)