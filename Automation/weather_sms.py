import requests
import geocoder 
import os 
from dotenv import load_dotenv
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# ----- SMS Weather Report ------# 
load_dotenv('/home/noirnaur/automation/py_anywhere_creds.env')
PHONE_NUM = os.getenv('phone_num')
SID = os.getenv('account_sid')
AUTH = os.getenv('auth_token')
API_KEY = os.getenv('api_key')
TEST = os.getenv('test')


g = geocoder.ipinfo('me')
g.latlng

LAT = g.latlng[0]
LONG = g.latlng[1]


parameters = {
    'lat': LAT, 
    'lon': LONG,
    'units' : 'imperial',
    'exclude' : 'current,minutely,daily',
    'appid' : API_KEY
}

response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params = parameters)
response.raise_for_status() 
data = response.json()
data 

if [True for id in data['hourly'][:12] if id['weather'][0]['id'] < 700]:
    proxy_client = TwilioHttpClient() 
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(SID, AUTH, http_client=proxy_client)
    message = client.messages \
        .create(
            body = 'There is a change of precipitation today--bring an umbrella! ☂️', 
            from_= PHONE_NUM, 
            to = TEST
        )
    
    print(message.status)
