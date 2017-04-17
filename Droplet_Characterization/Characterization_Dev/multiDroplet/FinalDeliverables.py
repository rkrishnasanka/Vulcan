import os,sys
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if not path in sys.path:
	sys.path.insert(1, path)
del path

import numpy as np
import cv2
from VulcanParseAndFormatting import *
from VulcanUsefulFunctions import *

ap = CharacterizationInputParsing()
video = cv2.VideoCapture(ap.args["video"])
#video = cv2.VideoCapture(0)
outFormat = CharacterizationOutputFormatting()

bgSub = cv2.createBackgroundSubtractorMOG2()
movingAverageArea = 0

frameCount = 0
dropletCount = 0

channelWidthInPixels = 0
pixelToMMRatio = 0

while (video.isOpened()):
	ret, frame = video.read()
	if ret == True:
		frameCount = frameCount + 1
		frameCopy = frame

		cv2.line( frameCopy, (0,100), (1200,100), (255,0,0))
#		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		frame = cv2.medianBlur(frame, 13)
		frame = bgSub.apply(frame)
	
		frame = cv2.Canny(frame,100,100)		
		ret, thresh = cv2.threshold(frame,127,255,0)
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
#					print channelWidthInPixels, pixelToMMRatio

				if y+h < 100 and cArea > 100:
#					cv2.rectangle(frameCopy,(x,y),(x+w,y+h),(0,255,0),1)
					cv2.drawContours(frameCopy, contour, -1, (0,0,255), 1)
			
					if frameCount > 10:	
						dropletCount = dropletCount + 1
						frameCount = 0
						blueDist = ComputationalFunctions.colorDistance(frameCopy[y+h/2][x+w/2],[255,1,1])
						redDist = ComputationalFunctions.colorDistance(frameCopy[y+h/2][x+w/2],[1,1,255])
					
						if blueDist < 2000:
							print dropletCount, " blue", cv2.contourArea(contour)*pixelToMMRatio
							cv2.rectangle(frameCopy, (x,y), (x+w, y+h), (255,0,0),1)
						else:
							print dropletCount, " red", cv2.contourArea(contour)*pixelToMMRatio
							cv2.rectangle(frameCopy, (x,y), (x+w, y+h), (0,0,255), 1)

		cv2.imshow("frame", frameCopy)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

video.release()
cv2.destroyAllWindows()
