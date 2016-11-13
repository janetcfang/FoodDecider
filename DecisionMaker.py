import googlemaps as gm
import json
from datetime import datetime as dt

gmaps = gm.Client(key = "")


#user input
#userLoc = raw_input("Please enter your current location: " )
userAddress = raw_input("Please enter your current address: ")

loc = userAddress

userChoice = raw_input("What kind of food are you deciding on? ")

restaurants = gmaps.places("restaurant", location=userAddress, radius=8050, language="english")

#print(json.dumps(restaurants, sort_keys=True, indent=2))

for i in range(10):
    print('%d: %s - %s' % (i, restaurants['results'][i]['name'], restaurants['results'][i]['formatted_address']))

choice = int(input("Which restaurant would you like directions to? "))

now = dt.now()

directions = gmaps.directions(userAddress, restaurants['results'][choice]['formatted_address'], mode='driving',
                              departure_time=now)

jobj = json.load(directions)
for direct in jobj['legs']['steps']:
    print(direct['html_instructions'])

print(json.dumps(directions, indent=2))


#list results 
for i in range(10):
    print(i + '%s - %s' % (restaurants['results'][i]['name'], restaurants['results'][i]['formatted_address']))
