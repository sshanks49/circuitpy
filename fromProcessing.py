from time import sleep
import busio
import board
from adafruit_motor import servo
import pulseio

pwx = pulseio.PWMOut(board.D5, duty_cycle=2 ** 15, frequency=50)
servx = servo.Servo(pwx)

pwy = pulseio.PWMOut(board.D6, duty_cycle=2 ** 15, frequency=50)
servy = servo.Servo(pwy)

uart = busio.UART(board.TX, board.RX, baudrate=9600)

recieved = []

def twoServ(x, y):
    servx.angle = x
    servy.angle = y

print("go")
while True:
    new = uart.read(1)
    if new != None:
        new = new.decode("utf-8")
    recieved += new
    #print(recieved)
    if new == "&":
        comma = False
        x = ""
        y = ""
        for char in recieved:
            if char != "," and char != "&":
                if not comma:
                    x+=char
                else:
                    y+=char
            else:
                comma = True
        xi = int(x)
        yi = int(y)
        #print(xi, ",", yi)
        twoServ(xi,yi)
        recieved = []