from board import *

class RGB:

    def __init__(self, r, g, b, *, maxval = 65535):
        self.blueP = b
        self.greenP = g
        self.redP = r
        self.maxval = maxval

    def rgb(self, r, g, b):
        self.redP.duty_cycle = r
        self.greenP.duty_cycle = g
        self.blueP.duty_cycle = b

    def cyan(self):
        self.rgb(self.maxval,0,0)

    def yellow(self):
        self.rgb(0,0,self.maxval)

    def magenta(self):
        self.rgb(0,self.maxval,0)

    def red(self):
        self.rgb(0,self.maxval,self.maxval)

    def green(self):
        self.rgb(self.maxval,0,self.maxval)

    def blue(self):
        self.rgb(self.maxval,self.maxval,0)

    def off(self):
        self.rgb(self.maxval, self.maxval, self.maxval)

    def white(self):
        self.rgb(0,0,0)

    def rainbow(self, rate):
        r = 0
        g = self.maxval
        b = self.maxval
        count = 0
        while count < 3 * self.maxval:
            self.rgb(r,g,b)
            if count < self.maxval:
                r += rate
                g -= rate
            elif count < 2*self.maxval:
                g += rate
                b -= rate
            else:
                b += rate
                r -= rate
            count += rate