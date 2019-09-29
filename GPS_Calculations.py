from geographiclib.geodesic import Geodesic


class gpsCalculations:
	def __init__(self):
		self.geod = Geodesic.WGS84
		
	def calculateDistance(self,wp01,wp02):
		print (wp01[0], wp01[1],wp02[0],wp02[1],)
		distance = self.geod.Inverse(float(wp01[0]),float(wp01[1]),float(wp02[0]),float(wp02[1]))
		return distance['s12']
	
	def calculateDirection(self,wp01,wp02):
		distance = self.geod.Inverse(float(wp01[0]),float(wp01[1]),float(wp02[0]),float(wp02[1]))
		return distance['azi1']
		
		
#print ("The distance is {:.5f} m.".format(g['s12']))
#print ("The direction is {:.5f} m.".format(g['azi1']))
#The distance is 19959679.267 m.


