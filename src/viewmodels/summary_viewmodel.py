from ui.controllers.main_controller import MainController
from viewmodels.app_viewmodel import AppViewModel


class SummaryViewModel:
    def __init__(self, controller: MainController,
    app_viewmodel: AppViewModel) -> None:
        self.app_viewmodel: AppViewModel = app_viewmodel
        self.controller: MainController = controller

    def balance(self) -> float:
        return self.income() - self.expenses()

    def balance_text(self) -> str:
        return self.app_viewmodel.currency_service.format(
        value = self.balance())

    def expenses(self) -> float:
        return self.controller.get_expenses_total()

    def expenses_text(self) -> str:
        return self.app_viewmodel.currency_service.format(
        value = self.expenses())

    def formatted_income(self) -> str:
        value: float = self.income()
        return self.app_viewmodel.currency_service.format(value)

    def formatted_expenses(self) -> str:
        value: float = self.expenses()
        return self.app_viewmodel.currency_service.format(value)

    def formatted_max_value(self) -> str:
        max_value: float = max(self.income(), self.expenses(), 1.0)
        return self.app_viewmodel.currency_service.format(max_value)

    def income(self) -> float:
        return self.controller.get_income_total()

    def income_text(self) -> str:
        return self.app_viewmodel.currency_service.format(
        value = self.income())
