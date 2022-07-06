import requests 
import os 
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv('/Users/William/Desktop/creds.env')
ALPHA_API_KEY = os.getenv('alpha_vantage_api_key')
NEWS_API_KEY = os.getenv('news_api_key')
STOCK_NAME = "SPY"
COMPANY_NAME = "SPDR S&P 500 ETF TRUST"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
PHONE_NUM = os.getenv('phone_num')
SID = os.getenv('account_sid')
AUTH = os.getenv('auth_token')
API_KEY = os.getenv('api_key')
TEST = os.getenv('test')


stock_params = {
    'function' : 'TIME_SERIES_DAILY',
    'symbol' : STOCK_NAME,
    'apikey' : ALPHA_API_KEY
}


response = requests.get(STOCK_ENDPOINT, params = stock_params)
response.raise_for_status() 
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]


yesterday_closing_price = float(data_list[0]['4. close'])


day_before_yesterday_closing_price = float(data_list[1]['4. close'])


difference = yesterday_closing_price - day_before_yesterday_closing_price


up_down = None 
if difference > 0: 
    up_down = '📈' 
else: 
    up_down = '📉'


diff_percent = round((difference / yesterday_closing_price) * 100,2)
diff_percent


if abs(diff_percent) > 5: 
    news_params = {
        'apiKey' : NEWS_API_KEY,
        'qInTitle' : 'S&P 500'
    }

    news_response = requests.get(NEWS_ENDPOINT, params = news_params)
    news_response.raise_for_status()
    articles = news_response.json()['articles']
    top3 = articles[:3]

    formatted = [f'{STOCK_NAME}: {up_down}{diff_percent}% \nHeadline: {news_article["title"]}. \nBrief: {news_article["description"]}' for news_article in top3]
    formatted 

    for article in formatted: 
        client = Client(SID, AUTH)
        message = client.messages.create(
            body = article, 
            from_ = PHONE_NUM,
            to = TEST
        )