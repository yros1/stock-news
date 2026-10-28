from dotenv import load_dotenv
from stocks import Stocks
from news import News
from messenger import Messenger

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

# 2. If there was a difference more than 1.0% between yesterday's closing price and
#    the previous day, then get News API to fetch us some relevant news.
#    That way figure out what is the reason for this rise or what is the
#    reason for this fall. Send 4 messages with news articles to your WhatsUp.
print("""
###############################################
################## NEWS API ###################
###############################################
""")
if percentage_of_yesterday_closing_price > 1.0:
    past_days = 15

    news = News(about=stock_details["name"])
    news_data = news.get_news_data(from_last=past_days, number_of_news=4)
    # print(f"\nNews data:\n{news_data}")

    # Data fetched from JSON file just for dev testing.
    # news_data = None
    # with open("Data/NEWSAPI_EVERYTHING_response.json", "r") as file:
    #     news_data = json.load(file)

    articles = news_data["articles"]
    for article in articles:
        print(f"""
        {stock_details["name"]}({stock_details["ticker symbol"]}) {price_direction} by {percentage_of_yesterday_closing_price}%
        {article["title"]}
        {article["description"]}
        author: {article["author"]}
        link: {article["url"]}
        published at: {article["publishedAt"]}
        source: {article["source"]["name"]}
        """)

# 3. Next send yourself an What's up message telling what was the big fluctuation that happened.
#    Plus, what is the relevant news so that you can decide whether if you want to
#    sell our stock, or if you want to buy more. Use Twilio platform for sending messages.
    print("""
    ###############################################
    ############## TWILIO - SEND SMS ##############
    ###############################################
    """)

    messenger = Messenger()

    for article in articles:
        article_details = f"""
            {stock_details["name"]}({stock_details["ticker symbol"]}) {price_direction} by {percentage_of_yesterday_closing_price}%
            {article["title"]}
            {article["description"]}
            author: {article["author"]}
            link: {article["url"]}
            published at: {article["publishedAt"]}
            source: {article["source"]["name"]}
            """
        print(article_details)
        messenger_response = messenger.send_message(text=article_details)

        print(f"messenger status: {messenger_response[1]} \nmessenger sid: {messenger_response[0]}")
        print("Check your WhatsUp mobile app. Message should be now!")

print("\n\n##### END #####")
