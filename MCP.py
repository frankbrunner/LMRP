
import RPi.GPIO as GPIO
import time
import threading
import os
import math
GPIO.setmode(GPIO.BCM)
from Ultrasonic import ultrasonic
from movingCar import movingCar	
from distanceMeasure import distanceMeasure

from GPSData01 import GPSData
from GPS_Distance import gpsDistance
from geographiclib.geodesic import Geodesic
from GPS_Calculations import gpsCalculations
from compass import QMC5883L
	
GPIO.setwarnings(False)

ultrasFront = ultrasonic(20,21)
ultrasLeft = ultrasonic(19,26)
ultrasRight = ultrasonic(6,13)
distMeasure = distanceMeasure(16,6.5,20)

gpsData = GPSData()
gpsDist = gpsDistance()
gpsCalculations = gpsCalculations()
compass = QMC5883L()



move = movingCar(17,27,23,24)
#move.forwardDistance(35.0)

#Global Variablen deklaration
gpsWayPoints = {}
menue = "main"
messageLine = ""
bearing = 0

def GPSMainLoop():
     while True:
          if menue == "main":
               getMainMenue()
          if menue == "initial":
               getInitialMenue()
          if menue == "loadCSV":
               loadFromCsv()
               break
          if menue == "bearing":
               print(bearing)
          if menue == "move along boundary":
               moveAlongBoundary()
          time.sleep(0.5)  

def GPSdataLoop():
     while True:
          data = gpsData.readLine()
          gpsData.parseGPGGA(data)
     time.sleep(0.1)
     
def CompassLoop():
     global bearing
     while True:
          bearing = "%.0f" % compass.get_bearing()
     time.sleep(0.5)

def getMainMenue():
     global menue 
     clearConsole()
     print("1. Start cuttin Gras" +"\n" 
           "2. Initial field" + "\n" 
           "3. Get Bearing" + "\n" 
           "4. Move along boundary" + "\n" 
           "5. Exit")
     action = int(input())
     if action == 1:
          menue = "cuttin"
     if action == 2:
          menue = "initial"
     if action == 3:
          menue = "bearing"
     if action == 4:
          menue = "move along boundary"
     if action == 5:
          exit()     

def getInitialMenue():
     global menue   
     clearConsole()
     print(messageLine)
     print("1.Set initial Waypoint" +"\n"
           "2.Set border Waypoint" +"\n"
           "3.Save to CSV" +"\n"
           "4.Load from CSV" +"\n"
           "5.End initializing")
     action = int(input())
     if action == 1:
          setInitialWaypoint()
     if action == 2:
          setBorderWaypoints(stopTrigger = False)  
     if action == 4:
          loadFromCsv()
     if action == 3:
          saveToCsv(gpsWayPoints)   
     if action == 5:
          menue = "main"
  
def moveAlongBoundary():
     """checke closest waypoint to robot"""
     currentRobotPosition = [47.376762, 8.356943]#[gpsData.lat,gpsData.lng]
     index=getIndexOfClosestWaypoint(currentRobotPosition,gpsWayPoints)
     print (index)
     """check direction to closest waypoint"""
     directionToWaypoint = gpsCalculations.calculateDirection(urrentRobotPosition, gpsWayPoints[index])
     print (directionToWaypint)
     

def getIndexOfClosestWaypoint(robotPosition,wayPoints):
  """localVariables"""
  distClosest = 0
  indexWaypoint = 0
  for x in wayPoints:
    """check Distance between current Robot and waypoints"""
    callculatedDist = gpsCalculations.calculateDistance(currentRobotPosition,wayPoints[x])
    distClosest= checkFirstIteration(distClosest, callculatedDist)
    if callculatedDist < distClosest:
      indexWaypoint = x
  """Return the closest Waypoint"""
  return indexWaypoint

def checkFirstIteration(distClosest, callculatedDist):
     if distClosest == 0:
          distClosest = callculatedDist
     return distClosest
   
def setInitialWaypoint():
     global messageLine
     gpsWayPoints[0] = [gpsData.lat,gpsData.lng] 
     messageLine = "initial Waypoint is set"+str(gpsWayPoints[0]) 
     getInitialMenue()
  
def setBorderWaypoints(stopTrigger):  
     global messageLine
     if len(gpsWayPoints) == 0:
          messageLine = "Check if the inital was done"
          getInitialMenue()
          return
     maxWayPoints = 0
     while True:
          distBetweenWaypoints = 0
          currentRobotPosition = [gpsData.lat,gpsData.lng]
          distBetweenWaypoints = gpsCalculations.calculateDistance(currentRobotPosition,gpsWayPoints[-0])
          if distBetweenWaypoints > 2.0:
               gpsWayPoints[len(gpsWayPoints)] = [gpsData.lat,gpsData.lng]
               maxWayPoints += 1
               messageLine = "Distance:" + "%.3f" % distBetweenWaypoints
               break
          time.sleep(0.5)  
     getInitialMenue()   
               
def scanFrontforBounderys(currentPosition):
    scanArea = [currentPosition[0]+1,currentPosition[1]+1]
    print (boundarys[0:0])

def saveToCsv(data):
     global messageLine
     with open('waypoints.csv', 'w') as csvFile:
          i=0
          for line in data:
               csvFile.write(str(data[i])+"\n")
               i +=1
     messageLine = "WayPoint saved on file"

def loadFromCsv():
     global messageLine
     with open('waypoints.csv','r') as csvFile:
          i = 0
          for line in csvFile:
               gpsWayPoints[i] = line.strip()
               i = len(gpsWayPoints)
     messageLine = "data loaded"
        
def clearConsole():
     clear = lambda: os.system("clear")
     clear()

          

process01 = threading.Thread(target=GPSdataLoop)
process02 = threading.Thread(target=GPSMainLoop)
process03 = threading.Thread(target=CompassLoop)
process01.start()
process02.start()
process03.start()
         



     



    

