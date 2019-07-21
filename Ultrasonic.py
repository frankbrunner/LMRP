import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)



#Set GPIO in out


class Ultrasonic():
	def __init__(self, pinNumberGpioTrigger, pinNumberGpioEcho, intervallInSec):
		self.GPIO_Trigger = pinNumberGpioTrigger
		self.GPIO_Echo = pinNumberGpioEcho
		self.IntervallInSec = intervallInSec
		self.stop = False	
		
		#Set GPIO PIN Numbers
		GPIO_Trigger = self.GPIO_Trigger
		GPIO_Echo = self.GPIO_Echo

		GPIO.setup(self.GPIO_Trigger, GPIO.OUT)
		GPIO.setup(self.GPIO_Echo, GPIO.IN)
	
	def distanz(self):
		#setze trigger auf high
		GPIO.output(self.GPIO_Trigger, True)
		#den trigger nach 0.01sec auf low
		time.sleep(0.00001)
		GPIO.output(self.GPIO_Trigger, False)
		
		StartZeit=time.time()
		StopZeit=time.time()
		
		while GPIO.input(self.GPIO_Echo) == 0:
			StartZeit = time.time()
			
		while GPIO.input(self.GPIO_Echo) == 1:
			StopZeit = time.time()
			
		#Zeit differenz zwischen start und ankunft
		TimeElapse = StopZeit - StartZeit
		distanz = (TimeElapse * 34300) / 2
		return distanz

		
	def startMeasure(self):
		while True:
			abstand = self.distanz()
			print(abstand)
			time.sleep(self.IntervallInSec)

		
	def stopMeasure(self):
		self.stop = True
		GPIO.cleanup
