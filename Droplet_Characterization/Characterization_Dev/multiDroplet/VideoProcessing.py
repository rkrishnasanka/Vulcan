import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help = "path to the video")
args = vars(ap.parse_args())

#video = cv2.VideoCapture(args["video"])
bgSub = cv2.createBackgroundSubtractorMOG2()

video = cv2.VideoCapture(0)

while (video.isOpened()):
	ret, frame = video.read()
	if ret == True:
		frameCopy = frame
		frame = cv2.medianBlur(frame, 13)
#		frame = cv2.Canny(frame, 100, 100)
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#		frame = bgSub.apply(frame)
#		frame = cv2.Canny(frame, 100, 100)

#		th3 = cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)			
		thresh = cv2.threshold(frame,130,255,cv2.THRESH_BINARY)[1]
		im2, contours, hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)	

		for cnt in contours:
#			approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt,True), True)

#			if len (approx) == 4:
#				print  "square"
			x,y,w,h = cv2.boundingRect(cnt)

			if y > 200:	
				cv2.drawContours(frameCopy,[cnt],-1,(0,0,255),1)
				cv2.rectangle(frameCopy, (x,y), (x+w, y+h),(0,255,0),1)
#				cv2.imshow("frame", thresh)
#		cv2.drawContours(frameCopy, contours, -1, (0,255,0), 1)
		cv2.imshow("frame", thresh)
#		cv2.imshow("thresh", thresh)
#		cv2.imshow("copy", frameCopy)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

video.release()
cv2.destroyAllWindows()
