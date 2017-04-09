import cv2
import PIL
from PIL import Image
import numpy 
import RPi.GPIO as GPIO
import time
import Tkinter, tkFileDialog, tkMessageBox
import os
import datetime
import time
from threading import Thread

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(8,GPIO.OUT)



def LaserOn():
    GPIO.output(8,GPIO.HIGH)

def LaserOff():
    GPIO.output(8,GPIO.LOW)


def ScanImage(filename):
    im = Image.open(filename)
    im_grey = im.convert('LA')
    im_grey.convert('RGB').save("/home/pi/Desktop/gray.jpg")
    im_grey_shrunk = im_grey.resize((10,10))
    im_grey_shrunk.convert('RGB').save("/home/pi/Desktop/grayShrunk.jpg")
    width,height = im_grey_shrunk.size
    print "Pixels ",width,height," "

    #value=[[0 for x in range(0,width+1)] for y in range(0,height+1)]
    value = []
    for i in range(width):
        value.append([])
        for j in range(height):
            value[i].append(im_grey_shrunk.getpixel((i,j))[0])
            printValue = value[i][j]
##            print printValue, " "
    return value


#stop everything when switch is turned off
def StopEverything():
    
    while(GPIO.input(7) == True):
        pass
        print "Engraving Stopped"
        time.sleep(1)

def MoveLaserMotor(direction, numberOfHalfSteps):

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT) #direction pin
    GPIO.setup(23,GPIO.OUT) #step pin
    GPIO.setup(7, GPIO.IN)
    

    if(direction == True):
        GPIO.output(18,GPIO.HIGH) #set direction clockwise
    elif(direction == False):#not sure if this is correct for backwards
        GPIO.output(18,GPIO.LOW)  #set direction counter clockwise
        
    for i in range(numberOfHalfSteps):
        GPIO.output(23,GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(23,GPIO.LOW)
        time.sleep(0.001)
        if (GPIO.input(7) == True): StopEverything()

    GPIO.cleanup()


def StationMotor(direction, numberOfHalfSteps):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(24,GPIO.OUT)#direction pin
    GPIO.setup(25,GPIO.OUT)#step pin
    GPIO.setup(7, GPIO.IN)
    
    if(direction == True):
        GPIO.output(24,GPIO.HIGH) #set direction clockwise
    elif(direction == False):#not sure if this is correct for backwards
        GPIO.output(24,GPIO.LOW)  #set direction counter clockwise
        
    for i in range(numberOfHalfSteps):
        GPIO.output(25,GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(25,GPIO.LOW)
        time.sleep(0.001)
        if (GPIO.input(7) == True): StopEverything()


    GPIO.cleanup()

def set_to_RefPoint(PixelSize):
    for i in range(30):
        StationMotor(True, PixelSize)
        time.sleep(0.01)
        MoveLaserMotor(False, PixelSize)
        time.sleep(0.01)

def LEDTime(seconds):
    GPIO.output(8,GPIO.HIGH)
    time.sleep(seconds)
    #print "LASER off"
    GPIO.output(8,GPIO.LOW)

##def PixelBurn(GrayVal):
    
    #grayscale darkest to whitest (0 to 255)
    #graycale 1
##    if (GrayVal..
##      D2A(0 to 4095)
##      LEDTime(seconds)
##    elif (GrayVal
##    elif (GrayVal
##    elif (GrayVal
##    elif (GrayVal
##    elif (GrayVal
##    elif (GrayVal
##    elif (GrayVal


def D2A(D2AVal):            #0 = highest voltage (~4.8V, theoretically)
                            #4095 = lowest voltage (~3.9V, theoretic)
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(13,GPIO.OUT) #Chip Select (CS) line
    GPIO.setup(19,GPIO.OUT) #CLK line
    GPIO.setup(26,GPIO.OUT) #Data line

    #first 4 bits are 0011 to set up D/A
    D2AVal = D2AVal & 0x0FFF
    D2AVal = D2AVal | 0x3000

    GPIO.output(13,GPIO.HIGH)
    GPIO.output(19,GPIO.HIGH)

    #set CS low to select the D/A chip
    GPIO.output(13,GPIO.LOW)

    #send out data
    for i in range(16):
        if (D2AVal & 0x8000):
            GPIO.output(26,GPIO.HIGH)
        else:
            GPIO.output(26,GPIO.LOW)
        GPIO.output(19,GPIO.LOW)
        D2AVal = D2AVal << 1
        GPIO.output(19,GPIO.HIGH)


    #CS goes high to terminate communication
    GPIO.output(13,GPIO.HIGH)

def EngravePixels(TwodArrayofPixels, OnePixelSize):

    forward = True  
    backward = False
    width = len(TwodArrayofPixels)          #columns?
    height = len(TwodArrayofPixels[0])      #rows?
    print width,height
    for i in range(width - 1):
        if(i%2 == 0):                                     
            for j in range(height):
##                pixelBurn(TwodArrayofPixels[i][j])
                time.sleep(0.1)
                if (j == height-1): break
                MoveLaserMotor(False, OnePixelSize)
        else:
            for j in range(height - 1,-1,-1):
##                pixelBurn(TwodArrayofPixels[i][j])
                time.sleep(0.1)
                if (j == 0): break   #if at end of row,  
                MoveLaserMotor(True, OnePixelSize)
                
        StationMotor(True, OnePixelSize) 
        print "New Row"

##def FinishBurning():
##        result = tkMessageBox.askquestion("done?", "Laser will stop", icon = 'warning')
##    if result == 'yes'
##        print "done"
##    else
##        print "not done"tkMessageBox

################### Where the Magic Happens ####################
#This now takes pictures every row and promps user for a file to use
#count Variables 

def main():
    result = True
    root = Tkinter.Tk()
    root.withdraw()
    while(result):
    	result = False
        file = tkFileDialog.askopenfile( mode ='rb',title='Please select a file')
        
        pixels2DArray = ScanImage(file)
        EngravePixels(pixels2DArray, PixelTestingSize)
        result = tkMessageBox.askyesno("Laser", "Continue Burning?")
        if result:
            result = tkMessageBox.askyesno("Laser", "Is new burning material in place")
        print result
    ##ask to continue window, reset
    #B1 = Tkinter.Button(root, text = "Delete", command = FinishBurning)
    #B1.pack()
    #top.mainloop()

    
    ##reset()
    
PixelTestingSize = 30 #steps of Motor per Pixel
set_to_RefPoint(PixelTestingSize)
main()
