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
        self.qual = 0
        self.sat =0 
        
    def getGPSData(self):
        while True: 
            newdata = self.ser.readline()
            GPSdataString= str(newdata)
            GPSdataString= GPSdataString[2:-5]   #alle zeilenumbruch Zeichen am Anfang und ende werden entfernt
            if GPSdataString[0:6] == "$GPGGA":
                GPSdata=pynmea2.parse(GPSdataString)
                self.lng = GPSdata.longitude
                self.lat = GPSdata.latitude
                self.qual = GPSdata.gps_qual
                self.sat = GPSdata.num_sats
                break
            time.sleep(0.1)
            
    
    def getLongitude(self):
        gpsString = self.validateData()
        if gpsString != None:
            lng = gpsString.longitude
            return lng
        else:
            return None
            
    def getLatitude(self):
        gpsString = self.validateData()
        if gpsString != None:
            lat = gpsString.latitude
            return lat

        
    def getGPSQual(self):
        gpsString = self.validateData()
        if gpsString != None:
            gps_qual = gpsString.gps_qual
            return int(gps_qual)
        else:
            return 0
            
        
    def getGPSSat(self):
        gpsString = self.validateData()
        if gpsString != None:
            num_sats = gpsString.num_sats
            return gps_qual

    def validateData(self):
        GPSdataString = self.getGPSData()
        if GPSdataString[0:6] == "$GPGGA":
            returnObj = pynmea2.parse(GPSdataString)
            return returnObj

            

# x = GPSData()   
# def clearConsole():
     # clear = lambda: os.system("clear")
     # clear()    
# while True:
    # x.getGPSData()
    # clearConsole()
    # print ("GPS Quality:"+ str(x.qual))
    # print ("GPS Sat:"+ str(x.sat))
    # print (x.lat, x.lng)
    # time.sleep(0.5)
