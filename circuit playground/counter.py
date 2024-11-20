# challenge 9 - counter
# counts up with button A
# counts down with button B

from adafruit_circuitplayground import cp
import time

button = -1

while True:
  
    if cp.button_a:
        if button < 9:                      # stopper if the number of presses on button is over 9
            cp.pixels[button] = (0, 0, 1)   # will turn LED to blue
            button == button + 1            # LED + 1 every time button A is pressed
            time.sleep(0.2)

    if cp.button_b:
        if button > -1:                     # stopper if the number of presses on button is below -1
            cp.pixels[button] = (0, 0, 0)   # will turn LED to black
            button == button - 1            # LED - 1 evert time button B is pressed
            time.sleep(0.2)
