import cv2
import PIL
from PIL import Image
import RPi.GPIO as GPIO
import time


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
##    visual = (visual - visual.min()) / (visual.max() - visual.min())
##
##    result = Image.fromarray((visual * 255).astype(numpy.uint8))
##    result.save('/home/pi/Desktop/out.bmp')
##    #im_grey.save('/home/pi/Desktop/out.la')


def MoveMotor1(direction, numberOfHalfSteps):

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(23,GPIO.OUT) #direction pin
    GPIO.setup(18,GPIO.OUT) #step pin
    
    if(direction == True):
        GPIO.output(23,GPIO.HIGH) #set direction clockwise
        for i in range(numberOfHalfSteps):
            GPIO.output(18,GPIO.HIGH)
            time.sleep(0.0001)
            GPIO.output(18,GPIO.LOW)
            time.sleep(0.0001)
        
    elif(direction == False):#not sure if this is correct for backwards
        GPIO.output(23,GPIO.LOW)  #set direction counter clockwise  
        for i in range(numberOfHalfSteps):
            GPIO.output(18,GPIO.HIGH)
            time.sleep(0.0001)
            GPIO.output(18,GPIO.LOW)
            time.sleep(0.0001)

    GPIO.cleanup()


def MoveMotor2(direction, numberOfHalfSteps):
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
            MoveMotor1(forward, OnePixelSize)
            time =TimeLaserIsOn*(1/printValue)
            LEDTime(time)
        MoveMotor1(backward, height*OnePixelSize) 
        MoveMotor2(backward, OnePixelSize) 
        print "New Row"
        

################### Where the Magic Happens ####################

def main():
    FILENAME = '/home/pi/Desktop/download.jpg' #/media/pi/C666-B91B/googleimage.jpg'
    pixels2DArray = ScanImage(FILENAME)
    LaserOnTimePerPixel = 0.05 #seconds
    PixelTestingSize = 15 #steps of Motor per Pixel
    EngravePixels(pixels2DArray, PixelTestingSize, LaserOnTimePerPixel)

#MoveMotor1(True,1600)      
main()
