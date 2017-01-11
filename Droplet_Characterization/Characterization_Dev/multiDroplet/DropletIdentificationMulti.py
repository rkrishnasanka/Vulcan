import os,sys
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if not path in sys.path:
	sys.path.insert(1, path)
del path

import numpy as np
import cv2
from VulcanParseAndFormatting import *

ap = CharacterizationInputParsing()
video = cv2.VideoCapture(ap.args["video"])
outFormat = CharacterizationOutputFormatting()

bgSub = cv2.createBackgroundSubtractorMOG2()
movingAverageArea = 0
numContours = 0

while (video.isOpened()):
	ret, frame = video.read()
	if ret == True:
		frameCopy = frame
		frame = cv2.medianBlur(frame, 13)
		frame = bgSub.apply(frame)
			
		ret, thresh = cv2.threshold(frame,127,255,0)
		im2, contours, hierarchy = cv2.findContours(frame,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)	

		areas = []
		largestContour = []
		cArea = 0
#		movingAverageArea = 0
#		numContours = 0
		if len(contours) > 0:
			for contour in contours:
				cArea = cv2.contourArea(contour)
				movingAverageArea = (movingAverageArea*numContours + cArea) / (numContours+1)
				numContours = numContours + 1
#				if currArea > cArea:
#					cArea = currArea
#					largestContour = x
				print (cArea, movingAverageArea)
				if cArea > movingAverageArea:
					x,y,w,h = cv2.boundingRect(contour)
					cv2.rectangle(frameCopy,(x,y),(x+w,y+h),(0,255,0),1)
#				cv2.drawContours(frameCopy, contour, -1, (0,0,255), 2)			

		cv2.imshow("frame", frameCopy)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

video.release()
cv2.destroyAllWindows()
