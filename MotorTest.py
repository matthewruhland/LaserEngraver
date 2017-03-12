import cv2
import PIL
from PIL import Image
import numpy 
import RPi.GPIO as GPIO
import time
import Tkinter, tkFileDialog
import os
import datetime
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.IN) 

#stop shit on button
def StopEverything():
    while GPIO.input(7) == True:
        pass



def PixelBurn(GrayVal):
    seconds = 0.1
    #grayscale darkest to whitest (0 to 255)
    #graycale 1
    if (GrayVal >= 0 and GrayVal < 32): 
      D2A(80)
      LEDTime(seconds)
##    elif (GrayVal
##    elif (GrayVal
##    elif (GrayVal
##    elif (GrayVal
##    elif (GrayVal
##    elif (GrayVal
##    elif (GrayVal
    

def MoveLaserMotor(direction, numberOfHalfSteps):

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT) #direction pin
    GPIO.setup(23,GPIO.OUT) #step pin
    
    if(direction == True):
        GPIO.output(18,GPIO.HIGH) 
    elif(direction == False):
        GPIO.output(18,GPIO.LOW)  
        
    for i in range(numberOfHalfSteps):
        GPIO.output(23,GPIO.HIGH)
        time.sleep(0.0001)
        GPIO.output(23,GPIO.LOW)
        time.sleep(0.0001)

        ##pixelBurn(
        
        if (GPIO.input(7) == True): StopEverything()
        

##for i in range (0,5):
##    MoveLaserMotor(True, 2000)
##    time.sleep(1)
##    MoveLaserMotor(False, 2000)
##    time.sleep(1)

for i in range(0,300):
    MoveLaserMotor(True,30)
    time.sleep(0.1)

GPIO.cleanup()
