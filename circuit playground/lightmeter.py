# challenge 10 - light meter

from adafruit_circuitplayground import cp

while True:
    if cp.light >= 30:                      # if brightness is 30, LED 0 will turn blue
        cp.pixels[0] = (0, 0, 1)

    if cp.light == 27:                      # if brightness if 27, LED 1 will turn blue
        cp.pixels[1] = (0, 0, 1)

    if cp.light == 24:                      # if brightness is 24, LED 2 will turn blue
        cp.pixels[2] = (0, 0, 1)

    if cp.light == 21:                      # if brightness is 21, LED 3 will turn blue
        cp.pixels[3] = (0, 0, 1)

    if cp.light == 18:                      # if brightness is 18, LED 4 will turn blue
        cp.pixels[4] = (0, 0, 1)

    if cp.light == 15:                      # if brightness is 15, LED 5 will turn blue
        cp.pixels[5] = (0, 0, 1)   

    if cp.light == 12:                      # if brightness is 12, LED 6 will turn blue
        cp.pixels[6] = (0, 0, 1)

    if cp.light == 9:                       # if brightness is 9, LED 7 will turn blue
        cp.pixels[7] = (0, 0, 1)

    if cp.light == 6:                       # if brightness is 6, LED 8 will turn blue
        cp.pixels[8] = (0, 0, 1)

    if cp.light <= 3:                       # if brightness is 3, LED 9 will turn blue
        cp.pixels[9] = (0, 0, 1)
  