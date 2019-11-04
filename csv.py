import os

class csv():
	def saveToCsv(self,data):
		 with open('waypoints.csv', 'w') as csvFile:
			  i=0
			  for line in data:
				   csvFile.write(str(data[i])+"\n")
				   i +=1
		 messageLine = "WayPoint saved on file"

	def loadFromCsv(self,filepath):
		gpsWayPoints={}
		status = ""
		"""example path './file.txt' """
		if os.path.isfile(str(filepath)) ==True:
			with open('waypoints.csv','r') as csvFile:
				i = 0
				for line in csvFile:
					gpsWayPoints[i] = line.strip().split(",")
					gpsWayPoints[i][0] = gpsWayPoints[i][0].strip()
					gpsWayPoints[i][1] = gpsWayPoints[i][1].strip()
					gpsWayPoints[i][0] = gpsWayPoints[i][0].strip("[]")
					gpsWayPoints[i][1] = gpsWayPoints[i][1].strip("[]")
					gpsWayPoints[i][0] = gpsWayPoints[i][0].strip("'")
					gpsWayPoints[i][1] = gpsWayPoints[i][1].strip("'")
					i = len(gpsWayPoints)
				return gpsWayPoints, "Data has been loaded"
		else:
			return "Data File is not exist"
