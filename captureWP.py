

class captureWP():
	def __init__(self):
		print(test)
		
	def setHomeBase(self):
		gpsWayPoints[0] = [gpsData.lat,gpsData.lng] 
		messageLine = "initial Waypoint is set"+str(gpsWayPoints[0]) 
	
	def setStartMoving(self):
		gpsWayPoints[0] = [gpsData.lat,gpsData.lng] 
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
	
		

												
		
