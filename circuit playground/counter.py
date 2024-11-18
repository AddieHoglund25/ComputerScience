# WORK IN PROGRESS
# challenge 9 - counter
# counts up with button A
# counts down with button B

from adafruit_circuitplayground import cp

button = 0

while True:
  
    if cp.button_a:

        if button == 0 + 1:
            cp.pixels[0] = (0, 0, 100)
        if button == 0 + 2:
            cp.pixels[1] = (0, 0, 100)
        if button == 0 + 3:
            cp.pixels[2] = (0, 0, 100)
        if button == 0 + 4:
            cp.pixels[3] = (0, 0, 100)
        if button == 0 + 5:
            cp.pixels[4] = (0, 0, 100)
        if button == 0 + 6:
            cp.pixels[5] = (0, 0, 100)
        if button == 0 + 7:
            cp.pixels[6] = (0, 0, 100)
        if button == 0 + 8:
            cp.pixels[7] = (0, 0, 100)
        if button == 0 + 9:
            cp.pixels[8] = (0, 0, 100)
        if button == 0 + 10:
            cp.pixels[9] = (0, 0, 100)

    if cp.button_b:

        if button == 0 - 1:
            cp.pixels.fill((0, 0, 0))
