from PySide6.QtCore import QCoreApplication
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
        self.setWindowTitle(QCoreApplication.translate("MainWindow",
        "Orçamento Familiar"))
        self.resize(1040,720) # changed this from 800x600 -> 1280x720 for a /
        # better user view experience

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

        for tab in [
            self.income_tab,
            self.loans_tab,
            self.insurance_tab,
            self.personal_expenses_tab,
            self.transport_tab,
            self.health_education_tab,
            self.home_tab,
            self.duties_taxes_tab,
            self.savings_tab]:
            _ = tab.totalChanged.connect(self.refresh_summary)

        self.controller: MainController = MainController(
            income_tab=self.income_tab,
            expense_tabs=[
                self.loans_tab,
                self.insurance_tab,
                self.personal_expenses_tab,
                self.transport_tab,
                self.health_education_tab,
                self.home_tab,
                self.duties_taxes_tab])

        self.viewmodel: SummaryViewModel = SummaryViewModel(
        app_viewmodel = app_viewmodel, controller = self.controller)

        self.summary_chart: SummaryChart = SummaryChart(
        currency_symbol = self.currency_symbol)

        tab_labels: list[str] = [
            "Rendimentos",
            "Empréstimos",
            "Seguros",
            "Impostos e Taxas",
            "Casa",
            "Saúde e Educação",
            "Transportes",
            "Pessoal",
            "Aplicações de Poupança"]

        translated_labels: list[str] = [
            QCoreApplication.translate("MainWindow", text)
            for text in tab_labels]

        tabs: QTabWidget = QTabWidget()
        _ = tabs.addTab(self.income_tab, translated_labels[0])
        _ = tabs.addTab(self.loans_tab, translated_labels[1])
        _ = tabs.addTab(self.insurance_tab, translated_labels[2])
        _ = tabs.addTab(self.duties_taxes_tab, translated_labels[3])
        _ = tabs.addTab(self.home_tab, translated_labels[4])
        _ = tabs.addTab(self.health_education_tab, translated_labels[5])
        _ = tabs.addTab(self.transport_tab, translated_labels[6])
        _ = tabs.addTab(self.personal_expenses_tab, translated_labels[7])
        _ = tabs.addTab(self.savings_tab, translated_labels[8])

        layout: QGridLayout = QGridLayout()
        layout.addWidget(self.summary_chart, 0, 0)
        layout.addWidget(tabs, 1, 0)

        container: QWidget = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.refresh_summary()

    def refresh_summary(self) -> None:
        income: float = self.viewmodel.income()
        expenses: float = self.viewmodel.expenses()
        self.summary_chart.update_values(income,  expenses,
        formatted_income = self.viewmodel.formatted_income(),
        formatted_expenses = self.viewmodel.formatted_expenses())