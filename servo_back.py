import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12, 50)
p.start(7.5)

try:
    
    stop_time = time.time() + 0.005
    while time.time() < stop_time:
        p.ChangeDutyCycle(2.5)
        #p.ChangeDutyCycle(2.5)
        #time.sleep(1)
        #p.ChangeDutyCycle(12.5)
        #time.sleep(1)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
