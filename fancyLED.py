from board import *
from time import sleep
from digitalio import digitalInOut, Direction
import random

class FancyLED:

    def __init__(self, pin1, pin2, pin3):
        self.convert = [D0,D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,D11,D12,D13]
        self.l1 = digitalInOut(self.convert[pin1])
        self.l1.direction = Direction.OUTPUT
        self.l2 = digitalInOut(self.convert[pin2])
        self.l2.direction = Direction.OUTPUT
        self.l3 = digitalInOut(self.convert[pin3])
        self.l3.direction = Direction.OUTPUT

    def setVal(self,v1,v2,v3):
        self.l1.value = v1
        self.l2.value = v2
        self.l3.value = v3

    def alternate(self):
        self.setVal(1,0,1)
        sleep(0.15)
        self.setVal(0,1,0)
        sleep(0.15)
        self.setVal(1,0,1)
    
    def blink(self):
        self.setVal(1,1,1)
        sleep(0.5)
        self.setVal(0,0,0)
    
    def chase(self):
        self.setVal(1,0,0)
        sleep(0.05)
        self.setVal(0,1,0)
        sleep(0.05)
        self.setVal(0,0,1)
        sleep(0.05)
        self.setVal(0,1,0)
        sleep(0.05)
        self.setVal(1,0,0)
    
    def sparkle(self):
        self.vals = [0,0,0]
        self.count = 0
        while count < 1000:
            self.vals = [random.randrange(1),random.randrange(1),random.randrange(1),]
            self.setVal(vals[0],vals[1],vals[2])
            count += 1
            sleep(0.02)