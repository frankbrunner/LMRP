
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
from Ultrasonic import Ultrasonic

ultrasonic = Ultrasonic(12,24,1)
ultrasonic.startMeasure()
ultrasonic.stopMeasure()

