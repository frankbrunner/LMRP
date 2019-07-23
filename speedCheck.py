import RPi.GPIO as GPIO
import time



channel = 24
channel23 = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)



GPIO.setup(channel23, GPIO.OUT, initial=GPIO.LOW)

time.sleep(1)


def callbackRising(channel):
	print("my Callback changet")
	
def callbackFalling():
	print("my Callback low")
	
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(channel, GPIO.BOTH, callback=callbackRising, bouncetime=500)
#GPIO.add_event_detect(channel, GPIO.FALLING, callback=callbackFalling)


time.sleep(50)



time.sleep(5)
GPIO.cleanup()


#GPIO.add_event_detect(channel, GPIO.FALLING, callback=callbackFalling)

