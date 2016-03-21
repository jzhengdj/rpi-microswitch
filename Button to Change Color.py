from tkinter import *
from tkinter import ttk
import libFrame

# class MicroSwitchTester:
# 	"""A panel to test the status of MicroSwitch"""
# 	def __init__(self, root):

# 		mainframe = ttk.Frame(root, padding="3 3 12 12")

# 		s = ttk.Style()
# 		s.configure("My.TFrame", background = 'green')

# 		frame = ttk.Frame(mainframe, borderwidth=5, relief="sunken", width=200, height=100, style = 'My.TFrame')


# 		#ttk.Label(mainframe, text='meters').grid(column=0, row=0, rowspan = 4, columnspan = 2, sticky=(W, E))
# 		ttk.Button(mainframe, text="Green", command = self.changeGreen).grid(column=1, row=3, sticky=W)
# 		ttk.Button(mainframe, text="Red", command = self.changeRed).grid(column=2, row=3, sticky=W)

# 		mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# 		mainframe.columnconfigure(0, weight=1)
# 		mainframe.rowconfigure(0, weight=1)
# 		frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))

# 	def changeGreen(self):
# 		s = ttk.Style()
# 		s.configure('My.TFrame', background = 'green')
# 	def changeRed(self):
# 		s = ttk.Style()
# 		s.configure('My.TFrame', background = 'red')


root = Tk()
root.title("MicroSwitch Tester")
mstester = libFrame.MicroSwitchTester(root)
root.mainloop()
