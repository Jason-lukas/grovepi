#!/usr/bin/env python

from grovepi import *

led = 2
sonar = 4

while True:
    try:
        dist = ultrasonicRead(sonar)
        print dist
    except KeyboardInterrupt:
        print "koniec"
        break