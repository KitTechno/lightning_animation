import animation
import random_functions as ranfun
import init
import time

flash = init.init.flash
night = init.init.night
xzero = init.init.xzero
yzero = init.init.yzero

class run():
    while True:
        
        # for i in range(3):
            animation.flashscreen(night)
            animation.drawstrike(night,flash,xzero,yzero)
            time.sleep(2)
            # while True:
            night.update()

        # night.update()
