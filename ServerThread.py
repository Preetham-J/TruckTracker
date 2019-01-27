from Truck import Truck
from threading import Timer

class ServerThread: 

	alert = False
	
	def __init__(self, timeLimit, ID, code, startLocation, destination, latitude, longitude):
		self.truck = Truck(ID, code, startLocation, destination, latitude, longitude)
		self.timeLimit = timeLimit
		self.setRoute()

	def setRoute(self):
		return
		# instantiate/updates API with startLocation and destination
		# when API returns that it is finished, start receiveLocation and updateLocation()

	def setLatitude(self, latitude):
		self.latitude = latitude

	def setLongitude(self, longitude):
		self.longitude = longitude

	def getTimeLimit(self):
		return self.timeLimit

	def verifyLocation(self):
		# call API instance to check route
		# returns okay or not okay
		check = True #set to return value of API call
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
		alert = True
