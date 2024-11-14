# challenge 7 - randomizer

from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.3

while True:
    import random
    x, y, z = cp.acceleration
    shake_threshold = 2.0
    if abs(x) > shake_threshold or abs(y) > shake_threshold or abs(z) > shake_threshold:
        cp.pixels[0] = (random.randint(0,255), random.randit(0,255), random.randit(0,255))
        cp.pixels[1] = (random.randint(0,255), random.randit(0,255), random.randit(0,255)) 
        cp.pixels[2] = (random.randint(0,255), random.randit(0,255), random.randit(0,255))
        cp.pixels[3] = (random.randint(0,255), random.randit(0,255), random.randit(0,255))
        cp.pixels[4] = (random.randint(0,255), random.randit(0,255), random.randit(0,255))
        cp.pixels[5] = (random.randint(0,255), random.randit(0,255), random.randit(0,255))
        cp.pixels[6] = (random.randint(0,255), random.randit(0,255), random.randit(0,255))
        cp.pixels[7] = (random.randint(0,255), random.randit(0,255), random.randit(0,255))
        cp.pixels[8] = (random.randint(0,255), random.randit(0,255), random.randit(0,255))
        cp.pixels[9] = (random.randint(0,255), random.randit(0,255), random.randit(0,255))