# Stock price API
# https://www.alphavantage.co/

import os
import requests_cache
from datetime import timedelta

class Stocks:
    def __init__(self, ticker_symbol):
        self.ticker_symbol = ticker_symbol

    def get_stock_data(self):
        endpoint = "https://www.alphavantage.co/query"
        function = "TIME_SERIES_DAILY"
        symbol = self.ticker_symbol
        api_key = os.environ.get("ALPHAVANTAGE_API_KEY")

        parameters = {
            "function": function,
            "symbol": symbol,
            "apikey": api_key,
        }

        session = requests_cache.CachedSession(
            cache_name="stock_cache",
            backend="sqlite",
            expire_after=timedelta(hours=12),
        )

        response = session.get(url=endpoint, params=parameters, timeout=30)

        print(f"\nParameters:\n{parameters}\nResponse url:\n{response.url}\n")
        response.raise_for_status()
        traded_data = response.json()

        return traded_data