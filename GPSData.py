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
        self.sat = 0

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
        gpsData = {}
        gpsData = self.getData(2)
        gpsData = self.dataCorrection(gpsData)
        return
            
    def getData(self,duration):
        datalocal = {}
        dataCol = {}
        timer = time.time()
        x =0
        while time.time() < timer + duration:
            data = self.readLine()
            dataFields = data.split(",")
            if dataFields[0] =="$GPGGA":
                if int(dataFields[6]) == 1:
                    GPSdata=pynmea2.parse(data)
                    datalocal[0] = GPSdata.latitude
                    datalocal[1] = GPSdata.longitude
                    self.alt = GPSdata.altitude
                    self.sat = GPSdata.num_sats
                    dataCol[x] = datalocal
                    x +=1
            time.sleep(0.1)
        return dataCol
            
    def dataCorrection(self,data):
        coordinates = {}
        sumLat = 0.0
        sumLng = 0.0
        print (len(data))
        if len(data) < 1:
            self.lat = 0.0
            self.lng  = 0.0
            return coordinates 
        for item in data:
            sumLat = sumLat + data[item][0]
            sumLng = sumLng + data[item][1]

        self.lat = "%.6f" % (sumLat / len(data))
        self.lng = "%.6f" % (sumLng / len(data))
        return 

