from PySide6.QtCore import Signal
from PySide6.QtWidgets import QGridLayout, QWidget

from ui.widgets.frequency_row import FrequencyRow


class IncomeTab(QWidget):
    totalChanged: Signal = Signal()

    def __init__(self) -> None:
        super().__init__()
        self.total_income: float = 0.0

        layout: QGridLayout = QGridLayout()
        self.setLayout(layout)

        self.rows: list[FrequencyRow] = [
            FrequencyRow(text = "Ordenados (líquidos)", parent = self),
            FrequencyRow(text = "Pensões (líquidas)", parent = self),
            FrequencyRow(text = "Subsídios de desemprego", parent = self),
            FrequencyRow(text = "Abono de família", parent = self),
            FrequencyRow(text = ("Outros subsídios (Natal, férias, parental, "
            "assistência familiar)"), parent = self),
            FrequencyRow(text = "Remunerações de poupanças e investimentos",
            parent = self),
            FrequencyRow(text = "Rendas recebidas",
            parent = self),
            FrequencyRow(text = ("Regularização do Imposto sobre as Pessoas "
            "Singulares (IRS)"), parent = self),
            FrequencyRow(text = "Outros rendimentos", parent = self)
        ]

        for row_index, row in enumerate[FrequencyRow](self.rows):
            layout.addWidget(row.label, row_index, 0)
            layout.addWidget(row.input_box, row_index, 1)
            layout.addWidget(row.currency_left, row_index, 2)
            layout.addWidget(row.option, row_index, 3)
            layout.addWidget(row.equals, row_index, 4)
            layout.addWidget(row.result_label, row_index, 5)
            layout.addWidget(row.currency_right, row_index, 6)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setHorizontalSpacing(10)
        layout.setVerticalSpacing(6)

        for row in self.rows:
            _ = row.valueChanged.connect(self._on_row_changed)

    def get_total(self) -> float:
        return sum(r.get_value() for r in self.rows)

    def _on_row_changed(self) -> None:
        self.totalChanged.emit()