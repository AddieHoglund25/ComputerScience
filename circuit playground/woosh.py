
# challenge 2 - woosh
# create a program that turns pixels 0-9 on for 100 ms then off for 100 ms in number order
# this happens when button A is pressed
# it should appear as a signle light traveling through the circle of pixels on the board
from adafruit_circuitplayground import cp 
import time 
cp.pixels.brightness = 0.3                      # brightness control

while True:
    if cp.button_a:                             # if button A is pressed then the following will happen
        leds = [0,1,2,3,4,5,6,7,8,9]            # leds used
        for led in leds:            
            cp.pixels[led] = (0, 0, 200)        # set color of leds to blue
            time.sleep = (0.1)                  # time intervals of 0.1 seconds
            cp.pixels[led] = (0, 0, 0)          # set color of leds to black
            time.sleep = (0.1)                  # time intervals of 0.1
    else:
        cp.pixels.fill((0, 0, 0))               # if anything else happens, leds will go straight to black
