import cv2 
import numpy as np
import pyautogui
from time import sleep
# fist = cv2.CascadeClassifier('./data/fist.xml')
# palm = cv2.CascadeClassifier('./data/open_palm.xml')
palm = cv2.CascadeClassifier('./data/closed_palm.xml')
source = input("Kamera çeşmesini görkeziň:\n\
				> içki gurulan kamera üçin 0\n\
				> usb web kamera üçin 1\n\
				> IP kameranyň addresini\n\
				:")
if (len(source)>3):
	cap = cv2.VideoCapture(source)
else:
	cap = cv2.VideoCapture(int(source))
scaling_factor = 0.5
pressed = False

while True:
	ret, frame = cap.read() 
	frame = cv2.flip(frame,1)   
	frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
	palm_rects = palm.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=3)  
	for (x,y,w,h) in palm_rects:
		centerx = 150
		cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,100), 5)
		centerx=x+w//2
		centery=y+h//2
		cv2.circle(frame,(centerx,centery),4,(200,200,0),3)
		# pyautogui.keyUp('left')
		# pyautogui.keyUp('right')
		if (pressed==False and centerx<120):
			pyautogui.press('left')
			pressed = True
			sleep(1)
		if (pressed==False and centerx>210):
			pyautogui.press('right')
			pressed = True
			sleep(1)
		# if (centerx>120 and centerx<210):
		else:
			pressed = False
		print (centerx) #show the x position
	cv2.imshow('Presentation control', frame)
	
	c = cv2.waitKey(1)    
	if c == 27:        
		break
cap.release() 
cv2.destroyAllWindows()