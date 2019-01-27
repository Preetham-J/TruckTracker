import keys
import googlemaps
from datetime import datetime

class Directions:
	# Initialize Google Maps client and retrieve directions info
	def __init__(self, origin, destination):
		self.gmaps = googlemaps.Client(keys.gmaps)
		self.directions_result = self.gmaps.directions(origin, destination, mode="driving", departure_time=datetime.now())

	# Print direction, start/end latitude and longitude
	def print_info(self):
		for step in self.directions_result[0]["legs"][0]["steps"]:
			#print("Direction: " + str(step["distance"]["text"]))
			print(str(step["start_location"]["lat"]) + "," + str(step["start_location"]["lng"]))
			print(str(step["end_location"]["lat"]) + "," + str(step["end_location"]["lng"]))


# Main
if __name__ == '__main__':
	directions = Directions("McMaster University, Hamilton, ON", "CN Tower, Toronto, ON")
	directions.print_info()
