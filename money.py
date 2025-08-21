import requests
import smtplib

STOKE_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "7YJUKBB7F3V1B7ZC"
NEWS_API_KEY = "42552414bd724694b301282d1ca6c65b"

stock_parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOKE_NAME,
    "apikey" : STOCK_API_KEY,
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "↑"
else:
    up_down = "↓"

diff_percent = round((difference / float(yesterday_closing_price)) * 100)

if abs(diff_percent) > 2:
    news_parameters = {
        "apiKey" : NEWS_API_KEY,
        "qInTitle" : COMPANY_NAME,
    }
    response1 = requests.get(NEWS_ENDPOINT, params=news_parameters)
    articles = response1.json()["articles"]
    three_articles = articles[:3]
    data_to_send = [(f"{STOKE_NAME}: {up_down}{diff_percent}%\nHeadlines: {article['title']}."
                     f"\nBrief: {article['description']}")
                    for article in three_articles]
    for article in data_to_send:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login("aryapasupulate@gmail.com", "yzfajjgoszrcfjuy")
            connection.sendmail(from_addr="aryapasupulate@gmail.com", to_addrs="aryapasupulate@gmail.com",
                                msg=article)