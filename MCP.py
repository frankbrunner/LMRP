
import RPi.GPIO as GPIO
import time
import threading
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

gpsData = GPSData()

mainLoopFrq = 0.1 #0.1 Sec
subLoopFrq05 = 0
subLoopFrq1 = 0

move = movingCar(17,27,23,24)
#move.forwardDistance(35.0)

boundarys = [[-2.0,1.0],[1.0,1.0],[1.0,-1.0],[-1.0,-1.0]]
currentPosition = [0.1,0.0]


#Variablen deklaration
longitude = 0.0
latitude = 0.0
position = {}
gpsQuality = 0.0 
triggerSaveWaypoints = 0
initialPositionSet = False


def scanFrontforBounderys(currentPosition):
    scanArea = [currentPosition[0]+1,currentPosition[1]+1]
    print (boundarys[0:0])
    
     
def loadGpsData():
     global longitude 
     longitude = gpsData.getLongitude()
     latitude = gpsData.getLatitude()
     gpsQuality = gpsData.getGPSQual()
     
def defineWaypoints():
     global triggerSaveWaypoints
     if gpsData.qual >= 1:
          print("Do you want to start with define Waypoints yes/no:")
          inputValue = input()
          if inputValue == "yes":
               triggerSaveWaypoints = 1
     else:
          print("low GPS Quality:" + str(gpsQuality))
          
def saveWaypoints():
     file = open(waypoint.csv, w)
     global initialPositionSet
     if initialPositionSet == False:
          #set inital position
          i = 0
          position[i] = [float(gpsData.lng),float(gpsData.lat)]
          initialPositionSet = True
     if initialPositionSet == True:
          print("Set next gps point type yes:")
          inputValue = input()
          x = len(position)
          position[x] = [gpsData.lng,gpsData.lat]
          
          print (position)

def GPSdataLoop():
     while True:
          gpsData.getGPSData()
          time.sleep(0.5) 
          
def GPSMainLoop():
     while True:
          if triggerSaveWaypoints == 1:
               saveWaypoints()
          else:
               defineWaypoints()
          time.sleep(0.1)           
          
    
process01 = threading.Thread(target=GPSdataLoop)
process02 = threading.Thread(target=GPSMainLoop)
process01.start()
process02.start()
         



     



    

