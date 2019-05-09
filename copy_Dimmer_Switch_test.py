##### >>> Python GUI Guide: Introduction to Tkinter - learn.sparkfun.com <<< #####
import Tkinter as tk   # imports Tkinter
import RPi.GPIO as GPIO # imports RPi.GPIO as GPIO
pwm0 = None # Declare global variables
pwm1 = None # Declare global variables
pwm2 = None # Declare global variables
pwm3 = None # Declare global variables
fan_pin = 37 # Pin definitions
redled_pin = 36 # Pin definitions
greenled_pin = 38 # Pin definitions
blueled_pin = 40 # Pin definitions
# II This gets called whenever the scale is changed->->change brightness of LED II #
# V                                                                               V #
def dim0(i):
    global pwm0
    # Change the Duty Cycle based on the slider value
    pwm0.ChangeDutyCycle(float(i))
def dim1(i):
    global pwm1
    # Change the Duty Cycle based on the slider value
    pwm1.ChangeDutyCycle(float(i))
def dim2(i):
    global pwm2
    # Change the Duty Cycle based on the slider value
    pwm2.ChangeDutyCycle(float(i))
def dim3(i):
    global pwm3
    # Change the Duty Cycle based on the slider value
    pwm3.ChangeDutyCycle(float(i))
# Using " GPIO.BOARD " pin numbering #
GPIO.setmode(GPIO.BOARD)
# set LED pin as output #
GPIO.setup(fan_pin, GPIO.OUT)
GPIO.setup(redled_pin, GPIO.OUT)
GPIO.setup(greenled_pin, GPIO.OUT)
GPIO.setup(blueled_pin, GPIO.OUT)
# Initialize pwm object with (#)Hz and 0% Duty Cycle #
pwm0 = GPIO.PWM(fan_pin, 72)
pwm1 = GPIO.PWM(redled_pin, 75)
pwm2 = GPIO.PWM(greenled_pin, 750)
pwm3 = GPIO.PWM(blueled_pin, 60)
pwm0.start(0)
pwm1.start(0)
pwm2.start(0)
pwm3.start(0)
# Create the main window and set initial size #
root = tk.Tk()
root.title( "LED Dimmer" )
root.geometry("150x300")
# Create the main container #
frame0 = tk.Frame(root)
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)
# Lay out the main container (centers it in the window) #
frame0.place(relx=0.25, rely=0.5, anchor=tk.CENTER)
frame1.place(relx=0.45, rely=0.5, anchor=tk.CENTER)
frame2.place(relx=0.65, rely=0.5, anchor=tk.CENTER)
frame3.place(relx=0.85, rely=0.5, anchor=tk.CENTER)
# Create a scale widget #
scale = tk.Scale( frame0, orient=tk.VERTICAL, from_=0, to=100, length=200, width=20, sliderlength=50, showvalue=True, command=dim0 )
# Lay out widget in frame #
scale.pack()
# Create a scale widget #
scale = tk.Scale( frame1, orient=tk.VERTICAL, from_=0, to=100, length=200, width=20, sliderlength=50, showvalue=True, command=dim1 )
# Lay out widget in frame #
scale.pack()
# Create a scale widget #
scale = tk.Scale( frame2, orient=tk.VERTICAL, from_=0, to=100, length=200, width=20, sliderlength=50, showvalue=True, command=dim2 )
# Lay out widget in frame #
scale.pack()
# Create a scale widget #
scale = tk.Scale( frame3, orient=tk.VERTICAL, from_=0, to=100, length=200, width=20, sliderlength=50, showvalue=True, command=dim3 )
# Lay out widget in frame #
scale.pack()
# Run Loop #
root.mainloop()
# Stop, cleanup, and exit when window is closed #
pwm0.stop()
pwm1.stop()
pwm2.stop()
pwm3.stop()
GPIO.cleanup()
