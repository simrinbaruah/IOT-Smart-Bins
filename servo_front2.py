import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
def front():
    p = GPIO.PWM(18, 50)
    p.start(7.5)

    stop_time = time.time() + 0.01
    while time.time() < stop_time:
        p.ChangeDutyCycle(12.5)
        #p.ChangeDutyCycle(2.5)
        #time.sleep(1)
        #p.ChangeDutyCycle(12.5)
        #time.sleep(1)
    p.stop()
    GPIO.cleanup()
