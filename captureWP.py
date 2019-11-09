

class capture():
	def __init__(self):
		from mysqlConnect import mySql
		self.mysql = mySql("robot","Pass4you","robot")
		
	def setHomeBase(self,robotPosition):
		# ~ attributes =  [["latitude","47.22133"],["longitude", "8.222311"],["homePos", False]]
		homeBaseAllreadySet = self.mysql.checkIfRecordExists("waypoints", "homebase")
		if homeBaseAllreadySet:
			return "Home Base allready set"
		else:
			attributes = [["latitude",robotPosition[0]],["longitude", robotPosition[1]],["homeBase", True]]
			self.mysql.createRecord("waypoints",attributes)
			return "Home Base has been set"

	
	def setStartMoving(self):
		#gpsWayPoints[0] = [gpsData.lat,gpsData.lng] 
		messageLine = "initial Waypoint is set"+str(gpsWayPoints[0]) 

	# ~ def capture(self):  
		# ~ if len(gpsWayPoints) == 0:
			# ~ messageLine = "Check if the inital was done"
			# ~ getInitialMenue()
			# ~ return
		# ~ maxWayPoints = 0
		# ~ while True:
			# ~ distBetweenWaypoints = 0
			# ~ currentRobotPosition = [gpsData.lat,gpsData.lng]
			# ~ distBetweenWaypoints = gpsCalculations.calculateDistance(currentRobotPosition,gpsWayPoints[len(gpsWayPoints)-1])
			# ~ if distBetweenWaypoints > 2.0:
			# ~ gpsWayPoints[len(gpsWayPoints)] = [gpsData.lat,gpsData.lng]
			# ~ maxWayPoints += 1
			# ~ messageLine = "Nr. WP :"+ str(len(gpsWayPoints)-1) + "  Distance:" + "%.3f" % distBetweenWaypoints
			# ~ break
			# ~ time.sleep(0.5)  
	
		

												
		
