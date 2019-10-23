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
        dataCol = {}
        gpsSignal = 0
        x = 0
        while True:
            data = self.readLine()
            #print ("raw:", data) 
            sdata = data.split(",")
            if sdata[0] =="$GPGGA":
                datalocal = {}
                GPSdata=pynmea2.parse(data)
                if int(sdata[6]) == 0:
                    datalocal[0]= 0
                    return datalocal
                else:

                    datalocal[0] = 1 # GPS Signal alive
                    datalocal[1] = GPSdata.latitude
                    datalocal[2] = GPSdata.longitude
                    datalocal[3] = GPSdata.altitude
                    dataCol[x] = datalocal
                    x += 1  
                    if x == 3:
                        getData = self.dataCorrection(dataCol,x)
                        x = 0
                        datalocal.clear()
                        dataCol.clear()
                        return getData
            time.sleep(0.1)
                    
    def dataCorrection(self,data,cycle):

        datalocal = {}
        datalocal[0] = data[0][0]
        datalocal[1] = "%.7f" % ((float(data[0][1]) + float(data[1][1]) + float(data[2][1])) /cycle)
        datalocal[2] = "%.7f" % ((float(data[0][2]) + float(data[1][2]) + float(data[2][2])) /cycle)
        datalocal[3] = data[0][3] 
        
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
    
