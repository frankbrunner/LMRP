#GPS Position Script

import os
import time
import serial
import string
import pynmea2

#loop for the GPS
while True:
    port = "/dev/ttyAMA0"
    ser = serial.Serial(port, baudrate=9600,timeout=0.5)
    newdata = ser.readline()
    dataout = pynmea2.NMEAStreamReader()
    

    print ("GET Latitude and Longitude")

    if newdata[0:6] == "$GPGGA":
        newmsg = pynmea2.parse(newdata)
        lat = newmsg.latitude
        print(lat)
        lng = newmsg.longitude
        print(lng)
        time.sleep(10)
