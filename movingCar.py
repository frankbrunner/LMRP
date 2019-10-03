import RPi.GPIO as GPIO
import time
import threading
from GPS_Calculations import gpsCalculations
GPIO.setmode(GPIO.BCM)

class movingCar():
	DIST_PER_SEC = 35.0
	
	def __init__(self, left_pin1, left_pin2, right_pin1, right_pin2):
		#17,27,23,24
		self.MOTOR_LEFT_PIN1 = left_pin1
		self.MOTOR_LEFT_PIN2 = left_pin2
		self.MOTOR_RIGHT_PIN1 = right_pin1
		self.MOTOR_RIGHT_PIN2 = right_pin2
		"""set true the GPS DataLoop"""
		self.compass = 0
		self.robotPosition = {}
		
		GPIO.setup(self.MOTOR_LEFT_PIN1, GPIO.OUT)
		GPIO.setup(self.MOTOR_LEFT_PIN2, GPIO.OUT)
		GPIO.setup(self.MOTOR_RIGHT_PIN1, GPIO.OUT)
		GPIO.setup(self.MOTOR_RIGHT_PIN2, GPIO.OUT)
			
	def forward(self, time):
		print ("get forward")
		GPIO.output(self.MOTOR_RIGHT_PIN1, GPIO.HIGH)
		GPIO.output(self.MOTOR_RIGHT_PIN2, GPIO.LOW)
		GPIO.output(self.MOTOR_LEFT_PIN1, GPIO.LOW)
		GPIO.output(self.MOTOR_LEFT_PIN2, GPIO.HIGH)
		time.sleep(float(time))
		self.stop()

	def stop(self):
		GPIO.output(self.MOTOR_RIGHT_PIN1, GPIO.LOW)
		GPIO.output(self.MOTOR_RIGHT_PIN2, GPIO.LOW)
		GPIO.output(self.MOTOR_LEFT_PIN1, GPIO.LOW)
		GPIO.output(self.MOTOR_LEFT_PIN2, GPIO.LOW)
		
	def turn(self,turnDirection,directionToWaypoint):
		if turnDirection == "left":	
				GPIO.output(self.MOTOR_RIGHT_PIN1, GPIO.LOW)
				GPIO.output(self.MOTOR_RIGHT_PIN2, GPIO.HIGH)
				GPIO.output(self.MOTOR_LEFT_PIN1, GPIO.LOW)
				GPIO.output(self.MOTOR_LEFT_PIN2, GPIO.HIGH)
		if turnDirection == "right":
			while int(self.compass) >= int(directionToWaypoint):	
				GPIO.output(self.MOTOR_RIGHT_PIN1, GPIO.HIGH)
				GPIO.output(self.MOTOR_RIGHT_PIN2, GPIO.LOW)
				GPIO.output(self.MOTOR_LEFT_PIN1, GPIO.HIGH)
				GPIO.output(self.MOTOR_LEFT_PIN2, GPIO.LOW)
				print ("turning right")

		
	def forwardDistance(self, distance):
		self.forward()
		x = threading.Timer(distance/self.DIST_PER_SEC, self.stop)
		x.start()



		
		
