from cv2 import cv2
import numpy as np


face_cascade = cv2.CascadeClassifier('/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')



cap = cv2.VideoCapture(0)

while(True):
	# Capture frame by frame
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, scaleFactor=4, minNeighbors=5)

	for(x,y,w,h) in faces:
#		print(x,y,w,h)
		roi_gray = gray[y:y+h,x:x+w]
		roi_bgr = frame[y:y+h,x:x+w]

		img_item = 'face_image.png'
		cv2.imwrite(img_item,roi_gray)
		#draw square
		color = (0,0,255)
		stroke = 3
		end_cordx = x + w
		end_cordy = y + h
		cv2.rectangle(frame, (x, y) , (end_cordx, end_cordy), color, stroke)
	# show the camera with frames
	cv2.imshow('frame', frame)
	#kill the window/ exit
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()