from PySide6.QtWidgets import QComboBox, QWidget # QWidget import is needed /
# otherwise pyright throws a warning about not knowing about parent parameter /
# type

class StandardFrequencyComboBox(QComboBox):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.addItems([
            "Mensal",
            "Trimestral",
            "Semestral",
            "Anual"
        ])

        self.setCurrentIndex(0)
        self.setMaximumWidth(100)

    def value(self) -> str:
        return self.currentText()