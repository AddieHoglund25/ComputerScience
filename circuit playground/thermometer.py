# challenge 5 - thermometer
# create a program that turns on more pixels as the temperature gets hotter
# use table on website to indicate the colors with temperature

from adafruit_circuitplayground import cp 
cp.pixels.brightness = 0.3                          # pixel brightness to 30%

while True:
    temp_c = cp.temperature
    temp_f = (temp_c * 9 / 5) + 32
    if temp_f <= 78:
        cp.pixels[0] = (0, 0, 1)

    if temp_f > 78:
        cp.pixels[1] = (0, 0, 1)

    if temp_f > 79:
        cp.pixels[2] = (0, 0, 1)

    if temp_f > 80:
        cp.pixels[3] = (1, 1, 0)

    if temp_f > 81:
        cp.pixels[4] = (1, 1, 0)

    if temp_f > 82:
        cp.pixels[5] = (1, 1, 0)

    if temp_f > 83:
        cp.pixels[6] = (1, 1, 0)

    if temp_f > 84:
        cp.pixels[7] = (1, 0, 0)

    if temp_f > 85:
        cp.pixels[8] = (1, 0, 0)

    if temp_f > 86:
        cp.pixels[9] = (1, 0, 0)
