from PySide6.QtCore import QRect
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
QTabWidget, QWidget)

from services.translation_service import TranslationService # this /
# import is needed here for the type annotation
from ui.controllers.main_controller import MainController
from ui.widgets.health_education_tab import HealthEducationTab
from ui.widgets.home_tab import HomeTab
from ui.widgets.income_tab import IncomeTab
from ui.widgets.insurance_tab import InsuranceTab
from ui.widgets.loans_tab import LoansTab
from ui.widgets.personal_tab import PersonalTab
from ui.widgets.savings_tab import SavingsTab
from ui.widgets.summary_chart import SummaryChart
from ui.widgets.duties_taxes_tab import DutiesTaxesTab
from ui.widgets.transport_tab import TransportTab
from viewmodels.app_viewmodel import AppViewModel # this import is needed here /
# for the type annotation 
from viewmodels.summary_viewmodel import SummaryViewModel


class MainWindow(QMainWindow):
    def __init__(self, app_viewmodel: AppViewModel,
    translation: TranslationService) -> None:
        super().__init__()

        self.translation: TranslationService = translation

        labels: list[str] = (
        self.translation.get_list(key = "main_window_labels"))

        self.setWindowTitle(labels[0])

        screen: QRect = QApplication.primaryScreen().availableGeometry()

        scale: float = 0.7 # % of the screen size

        w: int = int(screen.width() * scale)
        h: int = int(screen.height() * scale)

        self.resize(w, h)
        self.move(
            (screen.width() - w) // 2,
            (screen.height() - h) // 2
        )

        self.currency_symbol: str = app_viewmodel.currency_symbol

        self.income_tab: IncomeTab = IncomeTab(
        currency_symbol = self.currency_symbol,
        translation = self.translation)
        self.loans_tab: LoansTab = LoansTab(
        currency_symbol = self.currency_symbol,
        translation = self.translation)
        self.insurance_tab: InsuranceTab = InsuranceTab(
        currency_symbol = self.currency_symbol,
        translation = self.translation)
        self.personal_tab: PersonalTab = PersonalTab(
        currency_symbol = self.currency_symbol,
        translation = self.translation)
        self.transport_tab: TransportTab = TransportTab(
        currency_symbol = self.currency_symbol,
        translation = self.translation)
        self.health_education_tab: HealthEducationTab = HealthEducationTab(
        currency_symbol = self.currency_symbol,
        translation = self.translation)
        self.home_tab: HomeTab = HomeTab(currency_symbol = self.currency_symbol,
        translation = self.translation)
        self.duties_taxes_tab: DutiesTaxesTab = DutiesTaxesTab(
        currency_symbol = self.currency_symbol,
        translation = self.translation)
        self.savings_tab: SavingsTab = SavingsTab(
        currency_symbol = self.currency_symbol,
        translation = self.translation)

        for tab in [
            self.income_tab,
            self.loans_tab,
            self.insurance_tab,
            self.personal_tab,
            self.transport_tab,
            self.health_education_tab,
            self.home_tab,
            self.duties_taxes_tab,
            self.savings_tab]:
            _ = tab.totalChanged.connect(self.refresh_summary)

        self.controller: MainController = MainController(
            income_tab = self.income_tab,
            expense_tabs = [
                self.loans_tab,
                self.insurance_tab,
                self.personal_tab,
                self.transport_tab,
                self.health_education_tab,
                self.home_tab,
                self.duties_taxes_tab])

        self.viewmodel: SummaryViewModel = SummaryViewModel(
        app_viewmodel = app_viewmodel, controller = self.controller)

        self.summary_chart: SummaryChart = SummaryChart(
        currency_symbol = self.currency_symbol,
        translation = translation)

        tabs: QTabWidget = QTabWidget()

        _ = tabs.addTab(self.income_tab, labels[1])
        _ = tabs.addTab(self.loans_tab, labels[2])
        _ = tabs.addTab(self.insurance_tab, labels[3])
        _ = tabs.addTab(self.duties_taxes_tab, labels[4])
        _ = tabs.addTab(self.home_tab, labels[5])
        _ = tabs.addTab(self.health_education_tab, labels[6])
        _ = tabs.addTab(self.transport_tab, labels[7])
        _ = tabs.addTab(self.personal_tab, labels[8])
        _ = tabs.addTab(self.savings_tab, labels[9])

        layout: QGridLayout = QGridLayout()
        layout.addWidget(self.summary_chart, 0, 0)
        layout.addWidget(tabs, 1, 0)

        layout.setRowStretch(0, 0)
        layout.setRowStretch(1, 1)

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