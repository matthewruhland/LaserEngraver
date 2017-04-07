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
GPIO.setwarnings(False)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(7, GPIO.IN)

def LaserOn():
    GPIO.output(8,GPIO.HIGH)

def LaserOff():
    GPIO.output(8,GPIO.LOW)

#stop shit on button
def StopEverything():
    while GPIO.input(7) == True:
        print("off")
        time.sleep(1)

def D2A(AnalogValue):

    GPIO.setup(13,GPIO.OUT) #Chip Select (CS) line
    GPIO.setup(19,GPIO.OUT) #CLK line
    GPIO.setup(26,GPIO.OUT) #Data line

    #first 4 bits are 0011 to set up D/A
    AnalogValue = AnalogValue & 0x0FFF
    AnalogValue = AnalogValue | 0x3000

    GPIO.output(13,GPIO.HIGH)
    GPIO.output(19,GPIO.HIGH)

    #set CS low to select the D/A chip
    GPIO.output(13,GPIO.LOW)

    #send out data
    for i in range(16):
        if (AnalogValue & 0x8000):
            GPIO.output(26,GPIO.HIGH)
        else:
            GPIO.output(26,GPIO.LOW)
        GPIO.output(19,GPIO.LOW)
        AnalogValue = AnalogValue << 1
        GPIO.output(19,GPIO.HIGH)

    #CS goes high to terminate communication
    GPIO.output(13,GPIO.HIGH)

def LEDTime(seconds):
    LEDPin = 8 #GPIO number
    
    #print "LASER on"
    GPIO.output(LEDPin,GPIO.HIGH)
    time.sleep(seconds)
    #print "LASER off"
    GPIO.output(LEDPin,GPIO.LOW)

def PixelBurn(GrayVal):
    seconds = 0.1
    #grayscale darkest to whitest (0 to 255)
    #graycale 1
    if (GrayVal >= 0 and GrayVal < 32): 
        print("not something")
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

    GPIO.setup(18,GPIO.OUT) #direction pin
    GPIO.setup(23,GPIO.OUT) #step pin
    
    if(direction == True):
        GPIO.output(18,GPIO.HIGH) 
    elif(direction == False):
        GPIO.output(18,GPIO.LOW)  
        
    for i in range(numberOfHalfSteps):
        GPIO.output(23,GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(23,GPIO.LOW)
        time.sleep(0.001)
        ##pixelBurn(
        if (GPIO.input(7) == True): StopEverything()


def StationMotor(direction, numberOfHalfSteps):
    
    GPIO.setup(24,GPIO.OUT)#direction pin
    GPIO.setup(25,GPIO.OUT)#step pin
    
    if(direction == True):
        GPIO.output(24,GPIO.HIGH) #set direction clockwise
    elif(direction == False):#not sure if this is correct for backwards
        GPIO.output(24,GPIO.LOW)  #set direction counter clockwise
        
    for i in range(numberOfHalfSteps):
        GPIO.output(25,GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(25,GPIO.LOW)


##for i in range (0,5):
##    MoveLaserMotor(True, 2000)
##    time.sleep(1)
##    MoveLaserMotor(False, 2000)
##    time.sleep(1)

    
##pixelSize = 20
##D2Aintensity = 0
##for i in range(7):
##    MoveLaserMotor(False,pixelSize)

##for i in range(750):
##    MoveLaserMotor(True,pixelSize)

LaserOn()
D2A(4000)





