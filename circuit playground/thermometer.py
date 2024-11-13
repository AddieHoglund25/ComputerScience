# WORK IN PROGRESS
# challenge 5 - thermometer
# create a program that turns on more pixels as the temperature gets hotter
# use table on website to indicate the colors with temperature

from abafruit_circuitplayground import cp 
import time
cp.pixels.brightness = 0.3

while True:
    temp_f = cp.temperature
    if temp_f <= 78:
        cp.pixels[0] = (0, 0, 255)
    elif temp_f > 78:
        cp.pixels[1] = (28, 0, 227)
    elif temp_f > 79:
        cp.pixels[2] = (57, 0, 199)
    elif temp_f > 80:
        cp.pixels[3] = (85, 0, 170)
    elif temp_f > 81:
        cp.pixels[4] = (113, 0, 142)
    elif temp_f > 82:
        cp.pixels[5] = (142, 0, 113)
    elif temp_f > 83:
        cp.pixels[6] = (170, 0, 85)
    elif temp_f > 84:
        cp.pixels[7] = (199, 0, 56)
    elif temp_f > 85:
        cp.pixels[8] = (227, 0, 28)
    elif temp_f >= 86:
        cp.pixels[9] = (255, 0, 0)
    
    else:
        cp.pixels.fill((0, 0, 0))
    time.sleep(0.5)
