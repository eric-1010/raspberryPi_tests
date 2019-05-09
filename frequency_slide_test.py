import tkinter as tk
import RPi.GPIO as GPIO # imports RPi.GPIO as GPIO

pwm0 = None # Declare global variables
pwm1 = None # Declare global variables
pwm2 = None # Declare global variables
pwm3 = None # Declare global variables
pwm4 = None # Declare global variables


fan_pin = 35 # Pin definitions
redLED_pin = 36 # Pin definitions
whiteLED_pin = 37 # Pin definitions
greenLED_pin = 38 # Pin definitions
blueLED_pin = 40 # Pin definitions

# II This gets called whenever the scale is changed->->change brightness of LED II #
# V                                                                               V #
def speed0(i):
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
def dim4(i):
    global pwm4
    # Change the Duty Cycle based on the slider value
    pwm4.ChangeDutyCycle(float(i))
def freq0(i):
    global pwm0
    # Change the Duty Cycle based on the slider value
    pwm0.ChangeFrequency(float(i))
def freq1(i):
    global pwm1
    # Change the Duty Cycle based on the slider value
    pwm1.ChangeFrequency(float(i))
def freq2(i):
    global pwm2
    # Change the Duty Cycle based on the slider value
    pwm2.ChangeFrequency(float(i))
def freq3(i):
    global pwm3
    # Change the Duty Cycle based on the slider value
    pwm3.ChangeFrequency(float(i))
def freq4(i):
    global pwm4
    # Change the Duty Cycle based on the slider value
    pwm4.ChangeFrequency(float(i))

    


# Using " GPIO.BOARD " pin numbering #
GPIO.setmode(GPIO.BOARD)
# set LED pin as output #
GPIO.setup(fan_pin, GPIO.OUT)
GPIO.setup(redLED_pin, GPIO.OUT)
GPIO.setup(greenLED_pin, GPIO.OUT)
GPIO.setup(blueLED_pin, GPIO.OUT)
GPIO.setup(whiteLED_pin, GPIO.OUT)

# Initialize pwm object with (#)Hz and 0% Duty Cycle #
pwm0 = GPIO.PWM(fan_pin, 1)
pwm1 = GPIO.PWM(redLED_pin, 1)
pwm2 = GPIO.PWM(greenLED_pin, 1)
pwm3 = GPIO.PWM(blueLED_pin, 1)
pwm4 = GPIO.PWM(whiteLED_pin, 1)

pwm0.start(0)
pwm1.start(0)
pwm2.start(0)
pwm3.start(0)
pwm4.start(0)

 # the main GUI window --> all the widgets are conained in the root
root = tk.Tk()
#root.get_themes()
#root.set_theme("clearlooks")
root.title('Frequency Control') # Title given to the root
root.configure(background='black')
root.geometry('800x800')

#titleLabel = tk.Label(root, text = "Frequency Control", fg='yellow', bg='black', font="Times 24 italic underline bold")
#titleLabel.grid(row=1, column=1, columnspan=2)

ledcolorLabel = tk.Label(root, text="Fan Hz", fg='yellow', bg='black', font="Verdana 12 bold")
ledcolorLabel.grid(row=3, column=1, sticky="E")

ledcolorLabel = tk.Label(root, text="Fan DC", fg='yellow', bg='black', font="Verdana 12 bold")
ledcolorLabel.grid(row=4, column=1, sticky="E")

ledcolorLabel = tk.Label(root, text="Red L.E.D. Hz", fg='red', bg='black', font="Verdana 12 bold")
ledcolorLabel.grid(row=5, column=1, sticky="E")

ledcolorLabel = tk.Label(root, text="Red L.E.D. DC", fg='red', bg='black', font="Verdana 12 bold")
ledcolorLabel.grid(row=6, column=1, sticky="E")

ledcolorLabel = tk.Label(root, text="Green L.E.D. Hz", fg='green', bg='black', font="Verdana 12 bold")
ledcolorLabel.grid(row=7, column=1, sticky="E")

ledcolorLabel = tk.Label(root, text="Green L.E.D. DC", fg='green', bg='black', font="Verdana 12 bold")
ledcolorLabel.grid(row=8, column=1, sticky="E")

ledcolorLabel = tk.Label(root, text="Blue L.E.D. Hz", fg='blue', bg='black', font="Verdana 12 bold")
ledcolorLabel.grid(row=9, column=1, sticky="E")

ledcolorLabel = tk.Label(root, text="Blue L.E.D. DC", fg='blue', bg='black', font="Verdana 12 bold")
ledcolorLabel.grid(row=10, column=1, sticky="E")

ledcolorLabel = tk.Label(root, text="White L.E.D. Hz", fg='white', bg='black', font="Verdana 12 bold")
ledcolorLabel.grid(row=11, column=1, sticky="E")

ledcolorLabel = tk.Label(root, text="White L.E.D. DC", fg='white', bg='black', font="Verdana 12 bold")
ledcolorLabel.grid(row=12, column=1, sticky="E")

ledcolorScale = tk.Scale(root, bd=3, relief=tk.GROOVE, orient=tk.HORIZONTAL, fg='yellow', bg='black', from_=1.0, to=1000.0, repeatdelay=150, resolution=.25, troughcolor='yellow', tickinterval=101, length=1000, width=5, sliderlength=100, showvalue=True, command=freq0)
ledcolorScale.grid(row=3, column=2, sticky="W")

ledcolorScale = tk.Scale(root, bd=3, relief=tk.GROOVE, orient=tk.HORIZONTAL, fg='yellow', bg='black', from_=0.0, to=100.0, repeatdelay=200, resolution=10, troughcolor='yellow', tickinterval=10, length=500, width=5, sliderlength=100, showvalue=True, command=speed0)
ledcolorScale.grid(row=4, column=2, sticky="W")

ledcolorScale = tk.Scale(root, bd=3, relief=tk.GROOVE, orient=tk.HORIZONTAL, fg='red', bg='black', from_=1.0, to=1000.0, repeatdelay=150, resolution=.25, troughcolor='red', tickinterval=101, length=1000, width=5, sliderlength=100, showvalue=True, command=freq1)
ledcolorScale.grid(row=5, column=2, sticky="W")

ledcolorScale = tk.Scale(root, bd=3, relief=tk.GROOVE, orient=tk.HORIZONTAL, fg='red', bg='black', from_=0.0, to=100.0, repeatdelay=200, resolution=.25, troughcolor='red', tickinterval=10, length=500, width=5, sliderlength=100, showvalue=True, command=dim1)
ledcolorScale.grid(row=6, column=2, sticky="W")

ledcolorScale = tk.Scale(root, bd=3, relief=tk.GROOVE, orient=tk.HORIZONTAL, fg='green', bg='black', from_=1.0, to=1000.0, repeatdelay=150, resolution=.25, troughcolor='green', tickinterval=101, length=1000, width=5, sliderlength=100, showvalue=True, command=freq2)
ledcolorScale.grid(row=7, column=2, sticky="W")

ledcolorScale = tk.Scale(root, bd=3, relief=tk.GROOVE, orient=tk.HORIZONTAL, fg='green', bg='black', from_=0.0, to=100.0, repeatdelay=200, resolution=.25, troughcolor='green', tickinterval=10, length=500, width=5, sliderlength=100, showvalue=True, command=dim2)
ledcolorScale.grid(row=8, column=2, sticky="W")

ledcolorScale = tk.Scale(root, bd=3, relief=tk.GROOVE, orient=tk.HORIZONTAL, fg='blue', bg='black', from_=1.0, to=1000.0, repeatdelay=150, resolution=.25, troughcolor='blue', tickinterval=101, length=1000, width=5, sliderlength=100, showvalue=True, command=freq3)
ledcolorScale.grid(row=9, column=2, sticky="W")

ledcolorScale = tk.Scale(root, bd=3, relief=tk.GROOVE, orient=tk.HORIZONTAL, fg='blue', bg='black', from_=0.0, to=100.0, repeatdelay=200, resolution=.25, troughcolor='blue', tickinterval=10, length=500, width=5, sliderlength=100, showvalue=True, command=dim3)
ledcolorScale.grid(row=10, column=2, sticky="W")

ledcolorScale = tk.Scale(root, bd=3, relief=tk.GROOVE, orient=tk.HORIZONTAL, fg='white', bg='black', from_=1.0, to=1000.0, repeatdelay=150, resolution=.25, troughcolor='white', tickinterval=101, length=1000, width=5, sliderlength=100, showvalue=True, command=freq4)
ledcolorScale.grid(row=11, column=2, sticky="W")

ledcolorScale = tk.Scale(root, bd=3, relief=tk.GROOVE, orient=tk.HORIZONTAL, fg='white', bg='black', from_=0.0, to=100.0, repeatdelay=200, resolution=.25, troughcolor='white', tickinterval=10, length=500, width=5, sliderlength=100, showvalue=True, command=dim4)
ledcolorScale.grid(row=12, column=2, sticky="W")

root.mainloop()
# Stop, cleanup, and exit when window is closed #
pwm0.stop()
pwm1.stop()
pwm2.stop()
pwm3.stop()
pwm4.stop()

GPIO.cleanup()
