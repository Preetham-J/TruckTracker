from Truck import Truck

#0 Server sends JSON to GUI (which is always listening for new missions)
#1 GUI class instantites new Truck in a new thread, with data from JSON
#2 GUI class adds truck ID to drop down menu to update GUI to this truck
#2.1 GUI passes in default timeLimit and has option to change it
#2.2 default timeLimit globally configurable
class ServerThread: 
	# corresponds to Start
	def __init__(self, timeLimit, ID, startLatitude, startLongitude, destination):
		self.truck = Truck(timeLimit, ID, startLatitude, startLongitude, destination)
		# call setRoute (or in GUI?)

	# corresponds to Start
	def setRoute(self):
		# instantiate/updates API with startLocation and destination
		# when API returns that it is finished, start receiveLocation and updateLocation()

	# corresponds to is data received
	def receiveLocation(self):
		# While loop until data is received
		# once data is received, update gpsData and call verifyLocation

	# corresponds to is correct
	def verifyLocation(self):
		# call API instance to check route
		# returns okay or not okay
		# if okay call receiveLocation (i.e. go back to loop)
		# if not okay call requestCode

	# correspond to send request, while loop, is past time limit, is code recieved
	def requestCode(self):
		# start timer
		# if timer exceeds timeLimit, call sendAlert()
		# otherwise, if code is received before timeLimit, call verifyCode

	# corresponds to is code correct, update route
	def verifyCode(self):
		# if not correct sendAlert()
		# if correct, call setRoute()

	# corresponds to Alert
	def sendAlert(self):
		# prompt GUI to notify user if they want to request driver code
		# this.parent.displayAlert
	# for GUI
	def updateLocation(self):
		# returns current latitude and longitude
		# this.parent.displayLocation
