

class ComputationalFunctions():	
	# Returns the distance between two rgb colors
	@staticmethod
	def colorDistance(rgb1, rgb2):
		'''d = {} distance between two colors(3)'''
		rm = 0.5*(rgb1[0]+rgb2[0])
		d = sum((2+rm,4,3-rm)*(rgb1-rgb2)**2)**0.5
		return d

	@staticmethod
	def rectangleAreaFromPoints(lowX, lowY, highX, highY):
		return (highY-lowY) * (highX - lowX)
