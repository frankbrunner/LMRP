
import RPi.GPIO as GPIO
import time
import threading
import os
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

move = movingCar(17,27,23,24)
#move.forwardDistance(35.0)

#Variablen deklaration
longitude = 0.0
latitude = 0.0
position = {}
gpsQuality = 0.0 
menue = "main"


def scanFrontforBounderys(currentPosition):
    scanArea = [currentPosition[0]+1,currentPosition[1]+1]
    print (boundarys[0:0])
    
def loadGpsData():
     global longitude 
     longitude = gpsData.getLongitude()
     latitude = gpsData.getLatitude()
     gpsQuality = gpsData.getGPSQual()
          
def gpsInitalizing():
     clearConsole()
     
     print("Set robot to first waypoint")
     action = input()
     if action != None:
          #set inital position
          i = 0
          position[i] = [gpsData.lng,gpsData.lat]
          while True:
               clearConsole()
               i = len(position)
               print (position)
               print("1. Set next Waypoint" + "\n" 
                     "2. if completd")
               action = int(input())
               if action == 1:
                    position[i] = [gpsData.lng,gpsData.lat]
               if action == 2:
                    saveToCsv(position)
                    break
          getMainMenue()
          
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
     print("1. Start cuttin Gras" +"\n" 
           "2. Initial field" + "\n" 
           "3. Load CSV" + "\n" 
           "4. Exit")
     action = int(input())
     #auswählen der Hautfunktion
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
          
    
process01 = threading.Thread(target=GPSdataLoop)
process02 = threading.Thread(target=GPSMainLoop)
process01.start()
process02.start()
         



     



    

