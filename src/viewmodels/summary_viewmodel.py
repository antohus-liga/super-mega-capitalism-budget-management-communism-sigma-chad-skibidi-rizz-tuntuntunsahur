from ui.controllers.main_controller import MainController


class SummaryViewModel:
    def __init__(self, controller: MainController):
        self.controller: MainController = controller

    def balance(self) -> float:
        return self.income() - self.expenses()

    def balance_text(self) -> str:
        return f"{self.balance():.2f} €"

    def expenses(self) -> float:
        return self.controller.get_expenses_total()

    def expenses_text(self) -> str:
        return f"{self.expenses():.2f} €"

    def income(self) -> float:
        return self.controller.get_income_total()

    def income_text(self) -> str:
        return f"{self.income():.2f} €"