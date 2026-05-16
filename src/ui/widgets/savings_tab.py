from PySide6.QtWidgets import QGridLayout, QWidget


class SavingsTab(QWidget):
    def __init__(self) -> None:
        super().__init__()

        layout: QGridLayout = QGridLayout()

        self.setLayout(layout)