import os
import requests
import statistics
import datetime as dt
from twilio.rest import Client
 
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
 
 
class AlphaVantage:
 
    def __init__(self):
        self.API_ENDPOINT = "https://www.alphavantage.co/query"
        self.API_KEY = os.environ["AV_API_KEY"]
        self.properties = {
            "open": "1. open",
            "high": "2. high",
            "low": "3. low",
            "close": "4. close",
            "volume": "5. volume"
        }
 
    def query(self, symbol, func="TIME_SERIES_DAILY"):
        response = requests.get(url=self.API_ENDPOINT, params={
            "function": func,
            "symbol": symbol,
            "apikey": self.API_KEY
        })
        response.raise_for_status()
        return response.json()
 
    def percentage_change(self, property: str, n: int):
        if n < 2:
            raise Exception("Parameter 'n' cannot be less than 2")
 
        stock_time_series = self.query(STOCK)
 
        days = [stock_time_series["Time Series (Daily)"][day]
                for day in stock_time_series["Time Series (Daily)"]][:n]
 
        combined_data = {}
        for day in days:
            [combined_data.setdefault(item, []).append(
                float(day[item])) for item in day]
 
        current_data = combined_data[self.properties[property]]
 
        if n == 2:
            return round(((current_data[0] - current_data[1]) / current_data[1]) * 100, 2)
 
        mean = statistics.mean(current_data)
        return round(((current_data[0] - mean) / mean) * 100, 2)
 
 
class NewsApi:
 
    def __init__(self):
        self.API_ENDPOINT = "https://newsapi.org/v2/everything"
        self.API_KEY = os.environ["NEWS_API_KEY"]
 
    def query(self, q, from_time=dt.datetime.today().strftime("%Y-%m-%d"), pageSize=10, sortBy="publishedAt"):
        response = requests.get(url=self.API_ENDPOINT, params={
            "q": q,
            "from": from_time,
            "pageSize": pageSize,
            "sortBy": sortBy,
            "language": "en",
            "apiKey": self.API_KEY
        })
        response.raise_for_status()
        return response.json()
 
 
class TwilioSMS:
 
    def __init__(self):
        self.ACCOUNT_SID = os.environ["ACCOUNT_SID"]
        self.AUTH_TOKEN = os.environ["AUTH_TOKEN"]
        self.PHONE_NUMBER = os.environ["TWILIO_PHONE_NUMBER"]
 
    def send(self, message_body, to_num):
        client = Client(self.ACCOUNT_SID, self.AUTH_TOKEN)
        message = client.messages \
            .create(
                body=message_body,
                from_=self.PHONE_NUMBER,
                to=to_num
            )
 
        print(message.sid)
 
## STEP 1: Use https://www.alphavantage.co
connection = AlphaVantage()
 
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday.
percentage_change = connection.percentage_change("close", 2)
 
if abs(percentage_change) >= 5:
    news_date_range = (dt.datetime.today() -
                       dt.timedelta(30)).strftime("%Y-%m-%d")
 
    # STEP 2: Use https://newsapi.org
    connection = NewsApi()
    # Get the first 3 news pieces for the COMPANY_NAME. 
    news = connection.query(COMPANY_NAME, news_date_range, 3)
 
    #Optional: Format the SMS message like this: 
    """
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    or
    "TSLA: 🔻5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    """
    news_headlines = [
        ("Headline: %s\nBrief: %s" % (article["title"], article["description"])) for article in news["articles"]
    ]
 
    message = "%s: %s%s%%\n%s" % (STOCK, "🔺" if percentage_change > 0 else "🔻" if percentage_change < 0 else "➖", percentage_change, '\n'.join(news_headlines))
 
    # STEP 3: Use https://www.twilio.com
    connection = TwilioSMS()
    
    # Send a message with the percentage change and each article's title and description to your phone number.
    connection.send(message, os.environ["MY_PHONE_NUMBER"])
else:
    print("No significant change.")