from typing import Protocol


class SupportsTotal(Protocol):
    def get_total(self) -> float:
        ...

class MainController:
    income_tab: SupportsTotal
    expense_tabs: list[SupportsTotal]

    def __init__(self, income_tab: SupportsTotal, expense_tabs: list[SupportsTotal]) -> None:
        self.income_tab = income_tab
        self.expense_tabs = expense_tabs

    def get_income_total(self) -> float:
        return self.income_tab.get_total()

    def get_expenses_total(self) -> float:
        return sum(tab.get_total() for tab in self.expense_tabs)