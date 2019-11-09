from flask import Flask, render_template,request
from movingCar import movingCar	
from compass import QMC5883L
from GPSData import GPSData
from csv import csv
from consoleOutput import consoleOutput
import threading
import RPi.GPIO as GPIO
import time
from captureWP import capture


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

moveRobot = movingCar(17,27,23,24)
compass = QMC5883L()
gpsData = GPSData()
csv = csv()
output = consoleOutput()
capture = capture()

"""Global Variables"""
gpsWP= {}
bearing =0.0
robotPosition =[0.0,0.0]
gpsSignal = 0
outputLines={}

def startProcedure():
	global gpsWP
	data = csv.loadFromCsv("./waypoints.csv")
	startServices(getCompassData)
	# ~ startServices(getGPSdata)
	webserver()	

def startServices(serviceName):
	service = threading.Thread(target=serviceName)
	service.start()
	#print ("Service:"+str(serviceName)+" has been started")
	output.outputStatic("Service:"+str(serviceName)+" has been started")
	
def getGPSdata():
	global robotPosition, gpsSignal
	startTime = time.time()
	while True:	
		"""get relevant GPS Data 0 = Signal 1 = lat 2= long"""
		gpsData.parseGPGGA()
		output.outputGpsStatus(str("test"))
		robotPosition = [gpsData.lat,gpsData.lng]
		output.outputGPS(gpsData.lat,gpsData.lng,gpsData.sat)

def getCompassData():
	global bearing
	while True:
		bearing = "%.0f" % compass.get_bearing()
		output.outputBearing(bearing)
		time.sleep(0.2)
	
"""Webservice"""

def webserver():	

	mcp = Flask(__name__) 
	
	@mcp.route('/')	
	def index():
		return(render_template("start.html", name="this ist Frank"))
	
	@mcp.route('/init')
	def initiate():
		value ="tst"
		if request.args.get("function") == "sethomebase":
			returnValue= capture.setHomeBase(robotPosition)
			return(returnValue)
		if request.args.get("function") == "getdirection":
			return(str(bearing))
			
		return(render_template("init.html", titel=value))
		
	
			
	@mcp.route('/move')
	def move():
		if request.args.get("function") == "forward":
			moveRobot.forward()
		if request.args.get("function") == "right":
			moveRobot.turn("right")
		if request.args.get("function") == "left":
			moveRobot.turn("left")
		if request.args.get("function") == "backward":
			moveRobot.backward()
		if request.args.get("function") == "stop":
			moveRobot.stop()
		"""render Template"""
		return(render_template("move.html", name="this ist Frank"))
	
	if __name__=='__main__':
		print("has been starting")
		mcp.run(debug=True, host = '0.0.0.0')

startProcedure()
