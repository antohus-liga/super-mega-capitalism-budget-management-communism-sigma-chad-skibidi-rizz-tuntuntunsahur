from PySide6.QtGui import QAction
from PySide6.QtWidgets import  QMainWindow, QMenu, QMenuBar, QWidget

from app.services.translation import TranslationService


class OptionsMenuBar(QMenuBar):
    def __init__(self, translation: TranslationService, parent:
        QWidget | None = None) -> None:
        super().__init__(parent)

        self.translation: TranslationService = translation

        self.labels: list[str] = (
        self.translation.get_list(key = "options_menu_bar_labels"))

        file_menu: QMenu = self.addMenu(self.labels[0])

        self.export_action: QAction = QAction(self.labels[1], self)
        file_menu.addAction(self.export_action)

        calculus_menu: QMenu = self.addMenu(self.labels[2])

        self.clear_inputs_action: QAction = QAction(self.labels[3], self)
        calculus_menu.addAction(self.clear_inputs_action)

        self.show_results_action: QAction = QAction(self.labels[4], self)
        calculus_menu.addAction(self.show_results_action)

    def get_labels(self) -> list[str]:
        return self.labels