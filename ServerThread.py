from Truck import Truck
from threading import Timer

class ServerThread: 

	alert = False
	
	def __init__(self, timeLimit, ID, code, startLocation, destination, latitude, longitude):
		self.truck = Truck(ID, code, startLocation, destination, latitude, longitude)
		self.timeLimit = timeLimit
		# call setRoute and API (or in GUI?)

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
			#self.receiveLocation() -- called by server instead
			return True
		else:	
			#self.requestCode() -- called by server instead 
			return False

	def verifyCode(self, inputCode):
		if (inputCode == self.truck.code):
			self.setRoute()
		else:
			self.sendAlert() 

	def sendAlert(self):
		alert = True
		# prompt GUI to notify user if they want to request driver code
		# this.parent.displayAlert
	
	def updateLocation(self):
		return
		# returns current latitude and longitude
		# this.parent.displayLocation
