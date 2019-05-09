#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
import RPi.GPIO as GPIO
import time
import os
fan_pin = 40
fan_pwm = None
var=None
GPIO.setmode(GPIO.BOARD)
GPIO.setup(fan_pin,GPIO.OUT)

fan_pwm=GPIO.PWM(fan_pin,12)
fan_pwm.start(0)

root = tk.Tk()
root.configure(bg="gray")
root.title("Color Adjust & Cooling Control")
root.geometry("600x300")


val=tk.IntVar()
radioButtons={0:"Off",1:"min",2:"low",3:"med",4:"high",5:"MAX",6:"AUTO"}

def getCPUtemp():
    cTemp = os.popen( 'vcgencmd measure_temp' ).readline()
    return float(cTemp.replace("temp=","").replace("'C\n",""))
def auto():
    
    var = getCPUtemp()
    if var >= 44.0:
        fan_pwm.start(100)
    
    elif var >= 43.0:
        fan_pwm.start(80)            

    elif var >= 42.0:
        fan_pwm.start(60)
            
    elif var >= 41.0:
        fan_pwm.start(50)
            
    elif var >= 40.0:
        fan_pwm.start(40)
        
    elif var >= 38.0:
        fan_pwm.start(30)
       
    elif var >= 36.0:
        fan_pwm.start(25)
        
    elif var >= 34.0:
        fan_pwm.start(20)
        
    else:
        fan_pwm.stop()
        
        
def change():
    if val.get()==0:        
        fan_pwm.ChangeDutyCycle(0)
    if val.get()==1:        
        fan_pwm.ChangeDutyCycle(20)
    if val.get()==2:        
        fan_pwm.ChangeDutyCycle(40)
    if val.get()==3:        
        fan_pwm.ChangeDutyCycle(60)
    if val.get()==4:        
        fan_pwm.ChangeDutyCycle(80)
    if val.get()==5:        
        fan_pwm.ChangeDutyCycle(100)
    if val.get()==6:
        fan_pwm.stop()
        auto()        
        
for a in radioButtons:
    var = getCPUtemp()
    r=tk.Radiobutton(root,
    highlightbackground="orange",
    bg="gray",
    fg="magenta",
    relief='groove',
    text=radioButtons[a],
    variable=val,
    value=a,
    width=8,command=change)
    
    r.grid(row=a,column=0,sticky='E')
text=getCPUtemp()    
label=tk.Label(root,font="Times 14 italic",text=text)
label.grid(row=2,column=2,columnspan=2)
root.after(10, getCPUtemp) 

root.mainloop()
fan_pwm.stop()
GPIO.cleanup()
