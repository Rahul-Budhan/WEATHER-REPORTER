"""Imports made here"""
from classes import *


"""Initialization"""
f = open('./env.json')
details =json.load(f)
url = "http://api.openweathermap.org/data/2.5/weather?appid="+details['API_KEY']+"&q="


"""Locations taken from locations.txt"""
locations = get_location()

for location in locations:
    recieved = connect(url+location)
    write_details(location,recieved)


