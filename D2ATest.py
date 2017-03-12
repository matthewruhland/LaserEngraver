import RPi.GPIO as GPIO
import time

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

def main():
    D2A(4095)
##    D2A(0x047B)
##    time.sleep(1)
##    D2A(0x04AC)
##    time.sleep(1)
##    D2A(0x04DD)
##    time.sleep(1)
##    D2A(0x050E)
##    time.sleep(1)
##    D2A(0x053F)
##    time.sleep(1)

main()
