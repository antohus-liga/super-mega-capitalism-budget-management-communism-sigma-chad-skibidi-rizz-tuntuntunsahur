from PySide6.QtWidgets import QPushButton, QSizePolicy, QWidget


class StandardButton(QPushButton):
    def __init__(self, text: str = "", parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
    
        self.setMaximumWidth(180)
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)