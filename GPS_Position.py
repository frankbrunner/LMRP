#GPS Position Script
import time
import serial
import pynmea2

#loop for the GPS

class GPSData:
    def __init__(self):
        self.port = "/dev/ttyAMA0"
        self.ser = serial.Serial(port, baudrate=9600,timeout=0.5)
        self.newdata = ser.readline()
        
    def getGPSData(self):
        if self.newdata[0:6] == "$GPGGA":
            newmsg = pynmea2.parse(self.newdata)
            return newmsg
        
    def getLonitude(self):
        newmsg = getGPSData()
        lng = newmsg.longitude
        return lng
        
    def getLatitude(self):
        newmsg = getGPSData()
        lat = newmsg.latitude
        return lat
        
    def getLatitude(self):
        newmsg = getGPSData()
        gps_qual = newmsg.gps_qual
        return gps_qual
        
    def getLatitude(self):
        newmsg = getGPSData()
        num_sats = newmsg.num_sats
        return gps_qual
        
        
