import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='ENTER_KEY')

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("McMaster University, Hamilton, ON",
                                     "CN Tower, Toronto, ON",
                                     mode="driving",
                                     departure_time=now)

