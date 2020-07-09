import RPi.GPIO as g
import time


btn_input = 15

g.setwarnings(False)
g.setmode(g.BCM)
g.setup(btn_input, g.IN, pull_up_down = g.PUD_DOWN)
g.setup(12 , g.OUT)

count = 0
while True:
    if g.input(btn_input) == g.HIGH:
        count += 1
        print("pushed!!!!")
    time.sleep(.1)

g.cleanup()
