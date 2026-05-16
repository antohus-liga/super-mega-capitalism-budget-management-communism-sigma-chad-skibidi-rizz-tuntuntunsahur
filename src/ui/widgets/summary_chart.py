from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QMouseEvent, QPainter, QPaintEvent, QPen
from PySide6.QtWidgets import QToolTip, QWidget
from typing import override


class SummaryChart(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.income: float = 0.0
        self.expenses: float = 0.0

        self.setMinimumHeight(120)
        self.setMouseTracking(True)

    @override
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        y: float = event.position().y()

        if 20 <= y <= 40:
            QToolTip.showText(event.globalPosition().toPoint(),
            f"Rendimentos: {self.income:.2f} €", w = self)
        elif 60 <= y <= 80:
            QToolTip.showText(event.globalPosition().toPoint(),
            f"Despesas: {self.expenses:.2f} €", w = self)
        else:
            QToolTip.hideText()

    @override
    def paintEvent(self, event: QPaintEvent) -> None:
        painter: QPainter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        w: int = self.width()

        max_value: float = max(self.income, self.expenses, 1)

        income_width: int = int((self.income / max_value) * (w -40))
        expenses_width: int = int((self.expenses / max_value) * (w -40))

        painter.setBrush(QColor("#4caf50"))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRect(20, 20, income_width, 20)

        painter.setBrush(QColor("#f44336"))
        painter.drawRect(20, 60, expenses_width, 20)

        painter.setPen(QPen(Qt.GlobalColor.black, 1))
        painter.drawLine(20, 100, w - 20, 100)

        intervals = 5
        step: float = max_value / intervals

        for i in range(intervals + 1):
            x: int = 20 + int((i / intervals) * (w - 40))
            painter.drawLine(x, 105, x, 115)
            painter.drawText(x - 10, 135, f"{step * i:.0f}")

    def update_values(self, income: float, expenses: float) -> None:
        self.income = income
        self.expenses = expenses
        self.update()