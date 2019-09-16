from geopy.distance import geodesic


boundary = {}
boundary[0]= [[47.376762, 8.356943],[47.376846, 8.356880]]
boundary[1]= [[47.376846, 8.356880],[47.376804, 8.356722]]
boundary[2]= [[47.376804, 8.356722],[47.376724, 8.356810]]
test = type(boundary[0][0])
print (type(test))

class gpsDistance:

	def getDistance(self,pointA,pointB):
		print (pointA)
		print (pointB)
		distance = geodesic(pointA, pointB).miles
		distance = self.milesToMeters(distance)
		return (distance)

	def getRelativeDistanceToRobot(self,positionRobot, boundary, element):
		length_A = getDistance(positionRobot, boundary[element][0])
		length_B = getDistance(positionRobot, boundary[element][1])
		return length_A + length_B
		
	def milesToMeters(self,value):
		value = value * 1.6 * 1000
		return value
			
	# for i in boundary:
		# print(getRelativeDistanceToRobot(positionRobot, boundary,i))
