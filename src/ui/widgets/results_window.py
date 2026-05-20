from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGridLayout, QMainWindow, QScrollArea, QWidget

from ui.widgets.results_widget import ResultsWidget
from ui.widgets.summary_chart import SummaryChart


class ResultsWindow(QMainWindow):
    def __init__(self, viewmodel, translation, currency_symbol, parent = None) -> None:
        super().__init__(parent)

        labels: list[str] = translation.get_list("results_window_labels")

        self.setWindowTitle(labels[0])

        container: QWidget = QWidget()
        layout: QGridLayout = QGridLayout(container)

        chart: SummaryChart = SummaryChart(
        currency_symbol = currency_symbol,
        translation = translation)
        
        chart.update_values(
        income = viewmodel.income(),
        expenses = viewmodel.expenses(),
        formatted_income = viewmodel.formatted_income(),
        formatted_expenses = viewmodel.formatted_expenses())

        result_widget: ResultsWidget = ResultsWidget(
        viewmodel = viewmodel, translation = translation,
        currency_symbol = currency_symbol, parent = self)

        layout.addWidget(chart, 0, 0)
        layout.addWidget(result_widget, 1, 0)

        scroll = QScrollArea()
        scroll.setWidget(container)
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(
        Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.setCentralWidget(scroll)