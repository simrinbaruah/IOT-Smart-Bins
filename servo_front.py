import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12, 50)
p.start(7.5)
stop_time = time.time() + 0.01
while time.time() < stop_time:
    p.ChangeDutyCycle(12.5)
        #p.ChangeDutyCycle(2.5)
        #time.sleep(1)
        #p.ChangeDutyCycle(12.5)
        #time.sleep(1):
p.stop()
GPIO.cleanup()
