from typing import override

from PySide6.QtCore import QLocale, Qt
from PySide6.QtGui import QDoubleValidator, QKeyEvent
from PySide6.QtWidgets import QLineEdit, QWidget


class StandardMoneyInputBox(QLineEdit):
    def __init__(self, placeholder: str = "", parent: QWidget | None = None
    ) -> None:
        super().__init__(parent)

        locale: QLocale = QLocale.system()
        self.decimal: str = locale.decimalPoint()

        validator: QDoubleValidator = QDoubleValidator(0.0, 9999999.99, 2)
        validator.setNotation(QDoubleValidator.Notation.StandardNotation)
        self.setValidator(validator)

        if placeholder:
            self.setPlaceholderText(placeholder)

        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setMaximumWidth(100)

    @override 
    def keyPressEvent(self, event: QKeyEvent) -> None:
        key: int = event.key()

        # Rejects the keyboard and the keypad plus key
        if key == Qt.Key.Key_Plus:
            return

        # Makes the full stop key on the keyboard and on the keypad act as a /
        # comma in the input field
        if key in (Qt.Key.Key_Period, Qt.Key.Key_Comma):
            self.insert(self.decimal)
            return

        super().keyPressEvent(event)