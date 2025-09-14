import aiohttp
from constants.constants import PRIVATBANK_API_URL
from constants.errors import APIError


class APIService:
    @staticmethod
    async def fetch_exchange_rates(date: str) -> dict:
        url = f"{PRIVATBANK_API_URL}{date}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    raise APIError(f"API request failed with status {response.status}")
                return await response.json()
