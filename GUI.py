from tkinter import *
from threading import Thread

class GUI:

	def __init__(self, values):
		self.thread = Thread(target=self.createGUI, args=values)
		self.thread.start()

	def createGUI(self, values):
		window = Tk()
		window.title("Controller GUI")
		labels = ['Truck ID', 'Code', 'Start Location', 'Destination']
		total_labels = dict(zip(labels, values))
		gridRow = 1
		self.setSafeLabel()
		alertButton = Button(text='Ignore Alert', relief=SUNKEN, height=4, width=12, command=self.setSafeLabel).grid(row=0, column=1)
		#self.text_values = {}
		for label in labels:
			value = total_labels[label]
			Label(text=label, relief=RIDGE, width=15).grid(row=gridRow, column=0)
			text = Text(relief=SUNKEN, width=15).grid(row=gridRow, column=1)
			#self.text_values[label] = text
			text.insert(1.0, value)
			gridRow = gridRow + 1
		window.mainloop()

	def updateGUI(self, values):
		labels = ['Truck ID', 'Start Location', 'Destination', 'Latitude', 'Longitude']
		total_labels = dict(zip(labels, values))
		for label in labels:
			value = total_labels[label]
			text = self.text_values[label]
			text.insert(1.0,value)
			
	def alertGUI(self, alert):
		try:
			if (int(alert)):
				self.setAlertLabel()
			else:
				self.setSafeLabel()
		except ValueError:
			pass

	def setSafeLabel(self):
		alertLabel = Label(text=" SAFE ", height=5, width=15, bg="white").grid(row=0, column=0)  

	'''def readServerParameters(self):
		with open("serverParameters.txt", "r") as f:
			alertFlag = f.read()
			try:
				if (int(alertFlag)):
					setAlertLabel()
				else:
					setSafeLabel()
			except ValueError:
				pass
		window.after(1000, readServerParameters)'''		

	def setAlertLabel(self):
		alertLabel = Label(text='ALERT', relief=RIDGE, height=5, width=15, bg="red").grid(row=0, column=0)




