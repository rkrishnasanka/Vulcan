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
		frame = cv2.medianBlur(frame, 9)
#		frame = cv2.Canny(frame, 100, 100)
#		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#		frame = bgSub.apply(frame)
		frame = cv2.Canny(frame, 100, 100)

#		th3 = cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)			
		ret, thresh = cv2.threshold(frame,0,255,0)
		im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)	

		cv2.drawContours(frameCopy, contours, -1, (0,255,0), 1)
		cv2.imshow("frame", frameCopy)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

video.release()
cv2.destroyAllWindows()
