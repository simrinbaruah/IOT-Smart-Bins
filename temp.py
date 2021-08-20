import stepC
from socket import *
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
def close():
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

    HOST = ''
    PORT = 21567
    BUFSIZE = 1024
    ADDR = (HOST, PORT)

    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(5)

    while True:
        print 'Waiting for connection'
        tcpCliSock, addr = tcpSerSock.accept()
        print '...connected from :', addr
        try:
            while True:
                data = ''
                data = tcpCliSock.recv(BUFSIZE)
                if not data:
                    break
                if data == "1":
                    stepC.clockwise(Seq, StepPins)
                    print 'Rotate clockwise'
        except KeyboardInterrupt:
            print "Closing"
        tcpSerSock.close()
