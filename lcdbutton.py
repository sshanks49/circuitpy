from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import CursorMode
import time
import board
from digitalio import DigitalInOut, Direction, Pull

# Talk to the LCD at I2C address 0x27 or 0x3F
lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)

switch = DigitalInOut(board.D3)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

pressed = True
lastState = True
count = 0

while True:
    lcd.set_cursor_pos(0, 0)
    lcd.print("Counting up")
    pressed = switch.value
    if not pressed and lastState:
        count += 1
    lcd.set_cursor_pos(1, 0)
    lcd.print("Presses:        ")
    lcd.set_cursor_pos(1,8)
    lcd.print(str(count))
    lastState = pressed