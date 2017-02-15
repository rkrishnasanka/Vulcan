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

channelWidthInPixels = 0
pixelToMMRatio = 0

countFlipper = False

def ColorDistance(rgb1,rgb2):
	'''d = {} distance between two colors(3)'''
	rm = 0.5*(rgb1[0]+rgb2[0])
	d = sum((2+rm,4,3-rm)*(rgb1-rgb2)**2)**0.5
	return d

while (video.isOpened()):
	ret, frame = video.read()
	if ret == True:
		time.sleep(0.1)
		countFlipper = False
		frameCopy = frame
		cv2.line(frameCopy, (X_DETECTION_BORDER,0), (X_DETECTION_BORDER,600), (255,0,0))
		cv2.line(frameCopy, (0, Y_DETECTION_BORDER), (1000, Y_DETECTION_BORDER), (255,0,0))
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		frame = cv2.medianBlur(frame, 13)
#		frame = bgSub.apply(frame)
	#	ret, thresh = cv2.threshold(frame,127,255,0)
#		frame = cv2.Canny(frame, 100, 100)			
#		ret, thresh = cv2.threshold(frame,127,255,0)
		thresh = cv2.adaptiveThreshold(frame.copy(), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
	#	thresh = cv2.Canny(frame, 100, 100)
		im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)	

		areas = []
		largestContour = []
		cArea = 0
		if len(contours) > 0:
			for contour in contours:
				cArea = cv2.contourArea(contour)
#				movingAverageArea = (movingAverageArea*numContours + cArea) / (numContours+1)
#				if currArea > cArea:
#					cArea = currArea
#					largestContour = x
#				print (cArea, movingAverageArea)
#				if cArea > movingAverageArea:
				x,y,w,h = cv2.boundingRect(contour)
				BGR = frameCopy[y+h/2][x+w//2]
				if channelWidthInPixels is 0:
					channelWidthInPixels = (w + h) / 2
					pixelToMMRatio = 1 / float(channelWidthInPixels)
					print channelWidthInPixels, pixelToMMRatio

				cv2.rectangle(frameCopy,(x,y),(x+w,y+h),(0,0,255),1)
				cv2.drawContours(frameCopy, contour, -1, (0,0,255), 1)
			
				if x+w > X_DETECTION_BORDER and x < X_DETECTION_BORDER and y > Y_DETECTION_BORDER and cArea > 375:
					if countFlipper is False:
						cv2.rectangle(frameCopy,(x,y),(x+w,y+h),(0,255,0),1)
				#	cv2.drawContours(frameCopy, contour, -1, (0,0,255), 1)
					countFlipper = True

					if frameCount > 0:
						dropletCount = dropletCount + 1
						frameCount = 0
						blueDist = ComputationalFunctions.colorDistance(frameCopy[y+h/2][x+w/2],[255,1,1])
						redDist = ComputationalFunctions.colorDistance(frameCopy[y+h/2][x+w/2],[1,1,255])
					
					#	if blueDist < 4000:
					#		print dropletCount, " blue", cv2.contourArea(contour)*pixelToMMRatio, cv2.contourArea(contour), cv2.mean(frameCopy, contour)#frameCopy[y+h/2][x+w/2]
					#	else:

						print dropletCount, cv2.contourArea(contour)*pixelToMMRatio, cv2.contourArea(contour), frameCopy[y+h/2][x+w/2]
						cv2.circle(frameCopy, (x+w/2, y+h/2), 3, (0,255,0), -1)	
	
		if countFlipper is False:
			frameCount = frameCount + 1

		cv2.imshow("frame", frameCopy)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

video.release()
cv2.destroyAllWindows()
