
import RPi.GPIO as GPIO
import time
import threading
import os
GPIO.setmode(GPIO.BCM)
from Ultrasonic import ultrasonic
from movingCar import movingCar	
from distanceMeasure import distanceMeasure
from GPSData import GPSData
from GPS_Distance import gpsDistance

	
GPIO.setwarnings(False)

ultrasFront = ultrasonic(20,21)
ultrasLeft = ultrasonic(19,26)
ultrasRight = ultrasonic(6,13)
distMeasure = distanceMeasure(16,6.5,20)

gpsData = GPSData()
gpsDist = gpsDistance()

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
          time.sleep(0.1)  

def GPSdataLoop():
     while True:
          gpsData.getGPSData()
          time.sleep(0.5) 

def getMainMenue():
     global menue 
     clearConsole()
     print("1. Start cuttin Gras" +"\n" 
           "2. Initial field" + "\n" 
           "3. Load CSV" + "\n" 
           "4. Exit")
     action = int(input())
     if action == 1:
          menue = "cuttin"
     if action == 2:
          menue = "initial"
     if action == 3:
          menue = "test"
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
     gpsWayPoints[0] = [47.376762, 8.356943] #[gpsData.lng,gpsData.lat] 
     messageLine = "initial Waypoint is set"
     getInitialMenue()
  
def setBorderWaypoints(stopTrigger):  
     global messageLine
     if len(gpsWayPoints) == 0:
          messageLine = "Check if the inital was done"
          getInitialMenue()
          return
     maxWayPoints = 0
     while True:
          currentRobotPosition = [47.376846, 8.356880]#[gpsData.lng,gpsData.lat]
          distBetweenWaypoints = gpsDist.getDistance(currentRobotPosition,gpsWayPoints[-0])
          if distBetweenWaypoints > 1.0:
               gpsWayPoints[len(gpsWayPoints)] = [gpsData.lng,gpsData.lat]
          if stopTrigger == True:
               getInitialMenue()
               break
          if maxWayPoints == 10:
               messageLine = "Reached Max Waypoints"
               break
          maxWayPoints += 1
          print( "Distance:" + str(distBetweenWaypoints)+"Anzahl Puntkte:"+ str(len(gpsWayPoints)),end="\r")     
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
          
    
process01 = threading.Thread(target=GPSdataLoop)
process02 = threading.Thread(target=GPSMainLoop)
process01.start()
process02.start()
         



     



    

