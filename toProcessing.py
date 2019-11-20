from time import sleep
import busio
import board
from analogio import AnalogIn
def scale(val, src, dst):
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]

potent = AnalogIn(board.A1)
uart = busio.UART(board.TX, board.RX, baudrate=9600)
while True:
    potVal = int(scale(potent.value, (0, 65520), (0,255)))
    byt = bytes([potVal])
    print(byt)
    uart.write(byt)
    sleep(0.1)