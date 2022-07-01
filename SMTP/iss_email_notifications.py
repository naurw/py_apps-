import requests
import datetime as dt 
import geocoder 
import smtplib
import os 
from dotenv import load_dotenv
import time 


load_dotenv('/Users/William/Desktop/creds.env')
EMAIL = os.getenv('email')
PASSWORD = os.getenv('password')
HOST = os.getenv('host')
PORT = int(os.getenv('port'))


g = geocoder.ipinfo('me')
g.latlng

LAT = g.latlng[0]
LONG = g.latlng[1]


def datetime_from_utc_to_local(utc_str_datetime):
    dt_local = dt.datetime.fromisoformat(utc_str_datetime).astimezone()
    # return dt_local.strftime(("%I:%M:%S %p"))
    return dt_local.strftime(("%H:%M:%S"))

def iss_overhead(): 
    api_endpoint = 'http://api.open-notify.org/iss-now.json'
    response = requests.get(url = api_endpoint)
    response.raise_for_status()

    response.json()['iss_position']
    iss_latitude = float(response.json()['iss_position']['latitude'])
    iss_longitude = float(response.json()['iss_position']['longitude'])

    if LAT - 5 <= iss_latitude <= LAT + 5 and LONG - 5 <= iss_longitude <= LONG + 5: 
        return True


def is_night(): 
    parameters = {
        'lat': LAT, 
        'lng': LONG,
        'formatted': 0
    }

    response = requests.get('https://api.sunrise-sunset.org/json', params = parameters)
    response.raise_for_status() 
    data = response.json()

    sunrise = int(datetime_from_utc_to_local(data['results']['sunrise']).split(':')[0])
    sunset = int(datetime_from_utc_to_local(data['results']['sunset']).split(':')[0])

    time_now = dt.datetime.now().hour 
    time_now

    if time_now >= sunset or time_now <= sunrise: 
        return True 

while True: 
    time.sleep(60)
    if iss_overhead() and is_night(): 
        subject = 'ISS Geo-location'
        message = 'Look up in the night sky--the ISS is above you!'
        with smtplib.SMTP(host= HOST, port=PORT) as connection:
            connection.starttls()
            connection.login(user= EMAIL, password = PASSWORD) 
            connection.sendmail(
                from_addr = EMAIL, 
                to_addrs= EMAIL,
                msg = f'Subject: {subject}\n\n{message}'
                )