import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)
def sms_IR():
    while True:
        i=GPIO.input(21)
        if(i==True):
            return True
            time.sleep(0.5)
        elif(i==False):
            return False
            time.sleep(0.5)
