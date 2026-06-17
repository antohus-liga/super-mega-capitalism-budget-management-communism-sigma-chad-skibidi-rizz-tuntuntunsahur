import locale

from typing import TypedDict


class LocaleInfo(TypedDict):
    currency_symbol: str
    decimal_point: str
    thousands_sep: str

class CurrencyService:
    def __init__(self) -> None:
        _ = locale.setlocale(category = locale.LC_ALL, locale = "")
        raw = locale.localeconv()

        self.locale_info: LocaleInfo = {
            "currency_symbol": raw.get("currency_symbol", ""),
            "decimal_point": raw.get("decimal_point", ""),
            "thousands_sep": raw.get("thousands_sep", "") 
        }

    def get_symbol(self) -> str:
        symbol: str = self.locale_info["currency_symbol"]
        return symbol if symbol else "€"

    def format(self, value: float) -> str:
        symbol: str = self.get_symbol()

        formatted: str = locale.currency(val = value, symbol = False,
        grouping = True)

        formatted = formatted.replace(".",
        self.locale_info["decimal_point"])
        return f"{formatted} {symbol}"