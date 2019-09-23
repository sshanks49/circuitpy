# CircuitPython
My CircuitPython assignments

## distanceSensor
Changes the onboard metapixel's color based on the distance detected by an HC-SR04 ultrasonic sensor
### Requirements
https://github.com/adafruit/Adafruit_CircuitPython_HCSR04/blob/master/adafruit_hcsr04.py

## helloCircuitPy
Makes the metapixel red

## lcdbutton
prints a number to the lcd which goes up when a button is pressed
### Requirements
https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
https://github.com/dhalbert/CircuitPython_LCD

## ledFade
makes an led fade brighter and dimmer

## photointerupt
prints the numbe of breaks a photointerrupter detects every 4 seconds

## servoTouch
makes a 180 servo turn when wires are touched
### Requirements
https://github.com/adafruit/Adafruit_CircuitPython_Motor

## rgbled
Makes an rgb led change to various colors
### Requirements
[rgb.py](#rgb)

## rgb
Library for rgb leds. Takes three pulseio PWMOut objects. Methods include Red, Blue, Green, Cyan, Yellow, Magenta, White, Off, a method that fades through all colors, and a manual value input.

## hellovscode
Test code, please ignore

## two_fancy
makes patterns on two sets of three leds.
### Requirements
[fancyLED.py](#fancyLED)

## fancyLED
Library for making patterns with three leds, takes the pin number of the leds, which don't need to be initialized or anything. Methods include alternate, which lights up every other led and then every other other led; blink, which turns them all on, and then all off; chase, which chases back and forward for 10 seconds; sparkle, which does random lights for 10 seconds; and setVal, which sets the values manually.