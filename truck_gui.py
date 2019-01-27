import tkinter as tk 
from tkinter import ttk
LARGE_FONT= ("Verdana", 12)
class mainframe(tk.Tk):
	def __init__(self, *args, **kwargs):
		
		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand = True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		frame = StartPage(container, self)


		self.frames = {}
		self.frames[StartPage] = frame
		frame.grid(row=0, column=0, sticky="nsew")
		self.show_frame(StartPage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)

		labelvar = tk.StringVar()
		labelvar.set("No Signal Received") 
		def update_signal():
			with open("get_code.txt","r") as f:
				items = f.read()
				try:
					items = int(items)
					if not items:
						labelvar.set("No Signal Received")
					else:
						labelvar.set("Warning, Signal Received")
				except ValueError:
					pass

			parent.after(1000, update_signal)

		label = tk.Label(self, textvar=labelvar, font=LARGE_FONT)
		label.pack()

		numvar = tk.StringVar()
		numvar.set("")

		number_disp = tk.StringVar()
		number_disp.set("")

		label = tk.Label(self, textvar=number_disp, font=LARGE_FONT)
		label.pack()
		
		def add_to_var(num):
			numvar.set("%s%d"%(numvar.get(),num))
			number_disp.set("%s*"%(number_disp.get()))

		for i in range(1,10):
			button = ttk.Button(self, text="%d"%i, command=lambda i=i: add_to_var(i))
			button.pack()

		def del_from_var():
			if numvar.get() == "":
				return
			numvar.set("%s"%numvar.get()[1:])
			number_disp.set("%s"%number_disp.get()[1:])

		button = ttk.Button(self, text="delete", command=lambda: del_from_var())
		button.pack()

		def save_code():
			with open("code.txt", "w") as f:
				f.write(numvar.get())

		button = ttk.Button(self, text="send code", command=lambda: save_code())
		button.pack()

		update_signal()

if __name__ == "__main__":
	app = mainframe()
	app.mainloop()