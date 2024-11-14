# challenge 6 - police simulator

from adafruit_circuitplayground import cp
import time
cp.pixels.brightness = 0.3                  # brightness to 0.3

while True:
    cp.pixels.fill((0, 0, 150))             # turn all lights to blue
    cp.play_tone(500, 0.5)                  # plays 500 hz for 0.5 seconds
    time.sleep(0.5)
    cp.pixels.fill((150, 0, 0))             # turns all lights to red
    cp.play_tone(900, 0.5)                  # plays 900 hz for 0.5 seconds
    time.sleep(0.5)
