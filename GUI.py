from tkinter import *

def setSafeLabel():
	alertLabel = Label(text=" SAFE ", height=5, width=15, bg="white").grid(row=0, column=0)  

def readServerParameters():
	with open("serverParameters.txt", "r") as f:
		alertFlag = f.read()
		try:
			if (int(alertFlag)):
				setAlertLabel()
			else:
				setSafeLabel()
		except ValueError:
			pass
	window.after(1000, readServerParameters)			
def setAlertLabel():
	alertLabel = Label(text='ALERT', relief=RIDGE, height=5, width=15, bg="red").grid(row=0, column=0)

window = Tk()
window.title("Controller GUI")

labels = ['Truck ID', 'Start Location', 'Destination', 'Latitude', 'Longitude']

gridRow = 1

setSafeLabel()

alertButton = Button(text='Ignore Alert', relief=SUNKEN, height=4, width=12, command=setSafeLabel).grid(row=0, column=1)

for label in labels:
	Label(text=label, relief=RIDGE, width=15).grid(row=gridRow, column=0)
	Entry(relief=SUNKEN, width=15).grid(row=gridRow, column=1)
	gridRow = gridRow + 1

readServerParameters()

window.mainloop()


