from typing import Protocol


class SupportsTotal(Protocol):
    def get_total(self) -> float:
        ...

class SupportsRowData(Protocol):
    def get_rows_data(self) -> list[dict]:
        ...

class SupportsExpenseTab(Protocol):
    def get_total(self) -> float:
        ...
    def get_rows_data(self) -> list[dict]:
        ...

class MainController:
    income_tab: SupportsTotal
    expense_tabs: list[SupportsExpenseTab]

    def __init__(self, income_tab: SupportsTotal,
    expense_tabs: list[SupportsExpenseTab], savings_tab) -> None:
        self.income_tab = income_tab
        self.expense_tabs = expense_tabs
        self.savings_tab = savings_tab

    def get_income_total(self) -> float:
        return self.income_tab.get_total()

    def get_expenses_total(self) -> float:
        return sum(tab.get_total() for tab in self.expense_tabs)

    def get_financial_commitments_total(self) -> float:
        loans_total: float = self.expense_tabs[0].get_total()
        return loans_total

    def get_savings_total(self) -> float:
        return self.savings_tab.get_total()