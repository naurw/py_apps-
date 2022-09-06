from selenium import webdriver 
from selenium.webdriver.common.by import By
import time 
import smtplib
import os 
from dotenv import load_dotenv 

load_dotenv('/Users/William/Desktop/creds.env')
EMAIL = os.getenv('email')
PASSWORD = os.getenv('password')
HOST = os.getenv('host')
PORT = int(os.getenv('port'))

INTERVAL = 3600
TARGET_PRICE = float(89)

chrome_driver_path = '/Users/William/Desktop/dev/chromedriver'
driver = webdriver.Chrome(executable_path = chrome_driver_path)
driver.get('https://www.amazon.com/Logitech-MX-Master-3S-Graphite/dp/B09HM94VDS/ref=sr_1_3?crid=1L5EV4X4VZ4XP&keywords=mx+master+3s&qid=1662409865&sprefix=mx+master+3s%2Caps%2C94&sr=8-3')
dollar = driver.find_element(By.CLASS_NAME, 'a-price-whole') 
cents = driver.find_element(By.CLASS_NAME, 'a-price-fraction')
price = float(f'{dollar.text}.{cents.text}')
print(price)

def send_mail(): 
    with smtplib.SMTP("smtp.gmail.com", PORT) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Watchlist Price Drop\n\nYour item price has dropped to: {price}. Click here to purchase {URL}"
            )

def check_price():
    print(f"Checking for price drop, current price is ${price}...")

    if price <= TARGET_PRICE:
        send_mail()
        print("Waiting...")
        time.sleep(INTERVAL)
    else:
        print("Waiting...")
        time.sleep(INTERVAL)


is_on = True
while is_on:
    check_price()