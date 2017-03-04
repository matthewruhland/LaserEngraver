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
from threading import Thread


def picFunc():
    filepath1 = '/home/pi/Desktop/PicturesTaken'
    os.system("fswebcam -r 640x480 --no-banner -save /home/pi/Desktop/PicturesTaken/%s.jpeg" %datetime.datetime.utcnow().strftime("%Y-%m-%d-%H:%M:%S"))

#Global Variables


def ScanImage(filename):
    im = Image.open(filename)
    im_grey = im.convert('LA')
    width,height = im_grey.size
    print "Pixels ",width,height," "

    #value=[[0 for x in range(0,width+1)] for y in range(0,height+1)]
    value = []
    for i in range(width):
        value.append([])
        for j in range(height):
            value[i].append(im_grey.getpixel((i,j))[0])
            printValue = value[i][j]
    return value

##    imGRAY = numpy.array(im_grey)
##    fft_mag = numpy.abs(numpy.fft.fftshift(numpy.fft.fft2(im_grey)))
##
##    visual = numpy.log(fft_mag)
import os
import datetime
import time
from threading import Thread
def picFunc():
    os.system("fswebcam -r 640x480 --no-banner -save /home/pi/Desktop/PicturesTaken/%s.jpeg" %datetime.datetime.utcnow().strftime("%Y-%m-%d-%H:%M:%S"))
##    visual = (visual - visual.min()) / (visual.max() - visual.min())
##
##    result = Image.fromarray((visual * 255).astype(numpy.uint8))
##    result.save('/home/pi/Desktop/out.bmp')
##    #im_grey.save('/home/pi/Desktop/out.la')


def MoveLaserMotor(direction, numberOfHalfSteps):

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT) #direction pin
    GPIO.setup(23,GPIO.OUT) #step pin
    
    if(direction == True):
        GPIO.output(18,GPIO.HIGH) #set direction clockwise
        for i in range(numberOfHalfSteps):
            GPIO.output(23,GPIO.HIGH)
            time.sleep(0.0001)
            GPIO.output(23,GPIO.LOW)
            time.sleep(0.0001)
        
    elif(direction == False):#not sure if this is correct for backwards
        GPIO.output(18,GPIO.LOW)  #set direction counter clockwise  
        for i in range(numberOfHalfSteps):
            GPIO.output(23,GPIO.HIGH)
            time.sleep(0.0001)
            GPIO.output(23,GPIO.LOW)
            time.sleep(0.0001)

    GPIO.cleanup()


def StationMotor(direction, numberOfHalfSteps):
    print "test1"
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(24,GPIO.OUT)#direction pin
    GPIO.setup(25,GPIO.OUT)#step pin
    
    if(direction == True):
        GPIO.output(24,GPIO.HIGH) #set direction clockwise
        for i in range(numberOfHalfSteps):
            GPIO.output(25,GPIO.HIGH)
            time.sleep(0.0001)
            GPIO.output(25,GPIO.LOW)
            time.sleep(0.0001)
        
    elif(direction == False):#not sure if this is correct for backwards
        GPIO.output(24,GPIO.LOW)  #set direction counter clockwise  
        for i in range(1600):
            GPIO.output(25,GPIO.HIGH)
            time.sleep(0.0001)
            GPIO.output(25,GPIO.LOW)

    GPIO.cleanup()


def LEDTime(seconds):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    LEDPin = 8 #GPIO number

    GPIO.setup(LEDPin,GPIO.OUT)
    #print "LASER on"
    GPIO.output(LEDPin,GPIO.HIGH)
    time.sleep(seconds)
    #print "LASER off"
    GPIO.output(LEDPin,GPIO.LOW)

def PixelBurn(GrayVal):
    
    #grayscale darkest to whitest (0 to 255)
    #graycale 1
    if (GrayVal ...
        D2a
    elif (
    

def D2A(AnalogValue):

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
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

def EngravePixels(TwodArrayofPixels, OnePixelSize, TimeLaserIsOn):
    forward = True
    #forwards is clockwise
    backward = False
    #backwards is counterclockwise
    width = len(TwodArrayofPixels)
    height = len(TwodArrayofPixels[0])
    for i in range(width):
        for j in range(height):
            printValue = TwodArrayofPixels[i][j]
            MoveLaserMotor(forward, OnePixelSize)
            time =TimeLaserIsOn*(1/printValue)      #???
            pixelBurn(pixels[i][j])
        MoveLaserMotor(backward, height*OnePixelSize) 
        StationMotor(backward, OnePixelSize) 
        print "New Row"
        target = picFunc()

################### Where the Magic Happens ####################
#This now takes pictures every row and promps user for a file to use
def main():
    root = Tkinter.Tk()
    file = tkFileDialog.askopenfile(parent=root, mode ='rb',title='Please select a file')
    ##FILENAME = '/home/pi/Desktop/download.jpg' #/media/pi/C666-B91B/googleimage.jpg'
    pixels2DArray = ScanImage(file)
    LaserOnTimePerPixel = 0.05 #seconds
    PixelTestingSize = 15 #steps of Motor per Pixel
    EngravePixels(pixels2DArray, PixelTestingSize, LaserOnTimePerPixel)

main()
