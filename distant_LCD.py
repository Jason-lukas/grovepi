from grovepi import *
from grove_rgb_lcd import *
ultrasonic_ranger = 4
while True :
	try:
		distant = ultrasonicRead(ultrasonic_ranger)
		print distant,'cm'
		setRGB(0,0,255)
		setRGB(0,255,0)
		setText("distance" + distant)

	except (IOError,TypeError) as e:
		print "error"
