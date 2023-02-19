import requests
from pprint import pprint
import time
import json


city = input("Enter your city\n")

f = open('./env.json')
details =json.load(f)
print(details)
url = "http://api.openweathermap.org/data/2.5/weather?appid="+details['API_KEY']+"&q="+city

from_url = ''
page = ''
while page == '':
    try:
        page = requests.get(from_url)
        break
    except:
        print("Connecting to server..")
        from_url = url
        a="./   "
        for i in range(20):
            b=a[1]
            a=a[0:3:2]
            if b =="/":
                a+="*"
            elif b =="*":
                a+= "+"
            elif b =="+":
                a+="-"
            elif b =="-":
                a+= "^"
            else:
                a+="/"
            print(a,end="\r")
            time.sleep(0.25)
        print("Connected...")
        time.sleep(2)
        continue

weather_data = requests.get(url).json()

pprint(weather_data)
