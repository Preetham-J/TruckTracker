from Truck import Truck
from directions.directions_analytics import Directions
import json
from GUI import GUI


class ServerThread: 

	alert = False

#	serverParameters = {
#		"Alert":'0'
#		"Truck ID":'0'
#		"Start Location":'0'
#		"Destination":'0'
#		"Latitude":'0'
#		"Longitude":'0'
#	}	

	
	def __init__(self, timeLimit, ID, code, startLocation, destination, latitude, longitude):
		self.truck = Truck(ID, code, startLocation, destination, latitude, longitude)
		self.timeLimit = timeLimit
		self.setRoute([ID, startLocation, destination, latitude, longitude])
		self.GUI = GUI([ID, startLocation, destination, latitude, longitude])

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
		print("input code is " + str(inputCode) + " truck code is " + str(self.truck.code))
		if int(inputCode) == int(self.truck.code):
			self.setRoute()
		else:
			self.sendAlert() 

	def sendAlert(self):
		alert = True
		self.GUI.updateGUI(alert)
