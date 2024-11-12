    
# challenge number 1 - Blinky
# create a program that flashes all lights green then off in 367ms intervals

from adafruit_circuitplayground import cp 
import time

cp.pixels.brightness = 0.3                              # turns brightness down for each pixel

while True:
    cp.pixels.fill((0, 255, 0))                         # set all pixels to green
    time.sleep(0.367)                                   # time intervals of 0.367 for green
    cp.pixels.fill((0, 0, 0))                           # set all pixels to black
    time.sleep(0.367)                                   # time intervals of 0.367 for black