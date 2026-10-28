from dotenv import load_dotenv
from stocks import Stocks

print("##### START #####\n\n")

load_dotenv(verbose=True)

# SpaceX stock details we want to explore with our API.
stock_details = {
    "name": "SpaceX",
    "ticker symbol": "SPCX"
}

# 1. Pull closing price of yesterday and the day of yesterday for given stock.
#    Calculate a difference between those two prices.
#    Based on it figure out a direction (UP, DOWN, FLAT).
#    Calculate a percentage of difference for yesterday closing price.
print("""
###############################################
################# STOCK API ###################
###############################################
""")

stock = Stocks(stock_details["ticker symbol"])
traded_data = stock.get_stock_data()
#print(traded_data)

# Data fetched from JSON file just for dev testing.
# traded_data = None
# with open("Data/TIME_SERIES_DAILY_response.json", "r") as file:
#     traded_data = json.load(file)

time_series = traded_data["Time Series (Daily)"]
time_series_day_list = list(time_series.values())
yesterday = time_series_day_list[0]
the_day_before_yesterday = time_series_day_list[1]

yesterday_close_price = float(yesterday["4. close"])
print(f"Yesterday close price:\n{yesterday_close_price}")
the_day_before_yesterday_close_price = float(the_day_before_yesterday["4. close"])
print(f"The day before yesterday close price:\n{the_day_before_yesterday_close_price}")

price_difference =  yesterday_close_price - the_day_before_yesterday_close_price
print(f"price difference:\n{price_difference}")

percentage_of_yesterday_closing_price = (abs(price_difference) * 100) / yesterday_close_price
print(f"percentage of yesterday closing price:\n{percentage_of_yesterday_closing_price:.2f}%")

price_direction = None
if price_difference > 0:
    price_direction = "UP"
elif price_difference < 0:
    price_direction = "DOWN"
else:
    price_direction = "FLAT"
print(f"price direction:\n{price_direction}")