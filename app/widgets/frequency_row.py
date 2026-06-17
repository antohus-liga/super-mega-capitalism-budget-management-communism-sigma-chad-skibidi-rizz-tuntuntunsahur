from functools import partial
from typing import cast, ClassVar

from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QWidget

from app.core.config import FREQUENCY_MULTIPLIERS
from app.services.translation import TranslationService
from app.widgets.standard_currency import StandardCurrencyLabel
from app.widgets.standard_frequency import StandardFrequencyComboBox
from app.widgets.standard_label import StandardLabel
from app.widgets.standard_money import StandardMoneyInputBox


class FrequencyRow(QObject):
    valueChanged: ClassVar[Signal] = Signal()

    def __init__(self, text: str, currency_symbol: str,
    translation: TranslationService, parent: QWidget
    | None = None) -> None:
        super().__init__(parent)

        self.translation: TranslationService = translation

        self.label: StandardLabel = StandardLabel(text = text, max_width = 200,
        parent = parent)
        self.input_box: StandardMoneyInputBox = StandardMoneyInputBox(
        parent = parent)
        self.currency_left: StandardCurrencyLabel = StandardCurrencyLabel(
        currency_symbol = currency_symbol, parent = parent)
        self.option: StandardFrequencyComboBox = StandardFrequencyComboBox(
        translation = self.translation, parent = parent)
        self.equals: StandardLabel = StandardLabel(text = "=", max_width = 10,
        parent = parent)
        self.result_label: StandardLabel = StandardLabel(text = "0.00",
        max_width = 100, parent = parent)
        self.currency_right: StandardCurrencyLabel = StandardCurrencyLabel(
        currency_symbol = currency_symbol, parent = parent)

        self._bind()

    def _bind(self) -> None:
        _ = self.input_box.textChanged.connect(partial[None](
        self._wrap_update, input_box = self.input_box, option = self.option,
        result_label = self.result_label))

        _ = self.option.currentIndexChanged.connect(partial[None](
            self._wrap_update, input_box = self.input_box,
            option = self.option, result_label = self.result_label,))

    def _wrap_update(self, _text: str, input_box: StandardMoneyInputBox,
    option: StandardFrequencyComboBox, result_label: StandardLabel) -> None:
        self.update(input_box, option, result_label)

    def clear(self) -> None:
        self.input_box.setText("")
        self.option.setCurrentIndex(0)
        self.result_label.setText("")
        self.valueChanged.emit()

    def get_value(self) -> float:
        raw: str = self.result_label.text().replace(",", ".")
        try:
            return float(raw)
        except ValueError:
            return 0.0

    def update(self, input_box: StandardMoneyInputBox,
    option: StandardFrequencyComboBox, result_label: StandardLabel) -> None:
        raw: str = input_box.text().replace(",", ".")
        try:
            value: float = float(raw)
        except ValueError:
            value = 0.0

        frequency: str = cast(str, option.currentData())
        multiplier: int = FREQUENCY_MULTIPLIERS.get(frequency, 0)

        total: float = value * multiplier
        result_label.setText(f"{total:.2f}")

        self.valueChanged.emit()