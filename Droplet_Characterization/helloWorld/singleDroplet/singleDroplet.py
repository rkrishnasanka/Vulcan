import numpy as np
import cv2

video = cv2.VideoCapture('fastSingle.mov')
#size = (int(video.get(cv2.CV_CAP_PROP_FRAME_WIDTH)),
 #       int(video.get(cv2.CV_CAP_PROP_FRAME_HEIGHT)))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('single.avi', fourcc, 20.0, (640,400))
#bgSub = cv2.createBackgroundSubtractorMOG2()

while (video.isOpened()):
	ret, frame = video.read()
	if ret == True:
#		frame = cv2.Canny(frame, 100, 100)
#		fgmask = bgSub.apply(frame)

#		out.write(frame)
		
		img = cv2.medianBlur(frame, 9)
		imgg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
		cimg = cv2.cvtColor(imgg, cv2.COLOR_GRAY2BGR)

		circles = cv2.HoughCircles(imgg, cv2.HOUGH_GRADIENT, 1, 1000, param1=100, param2=10, minRadius=30, maxRadius=70)	
		
		if circles is None:
			cv2.imshow('frame', frame)
			out.write(frame)
		else:
		
			for i in circles[0,:]:
				cv2.circle(frame,(i[0], i[1]), i[2], (0, 255, 0), 1)
				cv2.circle(frame,(i[0], i[1]), 2, (0,0,255), 3)	
	
			cv2.imshow("frame", frame)	
			out.write(frame)

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
	else:
		break
out.release()
video.release()
cv2.destroyAllWindows()
