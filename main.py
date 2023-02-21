"""Imports made here"""
from classes import *

"""Initialization"""
f = open('./config.json')
details =json.load(f)
url = "http://api.openweathermap.org/data/2.5/weather?appid="+details['API_KEY']+"&q="

"""Locations taken from locations.txt"""
locations = get_location()

"""Geet details and write details into file for each entry"""
for location in locations:
    recieved = connect(url+location)
    write_details(recieved)
print("Execution completed")
