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

    def parseGPGGA(self):
        datalocal = {}
        gpsSignal = 0
        while True:
            data = self.readLine()
            #print ("raw:", data) 
            sdata = data.split(",")
            if sdata[0] =="$GPGGA":
                GPSdata=pynmea2.parse(data)
                if int(GPSdata.gps_qual) == 0 :
                    datalocal[0]= 0
                    return datalocal
                else:
                    datalocal[0] = 1 # GPS Signal alive
                    datalocal[1] = "%.7f" % GPSdata.latitude
                    datalocal[2] = "%.7f" % GPSdata.longitude
                    datalocal[3] = "%.7f" % GPSdata.altitude
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
    
