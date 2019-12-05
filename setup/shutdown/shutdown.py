from sense_hat import SenseHat
import time
import os
sense = SenseHat()

lastpressed = 0

def shutdown():
    global lastpressed
    delta = time.time() - lastpressed
    print(delta)
    if delta < 4:
        sense.show_letter("X", (200,0,0))
        print('shutdown')
        os.system("halt -p")


def up():
    global lastpressed
    lastpressed = time.time()


sense.stick.direction_middle = shutdown
sense.stick.direction_up = up


while True:
    time.sleep(999999)