from PySide6.QtWidgets import QPushButton, QSizePolicy


def standard_button_rules(button: QPushButton) -> None:
    button.setMaximumWidth(180)
    button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)