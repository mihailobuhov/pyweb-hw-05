import asyncio
import sys
from services.date import DateService
from services.exchange import ExchangeService
from services.api import APIService
from constants.errors import DateError


async def main(days: int):
    date = DateService()
    api = APIService()
    exchange = ExchangeService(api)

    try:
        dates = date.generate_dates(days)
        rates = await exchange.get_exchange_rates(dates)
        print(rates)
    except DateError as e:
        print(e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Input: py .\\main.py <number_of_days>")
        sys.exit(1)

    try:
        days = int(sys.argv[1])
    except ValueError:
        print("The number of days must be an integer")
        sys.exit(1)

    asyncio.run(main(days))
