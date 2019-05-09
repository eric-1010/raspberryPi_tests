#!/usr/bin/env python3
try:
    import os
    import RPi.GPIO as GPIO
    import tkinter as tk 
except ImportError:
    import Tkinter as tk
# setup GPIO
fan_pwm = None
fan_pin = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(fan_pin,GPIO.OUT)
# Initialize pwm object ### GPIO mode set to PWM --> (GPIO pin number,frequency in Hz) #
fan_pwm = GPIO.PWM(fan_pin, 12)
# initial PWM DutyCycle (value=0-100) #
fan_pwm.start(0)
# Return CPU temperature as float
def getCPUtemp():
    cTemp = os.popen( 'vcgencmd measure_temp' ).readline()
    return float(cTemp.replace("temp=","").replace("'C\n",""))

def btn_off():
    fan_pwm.stop()
def btn_min():
    fan_pwm.start(20)
def btn_low():
    fan_pwm.start(40)
def btn_med():
    fan_pwm.start(60)
def btn_high():
    fan_pwm.start(80)
def btn_max():
    fan_pwm.start(100)

class Temp:
    def __init__(self, parent):
        # label displaying text in self.tempNamelabel
        self.tempNamelabel = tk.Label(parent,text="CPU Temp is", font="default 30", bg="cyan", width=10)
        self.tempNamelabel.grid(row=2,column=0,columnspan=3)
        # label displaying text in  self.tempDisplaylabel
        self.tempDisplaylabel = tk.Label(parent,text=getCPUtemp(), font="default 30", width=5)
        self.tempDisplaylabel.grid(row=2,column=3, columnspan=2)        
        # button to quit
        self.exitButton = tk.Button(parent, text="EXIT",command=parent.destroy)
        self.exitButton.grid(row=0, column=3) 
        # manual fan speed selection
        self.offButton = tk.Button(parent, text="OFF",bg="light blue",width=5,command=btn_off)
        self.offButton.grid(row=1, column=0)
        self.minButton = tk.Button(parent, text="MIN",bg="light blue",width=5,command=btn_min)
        self.minButton.grid(row=1, column=1)
        self.lowButton = tk.Button(parent, text="LOW",bg="light blue",width=5,command=btn_low)
        self.lowButton.grid(row=1, column=2)
        self.medButton = tk.Button(parent, text="MED",bg="light blue",width=5,command=btn_med)
        self.medButton.grid(row=1, column=3)
        self.highButton = tk.Button(parent, text="HIGH",bg="light blue",width=5,command=btn_high)
        self.highButton.grid(row=1, column=4)
        self.maxButton = tk.Button(parent, text="MAX",bg="light blue",width=5,command=btn_max)
        self.maxButton.grid(row=1, column=5)
        self.tempDisplaylabel.after(5000, self.refresh_label)
        if getCPUtemp()>=42.0:
            self.tempDisplaylabel.configure(bg="red")
        elif getCPUtemp()>=40.0:
            self.tempDisplaylabel.configure(bg="orange")
        elif getCPUtemp()>=36.0:
            self.tempDisplaylabel.configure(bg="yellow")
        elif getCPUtemp()>=31.1:
            self.tempDisplaylabel.configure(bg="green")
        elif getCPUtemp()<=31.0:
            self.tempDisplaylabel.configure(bg="blue")
    def refresh_label(self):
        """ refresh the content of the label every x second(s) """        
        # display the new temp
        self.tempDisplaylabel.configure(text=getCPUtemp())
        # request tkinter to call self.refresh after #s (the delay is given in ms)
        self.tempDisplaylabel.after(5000, self.refresh_label)
        if getCPUtemp()>=42.0:
            self.tempDisplaylabel.configure(bg="red")
            #fan_pwm.start(100)
        elif getCPUtemp()>=40.0:
            self.tempDisplaylabel.configure(bg="orange")
            #fan_pwm.start(75)
        elif getCPUtemp()>=36.0:
            self.tempDisplaylabel.configure(bg="yellow")
            #fan_pwm.start(40)
        elif getCPUtemp()>=31.1:
            self.tempDisplaylabel.configure(bg="green")
            #fan_pwm.start(25)
        elif getCPUtemp()<=31.0:
            self.tempDisplaylabel.configure(bg="blue")
            #fan_pwm.stop()        
        
if __name__ == "__main__":
    root = tk.Tk()
    temp = Temp(root)
    root.mainloop()
