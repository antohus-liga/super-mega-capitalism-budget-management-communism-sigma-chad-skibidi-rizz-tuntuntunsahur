from PySide6.QtWidgets import QGridLayout, QMainWindow, QPushButton, QWidget

from ui.helpers.ui_rules import standard_button_rules


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Orçamento Familiar")
        self.resize(800,600)

        self.quit_button: QPushButton = QPushButton("Sair")
        standard_button_rules(button = self.quit_button)

        layout: QGridLayout = QGridLayout()
        layout.addWidget(self.quit_button)

        container: QWidget = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)