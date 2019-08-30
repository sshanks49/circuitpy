import time
import board
from digitalio import DigitalInOut, Direction, Pull

photointerupter = DigitalInOut(board.D8)
photointerupter.direction = Direction.INPUT
photointerupter.pull = Pull.UP

breaks = 0
then = time.monotonic()
previous = False

while True:
    if photointerupter.value and not previous:
        breaks += 1
    if (time.monotonic() - then) % 4 == 0:
        print("There have been", breaks, "breaks")
        breaks = 0
    previous = photointerupter.value