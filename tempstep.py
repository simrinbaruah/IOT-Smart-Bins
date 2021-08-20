import stepAC
import stepC
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

stepAC.anticlockwise(Seq, StepPins)
time.sleep(3)
stepC.clockwise(Seq, StepPins)
GPIO.cleanup()
