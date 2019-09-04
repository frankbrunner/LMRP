#GPS Position Script
import time
import serial
import pynmea2

port = "/dev/ttyAMA0"  # Raspberry Pi 2
#port = "/dev/ttyS0"    # Raspberry Pi 3

ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)

#loop for the GPS
while True:
    newdata = ser.readline()
    data = str(newdata)
    data = data[2:-5]   #alle zeilenumbruch Zeichen am Anfang und ende werden entfernt
   
    if data[0:6] =="$GPGGA":
        newmsg = pynmea2.parse(data)
        lat = newmsg.latitude
        print("Lat:"+ str(lat))
        lng = newmsg.longitude
        print("Lng"+str(lng))
        gps_qual = newmsg.gps_qual
        print("GPS Qualität:"+str(gps_qual))
        num_sats = newmsg.num_sats
        print("Anzahl Sateliten:"+ str(num_sats))
        time.sleep(1)
