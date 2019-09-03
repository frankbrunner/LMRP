from geopy.distance import geodesic


positionRobot = 47.376764, 8.356791


boundary = {}
boundary[0]= [[47.376762, 8.356943],[47.376846, 8.356880]]
boundary[1]= [[47.376846, 8.356880],[47.376804, 8.356722]]
boundary[2]= [[47.376804, 8.356722],[47.376724, 8.356810]]


def getDistance(pointA,pointB):
	distance = geodesic(pointA, pointB).miles
	distance = milesToMeters(distance)
	return (distance)

def getRelativeDistanceToRobot(positionRobot, boundary, element):
	length_A = getDistance(positionRobot, boundary[element][0])
	length_B = getDistance(positionRobot, boundary[element][1])
	return length_A + length_B
	
def milesToMeters(value):
	value = value * 1.6 * 1000
	return value
		
for i in boundary:
	print(getRelativeDistanceToRobot(positionRobot, boundary,i))
