import RPi.GPIO as GPIO
import time
def load_value():
    DT=5
    SCK=6

    sample=0
    val=0

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SCK, GPIO.OUT)

    def readCount():
        i=0
        Count=0
        GPIO.setup(DT, GPIO.OUT)
        GPIO.output(DT, 1)
        GPIO.output(SCK, 0)
        GPIO.setup(DT, GPIO.IN)

        while GPIO.input(DT) == 1:
            i=0
        for i in range(24):
            GPIO.output(SCK, 1)
            Count=Count<<1

            GPIO.output(SCK, 0)
            time.sleep(0.001)
            if GPIO.input(DT)==0:
                Count = Count+1

        GPIO.output(SCK,1)
        Count=Count^0x800000
        time.sleep(0.001)
        GPIO.output(SCK, 0)
        return Count

    sample=readCount()
    #while 1:
    count = readCount()
    w=0
    w=(sample-count)/106
    return w
    
