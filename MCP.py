
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
from Ultrasonic import ultrasonic
from movingCar import movingCar	
from distanceMeasure import distanceMeasure
from GPSData import GPSData
	
GPIO.setwarnings(False)


ultrasFront = ultrasonic(20,21)
ultrasLeft = ultrasonic(19,26)
ultrasRight = ultrasonic(6,13)
distMeasure = distanceMeasure(16,6.5,20)

GPS = GPSData()



mainLoopFrq = 0.1 #0.1 Sec
subLoopFrq05 = 0
subLoopFrq1 = 0

move = movingCar(17,27,23,24)
#move.forwardDistance(35.0)

boundarys = [[-2.0,1.0],[1.0,1.0],[1.0,-1.0],[-1.0,-1.0]]
currentPosition = [0.1,0.0]

def scanFrontforBounderys(currentPosition):
    scanArea = [currentPosition[0]+1,currentPosition[1]+1]
    print (boundarys[0:0])
    
def timer(timer):
     timer = timer + 0.1
     return timer
     
         
#main Loop
while True:
     abstandFront = ultrasFront.distanz()
     
     if abstandFront < 30.0:
         print ("front %.1f cm" % abstandFront)
               
     if abstandFront < 20.0:
         move.stop()
         
     dist = distMeasure.distMeasure()
     print ("dist"+ str(dist) )
     if dist >= 20.0:
          move.stop()
          timer = 99999
          
     #sub Loop 0.5 sec
     subLoopFrq05 = timer(subLoopFrq05)
     if subLoopFrq05 == 0.5:
          print ("sub loop 0.5")
          subLoopFrq05 = 0          
     #sub End
     
     #sub Loop 1.0 sec
     subLoopFrq1 = timer(subLoopFrq1)
     if subLoopFrq1 >= 1.0:
          print ("sub loop 1")
          subLoopFrq1  = 0
          print("GPSDATA"+ str(GPS.getLongitude()))
     #sub End
 

     time.sleep(mainLoopFrq)
#main Loop End
     



    

