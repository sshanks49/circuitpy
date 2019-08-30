import board
import time
from analogio import AnalogOut

led = AnalogOut(board.A0)
inc = 32
val = 0

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

while True:
    if val+inc >= 65535 or val+inc < 0:
        inc = -inc
        clamp(val, 0, 65535)
    val = val + inc
    led.value = val