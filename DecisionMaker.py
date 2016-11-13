import googlemaps as gm
import json
from datetime import datetime as dt

gmaps = gm.Client(key = "")


loc = "36.1432074,-86.8060411"

restaurants = gmaps.places("restaurant", location=loc, radius=8050, language="english")

#print(json.dumps(restaurants, sort_keys=True, indent=2))

for i in range(10):
    print(i + '%s - %s' % (restaurants['results'][i]['name'], restaurants['results'][i]['formatted_address']))