import sys
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
StepPins = [4,17,27,22]
for pin in StepPins:
  print "Setup pins"
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)

Seq = [[1,0,0,1],
       [1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1]]
       
StepCount = len(Seq)
StepDir = 1
WaitTime = 0.001
stop_time = time.time() + 2
StepCounter = 0
while time.time() < stop_time:
    print StepCounter,
    print Seq[StepCounter]

    for pin in range(0, 4):
        xpin = StepPins[pin]
        if Seq[StepCounter][pin]!=0:
            print " Enable GPIO %i" %(xpin)
            GPIO.output(xpin, True)
        else:
            GPIO.output(xpin, False)

    StepCounter += StepDir
  
    if (StepCounter >= StepCount):
        StepCounter = 0
    if (StepCounter <0):
        StepCounter = StepCount + StepDir
    time.sleep(WaitTime)

