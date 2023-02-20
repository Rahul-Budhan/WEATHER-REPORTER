"""Imports made here"""
import requests
from pprint import pprint
import time
from datetime import datetime
import json

"""Get Location names from input file"""
def get_location():
    handle = open('./docs/locations.txt','r')
    data = handle.read()
    handle.close()
    lines = data.split("\n")
    for line in lines:
        if line[0] == "#" or line[0]== " ":
            lines.remove(line)
    return lines

"""Connect to server/api and add animation"""
def connect(url):
    from_url = ''
    page = ''
    while page == '':
        try:
            page = requests.get(from_url)
            break
        except:
            """For animation and interaction effect"""
            print("Connecting to server..\nMight take a few seconds..")
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

"""Convert Unix time into datetime and store as string"""
def convert_unix_to_datestr(dt):
    return datetime.utcfromtimestamp(int(dt)).strftime('%Y-%m-%d %H:%M:%S')

"""Write Output into details.txt"""
def write_details(details):
    print("Writing details..")
    handle = open("./docs/details.txt","a")

    """convert returned unix value to string"""
    current_time = convert_unix_to_datestr(details['dt'])
    sunrise_at = convert_unix_to_datestr(details['sys']['sunrise'])
    time_zone = convert_unix_to_datestr(details['timezone'])
    sunset_at = convert_unix_to_datestr(details['sys']['sunset'])

    """Format output data"""

    output= ("Location: "+details['name'])+"\n"+("ID :   "+str(details['weather'][0]['id']))+"\n"+("COD :  "+str(details['cod']))+"\n"+("Weather : "+details['weather'][0]['main'])+"\n"+("Wind : "+str(details['wind']['speed']))+"\n"+("Current Time : "+current_time)+"\n"+("Time Zone : "+time_zone)+"\n"+("Humidity: "+str(details['main']['humidity']))+"\n"+("Sunrise At : "+sunrise_at)+"\n"+("Sunset At : "+sunset_at)+"\n"

    """Write output into details.txt"""
    handle.write(output+"\n")


