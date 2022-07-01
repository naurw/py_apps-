import datetime as dt 
import pandas as pd 
import random 
import smtplib
import os 
from dotenv import load_dotenv

os.getcwd()
os.chdir('/Users/William/Desktop/100_python_projects/py_apps-/SMTP')



load_dotenv('/Users/William/Desktop/creds.env')
EMAIL = os.getenv('email')
PASSWORD = os.getenv('password')
HOST = os.getenv('host')
PORT = int(os.getenv('port'))


data = {
    'name' : [EMAIL],
    'email' : [EMAIL], 
    'year' : [dt.datetime.now().year],
    'month' : [dt.datetime.now().month], 
    'day': [dt.datetime.now().day] 
}

df = pd.DataFrame(data)
df['name'] = df.loc[(df['name'] == EMAIL), df.name] =  EMAIL.split('@')[0]
df.to_csv('random csv/bday.csv', index = False )

today_date = (dt.datetime.now().month, dt.datetime.now().day)
today_date

data = pd.read_csv('random csv/bday.csv')
data
bday_dict = {(row['month'], row['day']) : row for (index, row) in data.iterrows()}
bday_dict

file_path = f'/Users/William/Desktop/100_python_projects/100-Python-Projects-/input/letter_templates/letter_{random.randint(1,3)}.txt'
with open(file_path, 'r') as f:
    contents = f.read()
    if today_date in bday_dict: 
        with open(file_path, 'r') as f: 
            contents = f.read().replace('[NAME]', bday_dict[today_date]['name'])
            print(contents)
    
    subject = f'Happy Birthday!'
    message = contents
    with smtplib.SMTP(host= HOST, port=PORT) as connection:
        connection.starttls()
        connection.login(user= EMAIL, password = PASSWORD) 
        connection.sendmail(
            from_addr = EMAIL, 
            to_addrs= bday_dict[today_date]['email'],
            msg = f'Subject: {subject}\n\n{message}'
            )