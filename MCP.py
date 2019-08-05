
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
from Ultrasonic import ultrasonic
from movingCar import movingCar	
GPIO.setwarnings(False)

#ultrasonic = Ultrasonic(12,24,1)
#ultrasonic.startMeasure()
ultrasFront = ultrasonic(20,21)
ultrasLeft = ultrasonic(19,26)
ultrasRight = ultrasonic(6,13)

move = movingCar(17,27,23,24)
#move.forwardDistance(35.0)

#main Loop
while True:
     abstandFront = ultrasFront.distanz()
     abstandLeft = ultrasLeft.distanz()
     abstandRight = ultrasRight.distanz()
     if abstandFront < 10.0:
         print ("front %.1f cm" % abstandFront)
         
     if abstandLeft < 10.0:
         print ("left %.1f cm" % abstandLeft)
         
     if abstandRight < 10.0:
         print ("right %.1f cm" % abstandRight)
         
     time.sleep(0.25)
    



    

