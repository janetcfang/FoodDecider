import googlemaps as gm
import json
import random
from datetime import datetime as dt

gmaps = gm.Client(key = "")

###GET LOCATION###

userAddress = input("Please enter your current address: ")
#userAddress = "2201 West End Ave, Nashville, TN 37235"
geoc = gmaps.geocode(address=userAddress)

#latitude and longitude
loc = str(geoc[0]['geometry']['location']['lat']) + "," + str(geoc[0]['geometry']['location']['lng'])
#print(loc)

userChoice = input("What kind of food are you craving? (leave blank if undecided): ")
search = userChoice + "food"

#driving distance
userDistance = float(input("How far are you willing to drive? (miles): "))
distance = userDistance * 1609.34   #converts meters to miles

#JSON object - list of places
restaurants = gmaps.places(search, location=loc, radius=distance, language="english")
#print(json.dumps(restaurants, sort_keys=True, indent=2))

for i in range(len(restaurants['results'])):
    if "rating" in restaurants['results'][i]:
		rate = restaurants['results'][i]['rating'] 
	else:
		rate = "N/A"
	print('%d: %s - Rating: %s' % (i, restaurants['results'][i]['name'], rate))

#random generation
randQ = input("\nWould you like us to randomly generate a restaurant for you? Yes or No: ")
if randQ == "Yes":
    new = "Yes"
    while new != "No":
        rand = random.randrange(len(restaurants['results']))
        print(restaurants['results'][rand]['name'])
        new = input("\nWould you like a different restaurant? Yes or No: ")
    choice = rand
else:
    choice = int(input("\nWhich restaurant would you like directions to? "))

now = dt.now()

###GET DIRECTIONS###

directions = gmaps.directions(loc, restaurants['results'][choice]['formatted_address'], mode='driving',
                              departure_time=now)

#print(json.dumps(directions, indent=2))

#directions to food
for i in range(len(directions[0]['legs'][0]['steps'])):
    fix_string = directions[0]['legs'][0]['steps'][i]['html_instructions'].replace("<b>", "")
    fix_string = fix_string.replace("</b>", "")

    format = fix_string.find("<div")
    if(format != -1):
        fix_string = fix_string[:format]

    print('Step %d: %s ' % (i+1, fix_string))
