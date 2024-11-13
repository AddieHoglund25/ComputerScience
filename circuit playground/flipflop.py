# challenge 3 - flip flop
# create a program that turns pixels 0-4 to green and 5-9 off when the switch is in the left position
# when the switch is in the right position, pixels 0-4 should be off and 5-9 should be set to green

from adafruit_circuitplayground import cp
import time

while True:
    cp.pixels.brightness = 0.3                      # brightness setting to 30%
    if cp.switch:                                   # this is the right side of the switch
            cp.pixels[0] = (0, 100, 0)              # 0-4 are green
            cp.pixels[1] = (0, 100, 0)
            cp.pixels[2] = (0, 100, 0)
            cp.pixels[3] = (0, 100, 0)
            cp.pixels[4] = (0, 100, 0)
            cp.pixels[5] = (0, 0, 0)                # 5-9 are black/off
            cp.pixels[6] = (0, 0, 0)
            cp.pixels[7] = (0, 0, 0)
            cp.pixels[8] = (0, 0, 0)
            cp.pixels[9] = (0, 0, 0)
    else:                                           # this is the left side of the switch, everything flips
            cp.pixels[0] = (0, 0, 0)                # 0-4 are black/off
            cp.pixels[1] = (0, 0, 0)
            cp.pixels[2] = (0, 0, 0)
            cp.pixels[3] = (0, 0, 0)
            cp.pixels[4] = (0, 0, 0)
            cp.pixels[5] = (0, 100, 0)              # 5-9 are green
            cp.pixels[6] = (0, 100, 0)
            cp.pixels[7] = (0, 100, 0)
            cp.pixels[8] = (0, 100, 0)
            cp.pixels[9] = (0, 100, 0)