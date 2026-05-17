from PySide6.QtCore import Signal
from PySide6.QtWidgets import QGridLayout, QWidget

from ui.widgets.frequency_row import FrequencyRow


class HomeTab(QWidget):
    totalChanged: Signal = Signal()

    def __init__(self, currency_symbol: str) -> None:
        super().__init__()
        self.total_home: float = 0.0

        layout: QGridLayout = QGridLayout()
        self.setLayout(layout)

        self.rows: list[FrequencyRow] = [
            FrequencyRow(text = "Renda",
            currency_symbol = currency_symbol, parent = self),
            FrequencyRow(text = "Supermercado",
            currency_symbol = currency_symbol, parent = self),
            FrequencyRow(text = "Condomínio",
            currency_symbol = currency_symbol, parent = self),
            FrequencyRow(text = "Electricidade",
            currency_symbol = currency_symbol, parent = self),
            FrequencyRow(text = "Gás",
            currency_symbol = currency_symbol, parent = self),
            FrequencyRow(text = "Água",
            currency_symbol = currency_symbol, parent = self),
            FrequencyRow(text = "Telefone (fixo), Internet, TV",
            currency_symbol = currency_symbol, parent = self),
            FrequencyRow(text = "Telemóvel",
            currency_symbol = currency_symbol, parent = self),
            FrequencyRow(text = "Obras de manutenção",
            currency_symbol = currency_symbol, parent = self),
            FrequencyRow(text = "Lavandaria",
            currency_symbol = currency_symbol, parent = self),
            FrequencyRow(text = "Empregada doméstica",
            currency_symbol = currency_symbol, parent = self),
            FrequencyRow(text = "Outras despesas domésticas",
            currency_symbol = currency_symbol, parent = self)
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