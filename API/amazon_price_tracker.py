import time
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv
import os 

load_dotenv('/Users/William/Desktop/creds.env')
EMAIL = os.getenv('email')
PASSWORD = os.getenv('password')
HOST = os.getenv('host')
PORT = int(os.getenv('port'))

def send_mail(): 
    with smtplib.SMTP("smtp.gmail.com", PORT) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Watchlist Price Drop\n\nYour item price has dropped to: {PRICE}. Click here to purchase {URL}"
            )

def check_price():
    print(f"Checking for price drop, current price is ${PRICE}...")

    if PRICE <= TARGET_PRICE:
        send_mail()
        print("Waiting...")
        time.sleep(INTERVAL)
    else:
        print("Waiting...")
        time.sleep(INTERVAL)

window = tk.Tk() 
window.withdraw() 

messagebox.showinfo('Amazon Price Checker v1.0', "Welcome to Amazon Price Checker v1.0\n"
"Notice:\nEmails sent may be located in SPAM folder. Please press OK to continue.\n"
"URL Example: https://www.amazon.com/Elden-Ring-PlayStation-5/dp/B09743F8P6")


URL = 'https://www.amazon.com/Logitech-MX-Master-3S-Graphite/dp/B09HM94VDS/ref=sr_1_2?crid=1WR68UGTXTQNE&keywords=mx+master+3s&qid=1661119909&sprefix=mx+master+3+s%2Caps%2C82&sr=8-2'
CLASS_STRING_DOLLAR = 'a-price-whole'
CLASS_STRING_FRACTION = 'a-price-fraction'
INTERVAL = 3600
TARGET_PRICE = float(89)
HEADER = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36', 
    'Accept-Language': 'en-US;q=0.9'
}


response = requests.get(URL, headers=HEADER)
response.raise_for_status()
soup = BeautifulSoup(response.content, "lxml")
dollar = soup.find("span", class_=CLASS_STRING_DOLLAR).getText()
cents = soup.find(class_ = CLASS_STRING_FRACTION).getText()
PRICE = float(f'{dollar}{cents}')


is_on = True
while is_on:
    check_price()
