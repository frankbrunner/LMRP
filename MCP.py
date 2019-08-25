
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
from Ultrasonic import ultrasonic
from movingCar import movingCar	
from distanceMeasure import distanceMeasure
	
GPIO.setwarnings(False)


ultrasFront = ultrasonic(20,21)
ultrasLeft = ultrasonic(19,26)
ultrasRight = ultrasonic(6,13)
distMeasure = distanceMeasure(16,6.5,20)

frequenz = 2
timer = 5

move = movingCar(17,27,23,24)
#move.forwardDistance(35.0)

boundarys = [[-2.0,1.0],[1.0,1.0],[1.0,-1.0],[-1.0,-1.0]]
currentPosition = [0.1,0.0]

def scanFrontforBounderys(currentPosition):
    scanArea = [currentPosition[0]+1,currentPosition[1]+1]
    print (boundarys[0:0])

#main Loop
while True:
     if timer == 0:
         move.forward()
     else:
         timer = timer -1
         print ("TIMER:"+ str(timer))
         
     abstandFront = ultrasFront.distanz()
     #abstandLeft = ultrasLeft.distanz()
     #abstandRight = ultrasRight.distanz()
     if abstandFront < 30.0:
         print ("front %.1f cm" % abstandFront)
               
     if abstandFront < 20.0:
         move.stop()
         
    
     print ("dist"+ str(distMeasure.distance) )
     if distMeasure.distance >= 20.0:
          move.stop()
          timer = 99999
         

     time.sleep(0.1)
     



    

