from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QGridLayout, QWidget

from app.widgets.standard_frequency import StandardFrequencyComboBox
from app.widgets.standard_label import StandardLabel


class ResultsWidget(QWidget):
    def __init__(self, viewmodel, translation, currency_symbol,
    parent = None) -> None:
        super().__init__(parent)

        self.viewmodel = viewmodel
        self.translation = translation
        self.currency_symbol = currency_symbol

        self.labels: list[str] = translation.get_list("results_window_labels")

        self.grid: QGridLayout = QGridLayout(self)
        self.grid.setSpacing(20)

        self.period_selector: StandardFrequencyComboBox = (
        StandardFrequencyComboBox(translation = translation, parent = self))
        self.period_selector.currentIndexChanged.connect(
        self.update_values)

        self.income_label: StandardLabel = StandardLabel()
        self.expenses_label: StandardLabel = StandardLabel()
        self.savings_app_label: StandardLabel = StandardLabel()
        self.balance_label: StandardLabel = StandardLabel()
        self.saved_amount_label: StandardLabel = StandardLabel()
        self.saving_rate_label: StandardLabel = StandardLabel()
        self.effort_rate_label: StandardLabel = StandardLabel()
        self.message_label: StandardLabel = StandardLabel()
        self.message_label.setWordWrap(True)

        self._add_row(row = 0, label_text = self.labels[1],
        value_label = self.income_label)
        self._add_row(row = 1, label_text = self.labels[2],
        value_label = self.expenses_label)
        self._add_row(row = 2, label_text = self.labels[3],
        value_label = self.savings_app_label)
        self._add_row(row = 3, label_text = self.labels[4],
        value_label = self.balance_label)
        self._add_row(row = 4, label_text = self.labels[5],
        value_label = self.saved_amount_label)
        self._add_row(row = 5, label_text = self.labels[6],
        value_label = self.saving_rate_label)
        self._add_row(row = 6, label_text = self.labels[7],
        value_label = self.effort_rate_label)

        self.grid.addWidget(self.message_label)

        self.update_values()

    def _add_row(self, row, label_text, value_label) -> None:
        label: StandardLabel = StandardLabel(text = label_text)
        self.grid.addWidget(label, row, 0)
        self.grid.addWidget(value_label, row, 1)

    def update_values(self):
        mode: str = self.period_selector.currentData()

        yearly_income = self.viewmodel.income()
        yearly_expenses = self.viewmodel.expenses()
        yearly_savings = self.viewmodel.savings_total()

        if mode == "Monthly":
            divisor = 12
        elif mode == "Quarterly":
            divisor = 4
        elif mode == "Biannual":
            divisor = 2
        else:
            divisor = 1

        income = yearly_income / divisor
        expenses = yearly_expenses / divisor
        savings = yearly_savings / divisor

        balance_before_savings = income - expenses

        saved_amount = balance_before_savings

        balance = balance_before_savings - savings

        saving_rate = (saved_amount / income * 100) if (
        income) > 0 else 0

        effort_rate = self.viewmodel.effort_rate()

        format = lambda x: f"{x:,.2f} {self.currency_symbol
        }".replace(",", "X").replace(".", ",").replace("X",".")

        self.income_label.setText(format(income))
        self.expenses_label.setText(format(expenses))
        self.savings_app_label.setText(format(savings))
        self.balance_label.setText(format(balance))
        self.saved_amount_label.setText(format(saved_amount))
        self.saving_rate_label.setText(f"{saving_rate:.2f} %")
        self.effort_rate_label.setText(f"{effort_rate:.2f} %")

        palette: QPalette = self.balance_label.palette()

        if balance > 0:
            color = "green"
        elif balance < 0:
            color = "red"
        else:
            color = "#d4aa00"

        palette.setColor(QPalette.ColorRole.WindowText, QColor(color))
        self.balance_label.setPalette(palette)

        if balance > 0:
            self.message_label.setText(self.labels[8])
            self.message_label.setStyleSheet("color: green;")

        elif balance < 0:
            self.message_label.setText(self.labels[9])
            self.message_label.setStyleSheet("color: red;")

        else:
            self.message_label.setText(self.labels[10])
            self.message_label.setStyleSheet("color: #d4aa00;")
