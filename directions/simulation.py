from directions_analytics import Directions
from truck_simulator import Truck
import time

# Main
def main():
	directions = Directions("McMaster University, Hamilton, ON", "CN Tower, Toronto, ON")

	# Correct route (should pass)
	truck = Truck("McMaster University, Hamilton, ON", "CN Tower, Toronto, ON")
	# Incorrect route (should fail)
	# truck = Truck("McMaster University, Hamilton, ON", "Celebration Square, Mississauga, ON")

	print("Starting route...")
	start_time = time.time()
	# Get total points on the route to prevent bound errors
	route_length = truck.get_route_length()
	route_index = 0
	# Iterate through the points on the route (5 sec intervals as per Canada Cartage specs)
	while route_index < route_length:
		current_position = truck.get_point_on_route(route_index)
		valid_point = directions.check_distance(current_position[0], current_position[1])
		if (valid_point):
			print("Truck is on valid route.")
		else:
			print("Warning! The truck has deviated from the assigned route!")
			return
		route_index+=1
		# Canada Cartage time frame = 5 seconds
		# Lower to 0.0001 for faster simulation
		time.sleep(0.0001)
	route_index = 0
	print("Route completed!")

if __name__ == '__main__':
	main()