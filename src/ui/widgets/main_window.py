from PySide6.QtWidgets import QGridLayout, QMainWindow, QWidget

from ui.widgets.standard_button import StandardButton


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Orçamento Familiar")
        self.resize(800,600)

        self.quit_button: StandardButton = StandardButton(text = "Sair")

        layout: QGridLayout = QGridLayout()
        layout.addWidget(self.quit_button)

        container: QWidget = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)