# ------------------------ Split Your Video Into Fframes or Image sequence 


# STEP-1 import Libraries 

import cv2 as cv 

cap= cv.VideoCapture('resources\Welcome.mp4')

frameNr = 0

while(True):
    success, frame = cap.read()
    if success:
        cv.imwrite(f'resources/frames/frame_{frameNr}.jpg', frame)

        # Assignment 7:11 f-string known as " Literal String Interpolation". it works similar to % formating and str. 
        # format (). But the difference is, It is much faster as compared to the other two string formates
    else:
        break
    frameNr = frameNr+1

cap.release()
    
