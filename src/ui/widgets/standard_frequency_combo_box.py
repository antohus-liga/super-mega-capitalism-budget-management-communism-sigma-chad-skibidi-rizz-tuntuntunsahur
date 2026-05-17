from typing import cast # this is needed here because pyright throws a warning /
# complaining about self.currentData type is Any so by doing this it know it /
# is really str type

from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QComboBox, QWidget # QWidget import is needed /
# otherwise pyright throws a warning about not knowing about parent parameter /
# type


class StandardFrequencyComboBox(QComboBox):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)


        labels: list[str] = [
            "Mensal",
            "Trimestral",
            "Semestral",
            "Anual"]

        translated_labels: list[str] = [
            QCoreApplication.translate("StandardFrequencyComboBox", text)
            for text in labels]

        self.addItem(translated_labels[0], "Monthly")
        self.addItem(translated_labels[1], "Quarterly")
        self.addItem(translated_labels[2], "Biannual")
        self.addItem(translated_labels[3], "Annual")

        self.setCurrentIndex(0)
        self.setMaximumWidth(100)

    def value(self) -> str:
        return cast(str, self.currentData())