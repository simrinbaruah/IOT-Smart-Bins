import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)
while True:
    i=GPIO.input(21)
    if(i==True):
        print True
        time.sleep(0.5)
    elif(i==False):
        print False
        time.sleep(0.5)

GPIO.cleanup()
