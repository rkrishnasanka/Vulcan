import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help = "path to the video")
args = vars(ap.parse_args()) 
video = cv2.VideoCapture(args["video"])

bgSub = cv2.createBackgroundSubtractorMOG2()

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
		if len(contours) > 0:
			for x in contours:
				currArea = cv2.contourArea(x)
				if currArea > cArea:
					cArea = currArea
					largestContour = x
			if cArea > 3500:
				x,y,w,h = cv2.boundingRect(largestContour)
				cv2.rectangle(frameCopy,(x,y),(x+w,y+h),(0,255,0),1)
				print "Area: ",cArea
				
				try:
					BGR = frameCopy[y+h/2][x+w//2]
					print "BGR", BGR
				except Exception, e:
					pass

		cv2.imshow("frame", frameCopy)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

video.release()
cv2.destroyAllWindows()
