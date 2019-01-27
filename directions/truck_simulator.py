from directions_analytics import Directions

class Truck:
	# Initialize truck route using Directions class
	def __init__(self, origin, destination):
		self.directions = Directions(origin, destination)
		self.route_length = len(self.directions.get_points())

	# Get every point on the route
	def get_route(self):
		return self.directions.get_points()

	# Get total amount of points on the route
	def get_route_length(self):
		return self.route_length

	# Get a specific point on the route
	def get_point_on_route(self, index):
		returned_points = self.directions.get_points()
		if index >= len(returned_points):
			print("Error: index out of range!")
			return
		print("Point: %.5f, %.5f" % (returned_points[index][0], returned_points[index][1]))
		return returned_points[index]

	# Print all points on the route
	def print_points(self):
		self.directions.print_info()


# TESTING
# if __name__ == '__main__':
	# truck = Truck("McMaster University, Hamilton, ON", "CN Tower, Toronto, ON")
	# truck.get_point_on_route(0)
	# truck.get_point_on_route(1)
	# truck.get_point_on_route(2)
	# truck.get_point_on_route(3)
	# truck.begin_route()