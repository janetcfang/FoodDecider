import googlemaps as gm
import json
from datetime import datetime as dt

gmaps = gm.Client(key = "AIzaSyBByCmegtekUSBBXj-OG5AAuhc98GDDfhs")

#loc = "36.1432074,-86.8060411"

#user input
#userLoc = raw_input("Please enter your current location: " )
userAddress = raw_input("Please enter your current address: ")
<<<<<<< HEAD
=======
loc = userAddress
>>>>>>> f79a84676dcf2a5b46a87c6f492c8c7094689b3a
userChoice = raw_input("What kind of food are you deciding on? ")

restaurants = gmaps.places("restaurant", location=userAddress, radius=8050, language="english")

#print(json.dumps(restaurants, sort_keys=True, indent=2))
<<<<<<< HEAD
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
=======

#list results 
for i in range(10):
    print(i + '%s - %s' % (restaurants['results'][i]['name'], restaurants['results'][i]['formatted_address']))

#user pick results



>>>>>>> f79a84676dcf2a5b46a87c6f492c8c7094689b3a
