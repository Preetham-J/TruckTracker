from Truck import Truck
from Thread import Timer

class ServerThread: 
	
	def __init__(self, timeLimit, ID, code, startLocation, destination, latitude, longitude):
		self.truck = Truck(ID, code, startLocation, destination, latitude, longitude)
		self.timeLimit = timeLimit
		# call setRoute and API (or in GUI?)

	def setRoute(self):
		return
		# instantiate/updates API with startLocation and destination
		# when API returns that it is finished, start receiveLocation and updateLocation()

	def receiveLocation(self, latitude, longitude):
		while True:
			if (latitude and longitude):
				#call update location
				self.verifyLocation(latitude, longitude)
				
# While loop until data is received
		# once data is received, update gpsData and call verifyLocation

	def verifyLocation(self, latitude, longitude):
		# call API instance to check route
		# returns okay or not okay
		check = True #set to return value of API call
		if (check):
			self.receiveLocation()
		else:	
			self.requestCode()

	# correspond to send request, while loop, is past time limit, is code recieved
	def requestCode(self):
		timer = Timer(self.timeLimit, self.sendAlert) #start timer
		bFlag = True
		while (bFlag):
			bFlag = self.receiveCode(timer, code)	
		self.verifyCode(code)

	def receiveCode(self, timer, code):
		if (code):
			timer.cancel()
			print("code received.")
			#self.verifyCode(code)
			return False 
		else:
			return True
			
	# corresponds to is code correct, update route
	def verifyCode(self, code):
		if (code == self.truck.code):
			self.setRoute()
		else:
			self.sendAlert() 	

	# corresponds to Alert
	def sendAlert(self):
		# prompt GUI to notify user if they want to request driver code
		# this.parent.displayAlert
	# for GUI
	def updateLocation(self):
		return
		# returns current latitude and longitude
		# this.parent.displayLocation
