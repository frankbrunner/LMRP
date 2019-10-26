#GPS Position Script
import time
import serial
import pynmea2
import os


#loop for the GPS

class GPSData:
    def __init__(self):
        self.port = "/dev/ttyAMA0"
        self.ser = serial.Serial(self.port, baudrate=9600,timeout=0.5)
        self.lng = 0.0
        self.lat = 0.0
        self.alt = 0.0
        self.gpsstatus = ""

    def readLine(self):
        newdata = self.ser.readline()
        GPSdataString= str(newdata)
        GPSdataString= GPSdataString[2:-5]   #alle zeilenumbruch Zeichen am Anfang und ende werden entfernt
        return GPSdataString
        
    def parseGPRMC(self,data):
        datalocal = {}
        #print ("raw:", data) #prints raw data
        if data[0:6] == "$GPRMC":
            sdata = data.split(",")
            if sdata[2] == 'V':
                return "no satellite data available"
            datalocal[0] = sdata[7]                  #Speed in knots
            datalocal[1] = sdata[8]                  #True course
            return datalocal
            
    def gpsStatus(self,data):
        #print ("raw:", data) 
        dataFields = data.split(",")
        if dataFields[0] =="$GPGGA":
            if int(dataFields[6]) == 0:
                return "NO GPS DATA"
            else:
                return "RECIVING GPS DATA"
        else:
            return self.gpsstatus

    def parseGPGGA(self):
        timer = time.time()
        duration = 1.5
        gpsData = {}
        x = 0
        while time.time() < timer + duration:
            data = self.readLine()
            self.gpsstatus = self.gpsStatus(data)
            gpsData[x] = self.getData(data,self.gpsstatus)
            time.sleep(0.1)
            x +=1
        gpsData = self.dataCorrection(gpsData)
        return gpsData
            
    def getData(self,data,status):
        datalocal = {}
        if status == "RECIVING GPS DATA":
            GPSdata=pynmea2.parse(data)
            datalocal[0] = GPSdata.latitude
            datalocal[1] = GPSdata.longitude
            datalocal[2] = 0.0
            return datalocal
        else:
            datalocal[0] = 1.0
            datalocal[1] = 2.0
            datalocal[2] = 0.0
            return datalocal
          
                    
    def dataCorrection(self,data):
        datalocal = {}
        x=0
        sumLat = 0.0
        sumLon = 0.0
        
        print(data)
        for item in data:
            sumLat = sumLat + data[item][0]
            sumLon = sumLon + data[item][1]
        datalocal[0] = sumLat / len(data)
        datalocal[1] = sumLon / len(data)
        return datalocal



# x = GPSData()   
# def clearConsole():
     # clear = lambda: os.system("clear")
     # clear()    
# while True:
    # data = x.readLine()
    # value = x.parseGPGGA(data)
    # print (x.lng,x.lat)
    # time.sleep(0.1)
    
