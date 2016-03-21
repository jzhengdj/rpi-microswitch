import sys

if(sys.version_info[0]<3):
    from Tkinter import *
else:
    from tkinter import *
    from tkinter import ttk

import time
import RPi.GPIO as GPIO
import libFrame


#use 18 to test microswitch
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def check_button():
    if (GPIO.input(18) == GPIO.LOW):
        #labelText.set("Button Pressed.")
        mstester.changeGreen()
    else:
        #labelText.set("")
        mstester.changeRed()
    root.after(10,check_button)


root = Tk()
root.title("MicroSwitch Tester")
mstester = colorFrame.MicroSwitchTester(root)

# button = Button(root, text="Quit.", fg="red", command=quit)
# button.pack(side=RIGHT, padx=10, pady=10, ipadx=10, ipady=10)

# hi_there = Button(root, text="Light my LED!", command=say_hi)
# hi_there.pack(side=LEFT, padx=10, pady=10, ipadx=10, ipady=10)

# labelText = StringVar()
# labelText.set("Button Pressed.")
# label1 = Label(root, textvariable=labelText, height=4)
# label1.pack(side=LEFT)

# root.title("MicroSwitch Tester")
# root.geometry('500x300+200+200')

root.after(10,check_button)
root.mainloop()
