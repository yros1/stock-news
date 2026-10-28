# News API
# https://newsapi.org/
# https://newsapi.org/v2/everything?q=SpaceX&searchIn=title&from_date=2026-10-14&sortBy=popularity&pageSize=5&apiKey=your_api_key

import os
import requests_cache
from datetime import date, timedelta

class News:
    def __init__(self, about):
        self.about = about

    def get_news_data(self, from_last, number_of_news):
        base_endpoint = "https://newsapi.org/v2/"
        everything_endpoint = "everything"
        symbol = self.about  # "SpaceX"
        search_in = "title"
        from_date = (date.today() - timedelta(days=from_last)).strftime("%Y-%m-%d")  # get yesterday date
        sort_by = "popularity"
        page_size = number_of_news
        api_key = os.environ.get("NEWSAPI_API_KEY")

        parameters = {
            "q": symbol,
            "searchIn": search_in,
            "from": from_date,
            "sortBy": sort_by,
            "pageSize": page_size,
            "apikey": api_key
        }

        session = requests_cache.CachedSession(
            cache_name="news_cache",
            backend="sqlite",
            expire_after=timedelta(hours=12),
        )

        response = session.get(url=f"{base_endpoint}{everything_endpoint}", params=parameters, timeout=30)

        print(f"Requesting news for {self.about!r} from {from_date} (page size {page_size})")
        response.raise_for_status()
        news_data = response.json()

        return news_data