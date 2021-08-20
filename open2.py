import servo_front2
import temp2
import sys
import fbase
from firebase import firebase
import time
import send_sms
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN)
GPIO.setup(21, GPIO.IN)
StepPins = [4,17,27,22]
for pin in StepPins:
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
while True:
    i=GPIO.input(21)
    time.sleep(3)
    if(i==0):
        send_sms.sms()
        sys.exit(0)
    elif(i==1):
        i=GPIO.input(14)
        if(i==0):
            print "Searching for input"
            time.sleep(1)
        if(i==1):
            print "Input sensed"
            break
servo_front2.front()
fbase.post_value()
temp2.close()
GPIO.cleanup()
