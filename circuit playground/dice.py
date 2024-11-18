# challenge 8 - dice

from adafruit_circuitplayground import cp
import time

cp.pixels.brightness = 0.3              # pizel brightness to 30%

while True:
    import random
    dice = random.randint(1, 11)            # the number that is generated
    if cp.button_a:

        if dice == 1:                       # if 1 is generated, 1 pixel should be lit
            cp.pixels[0] = (0, 0, 100)
            cp.pixels[1] = (0, 0, 0) 
            cp.pixels[2] = (0, 0, 0) 
            cp.pixels[3] = (0, 0, 0) 
            cp.pixels[4] = (0, 0, 0) 
            cp.pixels[5] = (0, 0, 0) 
            cp.pixels[6] = (0, 0, 0) 
            cp.pixels[7] = (0, 0, 0) 
            cp.pixels[8] = (0, 0, 0) 
            cp.pixels[9] = (0, 0, 0) 

        if dice == 2:                       # if 2 is generated, 2 pixels should be lit
            cp.pixels[0] = (0, 0, 100)
            cp.pixels[1] = (0, 0, 100) 
            cp.pixels[2] = (0, 0, 0) 
            cp.pixels[3] = (0, 0, 0) 
            cp.pixels[4] = (0, 0, 0) 
            cp.pixels[5] = (0, 0, 0) 
            cp.pixels[6] = (0, 0, 0) 
            cp.pixels[7] = (0, 0, 0) 
            cp.pixels[8] = (0, 0, 0) 
            cp.pixels[9] = (0, 0, 0) 

        if dice == 3:                       # if 3 is generated, pixels 0-2 should be lit
            cp.pixels[0] = (0, 0, 100)
            cp.pixels[1] = (0, 0, 100) 
            cp.pixels[2] = (0, 0, 100) 
            cp.pixels[3] = (0, 0, 0) 
            cp.pixels[4] = (0, 0, 0) 
            cp.pixels[5] = (0, 0, 0) 
            cp.pixels[6] = (0, 0, 0) 
            cp.pixels[7] = (0, 0, 0) 
            cp.pixels[8] = (0, 0, 0) 
            cp.pixels[9] = (0, 0, 0) 
        
        if dice == 4:                       # if 4 is generated, pixels 0-3 should be lit
            cp.pixels[0] = (0, 0, 100)
            cp.pixels[1] = (0, 0, 100) 
            cp.pixels[2] = (0, 0, 100) 
            cp.pixels[3] = (0, 0, 100) 
            cp.pixels[4] = (0, 0, 0) 
            cp.pixels[5] = (0, 0, 0) 
            cp.pixels[6] = (0, 0, 0) 
            cp.pixels[7] = (0, 0, 0) 
            cp.pixels[8] = (0, 0, 0) 
            cp.pixels[9] = (0, 0, 0) 

        if dice == 5:                       # if 5 is generated, pixels 0-4 should be lit
            cp.pixels[0] = (0, 0, 100)
            cp.pixels[1] = (0, 0, 100) 
            cp.pixels[2] = (0, 0, 100) 
            cp.pixels[3] = (0, 0, 100) 
            cp.pixels[4] = (0, 0, 100) 
            cp.pixels[5] = (0, 0, 0) 
            cp.pixels[6] = (0, 0, 0) 
            cp.pixels[7] = (0, 0, 0) 
            cp.pixels[8] = (0, 0, 0) 
            cp.pixels[9] = (0, 0, 0) 

        if dice == 6:                       # if 6 is generated, pixels 0-5 should be lit
            cp.pixels[0] = (0, 0, 100)
            cp.pixels[1] = (0, 0, 100) 
            cp.pixels[2] = (0, 0, 100) 
            cp.pixels[3] = (0, 0, 100) 
            cp.pixels[4] = (0, 0, 100) 
            cp.pixels[5] = (0, 0, 100) 
            cp.pixels[6] = (0, 0, 0) 
            cp.pixels[7] = (0, 0, 0) 
            cp.pixels[8] = (0, 0, 0) 
            cp.pixels[9] = (0, 0, 0) 

        if dice == 7:                       # if 7 is generated, pixels 0-6 should be lit
            cp.pixels[0] = (0, 0, 100)
            cp.pixels[1] = (0, 0, 100) 
            cp.pixels[2] = (0, 0, 100) 
            cp.pixels[3] = (0, 0, 100) 
            cp.pixels[4] = (0, 0, 100) 
            cp.pixels[5] = (0, 0, 100) 
            cp.pixels[6] = (0, 0, 100) 
            cp.pixels[7] = (0, 0, 0) 
            cp.pixels[8] = (0, 0, 0) 
            cp.pixels[9] = (0, 0, 0) 

        if dice == 8:                       # if 8 is generated, pixels 0-7 should be lit
            cp.pixels[0] = (0, 0, 100)
            cp.pixels[1] = (0, 0, 100) 
            cp.pixels[2] = (0, 0, 100) 
            cp.pixels[3] = (0, 0, 100) 
            cp.pixels[4] = (0, 0, 100) 
            cp.pixels[5] = (0, 0, 100) 
            cp.pixels[6] = (0, 0, 100) 
            cp.pixels[7] = (0, 0, 100) 
            cp.pixels[8] = (0, 0, 0) 
            cp.pixels[9] = (0, 0, 0) 

        if dice == 9:                       # if 9 is generated, pixels 0-8 should be lit
            cp.pixels[0] = (0, 0, 100)
            cp.pixels[1] = (0, 0, 100) 
            cp.pixels[2] = (0, 0, 100) 
            cp.pixels[3] = (0, 0, 100) 
            cp.pixels[4] = (0, 0, 100) 
            cp.pixels[5] = (0, 0, 100) 
            cp.pixels[6] = (0, 0, 100) 
            cp.pixels[7] = (0, 0, 100) 
            cp.pixels[8] = (0, 0, 100) 
            cp.pixels[9] = (0, 0, 0) 

        if dice == 10:                      # if 10 is generated, all pixels should be lit
            cp.pixels.fill((0, 0, 100))

    if cp.button_b:                         # if button b is pressed, all pixels will turn off
        cp.pixels.fill((0, 0, 0))