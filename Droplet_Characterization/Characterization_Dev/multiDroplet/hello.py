import numpy as np
import cv2

video = cv2.VideoCapture('droplet.mov')

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mov', fourcc, 20.0, (640,400))
bgSub = cv2.createBackgroundSubtractorMOG2()

while (video.isOpened()):
	ret, frame = video.read()
	if ret == True:
#		frame = cv2.Canny(frame, 100, 100)
		fgmask = bgSub.apply(frame)

#		out.write(frame)
		
		#img = cv2.medianBlur(frame, 15)
		imgg = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
		cimg = cv2.cvtColor(imgg, cv2.COLOR_GRAY2BGR)

		circles = cv2.HoughCircles(imgg, cv2.HOUGH_GRADIENT, 1, 20, param1=100, param2=9, minRadius=1, maxRadius=10)	
		
		if circles is None:
			cv2.imshow('frame', frame)
		else:		
			for i in circles[0,:]:
				cv2.circle(fgmask,(i[0], i[1]), i[2], (0, 255, 0), 1)
				cv2.circle(fgmask,(i[0], i[1]), 2, (0,0,255), 3)	
	
			cv2.imshow("frame", fgmask)	
			out.write(frame)

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
	else:
		break
out.release()
video.release()
cv2.destroyAllWindows()
