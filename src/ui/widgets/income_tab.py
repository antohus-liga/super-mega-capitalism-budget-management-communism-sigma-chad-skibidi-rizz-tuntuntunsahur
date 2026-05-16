from PySide6.QtWidgets import QGridLayout, QWidget

from ui.widgets.standard_frequency_combo_box import StandardFrequencyComboBox
from ui.widgets.standard_currency_label import StandardCurrencyLabel
from ui.widgets.standard_label import StandardLabel
from ui.widgets.standard_money_input_box import StandardMoneyInputBox


class IncomeTab(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.total_income: float = 0.0

        layout: QGridLayout = QGridLayout()

        self.setLayout(layout)

        salary_input: StandardMoneyInputBox = StandardMoneyInputBox(
        parent = self)
        pensions_input: StandardMoneyInputBox = StandardMoneyInputBox(
        parent = self)
        unemployment_benefits_input: StandardMoneyInputBox = (
        StandardMoneyInputBox(parent = self))
        children_benefit_input: StandardMoneyInputBox = (
        StandardMoneyInputBox(parent = self))
        other_benefits_input: StandardMoneyInputBox = (
        StandardMoneyInputBox(parent = self))
        interest_savings_investments_input: StandardMoneyInputBox = (
        StandardMoneyInputBox(parent = self))
        rent_received_input: StandardMoneyInputBox = (
        StandardMoneyInputBox(parent = self))
        settlement_personal_income_tax_input: StandardMoneyInputBox = (
        StandardMoneyInputBox(parent = self))
        other_incomes_input: StandardMoneyInputBox = (
        StandardMoneyInputBox(parent = self))

        salary_result_label: StandardLabel = StandardLabel(text = "0.00",
        max_width = 100, parent = self)
        pensions_result_label: StandardLabel = StandardLabel(text = "0.00",
        max_width = 100, parent = self)
        unemployment_benefits_result_label: StandardLabel = StandardLabel(
        text = "0.00", max_width = 100, parent = self)
        children_benefit_result_label: StandardLabel = StandardLabel(
        text = "0.00", max_width = 100, parent = self)
        other_benefits_result_label: StandardLabel = StandardLabel(
        text = "0.00", max_width = 100, parent = self)
        interest_savings_investments_result_label: StandardLabel = (
        StandardLabel(text = "0.00", max_width = 100, parent = self))
        rent_received_result_label: StandardLabel = StandardLabel(
        text = "0.00", max_width = 100, parent = self)
        settlement_personal_income_tax_result_label: StandardLabel = (
        StandardLabel(text = "0.00", max_width = 100, parent = self))
        other_incomes_result_label: StandardLabel = StandardLabel(
        text = "0.00", max_width = 100, parent = self)

        rows: list[tuple[str, StandardMoneyInputBox, StandardLabel]] = [
            ("Ordenados (líquidos)", salary_input, salary_result_label),
            ("Pensões (líquidas)", pensions_input, pensions_result_label),
            ("Subsídios de desemprego", unemployment_benefits_input,
            unemployment_benefits_result_label),
            ("Abono de família", children_benefit_input,
            children_benefit_result_label),
            ("Outros subsídios (Natal, férias, parental, assistência familiar)",
            other_benefits_input, other_benefits_result_label),
            ("Remunerações de poupanças e investimentos",
            interest_savings_investments_input,
            interest_savings_investments_result_label),
            ("Rendas recebidas", rent_received_input,
            rent_received_result_label),
            ("Regularização do Imposto sobre as Pessoas Singulares (IRS)",
            settlement_personal_income_tax_input,
            settlement_personal_income_tax_result_label),
            ("Outros rendimentos", other_incomes_input,
            other_incomes_result_label),
        ]

        for row, (text, input_box, result_label) in enumerate[tuple[str,
        StandardMoneyInputBox, StandardLabel]](rows):
            label: StandardLabel = StandardLabel(text = text, parent = self)

            layout.addWidget(label, row, 0)
            layout.addWidget(input_box, row, 1)
            layout.addWidget(StandardCurrencyLabel(parent = self), row, 2)
            layout.addWidget(StandardFrequencyComboBox(parent = self), row, 3)
            layout.addWidget(StandardLabel(text = "=", max_width = 10,
            parent = self), row, 4)
            layout.addWidget(result_label, row, 5)
            layout.addWidget(StandardCurrencyLabel(parent = self), row, 6)

    def get_total(self) -> float:
        return self.total_income