
import serial
import time

#$GPGGA,212107.00,4722.61267,N,00821.39560,E,1,07,1.34,629.1,M,47.3,M,,*53



port = "/dev/ttyAMA0"  # Raspberry Pi 2
#port = "/dev/ttyS0"    # Raspberry Pi 3

ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)

def parseGPS(data):
    #print ("raw:", data)
    if "$GPGGA" in str(data[0:6]):
		
        s = str(data).split(",")
        if s[7] == '0':
            print ("no satellite data available")
            return        
        time = s[1][0:2] + ":" + s[1][2:4] + ":" + s[1][4:6]
        lat = decode(s[2])
        dirLat = s[3]
        lon = decode(s[4])
        dirLon = s[5]
        alt = s[9] + " m"
        sat = s[7]
        print ("Time(UTC): %s-- Latitude: %s(%s)-- Longitude:%s(%s)\
-- Altitute:%s--(%s satellites)" %(time, lat, dirLat, lon, dirLon, alt, sat) )

def decode(coord):
    # DDDMM.MMMMM -> DD deg MM.MMMMM min
    v = coord.split(".")
    head = v[0]
    tail =  v[1]
    deg = head[0:-2]
    min = head[-2:]
    return deg + " deg " + min + "." + tail + " min"

while True:
    data = ser.readline()
    parseGPS(data)
    
    
   
