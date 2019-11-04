import os

class consoleOutput:
	def __init__(self):
		self.messages = []
		self.status = ""
		self.bearing = 0
		self.lat = 0.0
		self.lon = 0.0
		self.sat = 0
		self.GPSstatus = ""
		
	def outputBearing(self, bearing):
		self.bearing = bearing
		
	def outputGPS(self, lat, lon, sat):
		self.lat = lat
		self.lon = lon
		self.sat = sat
		
			
	def outputStatus(self,status):	
		self.status = status
		self.console()
	def outputGpsStatus(self,status):	
		self.GPSstatus = status
		self.console()	
	
	def outputStatic(self,message):	
		self.messages.append(message)
		self.console()
	
	def console(self):
		self.clearConsole()
		print("***********************************"+"\n")
		print("********"+self.GPSstatus+"*********"+"\n")
		if len(self.messages) > 0:
			for item in self.messages:
				if item: 
					print("*"+ str(item)+"\n")
		print("***************Status********************"+"\n")
		print("bearing: "+ str(self.bearing))
		print("Stalites: "+ str(self.sat))
		print("GPS coordinates: "+ str(str(self.lat) +":"+ str(self.lon)))
		print("*"+str(self.status))
		
		
	def clearConsole(self):
	     clear = lambda: os.system("clear")
	     clear()
	     
