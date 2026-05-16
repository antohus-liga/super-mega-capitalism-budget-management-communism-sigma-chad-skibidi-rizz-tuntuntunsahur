from PySide6.QtWidgets import QGridLayout, QWidget


class TransportTab(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.total_transport: float = 0.0

        layout: QGridLayout = QGridLayout()

        self.setLayout(layout)

    def get_total(self) -> float:
        return self.total_transport