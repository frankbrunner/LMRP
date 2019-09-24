
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

	
GPIO.setwarnings(False)

ultrasFront = ultrasonic(20,21)
ultrasLeft = ultrasonic(19,26)
ultrasRight = ultrasonic(6,13)
distMeasure = distanceMeasure(16,6.5,20)

gpsData = GPSData()
gpsDist = gpsDistance()
gpsCalculations = gpsCalculations()

move = movingCar(17,27,23,24)
#move.forwardDistance(35.0)

#Global Variablen deklaration
gpsWayPoints = {}
menue = "main"
messageLine = "Message"

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
               bearing = getBearing(47.37676,8.356951,47.377545,8.356887)
               bearing1 = calculate_initial_compass_bearing((8.356951,47.37676),(8.356887,47.377545))
               print(bearing)
               print(bearing1)
               input()
               break
          time.sleep(0.1)  

def GPSdataLoop():
     while True:
          data = gpsData.readLine()
          gpsData.parseGPGGA(data)
     time.sleep(0.1)


def getMainMenue():
     global menue 
     clearConsole()
     print("1. Start cuttin Gras" +"\n" 
           "2. Initial field" + "\n" 
           "3. Get Bearing" + "\n" 
           "4. Exit")
     action = int(input())
     if action == 1:
          menue = "cuttin"
     if action == 2:
          menue = "initial"
     if action == 3:
          menue = "bearing"
     if action == 4:
          exit()     

def getInitialMenue():
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
    
     if action == 5:
          getMainMenue() 
     if action == 3:
          saveToCsv(gpsWayPoints)    
  
def getCuttingMenue():
     clearConsole()
     print(1)  
          
def loadGpsData():
     longitude = gpsData.getLongitude()
     latitude = gpsData.getLatitude()
     gpsQuality = gpsData.getGPSQual()
   
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
          if distBetweenWaypoints > 5.0:
               gpsWayPoints[len(gpsWayPoints)] = [gpsData.lat,gpsData.lng]
               maxWayPoints += 1
          if stopTrigger == True:
               getInitialMenue()
               break
          if maxWayPoints == 10:
               messageLine = "Reached Max Waypoints"
               break
          
          print( "Distance:" + "%.3f" % distBetweenWaypoints +" :Meter" + "Anzahl Puntkte:"+ str(len(gpsWayPoints)),end="\r")     
          time.sleep(2)  
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
          
def checkGpsAccurancy(gpsAccurancy, value, MaxTime):
     passtTime = 0
     while Maxtime < passtTime:
          passtTime += 1
          if gpsAccurancy < value:
               clearConsole()
               loadingBaar = loadingBaar + "*"
               print("GPS Quality low" + loadingBaar)
          time.sleep(1)  
     print("GPS Quality ist still to low press any key to exit")
     action = input()
     getMainMenue()
   
def getBearing(long1,lat1,long2, lat2):
    brng = Geodesic.WGS84.Inverse(lat1, long1, lat2, long2)['azi1']
    return brng   
def calculate_initial_compass_bearing(pointA, pointB):
     """
     Calculates the bearing between two points.
     The formulae used is the following:
        θ = atan2(sin(Δlong).cos(lat2),
                  cos(lat1).sin(lat2) − sin(lat1).cos(lat2).cos(Δlong))
     :Parameters:
      - `pointA: The tuple representing the latitude/longitude for the
        first point. Latitude and longitude must be in decimal degrees
      - `pointB: The tuple representing the latitude/longitude for the
        second point. Latitude and longitude must be in decimal degrees
     :Returns:
      The bearing in degrees
     :Returns Type:
      float
     """
     if (type(pointA) != tuple) or (type(pointB) != tuple):
        raise TypeError("Only tuples are supported as arguments")

     lat1 = math.radians(pointA[0])
     lat2 = math.radians(pointB[0])

     diffLong = math.radians(pointB[1] - pointA[1])

     x = math.sin(diffLong) * math.cos(lat2)
     y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
            * math.cos(lat2) * math.cos(diffLong))

     initial_bearing = math.atan2(x, y)

     # Now we have the initial bearing but math.atan2 return values
     # from -180° to + 180° which is not what we want for a compass bearing
     # The solution is to normalize the initial bearing as shown below
     initial_bearing = math.degrees(initial_bearing)
     compass_bearing = (initial_bearing + 360) % 360

     return compass_bearing   
          

process01 = threading.Thread(target=GPSdataLoop)
process02 = threading.Thread(target=GPSMainLoop)
process01.start()
process02.start()
         



     



    

