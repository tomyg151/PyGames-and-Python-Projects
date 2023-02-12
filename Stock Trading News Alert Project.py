import requests
from datetime import datetime
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# key for alphavantage.co - 40HPADCU0FNZE5D0
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
api_key_stock = "40HPADCU0FNZE5D0"

# API - https://newsapi.org/
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "e87503b33f3c477793104c78441c5d49"

ACCOUNT_SID = "AC3d342c8c9f10edadb2cfc6eaeac7fccc"
AUTH_TOKEN = ("18bb3bd2fa1521ffaecc25048782c29d")


## API for geting the stock data daily - use: "https://www.alphavantage.co/query"
# HINT 1: Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yerstday's closing stock price stock that their value is bigger than 5%.

parameters_stock = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": api_key_stock
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters_stock)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]  # slice to get only what inside the the key "Time Series (Daily)"

data_list = [value for (key, value) in data.items()]  # list Comprehension to convert the dictionary to list
yesterday_closing_price = data_list[0]["4. close"]
day_before_yesterday = data_list[1]["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
percent_dif = round((difference / float(day_before_yesterday)) * 100)

## API for article and news - Use https://newsapi.org/docs/endpoints/everything
# fetch the first 3 articles for the COMPANY_NAME.

if abs(percent_dif) == 5:
    parameters_news = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url=NEWS_ENDPOINT, params=parameters_news)
    response.raise_for_status()
    three_first_articles = response.json()["articles"][:3]

    ## Use twilio.com/docs/sms/quickstart/python
    # Send a separate message with each article's title and description to your phone number.

    formatted_articles = [
        f"{STOCK}: {up_down}{percent_dif}%. \nHeadline: {article['title']}. \nBrief: {article['description']}" for
        article in
        three_first_articles]  # list Comprehension that send the massage to the phone (the Format the SMS message
    # like this)

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages \
            .create(
            body=article,
            from_="+15185046063",
            to="+9720505427551"  # put the phone number we want to sent the massage
        )

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
