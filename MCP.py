
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
from Ultrasonic import Ultrasonic
from movingCar import movingCar	
GPIO.setwarnings(False)

#ultrasonic = Ultrasonic(12,24,1)
#ultrasonic.startMeasure()

move = movingCar(17,27,23,24)
move.forwardDistance(350.0)

delay = 5
timer = 0

while timer < delay:
	time.sleep(1)
	timer = timer + 1
	print("delay" + str( timer))
	

if timer >= delay:
	move.stop()
