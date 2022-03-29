# -------------- How To Detect Specific Colors Inside Python


# STEP-1 Import Libraries 

import cv2 as cv 
import numpy as np 

# STEP-2 Reading Image 

# img = cv.imread('resources\lion-4k.jpg')

# STEP- 3 Convert in HSV (Hue, Saturation, Value)

# hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# STEP-4 Make Sliders 

def Slider():
    pass
path = "resources\wrap_image.jpeg"
cv.namedWindow('Bars')
cv.resizeWindow('Bars', 700, 380)

# Track Bars
cv.createTrackbar('Hue Min', 'Bars', 0,179, Slider)
cv.createTrackbar('Hue Max', 'Bars', 179,179, Slider)
cv.createTrackbar('Sat Min', 'Bars', 0,255, Slider)
cv.createTrackbar('Sat Max', 'Bars', 255,255, Slider)
cv.createTrackbar('Val Min', 'Bars', 0,255, Slider)
cv.createTrackbar('Val Max', 'Bars', 255,255, Slider)

img = cv.imread(path)
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# hue_min = cv.getTrackbarPos('Hue Min', 'Bars')


while True:
    img = cv.imread(path)
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hue_min = cv.getTrackbarPos('Hue Min', 'Bars')
    hue_max = cv.getTrackbarPos('Hue Max', 'Bars')
    sat_min = cv.getTrackbarPos('Sat Min', 'Bars')
    sat_max = cv.getTrackbarPos('Sat Max', 'Bars')
    val_min = cv.getTrackbarPos('Val Min', 'Bars')
    val_max = cv.getTrackbarPos('Val Max', 'Bars')
    
    print(hue_min,hue_max,sat_min,sat_max,val_min,val_max)
    
    # To See These Changes inside an Image 
    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])
    mask_img = cv.inRange(hsv_img, lower, upper)
    out_img = cv.bitwise_and(img, img,mask=mask_img)


    cv.imshow('Original', img)
    cv.imshow('HSV Image', hsv_img)
    cv.imshow('Mask Image', mask_img)
    cv.imshow('Output Image',out_img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
   


cv.destroyAllWindows()

