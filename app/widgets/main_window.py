from pathlib import Path

from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
QMessageBox, QScrollArea, QTabWidget, QWidget)

from app.services.xlsx import ExportXLSXService
from app.services.translation import TranslationService
from app.controllers.main import MainController
from app.widgets.duties_taxes import DutiesTaxesTab
from app.widgets.health_education import HealthEducationTab
from app.widgets.home import HomeTab
from app.widgets.income import IncomeTab
from app.widgets.insurance import InsuranceTab
from app.widgets.loans import LoansTab
from app.widgets.options_menu import OptionsMenuBar
from app.widgets.personal import PersonalTab
from app.widgets.savings import SavingsTab
from app.widgets.summary import SummaryChart
from app.widgets.results_window import ResultsWindow
from app.widgets.transport import TransportTab
from app.views.app import AppViewModel
from app.views.summary import SummaryViewModel


class MainWindow(QMainWindow):
    def __init__(self, app_viewmodel: AppViewModel,
    translation: TranslationService, icon_path: Path) -> None:
        super().__init__()

        self.translation: TranslationService = translation

        labels: list[str] = (
        self.translation.get_list(key = "main_window_labels"))

        self.export_labels: list[str] = self.translation.get_list(
        key = "export_messages")

        self.setWindowTitle(labels[0])
        self.setWindowIcon(QIcon(str(icon_path)))

        screen: QRect = QApplication.primaryScreen().availableGeometry()

        scale: float = 0.8 # % of the screen size

        w: int = int(screen.width() * scale)
        h: int = int(screen.height() * scale)

        self.resize(w, h)
        self.move(
            (screen.width() - w) // 2,
            (screen.height() - h) // 2)

        options_menu_bar: OptionsMenuBar = OptionsMenuBar(
        translation = self.translation)
        options_menu_bar.export_action.triggered.connect(
        self.export_to_xlsx)
        options_menu_bar.clear_inputs_action.triggered.connect(
        self.clear_inputs)
        options_menu_bar.show_results_action.triggered.connect(
        self.view_results)

        self.export_service: ExportXLSXService = ExportXLSXService()

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
            self.duties_taxes_tab],
        savings_tab = self.savings_tab)

        self.viewmodel: SummaryViewModel = SummaryViewModel(
        app_viewmodel = app_viewmodel, controller = self.controller)

        self.summary_chart: SummaryChart = SummaryChart(
        currency_symbol = self.currency_symbol,
        translation = translation)

        tabs: QTabWidget = QTabWidget()

        tabs.addTab(self.make_scrollable(self.income_tab), labels[1])
        tabs.addTab(self.make_scrollable(self.loans_tab), labels[2])
        tabs.addTab(self.make_scrollable(self.insurance_tab), labels[3])
        tabs.addTab(self.make_scrollable(self.duties_taxes_tab), labels[4])
        tabs.addTab(self.make_scrollable(self.home_tab), labels[5])
        tabs.addTab(self.make_scrollable(self.health_education_tab), labels[6])
        tabs.addTab(self.make_scrollable(self.transport_tab), labels[7])
        tabs.addTab(self.make_scrollable(self.personal_tab), labels[8])
        tabs.addTab(self.make_scrollable(self.savings_tab), labels[9])

        layout: QGridLayout = QGridLayout()
        layout.addWidget(options_menu_bar, 0, 0)
        layout.addWidget(self.summary_chart, 1, 0)
        layout.addWidget(tabs, 2, 0)

        layout.setRowStretch(0, 0)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 1)

        container: QWidget = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.refresh_summary()

    def clear_inputs(self) -> None:
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
            if hasattr(tab, "clear_all_rows"):
                tab.clear_all_rows()

        self.refresh_summary()

        self.summary_chart.update_values(
            income = 0,
            expenses = 0,
            formatted_income = "",
            formatted_expenses = "")

    def collect_all_data(self) -> dict:
        return {
            "income": self.income_tab.get_rows_data(),
            "loans": self.loans_tab.get_rows_data(),
            "insurance": self.insurance_tab.get_rows_data(),
            "personal": self.personal_tab.get_rows_data(),
            "transport": self.transport_tab.get_rows_data(),
            "health_education": self.health_education_tab.get_rows_data(),
            "home": self.home_tab.get_rows_data(),
            "duties_taxes": self.duties_taxes_tab.get_rows_data(),
            "savings": self.savings_tab.get_rows_data()}

    def export_to_xlsx(self) -> None:
        data = self.collect_all_data()
        path: Path = self.export_service.create_summary_xlsx(data)

        title: str = self.export_labels[0]
        message: str = f"{self.export_labels[1]}\n{path}"

        QMessageBox.information(self, title, message)

    def make_scrollable(self, widget: QWidget) -> QScrollArea:
        scroll: QScrollArea = QScrollArea()
        scroll.setWidget(widget)
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(
        Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        return scroll

    def refresh_summary(self) -> None:
        income: float = self.viewmodel.income()
        expenses: float = self.viewmodel.expenses()
        self.summary_chart.update_values(income,  expenses,
        formatted_income = self.viewmodel.formatted_income(),
        formatted_expenses = self.viewmodel.formatted_expenses())

    def view_results(self) -> None:
        self.results_window: ResultsWindow = ResultsWindow(
        viewmodel = self.viewmodel,
        translation = self.translation,
        currency_symbol = self.currency_symbol,
        parent = self)

        self.results_window.setGeometry(self.geometry())

        self.results_window.show()