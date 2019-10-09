import RPi.GPIO as GPIO
import time
import threading
import os
from GPS_Calculations import gpsCalculations
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

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
			
	def forward(self, duration):
		print ("get forward")
		GPIO.output(self.MOTOR_RIGHT_PIN1, GPIO.LOW)
		GPIO.output(self.MOTOR_RIGHT_PIN2, GPIO.HIGH)
		GPIO.output(self.MOTOR_LEFT_PIN1, GPIO.HIGH)
		GPIO.output(self.MOTOR_LEFT_PIN2, GPIO.LOW)
		time.sleep(duration)
		self.stop()
		
	def backward(self, duration):
		print ("get backward")
		GPIO.output(self.MOTOR_RIGHT_PIN1, GPIO.HIGH)
		GPIO.output(self.MOTOR_RIGHT_PIN2, GPIO.LOW)
		GPIO.output(self.MOTOR_LEFT_PIN1, GPIO.LOW)
		GPIO.output(self.MOTOR_LEFT_PIN2, GPIO.HIGH)
		time.sleep(duration)
		self.stop()
	

	def stop(self):
		GPIO.output(self.MOTOR_RIGHT_PIN1, GPIO.LOW)
		GPIO.output(self.MOTOR_RIGHT_PIN2, GPIO.LOW)
		GPIO.output(self.MOTOR_LEFT_PIN1, GPIO.LOW)
		GPIO.output(self.MOTOR_LEFT_PIN2, GPIO.LOW)
		
	def turn(self,turnDirection,angle):
		duration = float(angle) * 0.01
		if turnDirection == "right":	
				GPIO.output(self.MOTOR_RIGHT_PIN1, GPIO.LOW)
				GPIO.output(self.MOTOR_RIGHT_PIN2, GPIO.HIGH)
				GPIO.output(self.MOTOR_LEFT_PIN1, GPIO.LOW)
				GPIO.output(self.MOTOR_LEFT_PIN2, GPIO.HIGH)
				print ("turning right")
				time.sleep(duration)
				self.stop()
		if turnDirection == "left":	
				GPIO.output(self.MOTOR_RIGHT_PIN1, GPIO.HIGH)
				GPIO.output(self.MOTOR_RIGHT_PIN2, GPIO.LOW)
				GPIO.output(self.MOTOR_LEFT_PIN1, GPIO.HIGH)
				GPIO.output(self.MOTOR_LEFT_PIN2, GPIO.LOW)
				print ("turning left")
				time.sleep(duration)
				self.stop()

		
	def forwardDistance(self, distance):
		self.forward()
		x = threading.Timer(distance/self.DIST_PER_SEC, self.stop)
		x.start()

# move = movingCar(17,27,23,24)

# def clearConsole():
	# clear = lambda: os.system("clear")
	# clear()

# while True:
	# clearConsole()
	# print("1. move forward" +"\n" 
			   # "2. move backward" + "\n"
			   # "3. move left" + "\n" 
			   # "4. move right" + "\n" 
			   # "5. Exit")
			   
	# action = input()	
	
	# if int(action) == 1:
		# move.forward(2.0)	
	# if int(action) == 2:
		# move.backward(2.0)
	# if int(action) == 3:
		# move.turn("left", 10)
	# if int(action) == 4:
		# move.turn("right", 10)
	# if int(action) == 5:
		# GPIO.cleanup()
		# exit()	
		


		
	
