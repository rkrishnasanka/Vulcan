import numpy as np
import cv2
import argparse

import os,sys
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if not path in sys.path:
	sys.path.insert(1, path)
del path

from VulcanParseAndFormatting import *
from VulcanUsefulFunctions import *

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help = "path to the video")
args = vars(ap.parse_args())

video = cv2.VideoCapture(args["video"])
bgSub = cv2.createBackgroundSubtractorMOG2()

while (video.isOpened()):
	ret1, frame1 = video.read()
#	ret2, frame2 = video.read()
	if ret1 == True:

		frame1Copy = frame1.copy()
#		frame2Copy = frame2

		frame1Copy = cv2.cvtColor(frame1Copy.copy(), cv2.COLOR_BGR2GRAY)
#		frame2Copy = cv2.cvtColor(frame2Copy, cv2.COLOR_BGR2GRAY)
		
#		frame1Copy = cv2.medianBlur(frame1Copy, 11)
		frame1Copy = cv2.GaussianBlur(frame1Copy.copy(), (5, 5), 0)

#		frame1Copy = bgSub.apply(frame1Copy)
	
#		diffFrame = cv2.absdiff(frame1Copy, frame2Copy)
#		diffFrame = cv2.Canny(frame1Copy, 25, 100)

#		ret, frame1Copy = cv2.threshold(frame1Copy, 100, 255, cv2.THRESH_BINARY_INV)		
		frame1Copy = cv2.adaptiveThreshold(frame1Copy.copy(), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
	#	frame1Copy = cv2.erode(frame1Copy, None, iterations=1)
	#	frame1Copy = cv2.dilate(frame1Copy, None, iterations=2)
		im2, contours, hierarchy = cv2.findContours(frame1Copy.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

		if len(contours) > 0:
			cv2.drawContours(frame1Copy, contours, -1, (255,255,255), -1)

			hulls = [cv2.convexHull(cnt) for cnt in contours]

			for hull in hulls:
				cv2.fillConvexPoly(frame1Copy, hull, (255,255,255), lineType=8, shift=0)
				
#				x,y,w,h = cv2.boundingRect(hull)
#				cv2.rectangle(frame1Copy, (x,y), (x+w,y+h), (255,255,255),1)
#			for contour in contours:
#				hulls.append(cv2.convexHull(contour))

#			cv2.drawContours(frame1Copy, hulls[0], -1 (255,255,255), -1)
	
		cv2.imshow("frame", frame1Copy)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

video.release()
cv2.destroyAllWindows()
