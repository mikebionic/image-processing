import cv2 
import numpy as np
import pyautogui
# cascade = cv2.CascadeClassifier('./data/haarcascade_frontalface_alt.xml')
cascade = cv2.CascadeClassifier('./data/fist.xml')
# cascade = cv2.CascadeClassifier('./data/haarcascade_righteye_2splits.xml')
cap = cv2.VideoCapture(0) 
scaling_factor = 0.5
while True:
	ret, frame = cap.read() 
	frame = cv2.flip(frame,1)   
	frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
	face_rects = cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=3)  
	for (x,y,w,h) in face_rects:
		centerx = 150
		cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,100), 5)
		centerx=x+w//2
		centery=y+h//2
		cv2.circle(frame,(centerx,centery),4,(200,200,0),3)
		pyautogui.keyUp('left')
		pyautogui.keyUp('right')
		if centerx < 120:
			pyautogui.keyDown('left')
		elif centerx >210:
			pyautogui.keyDown('right')
		# else: print('center')
		print (centerx) #show the x position
	cv2.imshow('Face Detector', frame)
	
	c = cv2.waitKey(1)    
	if c == 27:        
		break
cap.release() 
cv2.destroyAllWindows()