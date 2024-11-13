# challenge 4 - tippy
# create a program that turns on pixels 1-3 on as green when tipped to the left
# 6-8 should light up red when the board is tipped to the right
# turn off the pixels on the opposite sides when flipped


from adafruit_circuitplayground import cp 
cp.pixels.brightness = 0.1

while True:
    x, y, z = cp.acceleration               # get acceleration along X, Y, and Z axes
    if x > 5:                               # when board is tilting right
        cp.pixels[1] = (0, 100, 0)          # leds 1, 2, and 3 turn green
        cp.pixels[2] = (0, 100, 0)
        cp.pixels[3] = (0, 100, 0)

        cp.pixels[6] = (0, 0, 0)            # leds 6, 7, and 8 are off
        cp.pixels[7] = (0, 0, 0)
        cp.pixels[8] = (0, 0, 0)

    elif x < -5:                            # when board is tilting left
        cp.pixels[1] = (0, 0, 0)            # leds 1, 2, and 3 are off
        cp.pixels[2] = (0, 0, 0)
        cp.pixels[3] = (0, 0, 0)

        cp.pixels[6] = (100, 0, 0)          # leds 6, 7, and 8 turn green
        cp.pixels[7] = (100, 0, 0)
        cp.pixels[8] = (100, 0, 0)

    else:
        cp.pixels.fill((0, 0, 0))           # if board goes any other way, all leds turn off