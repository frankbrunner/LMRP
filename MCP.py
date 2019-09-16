
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

#Variablen deklaration
longitude = 0.0
latitude = 0.0
position = {}
gpsQuality = 0.0 
menue = "main"

def GPSMainLoop():
     while True:
          print(menue)
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
          
def scanFrontforBounderys(currentPosition):
    scanArea = [currentPosition[0]+1,currentPosition[1]+1]
    print (boundarys[0:0])
    
def loadGpsData():
     longitude = gpsData.getLongitude()
     latitude = gpsData.getLatitude()
     gpsQuality = gpsData.getGPSQual()
          
def gpsInitalizing():
     clearConsole()
     trigger = True
     print("1.Set robot to first waypoint")
     action = int(input())
     if action != None:
          #set initial GPS Position
          gpsWayPoints = [47.376762, 8.356943] #[gpsData.lng,gpsData.lat] 
         
          while True:
               clearConsole()
               print("1. Start initial Waypoints" + "\n" 
                     "2. if completd")
               action = int(input())
               if action == 1:
                    gpsWayPoints= addGpsPointduringMovement(gpsWayPoints, 1.0, trigger)
                    print(gpsWayPoints)
                    input()
               if action == 2:
                    saveToCsv(gpsWayPoints)
                    break
          getMainMenue()
  
def addGpsPointduringMovement(gpsWayPoints,distance,trigger):
     print ("bla"+str(gpsWayPoints))
     maxWayPoints = 0
     while True:
          #check the curretn Robot positions
          robotPosition = [47.376846, 8.356880]#[gpsData.lng,gpsData.lat]
          #check th lenght of the list to set the correct index -0 or 0
          index = getIndex(gpsWayPoints)
          passtWayPoint = gpsWayPoints
          #mesure lenght between passt point and robot    
          distBetweenWayPoints = gpsDist.getDistance(robotPosition,passtWayPoint)
          print("Distance:" + str(distBetweenWayPoints))
          if distBetweenWayPoints > distance:
               gpsWayPoints[len(gpsWayPoints)] = [gpsData.lng,gpsData.lat]
          clearConsole()
          print("Distance:" + str(distBetweenWayPoints))
          print("Anzahl Puntkte"+ str(len(gpsWayPoints)))
          if trigger == False:
               return gpsWayPoints
               break
          if maxWayPoints == 500:
               return gpsWayPoints
               break
          maxWayPoints += 1
          time.sleep(0.5)
def getIndex(privateList):
     length = len(privateList)
     if length > 1:
          return (-0)
     else:
          return 0
          
def saveToCsv(data):
     with open('waypoints.csv', 'w') as csvFile:
          i=0
          for line in data:
               csvFile.write(str(data[i])+"\n")
               i +=1

def loadFromCsv(position):
     with open('waypoints.csv','r') as csvFile:
          i = 0
          for line in csvFile:
               position[i] = line.strip()
               i +=1
          return position

def clearConsole():
     clear = lambda: os.system("clear")
     clear()
          
def getMainMenue():
     global menue 
     clearConsole()
     print("Current GPS Coordinates: " + str(gpsData.lng)+","+str(gpsData.lat)+"\n"
           "1. Start cuttin Gras" +"\n" 
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

def getCuttingMenue():
     clearConsole()
     print(1)
     
def getInitialMenue():
     clearConsole()
     print("1. Start initalizing" +"\n" 
           "2. End initializing")
     action = int(input())
     if action == 1:
          gpsInitalizing()
     if action == 2:
          getMainMenue()    

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
         



     



    

