import board
import time
import pulseio
from adafruit_motor import servo
import touchio

pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)
touch1 = touchio.TouchIn(board.A0)
touch2 = touchio.TouchIn(board.A1)

inc = 5
val = 90

while True:
    if touch1.value:
        val = val + inc
    if touch2.value:
        val = val - inc
    if val > 180: val = 180
    if val < 0: val = 0
    #print(val)
    my_servo.angle = val
    time.sleep(0.015)