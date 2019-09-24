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

    def parseGPGGA(self,data):
        datalocal = {}
        print ("raw:", data) #prints raw data
        if data[0:6] == "$GPGGA":
            GPSdata=pynmea2.parse(data)
            if int(GPSdata.gps_qual) < 1 :
                return "Fix quality below 1"
            self.lng  =  "%.7f" % GPSdata.longitude
            self.lat  =  "%.7f" % GPSdata.latitude
            self.alt  =   GPSdata.altitude



# x = GPSData()   
# def clearConsole():
     # clear = lambda: os.system("clear")
     # clear()    
# while True:
    # data = x.readLine()
    # value = x.parseGPGGA(data)
    # print (x.lng,x.lat)
    # time.sleep(0.1)
    
