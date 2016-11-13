import googlemaps as gm
import json
from datetime import datetime as dt

gmaps = gm.Client(key = "AIzaSyBByCmegtekUSBBXj-OG5AAuhc98GDDfhs")

#user input
#userLoc = raw_input("Please enter your current location: " )
#userAddress = input("Please enter your current address: ")

#userChoice = input("What kind of food are you deciding on? ")
userAddress = "36.1447034,-86.8048438"
restaurants = gmaps.places("restaurant", location=userAddress, radius=8050, language="english")

#print(json.dumps(restaurants, sort_keys=True, indent=2))

for i in range(len(restaurants['results'])):
    print('%d: %s - %s' % (i, restaurants['results'][i]['name'], ""))

choice = int(input("\nWhich restaurant would you like directions to? "))

now = dt.now()

directions = gmaps.directions(userAddress, restaurants['results'][choice]['formatted_address'], mode='driving',
                              departure_time=now)

#print(json.dumps(directions, indent=2))

for i in range(len(directions[0]['legs'][0]['steps'])):
    fix_string = directions[0]['legs'][0]['steps'][i]['html_instructions'].replace("<b>", "")
    fix_string = fix_string.replace("</b>", "")

    format = fix_string.find("<div")
    if(format != -1):
        fix_string = fix_string[:format]

    print('Step %d: %s ' % (i+1, fix_string))

