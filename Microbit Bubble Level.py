# Partners: Brett Silverberg, Kristina Puzack


from microbit import *
from math import *
import time


while True:
    # Just keep emitting three random numbers in a Python tuple.
    time.sleep(0.1)
    xtilt = atan2(accelerometer.get_x(), accelerometer.get_z())
    ytilt = atan2(accelerometer.get_y(), accelerometer.get_z())
    xtilt = xtilt * (180 / 3.141592653)
    ytilt = ytilt * (180 / 3.141592653)
    print(xtilt, ytilt)
    ##above lines finds angle of tilt & convert rads to degrees
    if xtilt < 170 and xtilt > 10:
        if ytilt > 10 and ytilt < 170:
            display.show(Image.ARROW_SE)
        elif ytilt < -10 and ytilt > -170:
            display.show(Image.ARROW_NE)

        else:
            display.show(Image.ARROW_E)

    elif xtilt < -10 and xtilt > -170:
        if ytilt > 10 and ytilt <170:
            display.show(Image.ARROW_SW)

        elif ytilt < -10 and ytilt > -170:
            display.show(Image.ARROW_NW)

        else:
            display.show(Image.ARROW_W)

    elif ytilt > 10 and ytilt < 170:
        display.show(Image.ARROW_S)

    elif ytilt < -10 and ytilt > -170:
        display.show(Image.ARROW_N)
    else:
        display.show(Image.HAPPY)