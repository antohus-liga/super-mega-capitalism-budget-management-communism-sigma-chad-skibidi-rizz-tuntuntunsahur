from services.currency_service import CurrencyService


class AppViewModel:
    def __init__(self, currency_service: CurrencyService) -> None:
        self.currency_symbol: str = currency_service.get_symbol()