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
		frame = cv2.Canny(frame, 100, 100)
			
		ret, thresh = cv2.threshold(frame,127,255,0)
		im2, contours, hierarchy = cv2.findContours(frame,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)	

		cv2.imshow("frame", frame)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break

video.release()
cv2.destroyAllWindows()
