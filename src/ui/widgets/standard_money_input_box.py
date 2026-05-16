from PySide6.QtCore import Qt
from PySide6.QtGui import QDoubleValidator, QKeyEvent
from PySide6.QtWidgets import QLineEdit, QWidget
from typing import override


class StandardMoneyInputBox(QLineEdit):
    def __init__(self, placeholder: str = "", parent: QWidget | None = None
    ) -> None:
        super().__init__(parent)

        validator: QDoubleValidator = QDoubleValidator(0.0, 9999999.99, 2)
        validator.setNotation(QDoubleValidator.Notation.StandardNotation)
        self.setValidator(validator)

        if placeholder:
            self.setPlaceholderText(placeholder)

        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setMaximumWidth(100)

    # Makes the full stop key on the keypad act as a comma in the input field
    @override 
    def keyPressEvent(self, event: QKeyEvent) -> None:
        key: int = event.key()
        mods: Qt.KeyboardModifier = event.modifiers()

        if key == Qt.Key.Key_Period and (
        (mods & Qt.KeyboardModifier.KeypadModifier)):
            self.insert(",")
            return

        if key == Qt.Key.Key_Comma:
            self.insert(",")
            return

        if key == Qt.Key.Key_Period:
            return

        super().keyPressEvent(event)