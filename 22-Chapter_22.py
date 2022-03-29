# ---------- Face Detection in Image 

# STEP-1 Import Libraries
import cv2 as cv 
import numpy as np


face_cascade= cv.CascadeClassifier('resources\haarcascade_frontalface_default.xml')
# STEP-2 Reading Image 

img = cv.imread('resources\mfaces.jpg')
gray_img= cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img,1.1,4)

# Draw a Ranctangle

for (x,y,w,h) in faces:
     cv.rectangle(img, (x,y), (x+w, y+h), (100,122,50),2)

cv.imshow('Image',img)
cv.imwrite('resources/face_detection.png', img)
cv.waitKey(0)
