from PySide6.QtWidgets import QGridLayout, QMainWindow, QTabWidget, QWidget

from ui.controllers.main_controller import MainController
from ui.widgets.health_education_tab import HealthEducationTab
from ui.widgets.home_tab import HomeTab
from ui.widgets.income_tab import IncomeTab
from ui.widgets.insurance_tab import InsuranceTab
from ui.widgets.loans_tab import LoansTab
from ui.widgets.personal_tab import PersonalExpensesTab
from ui.widgets.savings_tab import SavingsTab
from ui.widgets.summary_chart import SummaryChart
from ui.widgets.duties_taxes_tab import DutiesTaxesTab
from ui.widgets.transport_tab import TransportTab
from viewmodels.app_viewmodel import AppViewModel # this import is needed here /
# for the type annotation 
from viewmodels.summary_viewmodel import SummaryViewModel


class MainWindow(QMainWindow):
    def __init__(self, app_viewmodel: AppViewModel) -> None:
        super().__init__()
        self.setWindowTitle("Orçamento Familiar")
        self.resize(800,600)

        self.currency_symbol: str = app_viewmodel.currency_symbol

        self.income_tab: IncomeTab = IncomeTab(
        currency_symbol = self.currency_symbol)
        self.loans_tab: LoansTab = LoansTab(
        currency_symbol = self.currency_symbol)
        self.insurance_tab: InsuranceTab = InsuranceTab(
        currency_symbol = self.currency_symbol)
        self.personal_expenses_tab: PersonalExpensesTab = PersonalExpensesTab(
        currency_symbol = self.currency_symbol)
        self.transport_tab: TransportTab = TransportTab(
        currency_symbol = self.currency_symbol)
        self.health_education_tab: HealthEducationTab = HealthEducationTab(
        currency_symbol = self.currency_symbol)
        self.home_tab: HomeTab = HomeTab(currency_symbol = self.currency_symbol)
        self.duties_taxes_tab: DutiesTaxesTab = DutiesTaxesTab(
        currency_symbol = self.currency_symbol)
        self.savings_tab: SavingsTab = SavingsTab(
        currency_symbol = self.currency_symbol)

        _ = self.income_tab.totalChanged.connect(self.refresh_summary)
        _ = self.loans_tab.totalChanged.connect(self.refresh_summary)
        _ = self.insurance_tab.totalChanged.connect(self.refresh_summary)
        _ = self.personal_expenses_tab.totalChanged.connect(
            self.refresh_summary)
        _ = self.transport_tab.totalChanged.connect(self.refresh_summary)
        _ = self.health_education_tab.totalChanged.connect(self.refresh_summary)
        _ = self.home_tab.totalChanged.connect(self.refresh_summary)
        _ = self.duties_taxes_tab.totalChanged.connect(self.refresh_summary)
        _ = self.savings_tab.totalChanged.connect(self.refresh_summary)

        self.controller: MainController = MainController(
            income_tab=self.income_tab,
            expense_tabs=[
                self.loans_tab,
                self.insurance_tab,
                self.personal_expenses_tab,
                self.transport_tab,
                self.health_education_tab,
                self.home_tab,
                self.duties_taxes_tab,
            ]
        )

        self.viewmodel: SummaryViewModel = SummaryViewModel(self.controller)

        self.summary_chart: SummaryChart = SummaryChart()

        tabs: QTabWidget = QTabWidget()
        _ = tabs.addTab(self.income_tab, "Rendimentos")
        _ = tabs.addTab(self.loans_tab, "Empréstimos")
        _ = tabs.addTab(self.insurance_tab, "Seguros")
        _ = tabs.addTab(self.duties_taxes_tab, "Impostos e Taxas")
        _ = tabs.addTab(self.home_tab, "Casa")
        _ = tabs.addTab(self.health_education_tab, "Saúde e Educação")
        _ = tabs.addTab(self.transport_tab, "Transportes")
        _ = tabs.addTab(self.personal_expenses_tab, "Pessoal")
        _ = tabs.addTab(self.savings_tab, "Aplicações de Poupança")

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