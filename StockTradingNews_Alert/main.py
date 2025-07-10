import os
from dotenv import load_dotenv
import requests
from datetime import datetime, timedelta
from twilio.rest import Client

load_dotenv(dotenv_path="StockTradingNews_Alert/main.env")
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TODAY = datetime.today().date()

if not STOCK_API_KEY:
    raise Exception("API_KEY not found.")

STOCK_PARAMS = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : STOCK_API_KEY
}
response = requests.get(url=STOCK_ENDPOINT, params=STOCK_PARAMS)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

NEWS_PARAMS = {
    "q" : STOCK,
    "apiKey" : NEWS_API_KEY,
    "language" : "en"
}
news_response = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMS)
news_response.raise_for_status()
articles = news_response.json()["articles"]
three_articles = articles[:3]


def get_last_trading_day(day):
    if isinstance(day, str):
        day = datetime.strptime(day, "%Y-%m-%d").date()
    while True:
        day -= timedelta(days=1)
        if str(day) in data:
            return day

YESTERDAY = str(get_last_trading_day(TODAY))
DAY_BEFORE = str(get_last_trading_day(YESTERDAY))        
YESTERDAY_CLOSING_PRICE = float(data[YESTERDAY]["4. close"])
DAY_BEFORE_CLOSING_PRICE = float(data[DAY_BEFORE]["4. close"])
closing_price_difference = YESTERDAY_CLOSING_PRICE - DAY_BEFORE_CLOSING_PRICE
diff_percent = abs(closing_price_difference) / DAY_BEFORE_CLOSING_PRICE * 100

def send_alert():
    direction = "🔺" if closing_price_difference > 0 else "🔻"

    #Twilio free accounts have SMS length limits — brief (description) excluded to prevent truncation.
    message_body = [f"{STOCK}: {direction}{diff_percent:.2f}\nHeadline: {articles['title']}." for articles in three_articles]
    #message_body = [f"{STOCK}: {direction}{diff_percent}\nHeadline: {articles['title']}. \nBrief: {articles['description']}" for articles in three_articles]
    
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid=os.getenv("messaging_service_sid"),
        body= message_body,
        to=os.getenv("phone_number")
    )
    print("Message status:", message.status)


if diff_percent >= 5:
    send_alert()
