]import RPi.GPIO as g
import time

led= 12

g.setmode(g.BOARD)
g.setup(led, g.OUT)

for k in range(10):
    g.output(led, g.HIGH)
    time.sleep(.5)
    g.output(led, g.LOW)
    time.sleep(.5)
g.cleanup()
