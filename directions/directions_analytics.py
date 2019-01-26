import key
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key.key)

# Request directions
now = datetime.now()
directions_result = gmaps.directions("McMaster University, Hamilton, ON",
                                     "CN Tower, Toronto, ON",
                                     mode="driving",
                                     departure_time=now)

# Print direction, start and end latitude and longitude
for step in directions_result[0]["legs"][0]["steps"]:
    print("Direction: " + str(step["distance"]["text"]))
    print("Start Lat/Long: " + str(step["start_location"]["lat"]) + "/" + str(step["start_location"]["lng"]))
    print("End Lat/Long: " + str(step["end_location"]["lat"]) + "/" + str(step["end_location"]["lng"]))



