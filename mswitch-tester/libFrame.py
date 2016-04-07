from tkinter import *
from tkinter import ttk

w = 180
h = 300

class MicroSwitchTester:
    """A panel to test the status of MicroSwitch"""
    def __init__(self, root):

        mainframe = ttk.Frame(root, padding="3 3 12 12")

        s = ttk.Style()
        s.configure("My.TFrame", background = 'green')
        s.configure("My.TLabel", background = 'green')

        frame = ttk.Frame(mainframe, borderwidth=5, width=w, height=h, style = 'My.TFrame')
        ttk.Label(mainframe, text='MicroSwitch', font = "Verdana 18 bold italic", style = 'My.TLabel').grid(column=0, row=0, columnspan=3, rowspan=4, sticky = W)
        #c.create_text(text = 'test')
        # ttk.Button(mainframe, text="Green", command = self.changeGreen).grid(column=1, row=3, sticky=W)
        # ttk.Button(mainframe, text="Red", command = self.changeRed).grid(column=2, row=3, sticky=W)

        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        frame.grid(column=0, row=0, columnspan=3, rowspan=4, sticky=(N, S, E, W))
    #    c.grid(column=0, row=1, sticky = (W, N))

        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)


    def changeGreen(self):
        s = ttk.Style()
        s.configure('My.TFrame', background = 'green')
        s.configure("My.TLabel", background = 'green')
    def changeRed(self):
        s = ttk.Style()
        s.configure('My.TFrame', background = 'red')
        s.configure("My.TLabel", background = 'red')

    def geometryPoint(self, ws, hs):

        # get screen width and height
        #root = Tk()
        # ws = root.winfo_screenwidth() # width of the screen
        # hs = root.winfo_screenheight() # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = 0
        y = (hs*9/10) - (h)

        # set the dimensions of the screen
        # and where it is placed
        #root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        return (w, h, x, y)
