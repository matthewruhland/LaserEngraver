# Program to take a series of pictures
import os
import datetime
import time
from threading import Thread
def picFunc():
    os.system("fswebcam -r 640x480 --no-banner -save /home/pi/Documents/%s.jpeg" %datetime.datetime.utcnow().strftime("%Y-%m-%d-%H:%M:%S"))
t=5      # initialise the pause between pictures in seconds           
count=10 # initialise the number of pictures to be taken
i=1       # initialise (reset) the counting sequence
totalTime=(t*count) # Calculate the time in seconds
# Take a series of pictures one every t seconds
while (i<=count):
    # initialise variables
    leftTimeH=0
    leftTimeM=0
    leftTimeS=0
    # taking a picture by calling a command line prompt
    x=Thread(target=picFunc)
    x.start()
    totalTime=(t*(count-i))     # Calculate the time in seconds
    print (i)       # print the current count value to show progress
    while (totalTime>=3600):
        leftTimeH=leftTimeH+1
        totalTime=totalTime-3600
    while (totalTime>=60):
        leftTimeM=leftTimeM+1
        totalTime=totalTime-60
    leftTimeS=totalTime
    percentDone=((i/count)*100)
    percentDone=round(percentDone,2)
    message1=("Time left to finish " +repr(leftTimeH) +" Hours " + repr(leftTimeM) +" Minutes and " + repr(leftTimeS) +" Seconds")
    message2=(""+repr(percentDone) + "% Completed!")
    print (message1)
    print (message2)
    i=i+1
    if (i>count):  # leave the loop when count fulfilled (not really necessary)
        break
    time.sleep(t)   # wait the defined time t(s) between pictures
print ("Finished!") # print to show when finished
