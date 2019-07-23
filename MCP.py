
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
from Ultrasonic import Ultrasonic
from movingCar import movingCar	

ultrasonic = Ultrasonic(12,24,1)
#ultrasonic.startMeasure()

move = movingCar(17,27,23,24)
move.forward()
