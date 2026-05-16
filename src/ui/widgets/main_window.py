from PySide6.QtWidgets import QGridLayout, QMainWindow, QTabWidget, QWidget

from ui.controllers.main_controller import MainController
from ui.widgets.health_tab import HealthTab
from ui.widgets.home_tab import HomeTab
from ui.widgets.income_tab import IncomeTab
from ui.widgets.insurance_tab import InsuranceTab
from ui.widgets.loans_tab import LoansTab
from ui.widgets.personal_expenses_tab import PersonalExpensesTab
from ui.widgets.savings_tab import SavingsTab
from ui.widgets.summary_chart import SummaryChart
from ui.widgets.taxes_tab import TaxesTab
from ui.widgets.transport_tab import TransportTab
from viewmodels.summary_viewmodel import SummaryViewModel


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Orçamento Familiar")
        self.resize(800,600)

        self.income_tab: IncomeTab = IncomeTab()

        self.loans_tab: LoansTab = LoansTab()
        self.insurance_tab: InsuranceTab = InsuranceTab()
        self.personal_expenses_tab: PersonalExpensesTab = PersonalExpensesTab()
        self.transport_tab: TransportTab = TransportTab()
        self.health_tab: HealthTab = HealthTab()
        self.home_tab: HomeTab = HomeTab()
        self.taxes_tab: TaxesTab = TaxesTab()

        self.savings_tab: SavingsTab = SavingsTab()

        self.controller: MainController = MainController(
            income_tab=self.income_tab,
            expense_tabs=[
                self.loans_tab,
                self.insurance_tab,
                self.personal_expenses_tab,
                self.transport_tab,
                self.health_tab,
                self.home_tab,
                self.taxes_tab,
            ]
        )

        self.viewmodel: SummaryViewModel = SummaryViewModel(self.controller)

        self.summary_chart: SummaryChart = SummaryChart()

        tabs: QTabWidget = QTabWidget()
        _ = tabs.addTab(self.income_tab, "Rendimentos")
        _ = tabs.addTab(self.loans_tab, "Créditos")
        _ = tabs.addTab(self.insurance_tab, "Seguros")
        _ = tabs.addTab(self.personal_expenses_tab, "Despesas Pessoais")
        _ = tabs.addTab(self.transport_tab, "Transportes")
        _ = tabs.addTab(self.health_tab, "Saúde")
        _ = tabs.addTab(self.home_tab, "Casa")
        _ = tabs.addTab(self.taxes_tab, "Impostos")
        _ = tabs.addTab(self.savings_tab, "Poupanças")

        _ = tabs.currentChanged.connect(self.refresh_summary) # _ is needed /
        # in all of this lines because otherwise pyright throws a warning /
        # about variables not being accessed


        layout: QGridLayout = QGridLayout()
        layout.addWidget(self.summary_chart, 0, 0)
        layout.addWidget(tabs, 1,0)

        container: QWidget = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.refresh_summary()

    def refresh_summary(self) -> None:
        income: float = self.viewmodel.income()
        expenses: float = self.viewmodel.expenses()
        self.summary_chart.update_values(income, expenses)