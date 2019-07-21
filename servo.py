#Module initialisieren
import RPi.GPIO as gpio
import time

#set usible Pin fo PWM
servoPin = 18

#const
multiplicator = 0.045
initialCycle = 7.0

#pin Belegung setzen
gpio.setmode(gpio.BCM)
gpio.setup(servoPin, gpio.OUT)

pwm = gpio.PWM(servoPin, 50)

#move to initial position
def servoInitial():
    print("Servo is Moving in initial Position")
    pwm.start(initialCycle)
    time.sleep(2)

def servoMoveRight(angle, speed):
    currentCycle = initialCycle
    angelCycle = currentCycle + (angle * multiplicator)   
    while currentCycle < angelCycle:
          currentCycle = currentCycle + 0.2
          pwm.ChangeDutyCycle(currentCycle)
          print(currentCycle)
          time.sleep(speed)

def servoMoveLeft(angle, speed):
    currentCycle = initialCycle
    angelCycle = currentCycle - (angle * multiplicator)
    while currentCycle > angelCycle:
          currentCycle = currentCycle - 0.2
          pwm.ChangeDutyCycle(currentCycle)
          print(currentCycle)
          time.sleep(speed)
          
def servoCleanup():
    print("Servo Cleanup")
    pwm.stop()
    gpio.cleanup()


#call functions
servoInitial()
servoMoveRight(90 , 0.02)
servoMoveLeft(90 , 0.02)
servoCleanup()

