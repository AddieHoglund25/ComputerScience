# challenge 10 - light meter

from adafruit_circuitplayground import cp

while True:
    if cp.light >= 30:
        cp.pixels[0] = (0, 0, 1)
    if cp.light == 27:
        cp.pixels[1] = (0, 0, 1)
    if cp.light == 24:
        cp.pixels[2] = (0, 0, 1)
    if cp.light == 21:
        cp.pixels[3] = (0, 0, 1)
    if cp.light == 18:
        cp.pixels[4] = (0, 0, 1)
    if cp.light == 15:
        cp.pixels[5] = (0, 0, 1)   
    if cp.light == 12:
        cp.pixels[6] = (0, 0, 1)
    if cp.light == 9:
        cp.pixels[7] = (0, 0, 1)
    if cp.light == 6:
        cp.pixels[8] = (0, 0, 1)
    if cp.light <= 3:
        cp.pixels.fill((0, 0, 1))    