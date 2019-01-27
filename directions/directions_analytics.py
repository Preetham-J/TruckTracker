import keys
import googlemaps
from datetime import datetime
import polyline
import numpy as np

class Directions:
	# Initialize Google Maps client and retrieve directions info
	def __init__(self, origin, destination):
		self.gmaps = googlemaps.Client(keys.gmaps)
		self.directions_result = self.gmaps.directions(origin, destination, mode="driving", departure_time=datetime.now())
		self.latitude_threshold = 0.00001
		self.get_points()

	# Gets points on route
	def get_points(self):
		point_array = []
		for step in self.directions_result[0]["legs"][0]["steps"]:
			polylines = step['polyline']['points']
			line = polyline.decode(polylines)
			point_array = point_array + line
		self.point_array = np.asarray(point_array)
 	
 	#get the closest points
	def get_distance(self, lat, lng):
		#get closest index
		point_array = self.point_array
		poi = np.asarray([lat,lng])
		poi = np.expand_dims(poi,axis=0)
		distance = np.power(point_array - poi,2)
		distance = np.sqrt(np.sum(distance,-1))
		min_point_idx = np.argmin(distance)
		min_points = point_array[min_point_idx-1:min_point_idx+2]
		min_points_distance_from_poi = distance[min_point_idx-1:min_point_idx+2]
		output = None
		#constrained optimization problem
		for i in range(1,len(min_points)):
			p1 = min_points[i-1]
			p2 = min_points[i]
			p3 = poi
			#poi distance if it is within the containt of p1 and p2
			v1 = p2-p1
			v2 = p3-p1
			v3 = p2-p1
			poi_distance = np.abs(np.cross(v1,v2)/np.linalg.norm(v3))

			#project v2 onto v1.
			proj_coor = (np.inner(v1,v2)/np.inner(v1,v1))*v1

			is_x_in_between = min(p1[0],p2[0]) < proj_coor[0] and max(p1[0],p2[0]) > proj_coor[0]

			if is_x_in_between:
				poi_distance = p2

			if output is None:
				output = poi_distance
			else:
				if output > poi_distance:
					output = poi_distance
					
		self.distance_from_route = output
		self.min_points = min_points
		self.min_distances = min_points_distance_from_poi
	#check if the distance is ok.
	def check_distance(self, lat, lng):
		self.get_distance(lat, lng)
		if self.distance_from_route > self.latitude_threshold:
			return False
		else:
			return True


	# Print direction, start/end latitude and longitude
	def print_direction(self):
		points = self.point_array
		for point in points:
			print(str(point[0]) + "\t" + str(point[1]) + "\tcircle3\tred\t1")

# Main
def main():
	#directions = Directions("McMaster University, Hamilton, ON", "CN Tower, Toronto, ON")
	directions = Directions((43.2609,-79.9192), "CN Tower, Toronto, ON")
	
	#np.save("test.npy", directions.point_array)
	#print(directions.point_array)
	#print(directions.check_distance(25, -79))
	directions.visualize()

if __name__ == '__main__':
	main()