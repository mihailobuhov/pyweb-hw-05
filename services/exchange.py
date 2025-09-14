from services.api import APIService
from constants.constants import CURRENCIES
from constants.errors import APIError

class ExchangeService:
    def __init__(self, api: APIService):
        self.api = api

    async def get_exchange_rates(self, days: list) -> list:
        results = []
        for day in days:
            try:
                data = await self.api.fetch_exchange_rates(day)
                exchange_rates = {currency: {} for currency in CURRENCIES}
                for rate in data.get('exchangeRate', []):
                    if rate.get('currency') in CURRENCIES:
                        exchange_rates[rate['currency']] = {
                            'sale': rate.get('saleRateNB'),
                            'purchase': rate.get('purchaseRateNB')
                        }
                results.append({day: exchange_rates})
            except APIError as e:
                print(f"Failed to fetch data for {day}: {e}")
        return results
