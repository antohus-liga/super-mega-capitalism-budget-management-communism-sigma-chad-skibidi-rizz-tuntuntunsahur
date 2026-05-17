import math

from typing import override

from PySide6.QtCore import Qt
from PySide6.QtGui import (QColor, QFontMetrics, QMouseEvent, QPainter,
QPaintEvent)
from PySide6.QtWidgets import QToolTip, QWidget

from ui.shared.theme import is_dark_mode


class SummaryChart(QWidget):
    def __init__(self, currency_symbol: str, parent:
        QWidget | None = None) -> None:
        super().__init__(parent)

        self.currency_symbol: str = currency_symbol
        self.income: float = 0.0
        self.expenses: float = 0.0
        self.formatted_income: str = ""
        self.formatted_expenses: str = ""

        self.setMinimumHeight(150)
        self.setMouseTracking(True)

    @override
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        y: float = event.position().y()

        income_label: str = self.tr("Rendimentos")
        expenses_label: str = self.tr("Despesas")

        if 20 <= y <= 40:
            QToolTip.showText(event.globalPosition().toPoint(),
            f"{income_label}: {self.formatted_income}", w = self)
        elif 60 <= y <= 80:
            QToolTip.showText(event.globalPosition().toPoint(),
            f"{expenses_label}: {self.formatted_expenses}", w = self)
        else:
            QToolTip.hideText()

    @override
    def paintEvent(self, event: QPaintEvent) -> None:
        painter: QPainter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        w: int = self.width()

        dark: bool = is_dark_mode()
        text_color: QColor = QColor("#ffffff" if dark else "#000000")
        tick_color: QColor = QColor("#ffffff" if dark else "#000000")

        max_value: float = max(self.income, self.expenses, 1.0)

        scaled: float = max_value * 1.2
        nice_max: float = math.ceil(scaled / 1000) * 850

        income_width: int = int((self.income / nice_max) * (w -40))
        expenses_width: int = int((self.expenses / nice_max) * (w -40))

        painter.setBrush(QColor("#4caf50"))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRect(20, 20, income_width, 20)

        painter.setBrush(QColor("#f44336"))
        painter.drawRect(20, 60, expenses_width, 20)

        metrics: QFontMetrics = painter.fontMetrics()

        zero_width: int = metrics.horizontalAdvance("0")
        painter.drawText(20 - zero_width // 2, 95, "0")

        formatted_max: str = f"{nice_max:,.0f}".replace(",", ".")
        text_width: int = metrics.horizontalAdvance(formatted_max)

        painter.drawText(w - 20 - text_width, 95, formatted_max)

        painter.setPen(text_color)
        painter.drawLine(20, 100, w - 20, 100)

        intervals = 5
        step: float = nice_max / intervals

        painter.setPen(tick_color)

        for i in range(intervals + 1):
            x: int = 20 + int((i / intervals) * (w - 40))
            painter.drawLine(x, 105, x, 115)

            label: str = f"{step * i:.0f}"
            label_width: int = metrics.horizontalAdvance(label)
            painter.drawText(x - label_width // 2, 140, label)

    def update_values(self, income: float, expenses: float,
    formatted_income: str, formatted_expenses: str) -> None:
        self.income = income
        self.expenses = expenses
        self.formatted_income = formatted_income
        self.formatted_expenses = formatted_expenses
        self.update()