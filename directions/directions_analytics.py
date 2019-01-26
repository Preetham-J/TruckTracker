import key
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key.key)

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("McMaster University, Hamilton, ON",
                                     "CN Tower, Toronto, ON",
                                     mode="driving",
                                     departure_time=now)

for route in directions_result[0]["legs"][0]["steps"]:
    print("Lat, Long: " + str(route["start_location"]["lat"]) + ", " + str(route["start_location"]["lng"]))


