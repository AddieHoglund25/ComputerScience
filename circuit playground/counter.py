# challenge 9 - counter
# counts up with button A
# counts down with button B

from adafruit_circuitplayground import cp
import time

button = 0

while True:
  
    if cp.button_a:
        if button <= 9:
            cp.pixels[button] = (0, 0, 1)
            button == button + 1
            time.sleep(0.2)

    if cp.button_b:
            cp.pixels[button] = (0, 0, 0)
            button == button - 1
            time.sleep(0.2)