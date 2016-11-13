import googlemaps as gm
import json
import random
from datetime import datetime as dt

gmaps = gm.Client(key = "")

#user input
#userLoc = raw_input("Please enter your current location: " )
#userAddress = input("Please enter your current address: ")
#userAddress = "36.1447034,-86.8048438"

userAddress = "2201 West End Ave, Nashville, TN 37235"
geoc = gmaps.geocode(address=userAddress)

loc = str(geoc[0]['geometry']['location']['lat']) + "," + str(geoc[0]['geometry']['location']['lng'])
#print(loc)

userChoice = input("What kind of food are you craving? (leave blank if undecided): ")
search = userChoice + "food"
restaurants = gmaps.places(search, location=loc, radius=8050, language="english")

#print(json.dumps(restaurants, sort_keys=True, indent=2))

randQ = raw_input("\nWould you like us to randomly generate a restaurant for you? Yes or No: ")
if randQ == "Yes":
	new = "Yes"
	while(new != "No"):
		rand = random.randrange(len(restaurants['results']))
		print(restaurants['results'][rand]['name'])
		new = raw_input("\nWould you like a different restaurant? Yes or No: ")
	choice = rand
else:
	choice = int(raw_input("\nWhich restaurant would you like directions to? "))


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

