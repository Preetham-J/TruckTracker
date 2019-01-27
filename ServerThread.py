from Truck import Truck
from directions.directions_analytics import Directions

class ServerThread: 

	alert = False
	
	def __init__(self, timeLimit, ID, code, startLocation, destination, latitude, longitude):
		self.truck = Truck(ID, code, startLocation, destination, latitude, longitude)
		self.timeLimit = timeLimit
		self.setRoute()

	def setRoute(self):
		truck = self.truck

		# destination and startLocation must be of fromat: "McMaster University, Hamilton, ON"
		self.directions = Directions(truck.startLocation, truck.destination)
		# instantiate/updates API with startLocation and destination
		# when API returns that it is finished, start receiveLocation and updateLocation()

	def updateRoute(self):
		truck = self.truck
		self.directions = Directions((truck.latitude, truck.longitude), truck.destination)

	def setLatitude(self, latitude):
		self.truck.latitude = latitude

	def setLongitude(self, longitude):
		self.truck.longitude = longitude

	def getTimeLimit(self):
		return self.timeLimit

	def verifyLocation(self):
		# call API instance to check route
		# returns okay or not okay
		check = self.directions.check_distance(self.truck.latitude, self.truck.longitude) #set to return value of API call
		if (check):
			return True
		else:	
			return False

	def verifyCode(self, inputCode):
		if (inputCode == self.truck.code):
			self.setRoute()
		else:
			self.sendAlert() 

	def sendAlert(self):
		#with open("serverParameters.txt", "w") as f:
		#	f.write(
		alert = True
