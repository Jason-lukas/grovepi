#!/usr/bin/env python

from grovepi import *

led = 5
sonar = 4
max_dist = float(30)

while True:
    try:
        dist = float(ultrasonicRead(sonar))
        if dist <= max_dist:
            power = int((1 - dist/max_dist)*255)
            print power

        else:
            print "za daleko"
            power = 0

        analogWrite(led,power)

    except KeyboardInterrupt:
        print "koniec"
        analogWrite(led,0)
        break