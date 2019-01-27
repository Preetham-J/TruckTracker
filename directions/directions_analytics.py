import key
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key.key)

# Request directions via driving
now = datetime.now()
directions_result = gmaps.directions("McMaster University, Hamilton, ON",
                                     "CN Tower, Toronto, ON",
                                     mode="driving",
                                     departure_time=now)

lats = []
longs = []
for route in directions_result[0]["legs"][0]["steps"]:
    lat = route["start_location"]["lat"]
    lng = route["start_location"]["lng"]
    print("Lat, Long: " + str(lat) + ", " + str(lng))
    lats.append(lat)
    longs.append(lng)
