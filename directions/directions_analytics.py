import key
import googlemaps
from datetime import datetime
import polyline

class Directions:
	# Initialize Google Maps client and retrieve directions info
	def __init__(self, origin, destination):
		self.gmaps = googlemaps.Client(key.key)
		self.directions_result = self.gmaps.directions(origin, destination, mode="driving", departure_time=datetime.now())

	# Gets points on route
	def get_points(self):
		point_array = []
		for step in self.directions_result[0]["legs"][0]["steps"]:
			polylines = step['polyline']['points']
			line = polyline.decode(polylines)
			point_array = point_array + line
		
		return(point_array)


	# Print direction, start/end latitude and longitude
	def print_info(self):
		points = self.get_points()
		for point in points:
			print(str(point[0]) + "\t" + str(point[1]) + "\tcircle3\tred\t1")
		# for step in self.directions_result[0]["legs"][0]["steps"]:
		# 	# print("Direction: " + str(step["distance"]["text"]))
		# 	# print("Start Lat/Long: " + str(step["start_location"]["lat"]) + "/" + str(step["start_location"]["lng"]))
		# 	# print("End Lat/Long: " + str(step["end_location"]["lat"]) + "/" + str(step["end_location"]["lng"]))
			
		# 	# print(str(step["start_location"]["lat"]) + "\t" + str(step["start_location"]["lng"]) + "\tcircle3\tred\t1")
		# 	# print(str(step["end_location"]["lat"]) + "\t" + str(step["end_location"]["lng"]) + "\tcircle3\tred\t1")

		# 	# Polylines
		# 	polylines = step['polyline']['points']
		# 	line = polyline.decode(polylines)
		# 	for point in line:
		# 		print(str(point[0]) + "\t" + str(point[1]) + "\tcircle3\tred\t1")



# Main
if __name__ == '__main__':
	directions = Directions("McMaster University, Hamilton, ON", "CN Tower, Toronto, ON")
	directions.print_info()