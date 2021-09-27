# rpi-microswitch
MicroSwitch Testing using RPi2, using tkinter GUI and RPi2 GPIO.


Show Green when MicroSwitch is in Close position.
Show Red when MicroSwitch is open.


```
'rc.local' is to autostart 'scripts' at boot screen.(Not applicable in this case)
For 'GUI applications', need to edit 'autostart' file.
Rpi keyboard layout need to change to display '@' symbol
```

Step0:
```
sudo apt-get install unzip
```

Step1: create 'scripts' folder under '/home/pi/', copy the 'mswitch-tester' folder into '/home/pi/scripts'

Step2: change keyboard layout, (to input @ symbol)

```
sudo nano /etc/default/keyboard
```
look for `XKBLAYOUT="gb"`,

replace "gb" with "us", then reboot.


Step3: edit the autostart list
```
sudo nano /home/pi/.config/lxsession/LXDE-pi/autostart
```
add
```
@/usr/bin/python3 /home/pi/scripts/mswitch-tester/SwitchTester.py
```
before @screensaver

I am editing the README file. Adding some more details about the project description.
