import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

aMotorPins = [7, 11, 13, 15]

for pin in aMotorPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

aSequence = [
            [1,0,0,1],
            [1,0,0,0],
            [1,1,0,0],
            [0,1,0,0],
            [0,1,1,0],
            [0,0,1,0],
            [0,0,1,1],
            [0,0,0,1]
            ]
        
iNumSteps = len(aSequence)

if sys.argv[2] == "cw":
    iDirection = 1
else:
    iDirection = -1
fWaitTime = 0.001
iDeg = int(int(sys.argv[1]) * 11.377777777777)
iSeqPos = 0

if len(sys.argv) > 3:
    iSeqPos = int(sys.argv[3])

        # 1024 steps is 90 degrees
        # 4096 steps is 360 degrees
for step in range(0,iDeg):
    for iPin in range(0, 4):
        iRealPin = aMotorPins[iPin]
        if aSequence[iSeqPos][iPin] != 0:
            GPIO.output(iRealPin, True)
        else:
            GPIO.output(iRealPin, False)
        iSeqPos += iDirection
        if (iSeqPos >= iNumSteps):
            iSeqPos = 0
        if (iSeqPos < 0):
            iSeqPos = iNumSteps + iDirection
            
        time.sleep(fWaitTime)
        
for pin in aMotorPins:
    GPIO.output(pin, False)

print iSeqPos
