from app.services.currency import CurrencyService


class AppViewModel:
    def __init__(self, currency_service: CurrencyService) -> None:
        self.currency_service: CurrencyService = currency_service
        self.currency_symbol: str = currency_service.get_symbol()