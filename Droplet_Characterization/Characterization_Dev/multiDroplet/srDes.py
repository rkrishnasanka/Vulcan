import numpy as np
import cv2

video = cv2.VideoCapture('droplet.mov')

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mov', fourcc, 20.0, (640,400))
#bgSub = cv2.createBackgroundSubtractorMOG2()

while (video.isOpened()):
	ret, frame = video.read()
	if ret == True:
		frame = cv2.Canny(frame, 100, 100)
		fgmask = bgSub.apply(frame)

	
		cv2.imshow("frame", frame)	
		out.write(frame)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break
out.release()
video.release()
cv2.destroyAllWindows()
