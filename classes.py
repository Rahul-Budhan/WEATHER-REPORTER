import requests
from pprint import pprint
import time
import json

def get_location():
    handle = open('./docs/locations.txt','r')
    data = handle.read()
    handle.close()
    lines = data.split("\n")
    for line in lines:
        if line[0] == "#" or line[0]== " ":
            lines.remove(line)
    print(lines)
    return lines


def connect(url):
    from_url = url
    page = ''
    while page == '':
        try:
            page = requests.get(from_url)
            break
        except:
            print("Connecting to server..")
            from_url = url
            a="./   "
            for i in range(30):
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
                time.sleep(0.15)
        print("Connected...")
        time.sleep(1)
        continue

    return requests.get(url).json()

def write_details(location,details):
    handle = open("./docs/details.txt","w")
    weather_status = details['weather'][0]['main']
    handle.write(location+":\n")
    handle.write("Weather: ", weather_status)
    

