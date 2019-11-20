# CircuitPython
My CircuitPython assignments

## distanceSensor
> The HC-SR04 measures the distance to an object roughly 10 times per second.
> The distance is printed out to your serial monitor.
> The color of the onboard neopixel on your Metro corresponds to the distance, according to the graphic below.
[[http://wiki.chssigma.com/images/8/8b/Color_spectrum.png]]

### Process
Read documentation of `adafruit_hcsr04`, got distance sensing working. Then I did some quick math about how to scale the rgb values based on distance, which needed `constrain()`(see [ledFade](#ledFade)) `abs()`, and `int()` to prevent value errors. I later realized that the g and b values were backwards and fixed it
### Requirements
https://github.com/adafruit/Adafruit_CircuitPython_HCSR04/blob/master/adafruit_hcsr04.py

## helloCircuitPy
> Make the onboard metapixel red
### Process
The code was basically provided, making it no big feat.

## lcdbutton
> Set up an LCD that displays a number that increases on button press and switches direction on switch
### Process
So the process for this one was: copy stuff from the documentation, be confused as to why it's giving errors for three days, and then updating circuitpy when Dr. Shields figure out that that was the problem. It then proceeded to work. Later I realized that I misinterpretted the assignment and went back to fix it.
### Requirements
https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
https://github.com/dhalbert/CircuitPython_LCD

## ledFade
> Make an led fade in and out
### Process
Some quick googling of how to do analog stuff in circuitpy, and I found that <code>from analogio import AnalogOut</code> allows you to do analog outputs. From there it was only a matter of finding that the max analog value was 65535 in circuitpy instead of the 255 it was in arduino, and a constrain function I copied from stackoverflow, and it worked.

## photointerupt
> Output the number of interrupts a photointerrupter detects over 4 seconds without using `time.sleep()`
### Process
The first thing I did was check out the `time` library's documentation. This told me about three different functions that I thought worked like arduino's `millis()`. The first one was deprecated, the second didn't work, and the third wasn't precise enough. When I brought it up to Dr Shields he mentioned `time.monotonic()` which was exactly what I was looking for. I then set up a check for every 4 seconds, like I did with the PID box.

## servoTouch
> Make a 180° servo rotate in one direction if one wire is touched and in the other direction if the other is touched.
### Process
I looked up the servo library and based my code on the example for the setup, and the fading led for the rotating. I then looked up the touch library and changed when it increments the angle
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

## toProcessing
> Communicate the value of a potentiometer with a processing program
### Process
This half was mostly copying from the assignment, but the other half, serial.pde, took some effort. Read about that [here](https://github.com/sshanks49/Processing#serial). 