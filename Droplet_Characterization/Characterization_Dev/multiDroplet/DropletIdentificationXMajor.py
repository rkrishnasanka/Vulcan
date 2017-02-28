import os,sys
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if not path in sys.path:
	sys.path.insert(1, path)
del path

import numpy as np
import cv2
from VulcanParseAndFormatting import *
from VulcanUsefulFunctions import *
import time

ap = CharacterizationInputParsing()
video = cv2.VideoCapture(ap.args["video"])
outFormat = CharacterizationOutputFormatting()

bgSub = cv2.createBackgroundSubtractorMOG2()
X_DETECTION_BORDER = 100
Y_DETECTION_BORDER = 400
movingAverageArea = 0

frameCount = 1
dropletCount = 0
elapsedFrames = 0
eclipseFrames = 0

channelWidthInPixels = 0
pixelToMMRatio = 0

currentEclipse = False
countedArea = False
macroCountedArea = False

largestReferenceArea = 0
referenceSize = 0

outputList = []

def ColorDistance(rgb1,rgb2):
	'''d = {} distance between two colors(3)'''
	rm = 0.5*(rgb1[0]+rgb2[0])
	d = sum((2+rm,4,3-rm)*(rgb1-rgb2)**2)**0.5
	return d

# Main loop to read in frames
while (video.isOpened()):
	ret, frame = video.read()
	if ret == True:
		elapsedFrames = elapsedFrames + 1
		currentEclipse = False
		frameCopy = frame

		# Draw the detection lines
		cv2.line(frameCopy, (X_DETECTION_BORDER,0), (X_DETECTION_BORDER,600), (255,0,0))
		cv2.line(frameCopy, (0, Y_DETECTION_BORDER), (1000, Y_DETECTION_BORDER), (255,0,0))

		#Processing the frames
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		frame = cv2.medianBlur(frame, 13)
		thresh = cv2.adaptiveThreshold(frame.copy(), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
		im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)	

		areas = []
		largestContour = []
		cArea = 0

		# If we found contours in the frame
		if len(contours) > 0:
			# Loop through the found contours
			for contour in contours:
				cArea = cv2.contourArea(contour)
				x,y,w,h = cv2.boundingRect(contour)
				BGR = frameCopy[y+h/2][x+w//2]
	#			if channelWidthInPixels is 0:
	#				channelWidthInPixels = (w + h) / 2
	#				pixelToMMRatio = 1 / float(channelWidthInPixels)
	#				print channelWidthInPixels, pixelToMMRatio

				cv2.rectangle(frameCopy,(x,y),(x+w,y+h),(0,0,255),1)
				cv2.drawContours(frameCopy, contour, -1, (0,0,255), 1)

				# Isolate the reference and make sure we have not marked a reference yet
				if y < Y_DETECTION_BORDER and not macroCountedArea and x+w > X_DETECTION_BORDER and x < X_DETECTION_BORDER:
					currentContour = cv2.contourArea(contour)
					countedArea = True
	
					# Eliminate the smaller contours are not the reference
					if (currentContour > largestReferenceArea):
						savedX = x
						savedY = y
						savedW = w
						savedH = h
						largestReferenceArea = currentContour
				
				# If there is a new contour in the droplet zone, count it and characterize it
				if x+w > X_DETECTION_BORDER and x < X_DETECTION_BORDER and y > Y_DETECTION_BORDER and cArea > 375:
					# Highlight the contour bound in green
					if currentEclipse is False:
						cv2.rectangle(frameCopy,(x,y),(x+w,y+h),(0,255,0),1)
				#	cv2.drawContours(frameCopy, contour, -1, (0,0,255), 1)
					# We can currently in a contour eclipse
					currentEclipse = True

					# If teh time between the last eclipse is non-zero (space between droplet)
					if frameCount > 0:
						dropletCount = dropletCount + 1

					#	print "Frames since last droplet:", frameCount

						frameCount = 0
						blueDist = ComputationalFunctions.colorDistance(frameCopy[y+h/2][x+w/2],[255,1,1])
						redDist = ComputationalFunctions.colorDistance(frameCopy[y+h/2][x+w/2],[1,1,255])
					
					#	if blueDist < 4000:
					#		print dropletCount, " blue", cv2.contourArea(contour)*pixelToMMRatio, cv2.contourArea(contour), cv2.mean(frameCopy, contour)#frameCopy[y+h/2][x+w/2]
					#	else:
						
						dropletRGB = frameCopy[y+h/2][x+w/2]
						print dropletCount, cv2.contourArea(contour)*pixelToMMRatio, cv2.contourArea(contour), dropletRGB
						outputList.append([dropletCount, cv2.contourArea(contour), dropletRGB.copy()])
						cv2.circle(frameCopy, (x+w/2, y+h/2), 3, (0,255,0), -1)	
	
			if countedArea is True:
				macroCountedArea = True

		if macroCountedArea is True and elapsedFrames > 10:
			cv2.rectangle(frameCopy, (savedX, savedY), (savedX+savedW, savedY+savedH), (0,255,0),1)
			referenceSize = savedX+savedW * savedH
			pixelToMMRatio = float(1) / referenceSize

		# If a droplet eclipse isn't current happening, count the number of frames that have elapsed
		if currentEclipse is False:
			frameCount = frameCount + 1

			if eclipseFrames is not 0:
				print "Duration that the droplet was within the zone:", eclipseFrames
				outputList[-1].append(eclipseFrames)
				outputList[-1].append(dropletCount)
			eclipseFrames = 0
		# If we are in an eclipse, track how many frames it is occuring for
		else:
			eclipseFrames = eclipseFrames + 1

		cv2.imshow("frame", frameCopy)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

for dropletInfo in outputList:
	dropletInfo[1] = dropletInfo[1]*pixelToMMRatio

video.release()
cv2.destroyAllWindows()
