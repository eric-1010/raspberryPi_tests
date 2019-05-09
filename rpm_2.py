#!/bin/bash

import RPi.GPIO as GPIO
import time



elapse=0
sensor=12 #GPIO.BOARD physical pin #12 
pulse=0
start_timer=round(time.time(),4)


def init_GPIO():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(sensor,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
def calculate_elapse(channel):
    global pulse , start_timer , elapse
    pulse += 1
    elapse = round(time.time() - start_timer,4)
    start_timer = time.time()
    
def init_interrupt():
    GPIO.add_event_detect(sensor,edge=GPIO.FALLING,bouncetime=8,callback=calculate_elapse)
if __name__=='__main__':
    init_GPIO()
    init_interrupt()
    
    
    try:
        while True:
            
            if GPIO.input(sensor)==1 and pulse >= 1:
                print(elapse,'RPM = ',int(1/elapse*60))
                    
                
                
            KeyboardInterrupt()
    finally:
        GPIO.cleanup()

